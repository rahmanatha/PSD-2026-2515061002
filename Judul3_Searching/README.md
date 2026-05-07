# Pencarian Posisi Mahasiswa di Barisan Upacara

## 1. Judul Program

Pencarian Posisi Mahasiswa di Barisan Upacara Menggunakan Binary Search

## 2. Deskripsi Singkat

Program ini merupakan program sederhana berbasis bahasa Python yang digunakan untuk mencari posisi mahasiswa dalam barisan upacara berdasarkan tinggi badan. Pada studi kasus ini, mahasiswa disusun dari yang paling pendek di bagian depan sampai yang paling tinggi di bagian belakang.

Program ini menerapkan algoritma **Binary Search** untuk mencari tinggi badan mahasiswa tertentu di dalam data barisan. Struktur data yang digunakan adalah **list**, yaitu untuk menyimpan kumpulan data tinggi badan mahasiswa. Karena menggunakan Binary Search, data tinggi badan harus sudah dalam keadaan terurut dari yang paling kecil sampai yang paling besar. Dengan algoritma ini, proses pencarian menjadi lebih efisien karena setiap langkah pencarian membagi data menjadi dua bagian, yaitu bagian kiri dan bagian kanan.

## 3. Source Code

<img width="1400" height="4242" alt="ss source code" src="https://github.com/user-attachments/assets/4e02f2cb-0e06-4ffc-b410-36fc1bf8000f" />

### Penjelasan Source Code

Program diawali dengan pembuatan fungsi `binary_search_barisan(data_tinggi, n, target)`. Fungsi ini digunakan untuk mencari tinggi badan mahasiswa dalam barisan upacara menggunakan algoritma **Binary Search**. Parameter `data_tinggi` digunakan untuk menerima list yang berisi data tinggi badan mahasiswa, parameter `n` digunakan untuk menerima jumlah data mahasiswa, sedangkan parameter `target` digunakan untuk menerima tinggi badan yang ingin dicari.

Di dalam fungsi tersebut, terdapat variabel `kiri` yang diberi nilai 0. Variabel ini digunakan untuk menunjukkan batas awal atau indeks paling kiri dari area pencarian. Selanjutnya, terdapat variabel `kanan` yang diberi nilai `n - 1`. Variabel ini digunakan untuk menunjukkan batas akhir atau indeks paling kanan dari area pencarian.

Variabel `posisi` diberi nilai awal -1. Nilai -1 digunakan sebagai tanda bahwa data belum ditemukan. Jika nantinya tinggi badan yang dicari ditemukan, maka nilai `posisi` akan diubah menjadi indeks tempat data tersebut berada.

Bagian `while kiri <= kanan` digunakan untuk menjalankan proses pencarian selama batas kiri masih lebih kecil atau sama dengan batas kanan. Artinya, selama masih ada bagian data yang bisa diperiksa, proses pencarian akan terus dilakukan.

Di dalam perulangan tersebut, terdapat variabel `tengah` yang digunakan untuk menentukan indeks tengah dari data yang sedang diperiksa. Rumus yang digunakan adalah `kiri + (kanan - kiri) // 2`. Indeks tengah ini menjadi titik pembanding antara tinggi badan yang dicari dengan data tinggi badan yang ada di dalam list.

Program kemudian menampilkan indeks tengah dan tinggi badan pada posisi tengah menggunakan perintah `print`. Bagian ini bertujuan untuk memperlihatkan proses kerja Binary Search, sehingga pengguna dapat melihat bagaimana program menentukan bagian data yang akan diperiksa.

Bagian `if data_tinggi[tengah] == target` digunakan untuk memeriksa apakah tinggi badan pada indeks tengah sama dengan tinggi badan yang dicari. Jika sama, maka data ditemukan. Nilai `posisi` akan diisi dengan indeks tengah, lalu perulangan dihentikan menggunakan perintah `break`.

Jika tinggi badan pada indeks tengah lebih kecil dari target, maka program menjalankan bagian `elif data_tinggi[tengah] < target`. Kondisi ini berarti tinggi badan yang dicari berada di bagian kanan list, karena data sudah terurut dari yang paling pendek sampai yang paling tinggi. Oleh karena itu, nilai `kiri` diubah menjadi `tengah + 1`.

Sebaliknya, jika tinggi badan pada indeks tengah lebih besar dari target, maka program akan masuk ke bagian `else`. Kondisi ini berarti tinggi badan yang dicari berada di bagian kiri list. Oleh karena itu, nilai `kanan` diubah menjadi `tengah - 1`.

Setelah proses pencarian selesai, fungsi akan mengembalikan nilai `posisi`. Jika data ditemukan, nilai yang dikembalikan adalah indeks dari tinggi badan yang dicari. Jika data tidak ditemukan, nilai yang dikembalikan tetap -1.

Selanjutnya, program memiliki fungsi `tentukan_bagian_barisan(posisi, n)`. Fungsi ini digunakan untuk menentukan apakah mahasiswa berada di bagian depan atau bagian belakang barisan. Parameter `posisi` digunakan untuk menerima indeks mahasiswa yang ditemukan, sedangkan parameter `n` digunakan untuk menerima jumlah seluruh mahasiswa dalam barisan.

Di dalam fungsi tersebut, variabel `nomor_barisan` diberi nilai `posisi + 1`. Hal ini dilakukan karena indeks list dimulai dari 0, sedangkan nomor barisan dalam kehidupan nyata biasanya dimulai dari 1. Jadi, jika data berada pada indeks 0, maka mahasiswa tersebut berada di barisan ke-1.

Variabel `batas_tengah` diberi nilai `n / 2`. Variabel ini digunakan sebagai batas untuk membedakan bagian depan dan bagian belakang barisan. Jika nomor barisan lebih kecil atau sama dengan batas tengah, maka mahasiswa dianggap berada di bagian depan. Jika nomor barisan lebih besar dari batas tengah, maka mahasiswa dianggap berada di bagian belakang.

Bagian `if nomor_barisan <= batas_tengah` digunakan untuk menentukan apakah mahasiswa berada pada bagian depan barisan. Jika kondisi tersebut benar, fungsi akan mengembalikan teks `"bagian depan"`. Jika tidak, fungsi akan mengembalikan teks `"bagian belakang"`.

Selanjutnya, terdapat fungsi `main()` yang menjadi fungsi utama program. Fungsi ini berisi alur utama mulai dari input data, proses pencarian, sampai menampilkan hasil pencarian.

Pada awal fungsi `main()`, program menampilkan judul program menggunakan perintah `print`. Judul ini berfungsi sebagai tampilan awal agar pengguna mengetahui bahwa program yang dijalankan adalah program pencarian posisi mahasiswa di barisan upacara.

Setelah itu, program meminta pengguna memasukkan jumlah mahasiswa menggunakan perintah `input`. Input tersebut diubah menjadi tipe data integer menggunakan `int`. Bagian ini diletakkan di dalam blok `try` agar program dapat menangani kesalahan input apabila pengguna memasukkan data yang bukan angka.

Jika pengguna memasukkan jumlah mahasiswa dengan format yang salah, maka bagian `except ValueError` akan dijalankan. Program akan menampilkan pesan bahwa input tidak valid dan jumlah mahasiswa harus berupa angka. Setelah itu, perintah `return` digunakan untuk menghentikan program agar tidak terjadi error pada proses berikutnya.

Setelah jumlah mahasiswa berhasil dimasukkan, program membuat list kosong bernama `data_tinggi`. List ini digunakan untuk menyimpan seluruh data tinggi badan mahasiswa yang akan dimasukkan oleh pengguna.

Program kemudian menampilkan instruksi bahwa tinggi badan mahasiswa harus dimasukkan dari yang paling pendek sampai yang paling tinggi. Hal ini penting karena algoritma Binary Search hanya dapat berjalan dengan benar jika data sudah dalam keadaan terurut.

Selanjutnya, program menjalankan perulangan `for i in range(n)`. Perulangan ini digunakan untuk meminta input tinggi badan mahasiswa sebanyak jumlah mahasiswa yang telah dimasukkan oleh pengguna.

Di dalam perulangan tersebut, terdapat perulangan `while True`. Perulangan ini digunakan agar program terus meminta input tinggi badan sampai pengguna memasukkan data yang valid berupa angka.

Pada bagian input tinggi badan, program menggunakan `int(input(...))` untuk mengubah input menjadi angka. Jika input valid, maka tinggi badan akan dimasukkan ke dalam list `data_tinggi` menggunakan perintah `append`, lalu perulangan dihentikan dengan perintah `break`.

Jika input tinggi badan tidak valid, maka blok `except ValueError` akan dijalankan. Program akan menampilkan pesan bahwa tinggi badan harus berupa angka, kemudian meminta pengguna untuk memasukkan ulang data tinggi badan.

Setelah semua data tinggi badan mahasiswa berhasil dimasukkan, program menampilkan isi list `data_tinggi`. Data ini menunjukkan urutan tinggi badan mahasiswa dalam barisan upacara, mulai dari yang paling pendek di depan sampai yang paling tinggi di belakang.

Selanjutnya, program meminta pengguna memasukkan tinggi badan mahasiswa yang ingin dicari. Input ini juga diletakkan di dalam perulangan `while True` dan blok `try-except` agar program hanya menerima input berupa angka.

Setelah tinggi badan target dimasukkan, program memanggil fungsi `binary_search_barisan(data_tinggi, n, target)`. Pemanggilan fungsi ini bertujuan untuk mencari apakah tinggi badan yang dimasukkan pengguna terdapat di dalam data barisan atau tidak.

Hasil dari fungsi tersebut disimpan ke dalam variabel `posisi`. Jika nilai `posisi` tidak sama dengan -1, berarti tinggi badan mahasiswa ditemukan dalam list. Program kemudian menghitung nomor barisan dengan rumus `posisi + 1`.

Setelah itu, program memanggil fungsi `tentukan_bagian_barisan(posisi, n)` untuk menentukan apakah mahasiswa berada di bagian depan atau bagian belakang barisan.

Jika data ditemukan, program akan menampilkan hasil pencarian. Hasil tersebut berisi informasi bahwa mahasiswa dengan tinggi badan yang dicari ditemukan, berada di barisan ke berapa, dan berada pada bagian depan atau bagian belakang barisan.

Jika nilai `posisi` sama dengan -1, berarti tinggi badan mahasiswa tidak ditemukan dalam data barisan. Program akan menampilkan pesan bahwa mahasiswa dengan tinggi badan tersebut tidak ditemukan.

Pada bagian akhir program terdapat kondisi `if __name__ == "__main__":`. Kondisi ini digunakan untuk memastikan bahwa fungsi `main()` hanya dijalankan ketika file Python dijalankan secara langsung. Perintah `main()` kemudian digunakan untuk menjalankan seluruh proses utama program.

## 4. Output Program

<img width="389" height="360" alt="Screenshot 2026-05-07 213609" src="https://github.com/user-attachments/assets/75050977-12f7-402f-9b31-870469d3f0d6" />

### Penjelasan Output Program

Pada output program, tampilan pertama yang muncul adalah judul program, yaitu **Pencarian Posisi Mahasiswa di Barisan Upacara**. Setelah itu, pengguna diminta memasukkan jumlah mahasiswa yang ada di dalam barisan.

Pada contoh output, pengguna memasukkan jumlah mahasiswa sebanyak **4 orang**. Setelah itu, program meminta pengguna memasukkan tinggi badan mahasiswa satu per satu dari yang paling pendek sampai yang paling tinggi.

Data tinggi badan yang dimasukkan adalah **140 cm**, **165 cm**, **170 cm**, dan **190 cm**. Data tersebut sudah dalam keadaan terurut menaik, sehingga sesuai dengan syarat penggunaan algoritma **Binary Search**.

Setelah semua data dimasukkan, program menampilkan data tinggi mahasiswa dalam barisan, yaitu `[140, 165, 170, 190]`. Data ini menunjukkan bahwa mahasiswa dengan tinggi badan paling pendek berada di bagian depan, sedangkan mahasiswa dengan tinggi badan paling tinggi berada di bagian belakang.

Kemudian pengguna memasukkan tinggi badan mahasiswa yang ingin dicari, yaitu **170 cm**. Program mulai melakukan pencarian menggunakan algoritma **Binary Search**.

Pada proses pertama, program menentukan indeks tengah yaitu **1** dengan nilai tinggi badan **165 cm**. Karena tinggi badan yang dicari, yaitu **170 cm**, lebih besar dari **165 cm**, maka program melanjutkan pencarian ke bagian kanan barisan.

Pada proses berikutnya, program menentukan indeks tengah yaitu **2** dengan nilai tinggi badan **170 cm**. Karena nilai tengah sama dengan target yang dicari, maka data berhasil ditemukan.

Hasil pencarian menunjukkan bahwa mahasiswa dengan tinggi badan **170 cm** ditemukan. Karena data tersebut berada pada indeks ke-2, maka posisi barisannya adalah **barisan ke-3**, sebab nomor barisan dihitung mulai dari 1, sedangkan indeks list dimulai dari 0.

Program juga menampilkan bahwa mahasiswa tersebut berada pada **bagian belakang barisan**. Hal ini karena barisan ke-3 dari total 4 mahasiswa sudah termasuk ke dalam setengah akhir barisan.

Dengan demikian, output program membuktikan bahwa program berhasil mencari posisi mahasiswa berdasarkan tinggi badan menggunakan algoritma **Binary Search**. Program juga berhasil menampilkan informasi tambahan berupa nomor barisan dan bagian posisi mahasiswa, yaitu bagian depan atau bagian belakang barisan.

## 5. Link YouTube

Link video presentasi/demo program:
https://youtu.be/mQOsM6W4vmE
