import json, itertools, collections, sys
import numpy as np
F=sys.argv[1]
rows=[json.loads(l) for l in open(F)]
ANN=sorted({r['_annotator_id'] for r in rows})
LABELS=['INSULTING','ACCUSING','MOCKING','PROVOKING','CURSING','NONE','UNANNOTATABLE']
ATT=LABELS[:5]
D=collections.defaultdict(dict); TXT={}
for r in rows:
    D[r['id']][r['_annotator_id']]=r; TXT[r['id']]=r['text']
ids=sorted(D)
assert all(len(D[i])==3 for i in ids), 'item tidak lengkap'
print('annotator:',ANN,'| item:',len(ids))

# --- validasi aturan ---
print('\n== Pelanggaran aturan ==')
for i in ids:
    for a in ANN:
        acc=set(D[i][a].get('accept',[]))
        if not acc: print(' kosong:',i,a)
        if ({'NONE','UNANNOTATABLE'}&acc) and len(acc)>1: print(' NONE/UNANNOT digabung:',i,a,sorted(acc))

def fleiss(mat):  # mat: n_items x n_categories counts
    n=mat.sum(1)[0]; N=mat.shape[0]
    p=mat.sum(0)/(N*n)
    P=((mat**2).sum(1)-n)/(n*(n-1))
    Pbar=P.mean(); Pe=(p**2).sum()
    return (Pbar-Pe)/(1-Pe) if Pe<1 else float('nan'), Pbar, Pe

def cohen(a,b):
    a=np.array(a);b=np.array(b); po=(a==b).mean()
    pe=a.mean()*b.mean()+(1-a.mean())*(1-b.mean())
    return (po-pe)/(1-pe) if pe<1 else float('nan')

print('\n== Skema A: Fleiss kappa per label ==')
res={}
for L in LABELS:
    cnt=np.array([sum(L in D[i][a].get('accept',[]) for a in ANN) for i in ids])
    mat=np.stack([cnt,3-cnt],1)
    k,po,pe=fleiss(mat)
    pairs=[cohen([L in D[i][x].get('accept',[]) for i in ids],[L in D[i][y].get('accept',[]) for i in ids]) for x,y in itertools.combinations(ANN,2)]
    per_ann={a:sum(L in D[i][a].get('accept',[]) for i in ids) for a in ANN}
    res[L]=k
    print(f'{L:14s} kappa={k:6.3f}  Po={po:.3f}  dipilih per annotator={per_ann}  semua-3-setuju-ada={int((cnt==3).sum())}  cohen-pasangan={[round(x,3) for x in pairs]}')
print(f"rata-rata kappa 5 label serangan = {np.nanmean([res[L] for L in ATT]):.3f}; 7 label = {np.nanmean(list(res.values())):.3f}")

# set-level agreement
exact=sum(len({frozenset(D[i][a]['accept']) for a in ANN})==1 for i in ids)
jac=[]
for i in ids:
    for x,y in itertools.combinations(ANN,2):
        A=set(D[i][x]['accept']);B=set(D[i][y]['accept'])
        jac.append(len(A&B)/len(A|B) if A|B else 1)
print(f'\nSet label identik di ketiga annotator: {exact}/{len(ids)} ({exact/len(ids):.0%}); rata-rata Jaccard berpasangan: {np.mean(jac):.3f}')

# biner abusif vs NONE
cnt=np.array([sum(bool(set(D[i][a]['accept'])&set(ATT)) for a in ANN) for i in ids])
k,_,_=fleiss(np.stack([cnt,3-cnt],1)); print(f'Fleiss kappa "ada serangan vs tidak": {k:.3f}')

# --- NER ---
print('\n== Skema B: F1 entitas antar-annotator (exact start/end/label) ==')
def spans(i,a,lab=None): return {(s['start'],s['end'],s['label']) for s in D[i][a].get('spans',[]) if lab is None or s['label']==lab}
def f1(x,y,lab=None,partial=False):
    tp=fp=fn=0
    for i in ids:
        A=spans(i,x,lab);B=spans(i,y,lab)
        if partial:
            m=sum(any(b[2]==s[2] and b[0]<s[1] and s[0]<b[1] for b in B) for s in A)
            tp+=m; fp+=len(A)-m; fn+=len(B)-sum(any(b[2]==s[2] and b[0]<s[1] and s[0]<b[1] for s in A) for b in B)
        else:
            tp+=len(A&B); fp+=len(A-B); fn+=len(B-A)
    return 2*tp/(2*tp+fp+fn) if tp+fp+fn else float('nan')
for lab in [None,'GOV_ORG','NONGOV_ORG','PERSON','GROUP']:
    ex=[f1(x,y,lab) for x,y in itertools.combinations(ANN,2)]
    pa=[f1(x,y,lab,True) for x,y in itertools.combinations(ANN,2)]
    n={a:sum(len(spans(i,a,lab)) for i in ids) for a in ANN}
    print(f'{str(lab or "SEMUA"):11s} F1 exact rata2={np.nanmean(ex):.3f} {[round(v,3) for v in ex]} | F1 overlap rata2={np.nanmean(pa):.3f} | jumlah span={n}')
print('pasangan urutan:',list(itertools.combinations(ANN,2)))

# simpan tabel per item
out=[]
for i in ids:
    row={'id':i,'text':TXT[i]}
    for a in ANN:
        row['label_'+a]='|'.join(sorted(D[i][a]['accept']))
        row['span_'+a]='; '.join(f"{TXT[i][s:e]}={l}" for s,e,l in sorted(spans(i,a)))
    labs=[set(D[i][a]['accept']) for a in ANN]
    row['label_sama']=len({frozenset(x) for x in labs})==1
    row['span_sama']=len({frozenset(spans(i,a)) for a in ANN})==1
    maj=[L for L in LABELS if sum(L in x for x in labs)>=2]
    row['mayoritas_2dari3']='|'.join(maj)
    out.append(row)
import pandas as pd
pd.DataFrame(out).to_csv('pilot_iaa_per_item.csv',index=False)
