# Sistem Data Barang Toko Menggunakan Hash Map

## 1. Judul Program

Implementasi Hash Map pada Sistem Data Barang Toko

## 2. Deskripsi Singkat

Program ini merupakan program sederhana menggunakan bahasa Python yang menerapkan struktur data Hash Map.

Pada program ini, Hash Map digunakan untuk menyimpan data barang di toko.

Setiap barang memiliki kode barang yang digunakan sebagai key.

Data barang seperti nama barang, stok, dan harga digunakan sebagai value.

Program ini tidak menggunakan dictionary bawaan Python sebagai penyimpanan utama.

Penyimpanan data dibuat menggunakan class Hash Map sederhana agar konsep struktur datanya terlihat.

Setiap kode barang yang dimasukkan akan diproses menggunakan hash function.

Hash function digunakan untuk menentukan index penyimpanan data pada tabel hash.

Jika terdapat dua kode barang yang masuk ke index yang sama, maka terjadi collision.

Collision pada program ini ditangani menggunakan metode separate chaining.

Separate chaining dilakukan dengan menyimpan beberapa data dalam satu bucket atau list pada index yang sama.

Program ini memiliki beberapa fitur, yaitu menambahkan barang, mencari barang, menghapus barang, menampilkan semua barang, menampilkan isi hash table, dan keluar dari program.

## 3. Source Code

<img width="1200" height="4810" alt="image" src="https://github.com/user-attachments/assets/f0d7d30f-2ab8-4de3-a174-343b25da5fd8" />

### Penjelasan Source Code

Program ini dibuat menggunakan konsep Hash Map.

Pada program ini, data yang disimpan adalah data barang toko.

Data barang tersebut terdiri dari kode barang, nama barang, stok barang, dan harga barang.

Kode barang digunakan sebagai key karena setiap barang memiliki kode yang berbeda.

Nama barang, stok, dan harga digunakan sebagai value karena data tersebut merupakan informasi dari barang.

Program diawali dengan pembuatan class `hash_map`.

Class `hash_map` digunakan sebagai struktur utama untuk menyimpan dan mengolah data barang.

Di dalam class `hash_map`, terdapat method `__init__`.

Method `__init__` digunakan untuk membuat tabel hash ketika objek Hash Map pertama kali dibuat.

Pada method ini, terdapat atribut `size` dan `table`.

Atribut `size` digunakan untuk menentukan ukuran tabel hash.

Atribut `table` digunakan sebagai tempat penyimpanan data.

Tabel hash dibuat dalam bentuk list yang berisi beberapa bucket kosong.

Setiap bucket berbentuk list agar dapat menyimpan lebih dari satu data jika terjadi collision.

Setelah itu, terdapat method `hash_function`.

Method `hash_function` digunakan untuk mengubah key menjadi index pada tabel hash.

Key yang digunakan pada program ini adalah kode barang.

Di dalam method ini, setiap huruf pada key akan diubah menjadi nilai angka menggunakan fungsi `ord`.

Nilai dari setiap huruf kemudian dijumlahkan.

Hasil penjumlahan tersebut dibagi dengan ukuran tabel menggunakan operator modulus.

Hasil dari proses modulus digunakan sebagai index tempat data disimpan.

Method `tambah` digunakan untuk menambahkan data barang ke dalam Hash Map.

Method ini menerima dua parameter, yaitu `key` dan `value`.

Parameter `key` berisi kode barang.

Parameter `value` berisi data barang berupa nama barang, stok, dan harga.

Saat method `tambah` dijalankan, program akan mencari index menggunakan `hash_function`.

Setelah index ditemukan, program akan memeriksa bucket pada index tersebut.

Jika kode barang sudah ada di dalam bucket, maka data barang akan diperbarui.

Jika kode barang belum ada, maka data barang baru akan ditambahkan ke bucket.

Dengan cara ini, program dapat melakukan insert dan update data.

Method `cari` digunakan untuk mencari data barang berdasarkan kode barang.

Method ini juga menggunakan `hash_function` untuk menentukan index pencarian.

Setelah index ditemukan, program akan menelusuri bucket pada index tersebut.

Jika key yang dicari sama dengan kode barang yang tersimpan, maka data barang akan dikembalikan.

Jika data tidak ditemukan, maka method akan mengembalikan nilai `None`.

Method `hapus` digunakan untuk menghapus data barang berdasarkan kode barang.

Method ini mencari index terlebih dahulu menggunakan `hash_function`.

Setelah itu, program akan menelusuri bucket pada index tersebut.

Jika data dengan kode barang yang sesuai ditemukan, maka data tersebut akan dihapus dari bucket.

Jika data berhasil dihapus, method akan mengembalikan nilai `True`.

Jika data tidak ditemukan, method akan mengembalikan nilai `False`.

Method `tampilkan_semua` digunakan untuk menampilkan seluruh data barang.

Method ini menelusuri semua bucket yang ada di dalam tabel hash.

Jika bucket memiliki data, maka program akan menampilkan kode barang, nama barang, stok, dan harga.

Jika tidak ada data sama sekali, maka program akan menampilkan pesan bahwa data barang masih kosong.

Method `tampilkan_table` digunakan untuk menampilkan struktur isi hash table.

Method ini berguna untuk melihat posisi data berdasarkan index hasil hash function.

Dengan method ini, pengguna dapat melihat apakah ada data yang masuk ke index yang sama.

Jika lebih dari satu data berada pada index yang sama, maka hal tersebut menunjukkan adanya collision.

Collision tersebut tetap dapat ditangani karena program menggunakan separate chaining.

Setelah class `hash_map`, program membuat fungsi `menu`.

Fungsi `menu` digunakan untuk menampilkan pilihan menu kepada pengguna.

Menu yang tersedia terdiri dari tambah barang, cari barang, hapus barang, tampilkan semua barang, tampilkan hash table, dan keluar.

Selanjutnya terdapat fungsi `main`.

Fungsi `main` merupakan bagian utama dari program.

Di dalam fungsi ini, objek `data_barang` dibuat dari class `hash_map`.

Objek tersebut digunakan untuk menjalankan operasi pada Hash Map.

Program menggunakan perulangan `while True` agar menu terus ditampilkan selama pengguna belum memilih keluar.

Jika pengguna memilih menu 1, program akan meminta input kode barang, nama barang, stok barang, dan harga barang.

Setelah data dimasukkan, program akan menyimpan data tersebut ke dalam Hash Map menggunakan method `tambah`.

Jika pengguna memilih menu 2, program akan meminta kode barang yang ingin dicari.

Program kemudian menjalankan method `cari`.

Jika data ditemukan, maka program akan menampilkan nama barang, stok, dan harga barang.

Jika data tidak ditemukan, maka program akan menampilkan pesan bahwa data barang tidak ditemukan.

Jika pengguna memilih menu 3, program akan meminta kode barang yang ingin dihapus.

Program kemudian menjalankan method `hapus`.

Jika data berhasil dihapus, program akan menampilkan pesan bahwa data barang berhasil dihapus.

Jika data tidak ditemukan, program akan menampilkan pesan bahwa data barang tidak ditemukan.

Jika pengguna memilih menu 4, program akan menampilkan seluruh data barang yang sudah tersimpan.

Jika pengguna memilih menu 5, program akan menampilkan isi hash table.

Menu ini digunakan untuk menunjukkan bagaimana data disimpan berdasarkan index hash.

Jika pengguna memilih menu 0, program akan menampilkan pesan bahwa program selesai.

Setelah itu, perulangan dihentikan menggunakan perintah `break`.

Jika pengguna memasukkan pilihan selain menu yang tersedia, maka program akan menampilkan pesan bahwa pilihan tidak valid.

Secara keseluruhan, program ini menerapkan operasi dasar pada Hash Map.

Operasi tersebut terdiri dari insert, search, delete, dan display.

Program ini dibuat sederhana agar konsep Hash Map mudah dipahami.

Contoh penerapannya dikaitkan dengan kehidupan sehari-hari, yaitu sistem data barang toko.

## 4. Output Program

<img width="990" height="5436" alt="image" src="https://github.com/user-attachments/assets/fdfea689-4488-4da4-85cc-89e07a5c2683" />

### Penjelasan Output Program

Pada output program, pertama kali muncul menu utama Sistem Data Barang Toko.

Menu tersebut berisi pilihan untuk menambah barang, mencari barang, menghapus barang, menampilkan semua barang, menampilkan hash table, dan keluar dari program.

Pada contoh demo, pengguna memasukkan beberapa data barang.

Data barang yang dimasukkan adalah BRG001, BRG002, dan BRG010.

Barang pertama memiliki kode BRG001 dengan nama Mouse.

Barang kedua memiliki kode BRG002 dengan nama Keyboard.

Barang ketiga memiliki kode BRG010 dengan nama Flashdisk.

Ketika pengguna memilih menu tampilkan semua barang, program akan menampilkan semua data barang yang sudah dimasukkan.

Data yang ditampilkan terdiri dari kode barang, nama barang, stok, dan harga.

Kemudian pengguna mencari barang dengan kode BRG010.

Karena kode tersebut sudah tersimpan di dalam Hash Map, program menampilkan data barang yang sesuai.

Setelah itu, pengguna menghapus barang dengan kode BRG002.

Program kemudian menampilkan pesan bahwa data barang berhasil dihapus.

Ketika pengguna menampilkan semua barang lagi, data BRG002 sudah tidak muncul.

Hal ini menunjukkan bahwa proses penghapusan data berhasil dilakukan.

Selanjutnya pengguna memilih menu tampilkan hash table.

Pada menu ini, program menampilkan posisi data berdasarkan index pada tabel hash.

Jika terdapat lebih dari satu kode barang pada index yang sama, maka hal tersebut menunjukkan terjadinya collision.

Collision tersebut ditangani menggunakan separate chaining.

Dengan demikian, output program menunjukkan bahwa Hash Map dapat digunakan untuk menyimpan, mencari, dan menghapus data barang.

## 5. Contoh Alur Demo Program

Contoh data yang digunakan:

1. BRG001 - Mouse - 10 - 75000
2. BRG002 - Keyboard - 5 - 150000
3. BRG010 - Flashdisk - 12 - 65000

Alur demo:

1. Jalankan program.
2. Pilih menu 1 untuk menambahkan barang pertama.
3. Masukkan kode barang BRG001.
4. Masukkan nama barang Mouse.
5. Masukkan stok barang 10.
6. Masukkan harga barang 75000.
7. Pilih menu 1 lagi untuk menambahkan barang kedua.
8. Masukkan kode barang BRG002.
9. Masukkan nama barang Keyboard.
10. Masukkan stok barang 5.
11. Masukkan harga barang 150000.
12. Pilih menu 1 lagi untuk menambahkan barang ketiga.
13. Masukkan kode barang BRG010.
14. Masukkan nama barang Flashdisk.
15. Masukkan stok barang 12.
16. Masukkan harga barang 65000.
17. Pilih menu 4 untuk menampilkan semua data barang.
18. Pilih menu 2 untuk mencari data barang.
19. Masukkan kode barang BRG010.
20. Pilih menu 3 untuk menghapus data barang.
21. Masukkan kode barang BRG002.
22. Pilih menu 4 untuk menampilkan data setelah penghapusan.
23. Pilih menu 5 untuk menampilkan struktur hash table.
24. Pilih menu 0 untuk keluar dari program.

## 6. Kesimpulan

Program Sistem Data Barang Toko berhasil menerapkan konsep Hash Map.

Hash Map digunakan untuk menyimpan data dalam bentuk pasangan key dan value.

Kode barang digunakan sebagai key.

Data barang berupa nama, stok, dan harga digunakan sebagai value.

Program menggunakan hash function untuk menentukan index penyimpanan data.

Hash function mengubah kode barang menjadi index pada tabel hash.

Jika terdapat data yang masuk ke index yang sama, maka terjadi collision.

Collision pada program ini ditangani menggunakan metode separate chaining.

Separate chaining membuat beberapa data tetap dapat disimpan pada index yang sama.

Program ini dapat melakukan penambahan data, pencarian data, penghapusan data, dan menampilkan data.

Dengan program ini, konsep Hash Map dapat diterapkan pada contoh sederhana dalam kehidupan sehari-hari.

Contoh penerapan tersebut adalah sistem data barang toko.

## 7. Link YouTube

Link video presentasi/demo program:
https://youtu.be/atJrV5Im33U
