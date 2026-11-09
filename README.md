# KelpNLP — Jenis Serangan Verbal dan Sasarannya pada Komentar Berita Polemik KPAI vs PB Djarum

Proyek UTS Pemrosesan Bahasa Alami: pengembangan **gold dataset** berbahasa Indonesia untuk dua tugas:

- **Klasifikasi multilabel** jenis serangan verbal: `INSULTING`, `ACCUSING`, `MOCKING`, `PROVOKING`, `CURSING`, ditambah `NONE` (selalu berdiri sendiri). Saat anotasi ada juga `UNANNOTATABLE` untuk teks yang tidak bisa dinilai; teks seperti itu dikeluarkan dari gold dataset.
- **Named Entity Recognition (NER)** pihak yang disebut: `GOV_ORG`, `NONGOV_ORG`, `PERSON`, `GROUP`, dengan tag BIO.

| NPM | Nama |
|---|---|
| 240712822 | Edward Christian Imanuel Tambunan |
| 240712828 | Samuel Viva Gracia |
| 240712846 | Rhiquelshen Charolim |

## Sumber data

*Abusive Language Detection on Indonesian Online News Comments* (NusaCrowd: `id_abusive_news_comment`; paper IEEE Xplore 9034620). Dataset ini berisi 3.184 komentar pembaca Kompas, Kaskus, dan Detik pada 15 berita tahun 2019, dengan label asli 1 = not abusive, 2 = abusive but not offensive, 3 = abusive and offensive.

Proyek ini hanya memakai komentar dari **3 berita tentang polemik KPAI vs PB Djarum (2019)**.

## Hasil singkat

| Tahap | Hasil |
|---|---|
| Cleaning (C1–C11) | 3.184 → **3.157** teks bersih (5 tanpa huruf, 22 duplikat dibuang) |
| Seleksi domain | **1.515** teks dari 3 utas berita KPAI vs PB Djarum |
| Sampling | pilot 50 teks + **1.000** teks utama (476 strata prioritas + 524 strata umum, `SEED = 42`) |
| Anotasi | 1.000 teks × **3 annotator** (100% overlap) di Prodigy |
| IAA label | Fleiss' κ rata-rata 5 label serangan **0,840** (hampir sempurna); himpunan label identik 3/3 di 72% teks |
| IAA NER | F1 exact **0,926**, F1 overlap **0,942** (rata-rata 3 pasangan) |
| Adjudikasi | mayoritas 2 dari 3 + **18 teks** diputuskan manual (5 label, 13 NER) + koreksi pedoman NER di 24 teks |
| Gold dataset | **999** teks (1 teks UNANNOTATABLE dikeluarkan), 2.205 entitas, rata-rata 1,42 label per teks |

Fleiss' κ per label (dihitung pada 1.000 teks yang dianotasi): PROVOKING 0,950 · INSULTING 0,886 · ACCUSING 0,833 · NONE 0,807 · MOCKING 0,795 · UNANNOTATABLE 0,750 · CURSING 0,737.

Distribusi label gold (999 teks): ACCUSING 370 · INSULTING 364 · MOCKING 332 · NONE 181 · PROVOKING 168 · CURSING 7.
Entitas gold: GOV_ORG 846 · GROUP 775 · NONGOV_ORG 517 · PERSON 67.

## Struktur folder

```
KelpNLP_UTS/
├── dataset/
│   ├── KelpNLP_dataset_original.xlsx        dataset asli
│   ├── KelpNLP_dataset_clean.csv            3.157 teks bersih + text_norm + penanda domain
│   ├── KelpNLP_dataset_annotation.jsonl     GOLD DATASET (999 teks)
│   └── pendukung/
│       ├── cleaning_log.csv, removed_rows.csv
│       ├── kamus_normalisasi.csv, normalization_log.csv, kamus_bawaan/
│       ├── sample_ids.csv
│       └── prodigy_input/                   prodigy_pilot_50.jsonl, prodigy_anotasi_1000.jsonl
├── file_pendukung/
│   ├── anotasi/pilot/                       IAA pilot 50 teks
│   └── KelpNLP_adjudikasi_lengkap/
│       ├── KelpNLP_anotasi_gabungan_FINAL_1000.jsonl   anotasi mentah 3 annotator (input)
│       ├── KelpNLP_keputusan_adjudikasi.json           keputusan adjudikasi manual (input)
│       ├── KelpNLP_iaa_per_item.csv                    label tiap annotator per teks
│       ├── KelpNLP_gold_auto.jsonl                     gold hasil mayoritas
│       ├── KelpNLP_log_adjudikasi.csv                  status adjudikasi per teks
│       ├── KelpNLP_perlu_adjudikasi.csv                18 teks manual + keputusannya
│       ├── KelpNLP_gold_final.jsonl                    gold setelah keputusan manual
│       ├── KelpNLP_log_keputusan.csv                   semua perubahan gold otomatis → final
│       └── KelpNLP_teks_dikeluarkan.csv                teks yang dikeluarkan dari gold (UNANNOTATABLE)
├── guideline/
│   ├── KelpNLP_annotation_guideline_final.docx / .pdf   pedoman anotasi final (v1.2)
│   └── log_perubahan_guideline.txt          riwayat perubahan pedoman
├── notebook/
│   └── KelpNLP_dataset_EDA.ipynb            seluruh pipeline (lihat di bawah)
├── streamlit/                               dataset explorer (menyusul)
├── report/                                  laporan (menyusul)
├── code_pdf/                                ekspor kode ke PDF (menyusul)
├── KelpNLP_anggota.txt
└── requirements.txt
```

## Isi notebook

`notebook/KelpNLP_dataset_EDA.ipynb` memuat seluruh pipeline secara berurutan:

1. **Cleaning**: perbaikan noise teknis (mojibake, escape `%uXXXX`, karakter tak terlihat, markup, URL → `[URL]`, username → `[USER]`, spasi), buang teks tanpa huruf dan duplikat, seleksi domain, dan 22 uji otomatis.
2. **Normalisasi**: kolom terpisah `text_norm` dengan kamus 758 entri hasil audit dua kamus bawaan, plus proteksi nama entitas. `text_clean` tidak diubah.
3. **Sampling**: populasi domain 1.509 teks (setelah varian hampir-duplikat dibuang), strata prioritas/umum, pilot 50 dan sampel utama 1.000, proporsional per utas berita.
4. **Anotasi, IAA, dan Adjudikasi → Gold Dataset**: gabung export Prodigy, cek kelengkapan dan pelanggaran aturan, Fleiss' κ dan Cohen's κ (dicocokkan dengan `statsmodels`/`sklearn`), F1 NER, adjudikasi otomatis, keputusan manual dan koreksi pedoman, pengeluaran teks UNANNOTATABLE, pembentukan gold, dan 17 uji otomatis.

Setiap bagian diakhiri uji `assert`. Kalau ada satu yang gagal, notebook berhenti, sehingga file yang tersimpan selalu lolos semua pengujian.

## Cara menjalankan ulang

Butuh Python 3.11 atau 3.12.

```bash
python -m venv .venv
.venv\Scripts\activate            # Windows
# source .venv/bin/activate       # Linux / macOS
pip install -r requirements.txt
jupyter lab
```

Buka `notebook/KelpNLP_dataset_EDA.ipynb`, lalu **Restart Kernel → Run All**. Path di notebook relatif terhadap folder proyek, jadi notebook bisa dijalankan dari folder `notebook/` maupun folder utama.

Hasil run ulang harus sama dengan file yang ada. Cek dua sidik SHA-256 berikut:

| Yang dicek | SHA-256 |
|---|---|
| `id` + `text_clean` di `KelpNLP_dataset_clean.csv` | `65ab5e50e5e04424c72cc655b88a603bd2e47a5aa0dd36c9e0ec37344bd4c2af` |
| file `KelpNLP_dataset_annotation.jsonl` | `8a8a77faa4fb7aa76b6d3d178cbc62fa4138525411bd80ab3971910ec6138b3d` |

Bagian 4 juga bisa dijalankan sendiri, mulai dari sel *Langkah 0* bagian tersebut. File input anotasi (`KelpNLP_anotasi_gabungan_FINAL_1000.jsonl` dan `KelpNLP_keputusan_adjudikasi.json`) tidak pernah ditimpa oleh notebook.

## Format gold dataset

`dataset/KelpNLP_dataset_annotation.jsonl`: satu baris JSON per teks, UTF-8.

| Field | Isi |
|---|---|
| `id` | ID permanen `ANC-xxxx` (urutan baris di dataset asli) |
| `text` | `text_clean`; offset span mengacu ke teks ini |
| `meta` | `thread` (1–3) dan `berita` (judul berita) |
| `labels` | label gold multilabel: INSULTING, ACCUSING, MOCKING, PROVOKING, CURSING, atau NONE (urutan tetap) |
| `spans` | entitas gold `{start, end, label, text}` |
| `tokens`, `ner_bio` | token Prodigy dan tag BIO gold (panjang sama) |
| `annotations` | label dan span asli tiap annotator (`Rhiquel`, `SamuelViva`, `edwardchristi4n`) |
| `adjudication` | status label dan NER (`sepakat 3/3` / `mayoritas 2/3` / `MANUAL`) dan `manual` = alasan keputusan manual (`null` bila tidak ada) |

Contoh membaca:

```python
import json
gold = [json.loads(l) for l in open("dataset/KelpNLP_dataset_annotation.jsonl", encoding="utf-8")]
g = gold[0]
print(g["id"], g["labels"])                    # ANC-1123 ['ACCUSING']
print(list(zip(g["tokens"], g["ner_bio"]))[:5])
```

## Catatan penting

- **Sampel sengaja diperkaya** teks berindikasi serangan (strata prioritas 47,6% dari sampel). Distribusi label di gold dataset karena itu tidak sama dengan proporsi di seluruh komentar.
- **CURSING sangat jarang (7 teks).** Perlu diperhatikan saat pemodelan (kelas sangat tidak seimbang).
- Teks **UNANNOTATABLE** (1 teks, ANC-2866) dikeluarkan dari gold dataset sesuai guideline, tetapi tetap ikut dihitung dalam IAA dan dicatat di `KelpNLP_teks_dikeluarkan.csv`.
- NER menandai **pihak yang disebut** di komentar. Sasaran serangan dibaca dari gabungan label dan entitas.
- Aturan anotasi lengkap ada di `guideline/`, dan seluruh perubahan pedoman sejak pilot tercatat di `guideline/log_perubahan_guideline.txt`.
