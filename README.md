# Projek-analisis-teks-dan-web-mining
Tugas akhir Data mining pertemuan 11
Kelompok 4:
 - Alfawaid Dhabbiyyish Ashahabi (241011402862)
 - Andika Septa Nugraha (241011401784)
 - Aska Agniya Marasabessy (241011401338)
 - Muhamad Abizar Al Ghifari (241011403265)
 - Sahrul Hidayat (241011401344)
## Analisis teks
Analisis teks adalah proses dalam menggali informasi, pola, dan pengetahuan dari data yang masih berbentuk teks. data teks ini termasuk kedalam data yang tidak terstruktur. Dewasa ini, jumlah data teks yang berada di internet semakin meningkat, seperti pada email, media sosial, artikel berita, forum diskusi, hingga dokumen digital. Oleh karena itu, analisis teks menjadi teknik pemrosesan yang banyak digunakan untuk mengolah informasi agar dapat menghasilkan informasi yang relevan dan berguna. 
Dalam proses menganalisis teks, terdapat beberapa tahapan, seperti: memperoleh data teks yang akan dianalisis/dataset. Selanjutnya akan dilakukan preprocessing(yaitu tahap membersihkan data dari karakter yang tidak diperlukan seperti tanda baca, angka, simbol, dan kata-kata yang tidak memiliki makna penting(stopword). Setelah data sudah dibersihkan, teks akan diubah menjadi bentuk angka melalui proses ekstraksi fitur, misalnya menggunakan metode TF-IDF(Term Frequency–Inverse Document Frequency). Data berupa angka tersebut kemudian akan digunakan untuk di training dan membangun model dengan menggunakan algoritma machine learning sehingga dapat melakukan klasifikasi atau prediksi terhadap data baru yang akan masuk.
Pada projek ini, analisis teks digunakan untuk membedakan email yang termasuk kategori spam dan ham(bukan spam) berdasarkan dataset yang telah ditraining dan testing.
## Web Mining
Web Mining adalah proses menggali informasi dari berbagai sumber data yang ada di internet dengan teknik data mining dan machine learning. Web Mining bertujuan untuk menemukan pola, hubungan, dan informasi yang tersembunyi dari data yang tersedia pada halaman web internet.
Web Mining dibagi menjadi tiga kategori:
1. Web Content Mining adalah proses mengekstraksi informasi dari isi halaman web. Proses ini banyak digunakan pada mesin pencari, analisis berita, klasifikasi dokumen, dan analisis sentimen.
2. Web Structure Mining lebih berfokus pada hubungan antarhalaman web yang berdasarkan pada struktur hyperlink yang menghubungkan satu halaman dengan halaman lainnya. proses ini digunakan untuk mengetahui hubungan antarwebsite dan menentukan tingkat kepentingan halaman web.
3. Web Usage Mining lebih memanfaatkan data aktivitas pengguna, seperti riwayat kunjungan. Informasi tersebut dapat digunakan untuk meningkatkan kualitas layanan, memahami perilaku pengguna, dan memberikan rekomendasi yang lebih sesuai dengan pengguna.
Dalam projek ini, konsep Web Mining berkaitan dengan sumber data yang berasal dari email. Email adalah bentuk data teks yang banyak bertebaran melalui internet sehingga analisis terhadap isi email menjadi bagian dari penerapan Web Content Mining. Dengan memanfaatkan proses text mining dan machine learning, sistem mampu mengenali pola-pola tertentu yang sering muncul pada email spam sehingga dapat mengklasifikasikan email secara otomatis.
