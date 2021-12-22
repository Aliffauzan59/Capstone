Dicoding X Kampus Merdeka Final Capstone Project: Website Pendeteksi Mata Katarak
CSD-009 Team Member:
M004T5006 - Muhammad Alif Fauzan
M123S4086 - Muhammad Iqbal

Overview
Website Eyecare ini adalah aplikasi berbasis website untuk mendiagnosa apakah mata mengalami gejala katarak atau tidak. website ini berguna sebagai tindakan preventif sebelum mendapatkan keputusan dokter apakah kondisi mata pasien mengalami gejala katarak atau tidak.

Model machine learning yang kami bangun menggunakan algoritma Deep Learning yaitu Convolutional Neural Network (CNN) yang mendukung data image. CNN dapat memberikan hasil klasifikasi dengan baik dengan nilai dari validation accuracy sebesar 0.95 dan nilai loss sebesar 0.1279. Model tersebut kami deploy ke dalam Framework Flask dengan output website.

Project Documentation
Download dataset yang akan digunakan, serta menyeleksi data yang akan digunakan
Pra-pemrosesan data gambar dengan Google Colab
Split dataset ke data latih dan data validasi
Build model CNN
Simpan model machine learning ke dalam format file *.h5
Deploy model machine learning ke Framework Flask & Build Website
How to Use this Application?
Kunjungi situs https://chestcov.pw
Pilih Home
Siapkan data image Chest X-Ray
Unggah data pada kolom unggah lalu klik submit
Sistem akan memberikan hasil prediksi kondisi paru-paru, dalam keadaan normal atau terinfeksi covid/tidak sehat
Hasil prediksi dengan nilai mendekati angka 1, maka menunjukkan kondisi paru-paru pasien Normal. Sedangkan hasil prediksi dengan nilai mendekati angka 0, maka menunjukkan kondisi paru-paru pasien terinfeksi Covid/tidak sehat
Menu Covid News : berisikan tentang Info Persebaran Covid di Indonesia, Info Persebaran Covid di dunia, berita Covid secara real time, serta chart perkembangan Covid di Indonesia untuk setiap provinsi
Menu About : berisikan deskripsi dari website ChestCov dan profile dari developer
Menu Contact : user dapat menggunakan menu ini untuk menghubungi developer dengan menginputkan data pada form
Select Language : user dapat memilih bahasa yang ingin digunakan pada website
Link
Dataset :
https://www.kaggle.com/tawsifurrahman/covid19-radiography-database
https://www.kaggle.com/praveengovi/coronahack-chest-xraydataset
Link Deploy Website : https://chestcov.pw
Link Video Presentasi : https://www.youtube.com/watch?v=js8rnvAtTmI
Link Video Demo Website :
Website Preview
HOME (MAIN MENU)
