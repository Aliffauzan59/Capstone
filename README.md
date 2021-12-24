# Dicoding X Kampus Merdeka Final Capstone Project: Website Pendeteksi Mata Katarak
CSD-009 Team Member: <br />
M004T5006 - Muhammad Alif Fauzan <br />
M123S4086 - Muhammad Iqbal <br />

### Overview <br />
Website Eyecare ini adalah aplikasi berbasis website untuk mendiagnosa apakah mata mengalami gejala katarak atau tidak. website ini berguna sebagai tindakan preventif sebelum mendapatkan keputusan dokter apakah kondisi mata pasien mengalami gejala katarak atau tidak.

Model machine learning yang kami bangun menggunakan algoritma Deep Learning yaitu Convolutional Neural Network (CNN) yang mendukung data image. CNN dapat memberikan hasil klasifikasi dengan baik dengan nilai dari validation accuracy sebesar 0.95 dan nilai loss sebesar 0.1279. Model tersebut kami deploy ke dalam Framework Flask dengan output website.

### Project Documentation <br />
Download dataset yang akan digunakan, serta menyeleksi data yang akan digunakan
Pra-pemrosesan data gambar dengan Google Colab
Split dataset ke data latih dan data validasi
Build model CNN
Simpan model machine learning ke dalam format file *.h5
Deploy model machine learning ke Framework Flask & Build Website
### How to Use this Application? <br />
Kunjungi situs https://predictioncataract.herokuapp.com/
Pilih Home
Siapkan data image mata yang akan diperiksa
Unggah data pada kolom unggah lalu klik submit
Sistem akan memberikan hasil prediksi kondisi mata apakah mata normal atau cataract
### Link <br />
* Dataset : https://drive.google.com/drive/folders/1S1-ED3EbNKB5O6GmLTxpNiTl8rQIaQiE?usp=sharing
* Link Deploy Website : https://predictioncataract.herokuapp.com/
* Link Video Presentasi : https://drive.google.com/drive/folders/1GRTFCuhSvRGXjqAhY_9xYeFqBNTbhz2B?usp=sharing
* Link Video Demo Website :
