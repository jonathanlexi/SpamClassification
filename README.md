# Spam Classification Neural Network

## Pendahuluan
Pesan spam atau email sampah adalah masalah umum dalam pengelolaan kotak masuk. Untuk menghadapi tantangan ini, pengklasifikasian spam menggunakan jaringan saraf atau neural network telah menjadi pendekatan yang efektif. Dalam pengklasifikasian spam menggunakan jaringan saraf, tujuan utama adalah membangun model yang dapat mengidentifikasi dengan akurasi tinggi apakah sebuah email adalah spam atau bukan.

Jaringan saraf adalah model pembelajaran mesin yang terinspirasi oleh struktur jaringan saraf biologis. Model ini terdiri dari sejumlah lapisan yang saling terhubung, yang mampu mempelajari pola dan fitur yang kompleks dari data. Dalam konteks pengklasifikasian spam, jaringan saraf dapat dilatih untuk mengidentifikasi pola khusus dalam email yang menunjukkan ciri-ciri spam.

Pendekatan menggunakan jaringan saraf untuk mengklasifikasikan spam memiliki beberapa keunggulan. Pertama, jaringan saraf dapat mempelajari fitur-fitur yang kompleks dan abstrak dari email, sehingga mampu menangkap pola-pola yang sulit untuk diidentifikasi oleh metode tradisional. Kedua, dengan melatih jaringan saraf menggunakan data pelatihan yang cukup, model dapat meningkatkan akurasi dan menggeneralisasi dengan baik untuk data yang belum pernah dilihat sebelumnya.

Dalam pendekatan pengklasifikasian spam menggunakan jaringan saraf, langkah-langkah umum meliputi preprocessing data, pembangunan arsitektur jaringan saraf, pelatihan model, evaluasi performa, dan penggunaan model untuk mengklasifikasikan email baru.

Dalam tahap preprocessing data, teks email biasanya diubah menjadi urutan token dan dilakukan pengolahan lainnya seperti penghapusan tanda baca atau stemming untuk mempersiapkan data sebagai input untuk jaringan saraf.

Selanjutnya, arsitektur jaringan saraf harus dibangun. Ini melibatkan memilih jenis lapisan dan konfigurasi mereka, seperti lapisan embedding untuk merepresentasikan kata-kata, lapisan LSTM untuk memproses urutan, dan lapisan dense untuk klasifikasi.

Setelah arsitektur jaringan saraf dibangun, model dilatih dengan menggunakan data pelatihan yang dilabeli. Selama pelatihan, bobot model diperbarui berdasarkan perbedaan antara hasil prediksi dan label yang benar.

Setelah pelatihan selesai, model dievaluasi dengan menggunakan data pengujian yang terpisah. Evaluasi performa dilakukan dengan memeriksa akurasi untuk mengukur seberapa baik model dapat mengklasifikasikan email sebagai spam atau bukan.

Setelah model dievaluasi, model yang dilatih dapat digunakan untuk mengklasifikasikan email baru dengan mengubahnya menjadi urutan token dan memberikan input ke model. Model akan memberikan prediksi apakah email tersebut adalah spam atau bukan.

Pengklasifikasian spam menggunakan jaringan saraf telah menjadi pendekatan yang populer dan efektif dalam menangani masalah spam di dunia nyata
## Data Preperation
- Load Data
Folder berbentuk rar diekstrak email spam dari file spam.tar.bz2 dan non-spam dari easy_ham.tar.bz2 . Lalu dipersiapkan dataset dengan mengambil konten teks dari setiap file email dalam direktori spam dan non-spam dimana spam disimpan dalam variable spam_emails dan non_spam di ham_emails. teks email yang diambil kemudian digabungkan dalam variabel emails dan dibuat array labels dimana spam akan dilabeli 1 dan non spam dilabeli 0 dan akhirnya mengembalikan variabel email dan labels sebagai hasil processing.
Fungsi classify_email() digunakan untuk mengklasifikasikan email yang diinputkan oleh pengguna. Email tersebut diproses dan dianalisis menggunakan model yang telah disiapkan sebelumnya. Hasilnya, email tersebut akan diklasifikasikan sebagai spam atau bukan spam. Setelah pengguna memasukkan email, fungsi classify_email() dipanggil untuk melakukan klasifikasi dan hasilnya ditampilkan.
- Data Visualisasi
Visualisasi data berbentuk diagram lingkaran yang dimana hasil dari visualisasi tersebut adalah dataset memiliki pesebaran yang tidak seimbang, dengan jumlah data non-spam lebih banyak daripada spam
## Model Building & Training
klasifikasi email. Dalam fungsi ini, dataset email dan labelnya dibagi menjadi set pelatihan dan pengujian menggunakan train_test_split. Kemudian, teks email di-tokenisasi menggunakan Tokenizer dari Keras, diikuti dengan langkah padding agar semua urutan memiliki panjang yang sama.

Setelah itu, model LSTM dibangun menggunakan Keras. Model tersebut terdiri dari lapisan embedding, lapisan LSTM, dan lapisan dense. Model dikompilasi dengan loss function binary cross-entropy, optimizer Adam, dan metrik akurasi.

Selanjutnya, model dilatih dengan menggunakan metode fit pada set pelatihan. Setelah pelatihan selesai, model dievaluasi pada set pengujian menggunakan evaluate, dan hasilnya dicetak ke layar.

Akhirnya, fungsi mengembalikan model yang dilatih dan tokenizer yang digunakan untuk tokenisasi teks. Dengan menggunakan model dan tokenizer ini, Anda dapat melakukan prediksi atau analisis lebih lanjut pada data email.

Jadi, fungsi train_model ini secara keseluruhan melakukan pemrosesan dataset, pembangunan model LSTM, pelatihan model, evaluasi performa, dan mengembalikan model yang dilatih dan tokenizer yang digunakan.
## Model Evaluation
Kode yang Anda berikan mendefinisikan sebuah fungsi classify_email yang mengklasifikasikan email yang diberikan oleh pengguna. Setelah itu, kode mengambil input email dari pengguna dan menggunakan fungsi classify_email untuk melakukan klasifikasi. Hasil klasifikasi kemudian dicetak ke layar.

Berikut adalah langkah-langkah yang dilakukan dalam kode tersebut:

1. Preprocessing: Email yang diberikan oleh pengguna diubah menjadi urutan token menggunakan tokenizer yang sama yang digunakan dalam pelatihan model. Kemudian, urutan tersebut dipad menjadi panjang yang sama seperti yang digunakan saat pelatihan.

2. Klasifikasi: Model yang telah dilatih digunakan untuk memprediksi probabilitas spam dari email yang diberikan. Probabilitas spam diperoleh dari hasil prediksi model.

3. Pengambilan keputusan: Jika probabilitas spam lebih besar dari 0,5, maka email tersebut diklasifikasikan sebagai spam. Jika tidak, email tersebut diklasifikasikan sebagai bukan spam.

4. Output: Hasil klasifikasi ("This email is classified as spam." atau "This email is not spam.") dicetak ke layar.

## Kesimpulan
Dari pengujian dapat kita ambil kesimpulan, melalui penggunaan neural network dalam proyek ini, model berhasil mengklasifikasikan email-email sebagai spam atau non-spam dengan akurasi yang dapat diandalkan. Dengan mempelajari pola dan karakteristik email spam, model dapat mengenali ciri-ciri khas yang membedakan email spam dari non-spam. Penggunaan neural network dalam klasifikasi email spam memungkinkan kita untuk secara efektif mengidentifikasi dan memfilter email-email yang tidak diinginkan, meningkatkan pengalaman pengguna dan keamanan komunikasi melalui email.
