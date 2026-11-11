**PROYEK UTS-UAS  •  PEMROSESAN BAHASA ALAMI** 

## **PROYEK TERINTEGRASI UTS & UAS** 

## **PENGEMBANGAN DATASET DAN PEMODELAN MULTILABEL TEXT CLASSIFICATION & NAMED ENTITY RECOGNITION** 

Problem formulation, label engineering, anotasi, pemodelan, evaluasi, dan deployment 

|**MATA KULIAH**|**Pemrosesan Bahasa Alami**|
|---|---|
|**JENIS TUGAS**|Proyek kelompok terintegrasi UTS dan UAS|
|**SEMESTER**|Gasal Tahun Akademik 2026/2027|
|**DOSEN PENGAMPU**|Theresia Devi Indriasari, Ph.D., dan Yohanes Sigit Purnomo W.P., Ph.D.|



### **Panduan Singkat Proyek** 

Proyek ini merupakan satu pipeline NLP yang berkesinambungan. Pada UTS, setiap kelompok memilih satu dataset, menganalisis domain dan karakteristik teks, mendefinisikan taxonomy multilabel dan taxonomy NER, kemudian membangun gold dataset melalui anotasi, inter-annotator agreement, adjudication, dan EDA. Pada UAS, gold dataset tersebut digunakan untuk membangun dan mengevaluasi model Multilabel Text Classification serta Named Entity Recognition (NER), lalu mengintegrasikan model terbaik ke dalam aplikasi Streamlit. 

|**Tahap**|**Fokus Utama**|
|---|---|
|UTS|Problem formulation, data cleaning, label taxonomy, annotation guideline, anotasi, agreement,<br>adjudication, EDA, dan dataset explorer.|
|UAS|Multilabel modeling, NER modeling, evaluasi, error analysis, penyimpanan model, dan<br>deployment terintegrasi.|



Proyek UTS-UAS  |  Pemrosesan Bahasa Alami  |  Gasal 2026/2027 

**PROYEK UTS-UAS  •  PEMROSESAN BAHASA ALAMI** 

# **1. Gambaran Umum dan Capaian Pembelajaran** 

Dalam proyek ini, mahasiswa tidak hanya melatih model pada label yang sudah tersedia. Setiap kelompok harus terlebih dahulu memahami domain dan pola teks, kemudian merumuskan dua permasalahan NLP yang saling terkait: klasifikasi multilabel pada level teks dan Named Entity Recognition (NER) pada level span. Hasil formulasi tersebut dituangkan menjadi taxonomy label dan annotation guideline yang menjadi dasar proses anotasi dan pemodelan. 

Gold dataset hasil UTS menjadi basis utama pemodelan UAS. Karena itu, kualitas taxonomy, konsistensi anotasi, validitas agreement, dan proses adjudication diperlakukan sebagai bagian dari rekayasa NLP, bukan sekadar tahap persiapan data. 

### **Capaian Pembelajaran** 

1. (CPMK1) Mahasiswa mampu mengkombinasikan ilmu pengetahuan domain, informatika, dan/atau prinsip rekayasa untuk menyelesaikan masalah di bidang pemrosesan bahasa alami dengan benar dan terukur (CPL1). 

2. (CPMK2) Mahasiswa mampu melakukan identifikasi, formulasi, dan analisis masalah rekayasa pada bidang pemrosesan bahasa alami dengan benar dan terukur (CPL4). 

#### **Setelah menyelesaikan proyek, mahasiswa diharapkan mampu:** 

- memformulasikan permasalahan NLP berdasarkan karakteristik domain dan data; 

- merancang taxonomy multilabel dan taxonomy entity/span yang jelas, tidak redundan, dan dapat dianotasi secara konsisten; 

- mengembangkan gold dataset melalui annotation guideline, inter-annotator agreement, dan adjudication; 

- membangun serta mengevaluasi model Multilabel Text Classification dan NER; 

- melakukan error analysis berbasis bukti serta menghubungkan prediksi level teks dengan evidence pada level span; 

- mengintegrasikan model terbaik ke dalam aplikasi Streamlit yang dapat dijalankan kembali. 

### **Alur Proyek** 

Dataset terpilih 

- -> Domain analysis & problem formulation 

- -> Cleaning & sampling 

- -> Multilabel taxonomy + NER taxonomy 

- -> Annotation guideline 

- -> Annotation 

- -> Agreement + adjudication 

- -> GOLD DATASET (UTS) 

- -> Train / validation / test split 

- -> Multilabel model + NER model 

- -> Evaluation + error analysis 

- -> STREAMLIT DEPLOYMENT (UAS) 

# **2. Ketentuan Umum** 

- Tugas dikerjakan secara berkelompok dengan maksimal 3 mahasiswa per kelompok, kecuali ditentukan berbeda oleh dosen pengampu. 

- Satu kelompok menggunakan satu dataset yang sama sejak UTS sampai UAS. Pergantian dataset setelah UTS hanya diperbolehkan dengan persetujuan dosen. 

- Setiap kelompok wajib mendefinisikan sendiri skema label multilabel dan skema entity/span NER berdasarkan karakteristik dataset yang dipilih. 

- Label asli dataset boleh digunakan sebagai referensi awal, tetapi tidak boleh langsung menjadi satu-satunya skema proyek tanpa analisis, reformulasi, dan justifikasi. 

- Notebook harus dapat dijalankan ulang dari awal sampai akhir. Setiap tahap utama harus dilengkapi penjelasan Markdown mengenai tujuan, keputusan teknis, dan interpretasi hasil. 

- Jika menggunakan pretrained model, library eksternal, dataset tambahan, atau kode referensi, sumber dan alasan penggunaannya wajib dituliskan. 

Proyek UTS-UAS  |  Pemrosesan Bahasa Alami  |  Gasal 2026/2027 

**PROYEK UTS-UAS  •  PEMROSESAN BAHASA ALAMI** 

- Penggunaan AI generatif sebagai alat bantu diperbolehkan. Kelompok tetap bertanggung jawab penuh atas kebenaran, orisinalitas, dan pemahaman terhadap dataset, anotasi, kode, serta hasil eksperimen. 

# **3. Pilihan Dataset** 

Setiap kelompok memilih satu dataset dari daftar berikut. Pembagian dataset dapat diatur oleh dosen agar topik antar kelompok tetap beragam. Dataset berfungsi sebagai bahan dasar proyek; taxonomy label akhir tetap harus diturunkan dari analisis isi data. 

|**No.**|**Nama Dataset**|**Sumber**|
|---|---|---|
|1|NusaX-Senti|Repository|
|2|Emotion Classification on Indonesian Twitter Dataset|Train|Validation |Test|
|3|EmotCMT|Repository|
|4|Emotion ID Opinion|Repository|
|5|HoASA|Train|Validation |Test|
|6|Indonesian Abusive Language Detection Dataset|Dataset|
|7|id_abusive_news_comment|Repository|
|8|Indonesian Google Play Review - e-commerce app|Train|Validation|
|9|Multi-label Hate Speech and Abusive Language Detection in Indonesian<br>Twitter|Dataset|
|10|Stance Classification Towards Political Figures on Blog Writing|Repository|
|11|Customer Review (Natasha Skincare)|Dataset|
|12|SmSA - sentence-level sentiment analysis|Train|Validation |Test|



#### Prinsip pemilihan dataset: 

Dataset dipilih sebagai bahan dasar, bukan sebagai pembatas skema label. Kelompok harus mengeksplorasi corpus terlebih dahulu, menunjukkan contoh evidence dari data, lalu mengusulkan taxonomy multilabel dan NER yang dapat dipertanggungjawabkan. Jika tautan pada daftar resmi/LMS diperbarui, gunakan versi terbaru yang diberikan dosen. 

Proyek UTS-UAS  |  Pemrosesan Bahasa Alami  |  Gasal 2026/2027 

**PROYEK UTS-UAS  •  PEMROSESAN BAHASA ALAMI** 

# **4. BAGIAN I - PROYEK UTS: DATASET DEVELOPMENT DAN ANOTASI** 

### **4.1 Fokus dan Target UTS** 

UTS berfokus pada pembangunan gold dataset yang valid, terdokumentasi, dan siap digunakan pada UAS. Nilai tidak hanya ditentukan oleh jumlah data atau kelengkapan anotasi, tetapi juga oleh ketepatan problem formulation, kualitas taxonomy label, konsistensi annotation guideline, kualitas agreement, dan proses adjudication. 

### **4.2 Dataset Selection dan Domain Analysis** 

Awali proyek dengan memahami dataset sebagai data nyata, bukan sekadar file yang akan diproses. Notebook dan laporan minimal harus menjelaskan: 

- sumber dan tujuan awal dataset; 

- bahasa serta domain data; 

- jumlah data dan struktur kolom; 

- label asli jika tersedia; 

- distribusi awal data; 

- masalah kualitas data yang ditemukan; 

- potensi pengembangan dataset menjadi permasalahan multilabel dan NER. 

### **4.3 Data Cleaning dan Kriteria Minimum** 

Cleaning minimal mencakup pemeriksaan missing values, duplicate text, empty text, karakter atau markup yang tidak relevan, URL/HTML jika diperlukan, spasi/encoding, dan teks yang terlalu pendek. Setiap perubahan harus dapat dilacak dan dijelaskan. 

#### Jumlah data: 

Target dataset final untuk anotasi adalah minimal 800 teks unik. Jika dataset asal setelah cleaning tidak mencapai 800 teks yang layak, gunakan seluruh data yang tersedia dan konsultasikan dengan dosen. Untuk dataset yang sangat besar, sampling diperbolehkan selama metode sampling dijelaskan dan distribusi utama tetap terwakili. 

### **4.4 Perancangan Skema Label** 

Taxonomy tidak diberikan sebagai label final. Kelompok harus merancang label berdasarkan pola yang benar-benar ditemukan pada data. Label yang baik memiliki batas konseptual yang jelas, tidak tumpang tindih secara tidak perlu, cukup terwakili dalam corpus, dan dapat diterapkan secara konsisten oleh annotator yang berbeda. 

#### **4.4.1 Skema A - Multilabel Text Classification** 

Label berada pada level teks/dokumen dan satu teks dapat menerima lebih dari satu label. Sebagai pedoman, rancang sekitar 5-12 label yang relevan. Label OTHER/OUT_OF_SCOPE hanya digunakan bila diperlukan dan tidak boleh menjadi jalan pintas untuk kasus yang sebenarnya dapat didefinisikan lebih jelas. 

|**Komponen**|**Isi yang Wajib Didefinisikan**|
|---|---|
|Label|Nama label yang singkat, konsisten, dan tidak ambigu.|
|Definisi operasional|Makna label dalam konteks domain dataset.|
|Inclusion rule|Kondisi ketika label harus diberikan.|
|Exclusion rule|Kondisi ketika label tidak boleh diberikan.|
|Positive example|Contoh teks yang termasuk label.|
|Negative example|Contoh teks yang tidak termasuk label.|
|Ambiguous case|Contoh kasus ambigu beserta keputusan anotasinya.|



Proyek UTS-UAS  |  Pemrosesan Bahasa Alami  |  Gasal 2026/2027 

**PROYEK UTS-UAS  •  PEMROSESAN BAHASA ALAMI** 

#### Contoh: 

Teks: "Aplikasinya mudah digunakan tetapi proses pembayarannya lambat." -> Label: [USABILITY_POSITIVE, PAYMENT_NEGATIVE]. 

#### **4.4.2 Skema B - Named Entity Recognition / Span Classification** 

NER pada proyek ini tidak dibatasi pada named entity klasik seperti PERSON, LOCATION, atau ORGANIZATION. Entity/span dapat berupa aspect, target, emotion trigger, abusive expression, product feature, issue, political actor, service, event, atau jenis span lain yang relevan dengan domain dataset. 

Kelompok disarankan mendefinisikan sekitar 3-8 entity/span types. Gunakan BIO sebagai skema tag minimum; BIOES atau BILOU diperbolehkan selama diterapkan secara konsisten dan dijelaskan pada guideline. 

#### Contoh: 

Teks: "Pelayanannya ramah tetapi harga makanannya mahal."  |  Pelayanannya ramah -> SERVICE_POSITIF | harga makanannya mahal -> PRICE_NEGATIF. 

#### **4.4.3 Hubungan Multilabel dan NER** 

Kedua taxonomy harus saling berhubungan secara konseptual. Multilabel menjawab pertanyaan "fenomena apa saja yang terdapat dalam teks ini?", sedangkan NER menjawab "bagian teks mana yang menjadi evidence atau representasi fenomena tersebut?". Hubungan ini tidak harus satu-ke-satu, tetapi harus dapat dijelaskan dengan contoh dari corpus. Contoh hubungan 

Teks: "Tempatnya nyaman tetapi parkirnya sempit." 

-> Multilabel: [PLACE_POSITIVE, FACILITY_NEGATIVE]. NER: "Tempatnya nyaman" -> PLACE_POSITIVE; " parkirnya sempit " -> FACILITY_ NEGATIVE. 

##### **Wajib:** 

Sebelum anotasi skala penuh, kelompok mendiskusikan 1x rancangan taxonomy multilabel, taxonomy NER, definisi label, aturan boundary span, dan contoh anotasi untuk ditinjau dosen. Saran atau masukan dari dosen bisa diperbaiki dan disetujui seluruh anggota kelompok dalam bentuk annotation guidlines. Setelah disetujui, taxonomy dinyatakan freeze. Perubahan substansial sesudahnya harus disertai alasan, catatan versi, dan persetujuan dosen. 

### **4.5 Annotation Guideline** 

Kelompok wajib menyusun KelpX_annotation_guideline.pdf. Dokumen harus cukup jelas sehingga annotator baru dapat menerapkan aturan tanpa penjelasan tambahan yang panjang. Minimal memuat: 

- definisi seluruh label multilabel; 

- definisi seluruh entity/span NER; 

- aturan pemberian multilabel; 

- aturan penentuan boundary span; 

- aturan untuk kasus ambigu dan konflik antarlabel; 

- minimal 2-3 contoh untuk setiap label/entity; 

- aturan untuk teks yang tidak relevan, tidak jelas, atau tidak dapat dianotasi. 

### **4.6 Proses Anotasi** 

Anotasi dapat dilakukan menggunakan Prodigy, Label Studio, Doccano, atau annotation tool lain yang disetujui. Setiap baris data minimal memiliki teks, label multilabel, dan daftar entities/spans. Seluruh anggota kelompok harus memiliki kontribusi anotasi yang jelas dan dapat ditelusuri. 

Proyek UTS-UAS  |  Pemrosesan Bahasa Alami  |  Gasal 2026/2027 

**PROYEK UTS-UAS  •  PEMROSESAN BAHASA ALAMI** 

{ "text": "Aplikasinya bagus tetapi sering crash", "labels": ["USABILITY_POSITIVE", "PERFORMANCE_NEGATIVE"], "entities": [ {"text": "Aplikasinya bagus", "label": " USABILITY_POSITIVE"}, {"text": "sering crash", "label": " PERFORMANCE_NEGATIVE"} ] } 

### **4.7 Inter-Annotator Agreement dan Adjudication** 

Gunakan sebagian data sebagai overlap annotation yang dikerjakan oleh lebih dari satu annotator sehingga tingkat kesepakatan dapat dihitung. Subset overlap harus cukup untuk mewakili label utama dan dijelaskan dalam laporan. Setelah agreement dihitung, kelompok wajib meninjau disagreement dan melakukan adjudication untuk menghasilkan satu versi gold dataset. 

**Ukuran yang dapat digunakan:** 

- Multilabel: Cohen's Kappa, Fleiss' Kappa, Krippendorff's Alpha, atau ukuran agreement lain yang relevan. 

- NER: span agreement, entity-level precision/recall/F1 antarannotator, token agreement, atau ukuran lain yang relevan. 

Laporan harus memuat nilai agreement, interpretasi, contoh disagreement, keputusan adjudication, serta perubahan guideline apabila dilakukan. 

### **4.8 Exploratory Data Analysis (EDA)** 

EDA dilakukan setelah dataset final tersedia. Visualisasi harus membantu menjawab apakah distribusi label cukup layak untuk pemodelan dan di mana potensi imbalance berada. 

|**Multilabel**|**NER**|
|---|---|
|Jumlah teks dan distribusi panjang teks|Distribusi jumlah token per teks|
|Distribusi setiap label|Jumlah entity/span setiap jenis|
|Jumlah label per teks|Jumlah entity/span per teks|
|Label co-occurrence|Distribusi panjang entity/span|
|Correlation matrix antarlabel|Contoh entity/span yang paling sering muncul|
|Analisis imbalance ratio|Analisis dominasi label O dan imbalance entity|



### **4.9 Aplikasi Streamlit UTS - Dataset Explorer** 

Aplikasi UTS berfungsi sebagai dataset explorer, bukan aplikasi prediksi. Minimal menyediakan: 

- Overview: ringkasan dataset dan taxonomy label; 

- Browse Data: menampilkan teks beserta anotasi multilabel dan span; 

- Multilabel Analysis: distribusi label, kombinasi label, dan filter; 

- NER Analysis: distribusi entity serta contoh span yang di-highlight; 

- Filter/Search: pencarian teks dan filter berdasarkan label atau entity. 

Proyek UTS-UAS  |  Pemrosesan Bahasa Alami  |  Gasal 2026/2027 

**PROYEK UTS-UAS  •  PEMROSESAN BAHASA ALAMI** 

### **4.10 Output Wajib Proyek UTS** 

1. Dataset asli: KelpX_dataset_original.* 

2. Dataset hasil cleaning: KelpX_dataset_clean.csv 

3. Dataset hasil anotasi dan adjudication: KelpX_dataset_annotation.jsonl 

4. Annotation guideline: KelpX_annotation_guideline.pdf 

5. Notebook cleaning + EDA: KelpX_dataset_EDA.ipynb 

6. Aplikasi dataset explorer: KelpX_dataset_explorer.py 

7. Laporan UTS: KelpX_laporan_UTS.pdf 

8. Export kode: KelpX_code_export_UTS.pdf 

9. File anggota dan tautan: KelpX_anggota.txt 

10. Seluruh file dikompres menjadi satu ZIP. 

#### **Struktur Folder yang Disarankan** 

project_uts/ |-- dataset/ |   |-- KelpX_dataset_original.* |   |-- KelpX_dataset_clean.csv |   `-- KelpX_dataset_annotation.jsonl |-- notebook/ |   `-- KelpX_dataset_EDA.ipynb |-- guideline/ |   `-- KelpX_annotation_guideline.pdf |-- streamlit/ |   `-- KelpX_dataset_explorer.py |-- report/ |   `-- KelpX_laporan_UTS.pdf |-- code_pdf/ |   `-- KelpX_code_export_UTS.pdf `-- KelpX_anggota.txt 

Proyek UTS-UAS  |  Pemrosesan Bahasa Alami  |  Gasal 2026/2027 

**PROYEK UTS-UAS  •  PEMROSESAN BAHASA ALAMI** 

# **5. RUBRIK PENILAIAN UTS - DETAIL** 

Penilaian UTS menggunakan delapan kriteria dengan total bobot 100%. Setiap kriteria diberi skor 1-5. Nilai akhir dihitung dengan rumus: 

##### **Rumus nilai UTS** 

Nilai UTS = jumlah dari [(Skor kriteria / 5) x Bobot kriteria]. Dengan demikian, skor 5 pada seluruh kriteria menghasilkan nilai 100. 

|**Kriteria**|**Bobot**|**Fokus Penilaian**|
|---|---|---|
|Dataset Selection & Problem Formulation|10%|Pemahaman domain, karakteristik corpus, dan perumusan dua<br>masalah NLP yang saling terkait.|
|Data Cleaning & Preparation|10%|Kualitas, keterlacakan, dan reproducibility proses cleaning<br>tanpa merusak informasi penting untuk NER.|
|Multilabel Taxonomy Design|15%|Kualitas label level teks, definisi operasional, rules, contoh,<br>dan relevansi terhadap corpus.|
|NER Taxonomy & Annotation Guideline|15%|Kualitas entity/span types, boundary rules,<br>BIO/BIOES/BILOU, dan kelengkapan guideline.|
|Annotation Process & Adjudication|15%|Konsistensi proses anotasi, kontribusi anggota, conflict<br>handling, dan pembentukan gold dataset.|
|Inter-Annotator Agreement|10%|Ketepatan metode agreement, interpretasi, disagreement<br>analysis, dan penggunaan hasil untuk memperbaiki anotasi.|
|EDA Multilabel & NER|15%|Kelengkapan EDA, visualisasi, imbalance analysis, serta<br>interpretasi karakteristik label dan entity.|
|Dataset Explorer & Reproducibility|10%|Fungsionalitas Streamlit, kemudahan eksplorasi dataset, dan<br>kemampuan notebook/aplikasi dijalankan ulang.|



##### **5.1 Dataset Selection & Problem Formulation** 

##### **Bobot 10%** 

**Indikator yang dinilai:** dataset berasal dari daftar resmi dan sumbernya terdokumentasi; struktur, ukuran, bahasa, domain, dan label asli dianalisis; masalah kualitas data awal diidentifikasi; masalah multilabel dan NER dirumuskan secara jelas; hubungan kedua tugas didukung contoh nyata dari corpus. 

|**Skor**|**Deskripsi Capaian**|
|---|---|
|5|Analisis dataset lengkap dan berbasis evidence. Problem formulation untuk multilabel dan NER jelas, relevan<br>dengan domain, berbeda secara konseptual tetapi saling terkait, serta didukung contoh data yang representatif.<br>Asumsi dan batasan masalah dijelaskan.|
|4|Analisis domain dan problem formulation sudah kuat. Kedua tugas telah dirumuskan dan dihubungkan dengan<br>corpus, tetapi masih terdapat satu atau dua kekurangan minor pada justifikasi, contoh evidence, atau pembahasan<br>batasan.|
|3|Karakteristik dasar dataset dijelaskan dan dua tugas NLP telah dirumuskan, tetapi analisis domain masih deskriptif.<br>Hubungan multilabel-NER atau justifikasi label masih terbatas dan hanya didukung sedikit contoh.|
|2|Analisis dataset sangat minimal. Salah satu tugas NLP tidak dirumuskan dengan jelas, hubungan antara multilabel<br>dan NER lemah, atau label diusulkan tanpa bukti yang memadai dari corpus.|
|1|Dataset tidak sesuai/ tidak terdokumentasi, problem formulation tidak tersedia, atau tugas yang dirumuskan tidak<br>merepresentasikan multilabel dan NER sebagaimana diminta.|



Proyek UTS-UAS  |  Pemrosesan Bahasa Alami  |  Gasal 2026/2027 

**PROYEK UTS-UAS  •  PEMROSESAN BAHASA ALAMI** 

##### **5.2 Data Cleaning & Preparation** 

##### **Bobot 10%** 

**Indikator yang dinilai:** missing/empty/duplicate text diperiksa; perubahan jumlah data sebelum-sesudah cleaning dilaporkan; normalisasi dan penghapusan noise dijelaskan; teks asli/offset NER tetap dapat ditelusuri; pipeline cleaning dapat dijalankan ulang. 

|**Skor**|**Deskripsi Capaian**|
|---|---|
|5|Pipeline cleaning lengkap, reproducible, dan terdokumentasi. Setiap keputusan cleaning memiliki alasan, statistik<br>sebelum-sesudah tersedia, deduplikasi/invalid data ditangani, serta perubahan tidak merusak informasi token/span<br>yang dibutuhkan NER.|
|4|Cleaning sudah sistematis dan dapat diulang. Hampir seluruh pemeriksaan kualitas dilakukan, namun ada<br>dokumentasi minor yang belum lengkap, misalnya statistik perubahan atau alasan satu tahap normalisasi.|
|3|Cleaning dasar dilakukan dengan benar, tetapi belum sepenuhnya reproducible atau tidak semua perubahan tercatat.<br>Risiko perubahan offset/span sudah disadari namun pengendaliannya belum konsisten.|
|2|Cleaning dilakukan secara ad hoc/manual, dokumentasi minim, statistik perubahan tidak tersedia, atau terdapat<br>transformasi yang berpotensi merusak teks/offset NER.|
|1|Tidak ada proses cleaning yang dapat dinilai, atau cleaning menyebabkan kehilangan/kerusakan data secara serius<br>tanpa mekanisme pelacakan.|



##### **5.3 Multilabel Taxonomy Design Bobot 15%** 

**Indikator yang dinilai:** taxonomy diturunkan dari corpus, bukan sekadar menyalin label asli; satu teks dapat menerima lebih dari satu label; definisi operasional dan inclusion/exclusion rule tersedia; positive, negative, dan ambiguous examples tersedia; overlap antarlabel dan OUT_OF_SCOPE ditangani dengan aturan jelas. 

|**Skor**|**Deskripsi Capaian**|
|---|---|
|5|Taxonomy multilabel sangat jelas dan sesuai corpus. Label cukup spesifik, dapat muncul bersama bila relevan,<br>tidak redundan secara tidak perlu, dan seluruh label memiliki definisi operasional, inclusion/exclusion rule, serta<br>contoh positif, negatif, dan ambigu yang konsisten.|
|4|Taxonomy sudah kuat dan dapat digunakan untuk anotasi. Mayoritas label memiliki batas yang jelas, tetapi masih<br>ada sedikit overlap konseptual, aturan pengecualian yang kurang tegas, atau contoh ambigu yang belum lengkap.|
|3|Taxonomy secara umum relevan dan multilabel, tetapi beberapa label masih terlalu umum/tumpang tindih. Definisi<br>dan contoh tersedia namun belum cukup untuk mengatasi kasus sulit secara konsisten.|
|2|Label sebagian besar diambil langsung dari label asli atau dirancang tanpa eksplorasi corpus yang memadai.<br>Beberapa label ambigu, tidak benar-benar multilabel, atau aturan anotasinya sangat terbatas.|
|1|Tidak ada taxonomy multilabel yang valid, label tidak dapat dianotasi secara konsisten, atau skema pada praktiknya<br>merupakan single-label classification.|



|**5.4 NER Taxonomy & Annotation Guideline**|**Bobot 15%**|
|---|---|



**Indikator yang dinilai:** entity/span types relevan dengan domain; aturan boundary untuk multiword, punctuation, repetition, dan kasus ambigu tersedia; skema BIO/BIOES/BILOU didefinisikan; alignment span/token dapat dipertanggungjawabkan; guideline memuat contoh jelas, negatif, dan ambigu. 

**Skor** 

**Deskripsi Capaian** 

Proyek UTS-UAS  |  Pemrosesan Bahasa Alami  |  Gasal 2026/2027 

**PROYEK UTS-UAS  •  PEMROSESAN BAHASA ALAMI** 

|**Skor**|**Deskripsi Capaian**|
|---|---|
|5|Taxonomy NER relevan, dapat dilatih, dan didukung guideline rinci. Boundary rules jelas untuk kasus umum<br>maupun sulit; skema tagging konsisten; contoh anotasi menunjukkan penggunaan entity type dan span secara tepat;<br>aturan ambigu/overlap/nesting dibahas sesuai kebutuhan corpus.|
|4|Entity types dan guideline sudah baik serta dapat digunakan. Hanya terdapat kekurangan minor pada aturan<br>boundary tertentu, kasus ambigu, atau konsistensi contoh.|
|3|Entity types cukup relevan, tetapi guideline terutama mencakup kasus mudah. Aturan boundary, overlap, atau<br>mapping ke BIO/BIOES/BILOU belum lengkap sehingga masih berpotensi menimbulkan inkonsistensi.|
|2|Entity/span types kurang jelas, sebagian bersifat terlalu luas/sempit, dan aturan boundary sangat terbatas. Contoh<br>anotasi sedikit atau tidak konsisten.|
|1|Tidak tersedia taxonomy NER/span yang dapat dinilai, atau anotasi tidak berbasis span/token sehingga tidak dapat<br>digunakan untuk pelatihan NER.|



|**5.5 Annotation Process & Adjudication**|**Bobot 15%**|
|---|---|



**Indikator yang dinilai:** tool dan alur anotasi terdokumentasi; kontribusi annotator dapat ditelusuri; overlap annotation tersedia; disagreement dicatat dan ditinjau; adjudication menghasilkan satu gold dataset final dengan span valid. 

|**Skor**|**Deskripsi Capaian**|
|---|---|
|5|Proses anotasi terstruktur dan terdokumentasi. Kontribusi anggota jelas, overlap annotation tersedia, disagreement<br>ditinjau menggunakan guideline, keputusan adjudication dicatat, dan gold dataset final konsisten serta lolos validasi<br>format/span.|
|4|Anotasi dan adjudication berjalan baik dengan bukti yang cukup. Terdapat kekurangan minor pada pencatatan<br>versi, dokumentasi konflik, atau pembagian kontribusi.|
|3|Anotasi selesai tetapi proses adjudication masih informal, overlap terbatas, atau keputusan konflik tidak selalu<br>terdokumentasi. Gold dataset tersedia tetapi masih memerlukan validasi tambahan.|
|2|Anotasi tidak konsisten, kontribusi tidak jelas, overlap annotation sangat terbatas, atau konflik antarannotator tidak<br>diselesaikan secara sistematis.|
|1|Dataset tidak dianotasi secara memadai, tidak ada adjudication, atau hasil akhir tidak dapat digunakan sebagai gold<br>dataset.|



|**5.6 Inter-Annotator Agreement**|**Bobot 10%**|
|---|---|



**Indikator yang dinilai:** metode agreement sesuai dengan tipe anotasi; subset overlap dijelaskan dan mencakup label/entity penting; nilai agregat dan/atau per-label/per-entity dilaporkan; hasil diinterpretasikan dengan benar; disagreement digunakan untuk memperbaiki guideline/anotasi. 

|**Skor**|**Deskripsi Capaian**|
|---|---|
|5|Agreement dihitung dengan metode yang tepat untuk multilabel dan NER, data overlap dijelaskan, hasil dilaporkan<br>secara transparan, serta disagreement dianalisis. Nilai agreement digunakan sebagai evidence untuk revisi guideline<br>atau adjudication bila diperlukan.|
|4|Perhitungan agreement benar dan interpretasi cukup baik, tetapi analisis per-label/per-entity atau hubungan hasil<br>dengan revisi guideline belum sepenuhnya lengkap.|
|3|Agreement dihitung dan dilaporkan, tetapi hanya secara agregat atau hanya kuat pada salah satu jenis anotasi.<br>Interpretasi dan analisis disagreement masih terbatas.|



Proyek UTS-UAS  |  Pemrosesan Bahasa Alami  |  Gasal 2026/2027 

**PROYEK UTS-UAS  •  PEMROSESAN BAHASA ALAMI** 

|**Skor**|**Deskripsi Capaian**|
|---|---|
|2|Metode agreement kurang sesuai, subset overlap tidak jelas, atau hasil hanya ditampilkan tanpa interpretasi yang<br>memadai.|
|1|Tidak ada perhitungan inter-annotator agreement yang dapat dinilai atau perhitungannya tidak valid.|



##### **5.7 EDA Multilabel & NER Bobot 15%** 

**Indikator yang dinilai:** distribusi panjang teks/token dianalisis; distribusi label dan jumlah label per teks dianalisis; cooccurrence/correlation dan imbalance multilabel dibahas; distribusi entity/span, entity per teks, dan panjang span dianalisis; visualisasi disertai interpretasi dan implikasi untuk modeling. 

|**Skor**|**Deskripsi Capaian**|
|---|---|
|5|EDA multilabel dan NER lengkap, visualisasi jelas, serta setiap temuan utama diinterpretasikan. Analisis<br>menunjukkan co-occurrence, imbalance, distribusi entity/span, dan karakteristik panjang teks/token yang relevan<br>untuk keputusan modeling pada UAS.|
|4|Hampir seluruh EDA wajib tersedia dan interpretasinya baik. Satu atau dua analisis tambahan masih kurang<br>mendalam, tetapi karakteristik utama dataset sudah terlihat jelas.|
|3|Distribusi dasar label dan entity tersedia, tetapi co-occurrence/correlation, imbalance, atau interpretasi implikasi<br>modeling masih terbatas.|
|2|EDA hanya berupa beberapa plot/statistik sederhana tanpa analisis yang memadai atau hanya mencakup salah satu<br>dari multilabel/NER.|
|1|EDA tidak tersedia, tidak relevan, atau output tidak dapat digunakan untuk memahami kualitas dan distribusi<br>dataset.|



##### **5.8 Dataset Explorer & Reproducibility Bobot 10%** 

**Indikator yang dinilai:** Streamlit dapat dijalankan tanpa error; overview, browse, filter/search, analisis multilabel, dan analisis NER tersedia; span dapat ditampilkan/highlight dengan benar; notebook berjalan dari awal sampai akhir tanpa langkah manual tersembunyi; path, dependency, dan file input terdokumentasi. 

|**Skor**|**Deskripsi Capaian**|
|---|---|
|5|Dataset explorer berfungsi penuh dan mudah digunakan. Dataset dapat ditelusuri, difilter, dan dianalisis; span/label<br>ditampilkan dengan benar. Notebook dan aplikasi dapat dijalankan ulang menggunakan struktur file yang<br>diserahkan tanpa hard-coded path yang menghambat reproducibility.|
|4|Aplikasi dan notebook dapat dijalankan dengan baik. Sebagian besar fitur eksplorasi tersedia, dengan kekurangan<br>minor pada tampilan, filter, dokumentasi dependency, atau penggunaan path.|
|3|Dataset explorer dapat dijalankan tetapi fitur masih dasar atau beberapa komponen analisis/visualisasi belum<br>lengkap. Notebook memerlukan sedikit penyesuaian manual untuk direproduksi.|
|2|Aplikasi hanya berjalan sebagian, beberapa fitur utama error/tidak tersedia, atau notebook sangat bergantung pada<br>path/konfigurasi lokal yang tidak didokumentasikan.|
|1|Aplikasi/notebook tidak dapat dijalankan atau bukti reproducibility tidak tersedia.|



Proyek UTS-UAS  |  Pemrosesan Bahasa Alami  |  Gasal 2026/2027 

**PROYEK UTS-UAS  •  PEMROSESAN BAHASA ALAMI** 

# **6. BAGIAN II - PROYEK UAS: MULTILABEL CLASSIFICATION DAN NER MODELING** 

### **6.1 Prinsip Continuity dari UTS ke UAS** 

Dataset hasil adjudication UTS menjadi gold dataset UAS. Taxonomy yang telah disahkan pada UTS tetap digunakan pada UAS. Perubahan label setelah proses split atau training hanya diperbolehkan jika ditemukan masalah metodologis yang substansial dan harus memperoleh persetujuan dosen. 

### **6.2 Proyek A - Multilabel Text Classification** 

Tujuan proyek A adalah membangun model yang menerima satu teks dan menghasilkan satu atau lebih label dari taxonomy multilabel UTS. 

Input: teks Output : [label_1, label_2, ..., label_n] 

#### **6.2.1 Data Preparation** 

- membaca gold dataset UTS dari file eksternal; 

- melakukan multilabel encoding; 

- memeriksa label imbalance; 

- membagi data menjadi train/validation/test secara terdokumentasi; 

- mencegah duplicate leakage atau text leakage antar split; 

- menggunakan multilabel stratification apabila sesuai dan memungkinkan. 

_Proporsi yang disarankan adalah 70% train, 15% validation, dan 15% test. Proporsi lain diperbolehkan bila dijustifikasi._ 

#### **6.2.2 Representasi Teks dan Model** 

Kelompok wajib membandingkan minimal dua representasi/pendekatan teks, misalnya TF-IDF, n-gram, FastText/embedding, transformer embedding, atau transformer fine-tuning. Minimal dua algoritma/model dibandingkan. Jika menggunakan problem transformation, dapat memilih Binary Relevance, Classifier Chain, Label Powerset, atau pendekatan relevan lainnya. 

#### **6.2.3 Evaluasi Multilabel** 

Evaluasi minimal memuat classification report per label, micro-F1, macro-F1, weighted-F1, Hamming Loss, dan subset accuracy atau metrik relevan lain yang dijelaskan. Kelompok juga wajib melakukan error analysis dengan membandingkan ground truth dan prediksi pada beberapa kasus yang representatif. 

### **6.3 Proyek B - Named Entity Recognition** 

Tujuan proyek B adalah membangun model yang mengenali entity/span pada teks menggunakan taxonomy NER hasil UTS. Anotasi span dikonversi menjadi BIO/BIOES/BILOU secara konsisten. 

#### **6.3.1 Tokenization dan Alignment** 

- tokenizer dan unit token dijelaskan; 

- span dikonversi ke tag token-level dengan benar; 

- word-to-subword alignment diverifikasi bila menggunakan transformer; 

- special token, padding, truncation, dan attention mask ditangani; 

- tag mapping dan label ID terdokumentasi. 

Proyek UTS-UAS  |  Pemrosesan Bahasa Alami  |  Gasal 2026/2027 

**PROYEK UTS-UAS  •  PEMROSESAN BAHASA ALAMI** 

#### **6.3.2 Model NER** 

Minimal satu model NER berbasis machine/deep learning wajib dibangun, misalnya CRF, BiLSTM, BiLSTM-CRF, IndoBERT Token Classification, mBERT, XLM-R, atau model lain yang relevan. Untuk capaian terbaik, disarankan membandingkan baseline dengan model yang lebih kuat. 

#### **6.3.3 Evaluasi NER** 

Evaluasi minimal memuat entity-level precision, recall, dan F1-score, F1 per entity type, serta contoh prediksi benar dan salah. Error analysis harus membedakan setidaknya boundary error dan label error. Token-level metrics dapat ditambahkan, tetapi tidak menggantikan entity/span-level evaluation. 

### **6.4 Analisis Hubungan Kedua Model** 

Kelompok wajib membandingkan output Multilabel Model dan NER Model pada contoh teks yang sama. Analisis harus membahas apakah kedua output konsisten, sebagian konsisten, atau kontradiktif, dan menjelaskan kemungkinan penyebabnya. 

##### **Contoh** 

Teks: "Harganya mahal tetapi makanannya enak." -> Multilabel: [PRICE_NEGATIVE, PRODUCT_POSITIVE]. NER: "Harganya mahal" -> PRICE_ NEGATIVE; "makanannya enak " -> PRODUCT_POSITIVE. 

### **6.5 Deployment UAS** 

Aplikasi Streamlit minimal memiliki dua menu: Prediksi Multilabel dan Prediksi NER. Sangat dianjurkan menambahkan menu Integrated Analysis yang menampilkan hasil kedua model untuk teks yang sama. 

|**Menu**|**Output Minimum**|
|---|---|
|Prediksi Multilabel|Input teks, predicted labels, confidence/probability jika tersedia, threshold jika<br>digunakan, dan interpretasi singkat.|
|Prediksi NER|Input teks, extracted entity/span, label entity, highlight span pada teks, dan interpretasi<br>singkat.|
|Integrated Analysis (disarankan)|Prediksi multilabel + NER pada teks yang sama serta ringkasan konsistensi kedua<br>output.|



Proyek UTS-UAS  |  Pemrosesan Bahasa Alami  |  Gasal 2026/2027 

**PROYEK UTS-UAS  •  PEMROSESAN BAHASA ALAMI** 

### **6.6 Output Wajib Proyek UAS** 

1. Dataset split multilabel: KelpX_multilabel_train.csv, KelpX_multilabel_val.csv, KelpX_multilabel_test.csv. 

2. Dataset split NER: KelpX_ner_train.jsonl, KelpX_ner_val.jsonl, KelpX_ner_test.jsonl atau format setara yang terdokumentasi. 

3. Notebook Multilabel: KelpX_multilabel_modeling.ipynb. 

4. Notebook NER: KelpX_NER_modeling.ipynb. 

5. Model terbaik Multilabel dan NER dalam format library yang digunakan. 

6. Aplikasi Streamlit: KelpX_NLP_app.py. 

7. Laporan UAS: KelpX_laporan_UAS.pdf. 

8. Export seluruh kode: KelpX_code_export_UAS.pdf. 

9. File anggota, repository, deployment, dan video demo: KelpX_anggota.txt. 

10. Seluruh file dikompres menjadi satu ZIP. 

#### **Struktur Folder yang Disarankan** 

- project_uas/ |-- dataset/ |   |-- KelpX_multilabel_train.csv |   |-- KelpX_multilabel_val.csv |   |-- KelpX_multilabel_test.csv |   |-- KelpX_ner_train.jsonl |   |-- KelpX_ner_val.jsonl |   `-- KelpX_ner_test.jsonl |-- notebook/ |   |-- KelpX_multilabel_modeling.ipynb |   `-- KelpX_NER_modeling.ipynb |-- models/ |   |-- KelpX_best_multilabel_model.* |   `-- KelpX_best_NER_model.* |-- streamlit/ |   `-- KelpX_NLP_app.py |-- report/ |   `-- KelpX_laporan_UAS.pdf |-- code_pdf/ |   `-- KelpX_code_export_UAS.pdf `-- KelpX_anggota.txt 

Proyek UTS-UAS  |  Pemrosesan Bahasa Alami  |  Gasal 2026/2027 

**PROYEK UTS-UAS  •  PEMROSESAN BAHASA ALAMI** 

# **7. RUBRIK PENILAIAN UAS** 

Nilai UAS terdiri dari dua komponen utama: Proyek A - Multilabel Text Classification sebesar 50% dan Proyek B - Named Entity Recognition sebesar 50%. Seperti rubrik UTS, setiap kriteria pada masing-masing proyek diberi skor 1-5 berdasarkan tingkat capaian yang dapat dibuktikan melalui dataset, notebook, hasil eksperimen, evaluasi, laporan, dan deployment. 

|**Komponen**|**Bobot Nilai**<br>**UAS**|**Fokus**|
|---|---|---|
|Proyek A - Multilabel Text Classification|50%|Pemodelan pada level teks/dokumen.|
|Proyek B - Named Entity Recognition|50%|Pemodelan pada level token/span.|



##### **Rumus nilai UAS** 

Nilai Proyek A = jumlah dari [(Skor kriteria / 5) x Bobot internal Proyek A]. Nilai Proyek B dihitung dengan rumus yang sama. Nilai UAS = (0,50 x Nilai Proyek A) + (0,50 x Nilai Proyek B). Skor 5 pada seluruh kriteria menghasilkan nilai 100 untuk proyek tersebut. 

### **7.1 Rubrik Proyek A - Multilabel Text Classification (50% Nilai UAS)** 

|**Kriteria**|**Bobot**|**Fokus Penilaian**|
|---|---|---|
|Data Loading & Validation|10%|Validitas gold dataset, struktur teks-label, dan reproducibility<br>data loading.|
|Preprocessing & Label Engineering|15%|Cleaning terkontrol, multilabel encoding, split, imbalance, dan<br>pencegahan leakage.|
|EDA Multilabel|10%|Distribusi teks/label, label cardinality, co-occurrence, dan<br>imbalance.|
|Text Representation|15%|Perbandingan representasi teks yang adil, terdokumentasi, dan<br>bebas leakage.|
|Model Training & Experiment|20%|Perbandingan model/strategi, validation, tuning, dan<br>pencatatan eksperimen.|
|Evaluation & Error Analysis|20%|Metrik multilabel yang tepat, test-set evaluation, threshold,<br>dan analisis kesalahan.|
|Deployment Multilabel|10%|Prediksi teks baru menggunakan model terbaik dan pipeline<br>inference yang konsisten.|



##### **7.1.1 Data Loading & Validation** 

|**Bobot Internal**|
|---|
|**10%**|



**Indikator yang dinilai:** gold dataset hasil UTS dibaca dari file eksternal; struktur kolom teks dan label diverifikasi; missing value, duplicate text, format label, dan konsistensi jumlah data diperiksa; contoh data serta statistik dasar ditampilkan; seluruh proses loading dapat dijalankan ulang tanpa manipulasi manual tersembunyi. 

|**Skor**|**Deskripsi Capaian**|
|---|---|



Proyek UTS-UAS  |  Pemrosesan Bahasa Alami  |  Gasal 2026/2027 

**PROYEK UTS-UAS  •  PEMROSESAN BAHASA ALAMI** 

|**Skor**|**Deskripsi Capaian**|
|---|---|
|5|Dataset dapat dimuat secara reproducible dan seluruh validasi utama dilakukan dengan bukti output. Struktur teks-<br>label, jumlah data, missing/duplicate, format label, contoh data, serta inkonsistensi dataset diperiksa dan ditangani<br>secara eksplisit. Tidak terdapat langkah manual yang tidak terdokumentasi.|
|4|Dataset dapat dimuat dan hampir seluruh validasi utama tersedia. Terdapat satu kekurangan minor, misalnya<br>statistik validasi tertentu belum lengkap atau penanganan satu jenis inkonsistensi belum dijelaskan secara rinci,<br>tetapi tidak memengaruhi validitas eksperimen.|
|3|Dataset dapat dimuat dan validasi dasar tersedia, tetapi pemeriksaan masih terbatas pada sebagian aspek seperti<br>bentuk data, jumlah baris, dan label. Pemeriksaan duplicate/missing/format label atau dokumentasi inkonsistensi<br>belum memadai.|
|2|Data loading berjalan, tetapi validasi struktur dan kualitas data sangat terbatas, banyak pemeriksaan dilakukan<br>secara implisit, atau terdapat ketidakjelasan mengenai data yang benar-benar digunakan untuk training.|
|1|Dataset tidak dapat dimuat secara konsisten, menggunakan dataset yang berbeda dari gold dataset UTS tanpa<br>persetujuan, atau proses loading/validasi tidak dapat direproduksi.|



##### **Bobot Internal 7.1.2 Preprocessing & Label Engineering 15%** 

**Indikator yang dinilai:** preprocessing dilakukan secara terkontrol dan tidak merusak informasi penting; label multilabel diencode dengan benar; train/validation/test split terdokumentasi; multilabel stratification digunakan bila sesuai; label imbalance dianalisis dan ditangani bila diperlukan; duplicate/text leakage antar split dicegah. 

|**Skor**|**Deskripsi Capaian**|
|---|---|
|5|Preprocessing, encoding, dan pembagian data dilakukan dengan benar dan terdokumentasi. Multilabel encoding<br>konsisten dengan taxonomy UTS, strategi split mempertimbangkan distribusi label, leakage diperiksa, serta<br>keputusan penanganan imbalance dijelaskan dan diterapkan secara tepat.|
|4|Seluruh komponen utama sudah benar, tetapi terdapat satu aspek minor yang kurang lengkap, misalnya analisis<br>imbalance atau dokumentasi stratification belum mendalam. Tidak ditemukan kesalahan yang mengubah validitas<br>eksperimen.|
|3|Encoding label dan split data sudah berjalan, tetapi strategi stratification, imbalance, atau leakage belum dianalisis<br>secara memadai. Preprocessing masih lebih bersifat prosedural daripada berbasis alasan metodologis.|
|2|Preprocessing atau split dilakukan secara ad hoc; dokumentasi train/validation/test tidak jelas; terdapat risiko<br>leakage atau distribusi label yang tidak diperhatikan; atau label engineering belum konsisten.|
|1|Encoding label salah, split tidak valid/tidak reproducible, terjadi leakage yang serius, atau preprocessing<br>menyebabkan data/label tidak lagi konsisten dengan gold dataset.|



##### **7.1.3 EDA Multilabel** 

|**Bobot Internal**|
|---|
|**10%**|



**Indikator yang dinilai:** EDA mencakup panjang teks/token, frekuensi setiap label, jumlah label per teks, kombinasi/cooccurrence label, correlation matrix atau analisis hubungan label yang setara, serta label imbalance; temuan EDA dihubungkan dengan keputusan pemodelan. 

|**Skor**|**Deskripsi Capaian**|
|---|---|



Proyek UTS-UAS  |  Pemrosesan Bahasa Alami  |  Gasal 2026/2027 

**PROYEK UTS-UAS  •  PEMROSESAN BAHASA ALAMI** 

|**Skor**|**Deskripsi Capaian**|
|---|---|
|5|EDA lengkap, visualisasi jelas, dan seluruh temuan utama diinterpretasikan. Distribusi label, jumlah label per teks,<br>co-occurrence/hubungan label, panjang teks, dan imbalance digunakan untuk menjelaskan implikasi terhadap split,<br>threshold, model, atau evaluasi.|
|4|Mayoritas komponen EDA dan interpretasi tersedia. Satu analisis tambahan, misalnya correlation/co-occurrence<br>atau implikasi terhadap pemodelan, belum dibahas secara mendalam.|
|3|EDA dasar tersedia dan benar, tetapi terbatas pada distribusi label dan panjang teks. Analisis multilabel spesifik<br>seperti co-occurrence, jumlah label per teks, atau imbalance masih kurang lengkap.|
|2|Visualisasi hanya sedikit dan sebagian besar bersifat deskriptif tanpa interpretasi yang mendukung keputusan<br>pemodelan.|
|1|EDA tidak dilakukan, tidak relevan dengan data multilabel, atau hasil yang ditampilkan tidak dapat ditelusuri ke<br>dataset yang digunakan.|



##### **7.1.4 Text Representation** 

|**Bobot Internal**|
|---|
|**15%**|



**Indikator yang dinilai:** minimal dua representasi/pendekatan teks dibandingkan; representasi dibangun hanya dari data training untuk mencegah leakage; parameter penting didokumentasikan; pemilihan representasi dijustifikasi berdasarkan karakteristik corpus dan model. 

|**Skor**|**Deskripsi Capaian**|
|---|---|
|5|Minimal dua representasi atau pendekatan teks dibandingkan secara adil pada split yang sama. Pipeline mencegah<br>leakage, parameter/ukuran representasi terdokumentasi, dan analisis menjelaskan kelebihan-kekurangan tiap<br>representasi berdasarkan hasil eksperimen.|
|4|Dua pendekatan dibandingkan dengan implementasi benar, tetapi analisis perbandingan, dokumentasi parameter,<br>atau justifikasi pemilihan representasi masih memiliki kekurangan minor.|
|3|Hanya satu representasi utama digunakan dengan implementasi dan penjelasan yang cukup, atau dua representasi<br>digunakan tetapi perbandingannya tidak sepenuhnya setara.|
|2|Representasi teks digunakan tanpa penjelasan memadai, terdapat ketidakjelasan kapan fitting dilakukan, atau<br>parameter penting tidak terdokumentasi.|
|1|Representasi teks tidak sesuai, menimbulkan leakage yang serius, atau tidak dapat direproduksi.|



##### **7.1.5 Model Training & Experiment** 

|**Bobot Internal**<br>**20%**|
|---|



**Indikator yang dinilai:** minimal dua model/algoritma dibandingkan; strategi multilabel seperti Binary Relevance, Classifier Chain, Label Powerset, atau pendekatan setara digunakan bila relevan; validation/tuning dilakukan; seed dan parameter dicatat; hasil eksperimen dirangkum dalam tabel/dataframe yang dapat dibandingkan. 

|**Skor**|**Deskripsi Capaian**|
|---|---|
|5|Eksperimen sistematis dan reproducible: minimal dua model/algoritma dibandingkan pada split yang sama, strategi<br>multilabel relevan dieksplorasi, validation/tuning dilakukan secara benar, parameter dan seed dicatat, serta hasil<br>seluruh konfigurasi dirangkum dan dianalisis.|



Proyek UTS-UAS  |  Pemrosesan Bahasa Alami  |  Gasal 2026/2027 

**PROYEK UTS-UAS  •  PEMROSESAN BAHASA ALAMI** 

|**Skor**|**Deskripsi Capaian**|
|---|---|
|4|Mayoritas unsur eksperimen terpenuhi dan perbandingan model valid. Terdapat satu kekurangan minor pada<br>keluasan tuning, variasi strategi multilabel, atau dokumentasi konfigurasi.|
|3|Model berhasil dilatih dan terdapat lebih dari satu eksperimen, tetapi variasi model/strategi terbatas, tuning<br>minimal, atau pencatatan konfigurasi belum konsisten.|
|2|Training hanya menunjukkan satu konfigurasi utama atau eksperimen tidak sistematis; penggunaan validation set<br>dan parameter sulit ditelusuri.|
|1|Model tidak berhasil dilatih, eksperimen tidak dapat dijalankan ulang, atau desain training tidak valid sehingga<br>hasil tidak dapat dipercaya.|



|**7.1.6 Evaluation & Error Analysis**|**Bobot Internal**<br>**20%**|
|---|---|



**Indikator yang dinilai:** model dibandingkan pada test set yang sama; classification report per label, micro-F1, macro-F1, weighted-F1, Hamming Loss, dan subset accuracy atau metrik relevan ditampilkan; threshold dijelaskan bila digunakan; error analysis menggunakan contoh prediksi dan membahas label langka/co-occurrence atau sumber kesalahan. 

|**Skor**|**Deskripsi Capaian**|
|---|---|
|5|Evaluasi lengkap dan metodologis: semua model final diuji pada test set yang sama, metrik per label dan agregat<br>dilaporkan, threshold/decision rule dijelaskan, serta error analysis menggunakan contoh konkret untuk<br>mengidentifikasi false positive/false negative, label langka, atau pola co-occurrence yang sulit.|
|4|Mayoritas metrik dan error analysis tersedia dengan interpretasi yang baik. Satu komponen minor, misalnya analisis<br>threshold atau satu jenis metrik, belum lengkap.|
|3|Evaluasi dasar sudah benar dan mencakup beberapa metrik multilabel, tetapi report per label, error analysis, atau<br>interpretasi perbedaan model masih terbatas.|
|2|Evaluasi hanya mengandalkan sedikit metrik, tidak membahas error secara memadai, atau penggunaan test<br>set/threshold kurang jelas.|
|1|Evaluasi tidak valid, hanya menggunakan training/validation performance sebagai hasil akhir, metrik tidak sesuai<br>dengan multilabel, atau tidak ada error analysis yang dapat dipertanggungjawabkan.|



##### **7.1.7 Deployment Multilabel** 

|**Bobot Internal**|
|---|
|**10%**|



**Indikator yang dinilai:** aplikasi Streamlit memuat model terbaik yang tersimpan; preprocessing/inference konsisten dengan training; menerima teks baru; menampilkan satu atau lebih predicted label, confidence/probability dan threshold bila tersedia; memiliki interpretasi output dan dapat dijalankan tanpa error. 

|**Skor**|**Deskripsi Capaian**|
|---|---|
|5|Deployment berfungsi end-to-end menggunakan model terbaik yang benar-benar disimpan dari eksperimen. Input<br>baru diproses dengan pipeline yang konsisten, hasil multilabel ditampilkan jelas beserta confidence/threshold bila<br>tersedia, interpretasi diberikan, dan aplikasi stabil pada beberapa contoh input.|
|4|Aplikasi berfungsi dengan baik dan menggunakan model terbaik, tetapi terdapat satu kekurangan minor pada<br>visualisasi confidence, interpretasi, validasi input, atau pengalaman penggunaan.|



Proyek UTS-UAS  |  Pemrosesan Bahasa Alami  |  Gasal 2026/2027 

**PROYEK UTS-UAS  •  PEMROSESAN BAHASA ALAMI** 

|**Skor**|**Deskripsi Capaian**|
|---|---|
|3|Prediksi dapat dijalankan, tetapi informasi output masih terbatas atau terdapat ketidakjelasan kecil mengenai<br>preprocessing/model yang digunakan dalam deployment.|
|2|Aplikasi hanya berfungsi sebagian, model/preprocessing tidak terintegrasi dengan baik, atau sering membutuhkan<br>langkah manual agar prediksi berjalan.|
|1|Aplikasi tidak dapat dijalankan, tidak menggunakan model hasil training, atau output yang ditampilkan bersifat<br>statis/rule-based dan tidak merepresentasikan model yang dikumpulkan.|



### **7.2 Rubrik Proyek B - Named Entity Recognition (50% Nilai UAS)** 

|**Kriteria**|**Bobot**|**Fokus Penilaian**|
|---|---|---|
|Data Loading & Span Validation|10%|Validitas text-span/entity, offset, overlap, dan reproducibility<br>data loading.|
|Tokenization & Tag Conversion|15%|BIO/BIOES/BILOU, alignment token-label, subword, special<br>token, dan split.|
|EDA Entity|10%|Distribusi token/span/entity, panjang span, dan dominasi<br>O/imbalance.|
|Embedding & Tag Mapping|15%|Representasi token, label mapping, batching, padding,<br>truncation, dan ignore label.|
|Model Configuration & Training|20%|Arsitektur, validation, tuning/early stopping, seed, history, dan<br>checkpoint.|
|Evaluation & Error Analysis|20%|Entity-level metrics, F1 per entity, boundary/label error, dan<br>contoh prediksi.|
|Deployment NER|10%|Ekstraksi dan highlight entity/span menggunakan model<br>terbaik secara end-to-end.|



**Bobot Internal 7.2.1 Data Loading & Span Validation 10%** 

**Indikator yang dinilai:** dataset NER dibaca dari file eksternal; struktur text-span/entity diverifikasi; offset start/end dan substring span dicek terhadap teks asli; invalid/overlapping span ditangani sesuai guideline; label entity dan statistik dasar ditampilkan; proses dapat direproduksi. 

|**Skor**|**Deskripsi Capaian**|
|---|---|
|5|Dataset NER dapat dimuat secara reproducible dan validasi span dilakukan menyeluruh. Offset, substring, label<br>entity, invalid/overlap span, jumlah entity, dan contoh anotasi diverifikasi dengan bukti output; masalah ditemukan<br>dan ditangani secara terdokumentasi.|
|4|Mayoritas validasi span sudah lengkap dan benar, dengan satu kekurangan minor pada pemeriksaan atau<br>dokumentasi yang tidak memengaruhi validitas dataset.|
|3|Dataset dapat dimuat dan beberapa span diperiksa, tetapi validasi offset, overlap, invalid span, atau statistik entity<br>masih terbatas.|
|2|Data dapat dibaca tetapi validasi span bersifat superficial; terdapat kemungkinan mismatch offset/teks atau struktur<br>label yang tidak diperiksa dengan baik.|



Proyek UTS-UAS  |  Pemrosesan Bahasa Alami  |  Gasal 2026/2027 

**PROYEK UTS-UAS  •  PEMROSESAN BAHASA ALAMI** 

|**Skor**|**Deskripsi Capaian**|
|---|---|
|1|Dataset/span tidak dapat dimuat dengan benar, banyak offset tidak valid tanpa penanganan, atau data yang<br>digunakan tidak dapat ditelusuri ke gold dataset UTS.|



|**7.2.2 Tokenization & Tag Conversion**|**Bobot Internal**<br>**15%**|
|---|---|



**Indikator yang dinilai:** span dikonversi ke BIO/BIOES/BILOU secara konsisten; tokenisasi dan aturan boundary dijelaskan; word-to-subword alignment diverifikasi bila menggunakan transformer; special token, padding, truncation, ignore index, serta train/validation/test split ditangani dengan benar. 

|**Skor**|**Deskripsi Capaian**|
|---|---|
|5|Konversi span-ke-tag dan token-label alignment benar serta diverifikasi melalui contoh sebelum training.<br>BIO/BIOES/BILOU konsisten, subword/special token ditangani tepat, padding/truncation dan ignore index<br>terdokumentasi, dan split data tetap mempertahankan integritas anotasi.|
|4|Seluruh proses utama benar dengan satu kekurangan minor pada dokumentasi atau jumlah contoh verifikasi<br>alignment.|
|3|Konversi tag berjalan dan model dapat dilatih, tetapi verifikasi alignment, penanganan subword/special token, atau<br>dokumentasi aturan boundary belum lengkap.|
|2|Tokenization/tag conversion dilakukan tetapi terdapat ketidakjelasan penting pada alignment atau penanganan<br>token; potensi label shift masih ada.|
|1|Alignment token-label salah atau tidak diverifikasi, tag conversion tidak konsisten, atau preprocessing<br>menghasilkan label token yang tidak valid.|



|**7.2.3 EDA Entity**|**Bobot Internal**<br>**10%**|
|---|---|



**Indikator yang dinilai:** EDA mencakup jumlah token per teks, jumlah span/entity per teks, distribusi setiap entity type, panjang span, frekuensi O dibanding entity label, dan indikasi imbalance; contoh entity representatif/ambigu ditampilkan dan diinterpretasikan. 

|**Skor**|**Deskripsi Capaian**|
|---|---|
|5|EDA NER lengkap dan informatif. Distribusi token, entity per tipe, entity per teks, panjang span, dominasi<br>O/imbalance, dan contoh entity dianalisis serta dikaitkan dengan keputusan training/evaluasi.|
|4|Mayoritas komponen EDA tersedia dengan interpretasi yang baik; satu analisis tambahan masih kurang mendalam.|
|3|Distribusi dasar entity dan panjang teks tersedia, tetapi analisis panjang span, O-label imbalance, atau implikasi<br>terhadap model masih terbatas.|
|2|EDA hanya menampilkan statistik sangat dasar atau grafik tanpa interpretasi yang relevan untuk NER.|
|1|EDA NER tidak dilakukan, tidak relevan, atau tidak berasal dari dataset yang digunakan untuk pemodelan.|
|**7.2.4 E**|**mbedding & Tag Mapping**<br>**Bobot Internal**<br>**15%**|



Proyek UTS-UAS  |  Pemrosesan Bahasa Alami  |  Gasal 2026/2027 

**PROYEK UTS-UAS  •  PEMROSESAN BAHASA ALAMI** 

**Indikator yang dinilai:** word/subword representation atau pretrained embedding dipilih secara tepat; label2id/id2label konsisten; batching, padding, truncation, attention mask, dan ignore label terdokumentasi; strategi terhadap dominasi O/imbalance dijelaskan bila diperlukan. 

|**Skor**|**Deskripsi Capaian**|
|---|---|
|5|Embedding/representasi sesuai dengan model dan corpus; tag mapping konsisten dua arah; batching, padding,<br>truncation, attention mask, serta ignore label diimplementasikan benar; keputusan penanganan O-label/imbalance<br>dijelaskan berdasarkan data.|
|4|Mayoritas aspek teknis benar dan terdokumentasi, tetapi terdapat satu kekurangan minor pada strategi imbalance<br>atau dokumentasi pipeline input.|
|3|Embedding dan tag mapping berjalan dengan benar, tetapi detail batching/padding/ignore label atau analisis<br>imbalance masih terbatas.|
|2|Model dapat menerima input, namun mapping label atau pipeline embedding kurang jelas dan berpotensi<br>menimbulkan inkonsistensi.|
|1|Tag mapping/embedding tidak konsisten, menyebabkan kesalahan label yang sistematis, atau pipeline input tidak<br>dapat direproduksi.|



|**7.2.5 Model Configuration & Training**|**Bobot Internal**<br>**20%**|
|---|---|



**Indikator yang dinilai:** arsitektur NER didefinisikan jelas; minimal satu model berbasis machine/deep learning dilatih dan baseline-vs-advanced model dianjurkan; validation set digunakan; tuning/early stopping diterapkan bila relevan; seed, hyperparameter, training history, dan checkpoint model dicatat. 

|**Skor**|**Deskripsi Capaian**|
|---|---|
|5|Konfigurasi model jelas dan reproducible. Training menggunakan validation set secara benar, hyperparameter/seed<br>terdokumentasi, tuning atau early stopping dilakukan secara relevan, training history dipantau, dan<br>checkpoint/model terbaik dipilih berdasarkan kriteria yang dijelaskan.|
|4|Mayoritas komponen training terpenuhi dan model terbaik dipilih secara valid, dengan satu kekurangan minor pada<br>tuning, baseline comparison, atau dokumentasi.|
|3|Model berhasil dilatih dan validation set digunakan, tetapi eksperimen konfigurasi terbatas atau pencatatan<br>parameter/training history belum lengkap.|
|2|Training berjalan namun pemilihan model terbaik, validation, hyperparameter, atau reproducibility kurang jelas.|
|1|Training gagal/tidak reproducible, tidak menggunakan validation secara benar, atau model yang dikumpulkan tidak<br>dapat ditelusuri ke proses training.|



##### **7.2.6 Evaluation & Error Analysis** 

|**Bobot Internal**<br>**20%**|
|---|



**Indikator yang dinilai:** model diuji pada test set; entity-level precision, recall, F1, dan F1 per entity type dilaporkan; tokenlevel metric boleh sebagai tambahan; prediksi disimpan/dapat diperiksa; boundary error, label error, missed entity, dan contoh prediksi benar/salah dianalisis. 

|**Skor**|**Deskripsi Capaian**|
|---|---|



Proyek UTS-UAS  |  Pemrosesan Bahasa Alami  |  Gasal 2026/2027 

**PROYEK UTS-UAS  •  PEMROSESAN BAHASA ALAMI** 

|**Skor**|**Deskripsi Capaian**|
|---|---|
|5|Evaluasi entity-level lengkap pada test set dan hasil per entity type disajikan jelas. Error analysis membedakan<br>boundary error, label error, false positive, missed entity, dan kasus ambigu menggunakan contoh nyata, lalu<br>menghubungkannya dengan karakteristik data/model.|
|4|Mayoritas metrik entity-level dan error analysis tersedia dengan interpretasi yang baik; satu komponen minor<br>belum lengkap.|
|3|Precision/recall/F1 dasar tersedia, tetapi evaluasi per entity type atau analisis boundary/label error masih terbatas.|
|2|Evaluasi terlalu bergantung pada token accuracy atau sedikit metrik; contoh error dan analisis entity-level tidak<br>memadai.|
|1|Evaluasi tidak valid, tidak menggunakan test set dengan benar, hanya menampilkan training metric, atau tidak<br>menyajikan entity-level evaluation yang dapat dipertanggungjawabkan.|
|**7.2.7 De**|**ployment NER**<br>**Bobot Internal**<br>**10%**|



**Indikator yang dinilai:** aplikasi Streamlit memuat model NER terbaik dan tokenizer/tag mapping yang sesuai; menerima teks baru; menampilkan extracted entity/span dan label; span di-highlight pada teks; offset/hasil ekstraksi konsisten; interpretasi tersedia dan aplikasi dapat dijalankan tanpa error. 

|**Skor**|**Deskripsi Capaian**|
|---|---|
|5|Deployment NER berfungsi end-to-end menggunakan model terbaik dan preprocessing/tokenizer yang tepat.<br>Entity/span diekstraksi serta di-highlight secara akurat, label ditampilkan jelas, offset konsisten, dan aplikasi stabil<br>pada beberapa contoh input.|
|4|Aplikasi berfungsi baik menggunakan model yang benar, dengan satu kekurangan minor pada highlight,<br>interpretasi, visualisasi, atau validasi input.|
|3|Prediksi entity berjalan, tetapi highlight/offset, interpretasi, atau integrasi tokenizer/model masih memiliki<br>keterbatasan.|
|2|Deployment hanya berfungsi sebagian, memerlukan langkah manual, atau hasil span sering tidak konsisten dengan<br>teks input.|
|1|Aplikasi tidak dapat dijalankan, tidak menggunakan model hasil training, atau output entity bersifat statis/rule-<br>based dan tidak berasal dari model NER yang dikumpulkan.|



Proyek UTS-UAS  |  Pemrosesan Bahasa Alami  |  Gasal 2026/2027 

**PROYEK UTS-UAS  •  PEMROSESAN BAHASA ALAMI** 

# **8. Aturan Pengumpulan dan Video Demo** 

### **8.1 Aturan Pengumpulan** 

- Pengumpulan dilakukan melalui uploader/LMS yang ditentukan dosen. 

- Format penamaan ZIP: Projek_UTS_PBA_Kelas_KEL.zip untuk UTS dan Projek_UAS_PBA_Kelas_KEL.zip untuk UAS, kecuali ada ketentuan lain. 

- Semua anggota kelompok wajib mengunggah file proyek yang sama apabila LMS mensyaratkan unggahan individual. 

- Notebook yang tidak dapat dieksekusi, file model yang tidak disertakan, atau aplikasi yang tidak dapat dijalankan akan memengaruhi penilaian sesuai tingkat masalah. 

- Kelompok harus siap menjelaskan kembali setiap bagian dataset, guideline, kode, parameter, dan keputusan eksperimen apabila diminta dosen. 

### **8.2 Video Demo UAS** 

- Durasi disarankan 5-10 menit. 

- Menunjukkan cara menjalankan aplikasi Streamlit. 

- Menunjukkan minimal satu contoh input untuk Multilabel Classification dan satu contoh untuk NER. 

- Menjelaskan output, confidence/threshold jika digunakan, dan highlight entity/span. 

- Menunjukkan bahwa aplikasi menggunakan model terbaik yang benar-benar dilatih, bukan rule-based sederhana atau output statis. 

- Menjelaskan secara singkat hubungan hasil multilabel dan NER pada teks yang sama. 

# **9. Catatan Akademik** 

- Dataset hasil anotasi, kode, eksperimen, dan laporan harus merupakan karya kelompok sendiri berdasarkan dataset yang dipilih. 

- Dataset tambahan, pretrained model, library, dan kode referensi harus disitasi serta dijelaskan penggunaannya. 

- Kemiripan kode/laporan yang tidak wajar tanpa sitasi atau penjelasan dapat dikenai pengurangan nilai atau sanksi akademik sesuai ketentuan. 

- Penggunaan AI generatif tidak mengurangi tanggung jawab kelompok untuk memahami dan dapat mempertanggungjawabkan semua artefak yang dikumpulkan. 

# **10. Checklist Pengumpulan** 

|**Tahap**|**Checklist**|**Status**|
|---|---|---|
|UTS|Dataset dipilih dan domain analysis selesai.|[ ]|
|UTS|Taxonomy multilabel dan NER telah disetujui dosen.|[ ]|
|UTS|Annotation guideline lengkap dan konsisten.|[ ]|
|UTS|Overlap annotation, agreement, dan adjudication telah dilakukan.|[ ]|
|UTS|Gold dataset, EDA, dan dataset explorer dapat dijalankan.|[ ]|
|UTS|Notebook UTS dapat dijalankan ulang dari awal sampai akhir tanpa error.|[ ]|
|UAS|Split train/validation/test terdokumentasi dan bebas leakage.|[ ]|
|UAS|Minimal dua pendekatan/model multilabel dibandingkan.|[ ]|
|UAS|Token-label alignment NER telah diverifikasi dengan contoh.|[ ]|
|UAS|Model terbaik diuji pada test set dan disimpan.|[ ]|
|UAS|Error analysis Multilabel dan NER tersedia.|[ ]|
|UAS|Streamlit menggunakan model terbaik dan dapat dijalankan.|[ ]|



Proyek UTS-UAS  |  Pemrosesan Bahasa Alami  |  Gasal 2026/2027 

**PROYEK UTS-UAS  •  PEMROSESAN BAHASA ALAMI** 

|**Tahap**|**Checklist**|**Status**|
|---|---|---|
|UAS|Laporan, export kode, repository, dan video demo tersedia.|[ ]|



Proyek UTS-UAS  |  Pemrosesan Bahasa Alami  |  Gasal 2026/2027 

