# Sistem Antrean Print Tugas

## 1. Judul Program

Implementasi Stack dan Queue pada Sistem Antrean Print Tugas

## 2. Deskripsi Singkat

Program ini merupakan program sederhana berbasis bahasa Python yang digunakan untuk mengelola antrean file yang akan diprint. Pada studi kasus ini, file yang masuk terlebih dahulu ke dalam antrean akan diproses atau diprint terlebih dahulu.

Program ini menerapkan dua struktur data, yaitu **Queue** dan **Stack**. Queue digunakan untuk menyimpan antrean file yang menunggu untuk diprint. Queue bekerja dengan prinsip **FIFO** atau **First In First Out**, yaitu data yang pertama masuk akan menjadi data yang pertama keluar.

Selain itu, program juga menggunakan Stack untuk menyimpan riwayat file yang sudah diprint. Stack bekerja dengan prinsip **LIFO** atau **Last In First Out**, yaitu data yang terakhir masuk akan menjadi data yang pertama keluar. Dalam program ini, riwayat file terakhir yang diprint akan berada di posisi paling atas dan dapat dihapus terlebih dahulu.

Dengan adanya program ini, pengguna dapat menambahkan file ke antrean print, memproses file yang berada di antrean paling depan, menampilkan antrean dan riwayat print, serta menghapus riwayat terakhir.

## 3. Source Code

<img width="1326" height="3634" alt="ss source code" src="https://github.com/user-attachments/assets/82fa1c10-d101-4422-9540-71177b938b28" />

### Penjelasan Source Code

Program diawali dengan pembuatan class `StackRiwayat`. Class ini digunakan untuk menyimpan riwayat file yang sudah diprint. Di dalam class tersebut terdapat atribut `stack` yang berupa list kosong. List ini digunakan sebagai tempat penyimpanan data riwayat file.

Pada class `StackRiwayat`, terdapat method `push(file)`. Method ini digunakan untuk menambahkan file ke dalam stack riwayat setelah file tersebut selesai diprint. Penambahan data dilakukan menggunakan perintah `append`, sehingga file baru akan masuk ke posisi paling akhir atau paling atas pada stack.

Selanjutnya, terdapat method `pop()`. Method ini digunakan untuk menghapus riwayat file terakhir yang sudah diprint. Sebelum menghapus data, program akan memeriksa apakah stack kosong atau tidak. Jika stack kosong, program akan menampilkan pesan bahwa riwayat print kosong. Jika stack tidak kosong, maka data paling akhir akan dihapus menggunakan perintah `pop`.

Method berikutnya adalah `display()`. Method ini digunakan untuk menampilkan seluruh riwayat file yang sudah diprint. Jika stack kosong, program akan menampilkan pesan bahwa riwayat print kosong. Jika stack berisi data, maka program akan menampilkan isi stack dari data terakhir ke data pertama menggunakan fungsi `reversed`.

Setelah class Stack dibuat, program dilanjutkan dengan pembuatan class `QueuePrint`. Class ini digunakan untuk menyimpan antrean file yang akan diprint. Di dalam class ini terdapat atribut `queue` yang berupa list kosong. List tersebut digunakan sebagai tempat penyimpanan data antrean file.

Pada class `QueuePrint`, terdapat method `enqueue(file)`. Method ini digunakan untuk menambahkan file baru ke dalam antrean print. File yang dimasukkan pengguna akan ditambahkan ke bagian belakang antrean menggunakan perintah `append`.

Selanjutnya, terdapat method `dequeue()`. Method ini digunakan untuk memproses file yang berada di antrean paling depan. Sebelum memproses file, program akan memeriksa apakah antrean kosong atau tidak. Jika antrean kosong, program akan menampilkan pesan bahwa antrean print kosong. Jika antrean berisi data, maka file paling depan akan diambil menggunakan perintah `pop(0)`.

Perintah `pop(0)` digunakan karena Queue menerapkan prinsip FIFO. Artinya, file yang pertama kali masuk ke antrean akan menjadi file pertama yang diproses atau diprint.

Method berikutnya adalah `display()`. Method ini digunakan untuk menampilkan semua file yang masih berada di dalam antrean print. Jika antrean kosong, program akan menampilkan pesan bahwa antrean print kosong. Jika antrean berisi data, maka program akan menampilkan file satu per satu sesuai urutan antrean.

Setelah kedua class dibuat, program memiliki fungsi `main()`. Fungsi ini menjadi bagian utama dari program yang mengatur jalannya menu dan interaksi dengan pengguna.

Di dalam fungsi `main()`, terdapat objek `antrean` yang dibuat dari class `QueuePrint`. Objek ini digunakan untuk mengelola file yang masih menunggu untuk diprint. Selain itu, terdapat objek `riwayat` yang dibuat dari class `StackRiwayat`. Objek ini digunakan untuk mengelola file yang sudah selesai diprint.

Program kemudian menjalankan perulangan `while True`. Perulangan ini digunakan agar menu program terus ditampilkan sampai pengguna memilih menu keluar.

Pada menu pertama, pengguna dapat menambahkan file ke antrean print. Program akan meminta nama file, kemudian file tersebut dimasukkan ke dalam Queue menggunakan method `enqueue`.

Pada menu kedua, pengguna dapat memproses atau mencetak file. Program akan mengambil file paling depan dari antrean menggunakan method `dequeue`. Jika file berhasil diproses, file tersebut akan dimasukkan ke dalam riwayat print menggunakan method `push`.

Pada menu ketiga, pengguna dapat menampilkan data. Program akan menampilkan antrean file yang belum diprint dan riwayat file yang sudah diprint.

Pada menu keempat, pengguna dapat menghapus riwayat terakhir. Program akan menghapus file terakhir yang masuk ke riwayat menggunakan method `pop` pada Stack.

Pada menu kelima, program akan berhenti. Perulangan dihentikan menggunakan perintah `break`, lalu program menampilkan pesan bahwa program selesai.

Pada bagian akhir program terdapat kondisi `if __name__ == "__main__":`. Kondisi ini digunakan agar fungsi `main()` hanya dijalankan ketika file Python dijalankan secara langsung.

## 4. Output Program

<img width="543" height="776" alt="image" src="https://github.com/user-attachments/assets/000a5287-0f5d-4626-a902-f2e0c93adf22" />
<br><br>
<img width="319" height="946" alt="image" src="https://github.com/user-attachments/assets/117e7513-d0a1-4f5c-9ba6-7eb4fcedff9b" />

### Penjelasan Output Program

Pada output program, tampilan pertama yang muncul adalah menu utama dari program **Sistem Antrean Print Tugas**. Menu tersebut berisi pilihan untuk menambahkan file ke antrean, mencetak file, menampilkan data, menghapus riwayat terakhir, dan keluar dari program.

Pada contoh demo, pengguna memasukkan tiga file ke dalam antrean, yaitu **File A**, **File B**, dan **File C**. File tersebut dimasukkan secara berurutan menggunakan menu tambah file ke antrean.

Setelah ketiga file dimasukkan, program menampilkan data antrean. Pada tampilan antrean, urutan file yang muncul adalah **File A**, **File B**, dan **File C**. Hal ini menunjukkan bahwa file disimpan sesuai urutan masuk.

Kemudian pengguna memilih menu print file. Program memproses file yang berada di antrean paling depan, yaitu **File A**. Hal ini menunjukkan penerapan Queue dengan prinsip **FIFO**, karena File A adalah file yang pertama masuk dan menjadi file pertama yang diproses.

Setelah File A diprint, file tersebut masuk ke dalam riwayat print. Ketika data ditampilkan kembali, antrean print hanya berisi **File B** dan **File C**, sedangkan riwayat print berisi **File A**.

Selanjutnya, pengguna kembali memilih menu print file. Program memproses file berikutnya, yaitu **File B**. Setelah File B diprint, file tersebut masuk ke dalam riwayat print.

Ketika data ditampilkan, antrean print hanya berisi **File C**. Pada bagian riwayat print, urutan yang muncul adalah **File B** kemudian **File A**. Hal ini menunjukkan penerapan Stack dengan prinsip **LIFO**, karena File B adalah file terakhir yang masuk ke riwayat dan ditampilkan di posisi paling atas.

Kemudian pengguna memilih menu hapus riwayat terakhir. Program menghapus **File B** dari riwayat print, karena File B berada di posisi paling atas pada Stack. Setelah itu, riwayat print hanya menyisakan **File A**.

Dengan demikian, output program membuktikan bahwa Queue digunakan untuk mengatur antrean file yang akan diprint, sedangkan Stack digunakan untuk mengatur riwayat file yang sudah diprint.

## 5. Contoh Alur Demo Program

Contoh data yang digunakan:

1. File A
2. File B
3. File C

Alur demo:

1. Pilih menu 1, lalu masukkan File A.
2. Pilih menu 1, lalu masukkan File B.
3. Pilih menu 1, lalu masukkan File C.
4. Pilih menu 3 untuk menampilkan data antrean.
5. Pilih menu 2 untuk print file pertama.
6. Pilih menu 3 untuk melihat perubahan antrean dan riwayat.
7. Pilih menu 2 untuk print file kedua.
8. Pilih menu 3 untuk melihat bahwa File B berada di posisi paling atas riwayat.
9. Pilih menu 4 untuk menghapus riwayat terakhir.
10. Pilih menu 5 untuk keluar dari program.

## 6. Kesimpulan

Program Sistem Antrean Print Tugas berhasil menerapkan konsep Stack dan Queue dalam kehidupan sehari-hari. Queue digunakan untuk mengatur antrean file yang akan diprint, sehingga file yang pertama masuk akan diproses terlebih dahulu. Stack digunakan untuk menyimpan riwayat file yang sudah diprint, sehingga file yang terakhir diprint akan berada di posisi paling atas dan dapat dihapus terlebih dahulu.

## 7. Link YouTube

Link video presentasi/demo program:
https://youtu.be/cN2vxKFCyJ8
