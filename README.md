# Projek-analisis-teks-dan-web-mining
Tugas akhir Data mining pertemuan 11
Kelompok 4:
 - Alfawaid Dhabbiyyish Ashahabi (241011402862)
 - Andika Septa Nugraha (241011401784)
 - Aska Agniya Marasabessy (241011401338)
 - Muhamad Abizar Al Ghifari (241011403265)
 - Sahrul Hidayat (241011401344)

DATASET: https://drive.google.com/file/d/1AzInltoN0o7o7R-qYLsSZK-HD-wGGpM2/view?usp=sharing

Video Penjelasan: https://youtu.be/LOExSSSmLwc
## Analisis teks
Analisis teks adalah proses dalam menggali informasi, pola, dan pengetahuan dari data yang masih berbentuk teks. data teks ini termasuk kedalam data yang tidak terstruktur. Dewasa ini, jumlah data teks yang berada di internet semakin meningkat, seperti pada email, media sosial, artikel berita, forum diskusi, hingga dokumen digital. Oleh karena itu, analisis teks menjadi teknik pemrosesan yang banyak digunakan untuk mengolah informasi agar dapat menghasilkan informasi yang relevan dan berguna. 
Dalam proses menganalisis teks, terdapat beberapa tahapan, seperti: memperoleh data teks yang akan dianalisis/dataset. Selanjutnya akan dilakukan preprocessing(yaitu tahap membersihkan data dari karakter yang tidak diperlukan seperti tanda baca, angka, simbol, dan kata-kata yang tidak memiliki makna penting(stopword). Setelah data sudah dibersihkan, teks akan diubah menjadi bentuk angka melalui proses ekstraksi fitur, misalnya menggunakan metode TF-IDF(Term Frequency–Inverse Document Frequency). Data berupa angka tersebut kemudian akan digunakan untuk di training dan membangun model dengan menggunakan algoritma machine learning sehingga dapat melakukan klasifikasi atau prediksi terhadap data baru yang akan masuk.
Pada projek ini, analisis teks digunakan untuk membedakan email yang termasuk kategori spam dan ham berdasarkan dataset yang telah ditraining dan testing.
## Web Mining
Web Mining adalah proses menggali informasi dari berbagai sumber data yang ada di internet dengan teknik data mining dan machine learning. Web Mining bertujuan untuk menemukan pola, hubungan, dan informasi yang tersembunyi dari data yang tersedia pada halaman web internet.
Web Mining dibagi menjadi tiga kategori:
1. Web Content Mining adalah proses mengekstraksi informasi dari isi halaman web. Proses ini banyak digunakan pada mesin pencari, analisis berita, klasifikasi dokumen, dan analisis sentimen.
2. Web Structure Mining lebih berfokus pada hubungan antarhalaman web yang berdasarkan pada struktur hyperlink yang menghubungkan satu halaman dengan halaman lainnya. proses ini digunakan untuk mengetahui hubungan antarwebsite dan menentukan tingkat kepentingan halaman web.
3. Web Usage Mining lebih memanfaatkan data aktivitas pengguna, seperti riwayat kunjungan. Informasi tersebut dapat digunakan untuk meningkatkan kualitas layanan, memahami perilaku pengguna, dan memberikan rekomendasi yang lebih sesuai dengan pengguna.
Dalam projek ini, konsep Web Mining berkaitan dengan sumber data yang berasal dari email. Email adalah bentuk data teks yang banyak bertebaran melalui internet sehingga analisis terhadap isi email menjadi bagian dari penerapan Web Content Mining. Dengan memanfaatkan proses text mining dan machine learning, sistem mampu mengenali pola-pola tertentu yang sering muncul pada email spam sehingga dapat mengklasifikasikan email secara otomatis.
## Implementasi Analisis teks dan Web Mining dalam program Pendeteksi Spam
Pada projek ini digunakan 2 file utama, yaitu file emails.csv yang digunakan sebagai dataset dan Pendeteksi spam.py sebagai program utama yang melakukan proses analisis teks hingga klasifikasi email spam. Kedua file ini saling berkaitan karena dataset akan menjadi sumber data yang akan ditraining dan ditesting oleh model machine learning, dan program Python berfungsi untuk mengolah data, membangun model, dan melakukan prediksi terhadap email baru yang akan masuk.
### Dataset emails.csv
emails.csv berisi kumpulan data email yang digunakan sebagai data yang akan dilatih (training data) dalam proses klasifikasi spam. Setiap baris pada dataset mewakili satu email yang telah diberi label spam atau ham. pada dataset ini terdapat 2 atribut utama:
1. text, berisi pesan email.
2. spam, berisi label klasifikasi. Nilai 1 menunjukkan spam, sedangkan nilai 0 menunjukkan ham.
### Program Pendeteksi Spam
Pada program Pendeteksi spam.py ini memanfaatkan beberapa library seperti Pandas, NLTK, dan Scikit-Learn untuk melakukan pengolahan teks sampai kepada proses klasifikasi email. Berikut alur yang bekerja pada program ini:

1.Import Library
Pada tahap pertama adalah mengimpor berbagai library yang dibutuhkan selama proses analisis. Program menggunakan Pandas untuk membaca dataset, Regular Expression untuk membersihkan teks, NLTK untuk menghapus stopword, serta Scikit-Learn untuk proses ekstraksi fitur, pembagian data, pelatihan model, dan evaluasi hasil klasifikasi. Pada setiap library memiliki fungsi yang berbeda tetapi saling melengkapi sehingga seluruh proses text mining dapat dilakukan secara otomatis.

<img width="676" height="338" alt="image" src="https://github.com/user-attachments/assets/840f373e-17ab-45c4-b79a-91f0b0922dd3" />

2.Membaca Dataset
Setelah mengimport library, program membaca file emails.csv menggunakan fungsi read_csv(). Dataset kemudian disimpan ke dalam variabel df yang berbentuk DataFrame sehingga data lebih mudah diproses. Selanjutnya program menampilkan jumlah data dan beberapa baris pertama untuk memastikan dataset berhasil dibaca tanpa kesalahan.

<img width="1249" height="26" alt="image" src="https://github.com/user-attachments/assets/bd35340e-4fbb-41cf-84d9-30e85c3777ac" />

3.Preprocessing Teks
Tahapan preprocessing merupakan proses membersihkan isi email agar lebih mudah dipahami oleh komputer. Pada penelitian ini preprocessing dilakukan melalui beberapa langkah.

<img width="661" height="28" alt="image" src="https://github.com/user-attachments/assets/4f2cb82c-75d6-4092-af55-8c00a34412f4" />

Pertama, seluruh huruf diubah menjadi huruf kecil (lowercase) sehingga kata seperti "FREE" dan "free" dianggap sama.

<img width="500" height="25" alt="image" src="https://github.com/user-attachments/assets/18920bc2-566d-423c-a4e2-586dba3a460a" />

Selanjutnya program menghapus alamat website atau URL menggunakan Regular Expression. Langkah ini dilakukan karena sebagian besar alamat website tidak memberikan informasi penting dalam proses klasifikasi spam.

<img width="648" height="24" alt="image" src="https://github.com/user-attachments/assets/bc9fb9ba-578a-4ced-8dec-798f7a9906a2" />

Setelah itu semua angka, simbol, dan karakter khusus dihapus sehingga hanya tersisa huruf alfabet.

<img width="572" height="27" alt="image" src="https://github.com/user-attachments/assets/1e3f278b-9761-48a3-a7df-27af5e99e2f7" />

Isi email kemudian dipisahkan menjadi beberapa kata (tokenization) menggunakan fungsi split().

<img width="401" height="25" alt="image" src="https://github.com/user-attachments/assets/10719f2c-72c4-48b1-85b2-98b315f212e7" />

Tahap terakhir adalah menghapus stopword, yaitu kata-kata umum seperti the, is, and, of, yang sering muncul tetapi tidak memberikan makna penting dalam proses klasifikasi. Setelah seluruh proses selesai, kata-kata yang tersisa digabung kembali menjadi sebuah kalimat bersih (clean text).

<img width="741" height="30" alt="image" src="https://github.com/user-attachments/assets/2a07fbd0-4aec-4907-b561-09052dd29f72" />

Hasil preprocessing menghasilkan teks yang lebih ringkas sehingga model lebih mudah mengenali pola yang membedakan email spam dan email biasa.

<img width="554" height="29" alt="image" src="https://github.com/user-attachments/assets/7f59ef2e-6bae-46f6-b00f-50f7444c5a33" />

4.Ekstraksi Fitur Menggunakan TF-IDF
Komputer tidak dapat memahami teks secara langsung sehingga setiap kata harus diubah menjadi bentuk numerik. Pada penelitian ini digunakan metode TF-IDF (Term Frequency–Inverse Document Frequency).
TF-IDF memberikan bobot pada setiap kata berdasarkan frekuensi kemunculannya dalam sebuah dokumen dan tingkat keunikannya di seluruh dataset. Kata yang sering muncul pada satu email tetapi jarang muncul pada email lain akan memperoleh bobot yang lebih tinggi.
Program juga menggunakan parameter ngram_range=(1,2) sehingga model tidak hanya mengenali satu kata (unigram), tetapi juga pasangan kata (bigram). Dengan demikian frasa seperti "click here", "free money", atau "claim prize" dapat dikenali sebagai ciri khas email spam. Selain itu jumlah fitur dibatasi sebanyak 5000 agar proses pelatihan lebih efisien.

<img width="491" height="97" alt="image" src="https://github.com/user-attachments/assets/095c0771-b699-42d0-b9c0-9888485508d1" />

5.Pembagian Data
Setelah seluruh teks berubah menjadi data numerik, dataset dibagi menjadi dua bagian, yaitu data latih (training data) dan data uji (testing data).

<img width="546" height="51" alt="image" src="https://github.com/user-attachments/assets/f8d0cafa-25ac-4ad0-9ce6-4abd5a967a65" />

Sebanyak 80% data digunakan untuk melatih model, sedangkan 20% sisanya digunakan untuk menguji kemampuan model dalam mengklasifikasikan email yang belum pernah dilihat sebelumnya.
Program juga menggunakan parameter stratify, sehingga proporsi jumlah email spam dan ham tetap seimbang pada data latih maupun data uji. Hal ini membantu menghasilkan evaluasi yang lebih adil dan akurat.

<img width="610" height="173" alt="image" src="https://github.com/user-attachments/assets/be673208-014e-4f53-b90d-4ae32e48e654" />

6.Pelatihan Model Logistic Regression
Pada penelitian ini algoritma yang digunakan adalah Logistic Regression.
Logistic Regression merupakan salah satu algoritma klasifikasi yang cukup sederhana tetapi memiliki performa yang baik untuk analisis teks. Algoritma ini mempelajari hubungan antara fitur TF-IDF dengan label spam sehingga mampu menghitung peluang suatu email termasuk kategori spam atau ham.

<img width="481" height="23" alt="image" src="https://github.com/user-attachments/assets/21bab596-4f97-4b57-af20-d85e4156e0c7" />

Model kemudian dilatih menggunakan data training melalui fungsi fit(). Setelah proses pelatihan selesai, model siap digunakan untuk melakukan prediksi.

<img width="376" height="27" alt="image" src="https://github.com/user-attachments/assets/bbd93fc2-e0b0-4d4e-90e0-590eaa3ff4c1" />

7.Evaluasi Model
Setelah model selesai dilatih, langkah berikutnya adalah mengevaluasi performanya menggunakan data testing.

<img width="409" height="27" alt="image" src="https://github.com/user-attachments/assets/29f89434-771e-43ff-95a4-f6cebdd8e56a" />

Program menghitung beberapa metrik evaluasi, yaitu Accuracy, Classification Report, dan Confusion Matrix.

<img width="595" height="197" alt="image" src="https://github.com/user-attachments/assets/c6fd0fb8-52de-4b64-b0e5-0bf6801df0ac" />

- Accuracy menunjukkan persentase prediksi yang benar dibandingkan seluruh data uji.
- Classification Report memberikan informasi mengenai Precision, Recall, dan F1-Score, sehingga peneliti dapat mengetahui seberapa baik model mengenali email spam maupun email ham.
- Confusion Matrix memperlihatkan jumlah prediksi yang benar dan salah dalam bentuk matriks, sehingga kesalahan klasifikasi dapat dianalisis dengan lebih mudah.
Tahap evaluasi ini menjadi indikator utama apakah model yang dibangun sudah memiliki kinerja yang baik atau masih perlu dilakukan perbaikan.

8.Prediksi Email Baru
Tahapan terakhir adalah menguji model menggunakan beberapa email baru yang tidak terdapat pada dataset.

<img width="702" height="167" alt="image" src="https://github.com/user-attachments/assets/6041a0be-e327-4ae2-9b80-e41370fd2759" />

Contoh email seperti "Congratulations! You have won $5000. Click here now." dan "Claim your free lottery prize today." diprediksi sebagai spam karena mengandung kata-kata promosi, hadiah, dan ajakan mengklik tautan. Sebaliknya email seperti "Please attend the meeting tomorrow at 9 AM." atau "The project report has been submitted." diprediksi sebagai ham karena berisi komunikasi yang bersifat formal dan tidak memiliki karakteristik spam.
Sebelum diprediksi, email baru tetap melalui proses preprocessing dan transformasi TF-IDF agar format datanya sama dengan data yang digunakan saat pelatihan model.

<img width="537" height="147" alt="image" src="https://github.com/user-attachments/assets/394456ef-6504-4111-b8bd-4ee958cd5ce3" />
