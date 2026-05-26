# Sistem Antrean Pasien Menggunakan BST

## 1. Judul Program

Implementasi Binary Search Tree pada Sistem Nomor Antrean Pasien

## 2. Deskripsi Singkat

Program ini merupakan program sederhana menggunakan bahasa Python yang menerapkan struktur data Binary Search Tree atau BST.

Pada program ini, BST digunakan untuk menyimpan nomor antrean pasien di klinik. Setiap nomor antrean yang dimasukkan akan disimpan berdasarkan aturan BST. Jika nomor antrean lebih kecil dari node saat ini, maka data akan masuk ke sebelah kiri. Jika nomor antrean lebih besar, maka data akan masuk ke sebelah kanan.

Program ini memiliki beberapa fitur, yaitu menambahkan nomor antrean, mencari nomor antrean, menampilkan nomor antrean secara urut, dan keluar dari program.

## 3. Source Code

<img width="1264" height="3710" alt="source_code" src="https://github.com/user-attachments/assets/ff725ef1-8bf3-485f-9b2b-bb962e8e193f" />

### Penjelasan Source Code

Program ini dibuat menggunakan konsep Binary Search Tree atau BST. Pada program ini, data yang disimpan adalah nomor antrean pasien. Nomor antrean tersebut menjadi nilai utama yang digunakan untuk menentukan posisi data di dalam tree.

Program diawali dengan pembuatan class `Node`. Class ini digunakan untuk membuat simpul atau node baru pada BST. Setiap node memiliki tiga bagian, yaitu `nomor`, `left`, dan `right`. Bagian `nomor` digunakan untuk menyimpan nomor antrean pasien. Bagian `left` digunakan untuk menghubungkan node dengan anak sebelah kiri, sedangkan bagian `right` digunakan untuk menghubungkan node dengan anak sebelah kanan.

Pada saat objek `Node` dibuat, nilai `left` dan `right` masih berisi `None`. Hal ini karena node yang baru dibuat belum memiliki cabang kiri maupun cabang kanan. Cabang tersebut baru akan terisi jika ada data lain yang dimasukkan ke dalam tree.

Setelah class `Node`, program membuat class `BST`. Class ini berfungsi sebagai tempat untuk mengatur seluruh proses yang berhubungan dengan Binary Search Tree, seperti menambahkan data, mencari data, dan menampilkan data. Di dalam class `BST`, terdapat atribut `root`. Atribut ini digunakan untuk menyimpan node pertama atau akar dari tree.

Pada awal program, nilai `root` adalah `None`. Artinya, tree masih kosong dan belum memiliki data. Ketika pengguna memasukkan nomor antrean pertama kali, nomor tersebut akan menjadi root dari BST.

Method `tambah` digunakan untuk menambahkan nomor antrean baru ke dalam BST. Method ini menerima satu parameter, yaitu `nomor`, yang berasal dari input pengguna. Di dalam method ini, proses penambahan data tidak langsung dilakukan, tetapi diteruskan ke method `_tambah`.

Method `_tambah` merupakan method rekursif yang digunakan untuk menentukan posisi nomor antrean di dalam tree. Rekursif berarti method tersebut dapat memanggil dirinya sendiri sampai menemukan posisi yang sesuai.

Jika `root` bernilai `None`, maka program akan membuat node baru dengan nomor antrean yang dimasukkan. Kondisi ini terjadi jika tree masih kosong atau jika proses penelusuran sudah sampai pada tempat kosong yang cocok untuk data baru.

Jika nomor antrean yang dimasukkan lebih kecil dari nomor pada node saat ini, maka data akan diarahkan ke sebelah kiri. Hal ini sesuai dengan aturan BST, yaitu nilai yang lebih kecil ditempatkan di bagian kiri.

Sebaliknya, jika nomor antrean yang dimasukkan lebih besar dari nomor pada node saat ini, maka data akan diarahkan ke sebelah kanan. Hal ini juga sesuai dengan aturan BST, yaitu nilai yang lebih besar ditempatkan di bagian kanan.

Jika nomor antrean yang dimasukkan sama dengan nomor yang sudah ada di dalam tree, maka program akan menampilkan pesan bahwa nomor antrean sudah ada. Dengan begitu, nomor antrean yang sama tidak akan dimasukkan dua kali.

Method `cari` digunakan untuk mencari nomor antrean yang sudah tersimpan di dalam BST. Method ini menerima input berupa nomor yang ingin dicari oleh pengguna. Proses pencarian kemudian diteruskan ke method `_cari`.

Method `_cari` juga menggunakan konsep rekursif. Pencarian dimulai dari root. Jika node yang sedang diperiksa bernilai `None`, maka artinya nomor antrean tidak ditemukan di dalam tree.

Jika nomor yang dicari sama dengan nomor pada node saat ini, maka method akan mengembalikan nilai `True`. Nilai ini menunjukkan bahwa nomor antrean berhasil ditemukan.

Jika nomor yang dicari lebih kecil dari nomor pada node saat ini, maka pencarian dilanjutkan ke bagian kiri. Namun, jika nomor yang dicari lebih besar, maka pencarian dilanjutkan ke bagian kanan.

Cara pencarian seperti ini membuat proses pencarian menjadi lebih terarah. Program tidak perlu mengecek semua data satu per satu dari awal, tetapi cukup mengikuti jalur kiri atau kanan sesuai nilai yang dicari.

Method `tampil_urut` digunakan untuk menampilkan semua nomor antrean yang tersimpan di dalam BST. Method ini memanggil method `_inorder` untuk melakukan proses traversal.

Method `_inorder` menggunakan teknik inorder traversal. Urutan inorder adalah kiri, root, lalu kanan. Pada BST, traversal inorder akan menghasilkan tampilan data yang terurut dari nilai terkecil sampai terbesar.

Contohnya, jika pengguna memasukkan nomor antrean 50, 30, dan 70, maka nomor 50 akan menjadi root. Nomor 30 masuk ke kiri karena lebih kecil dari 50, sedangkan nomor 70 masuk ke kanan karena lebih besar dari 50.

Ketika data ditampilkan menggunakan inorder traversal, hasil yang muncul adalah 30 50 70. Hal ini menunjukkan bahwa data berhasil ditampilkan secara urut meskipun urutan input awalnya adalah 50, 30, lalu 70.

Selanjutnya terdapat fungsi `main`. Fungsi ini merupakan bagian utama dari program. Di dalam fungsi ini, objek `bst` dibuat dari class `BST`. Objek tersebut digunakan untuk menjalankan operasi pada Binary Search Tree.

Program menggunakan perulangan `while True` agar menu dapat terus ditampilkan selama pengguna belum memilih keluar. Menu yang tersedia terdiri dari tambah nomor antrean, cari nomor antrean, tampilkan nomor antrean, dan keluar dari program.

Jika pengguna memilih menu 1, program akan meminta input nomor antrean. Nomor tersebut kemudian dimasukkan ke dalam BST menggunakan method `tambah`. Setelah itu, program menampilkan pesan bahwa nomor antrean berhasil ditambahkan.

Jika pengguna memilih menu 2, program akan meminta nomor antrean yang ingin dicari. Program kemudian menjalankan method `cari`. Jika hasilnya `True`, maka program menampilkan pesan bahwa nomor antrean ditemukan. Jika hasilnya `False`, maka program menampilkan pesan bahwa nomor antrean tidak ditemukan.

Jika pengguna memilih menu 3, program akan menampilkan seluruh nomor antrean yang sudah dimasukkan. Data ditampilkan menggunakan inorder traversal sehingga hasilnya tersusun dari nomor terkecil sampai nomor terbesar.

Jika pengguna memilih menu 4, program akan menampilkan pesan bahwa program selesai, lalu perulangan dihentikan menggunakan perintah `break`.

Jika pengguna memasukkan pilihan selain 1 sampai 4, maka program akan menampilkan pesan bahwa pilihan tidak valid. Hal ini dilakukan agar program tetap berjalan meskipun pengguna memasukkan menu yang salah.

Secara keseluruhan, program ini menerapkan operasi dasar pada Binary Search Tree, yaitu insert, search, dan inorder traversal. Program dibuat sederhana agar konsep BST lebih mudah dipahami dan dapat dikaitkan dengan contoh kehidupan sehari-hari, yaitu sistem nomor antrean pasien.

## 4. Output Program

<img width="683" height="1764" alt="codesnap_output_antrean_pasien" src="https://github.com/user-attachments/assets/db1ba77f-ef4d-4912-9cb7-f64c472516f5" />

### Penjelasan Output Program

Pada output program, pertama kali muncul menu utama Sistem Antrean Pasien. Menu tersebut berisi pilihan untuk menambah nomor antrean, mencari nomor antrean, menampilkan nomor antrean, dan keluar dari program.

Pada contoh demo, pengguna memasukkan beberapa nomor antrean, yaitu 50, 30, dan 70. Nomor 50 menjadi root karena dimasukkan pertama kali. Nomor 30 masuk ke kiri karena lebih kecil dari 50. Nomor 70 masuk ke kanan karena lebih besar dari 50.

Ketika pengguna memilih menu tampilkan nomor antrean, program menampilkan nomor antrean secara urut, yaitu 30 50 70.

Kemudian pengguna mencari nomor antrean 30. Karena nomor tersebut ada di dalam tree, program menampilkan pesan bahwa nomor antrean ditemukan.

Dengan demikian, output program menunjukkan bahwa Binary Search Tree dapat digunakan untuk menyimpan dan mencari data nomor antrean.

## 5. Contoh Alur Demo Program

Contoh data yang digunakan:

1. 50
2. 30
3. 70

Alur demo:

1. Pilih menu 1, lalu masukkan nomor antrean 50.
2. Pilih menu 1, lalu masukkan nomor antrean 30.
3. Pilih menu 1, lalu masukkan nomor antrean 70.
4. Pilih menu 3 untuk menampilkan nomor antrean.
5. Pilih menu 2 untuk mencari nomor antrean.
6. Masukkan nomor 30.
7. Pilih menu 4 untuk keluar dari program.

## 6. Kesimpulan

Program Sistem Antrean Pasien berhasil menerapkan konsep Binary Search Tree. BST digunakan untuk menyimpan nomor antrean pasien berdasarkan aturan kiri dan kanan.

Data yang lebih kecil akan masuk ke bagian kiri, sedangkan data yang lebih besar akan masuk ke bagian kanan. Program ini juga dapat menampilkan nomor antrean secara urut menggunakan inorder traversal.

Dengan program ini, konsep BST dapat diterapkan pada contoh sederhana dalam kehidupan sehari-hari, yaitu sistem nomor antrean pasien.

## 7. Link YouTube

Link video presentasi/demo program:
(https://youtu.be/P0snvAS_1jM)
