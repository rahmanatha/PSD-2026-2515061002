# Sistem Pengurutan Harga Kopi Coffee Shop

## 1. Judul Program

Sistem Pengurutan Harga Kopi Coffee Shop Menggunakan Insertion Sort

## 2. Deskripsi Singkat

Program ini merupakan program sederhana berbasis bahasa Python yang digunakan untuk mengelola data kopi pada sebuah coffee shop. Data yang dimasukkan oleh pengguna berupa nama kopi dan harga kopi. Setelah seluruh data dimasukkan, program akan menampilkan daftar kopi sebelum dilakukan proses pengurutan.

Program ini menerapkan algoritma **Insertion Sort** untuk mengurutkan data kopi berdasarkan harga dari yang termurah hingga yang termahal. Struktur data yang digunakan adalah **list** yang berisi kumpulan data berbentuk **dictionary**, di mana setiap dictionary menyimpan nama kopi dan harga kopi. Dengan menggunakan algoritma ini, setiap data kopi dibandingkan satu per satu berdasarkan harga, kemudian ditempatkan pada posisi yang sesuai agar urutannya menjadi benar.

## 3. Source Code

<img width="1402" height="2838" alt="SS SOURCE CODE" src="https://github.com/user-attachments/assets/2cd2f846-701a-45a9-8e1a-d3cb3c266226" />

### Penjelasan Source Code

Program diawali dengan pembuatan fungsi `insertion_sort_kopi(data_kopi, n)`. Fungsi ini digunakan untuk mengurutkan data kopi berdasarkan harga menggunakan algoritma **Insertion Sort**. Parameter `data_kopi` digunakan untuk menerima list yang berisi data-data kopi, sedangkan parameter `n` digunakan untuk menerima jumlah data kopi yang akan diurutkan.

Pada bagian awal fungsi, terdapat perulangan `for i in range(1, n)`. Perulangan ini dimulai dari indeks ke-1 karena data pada indeks ke-0 dianggap sudah berada pada posisi yang benar. Setiap data pada indeks ke-`i` akan dibandingkan dengan data-data sebelumnya untuk menentukan posisi yang tepat.

Variabel `temp` digunakan untuk menyimpan sementara data kopi yang sedang dibandingkan. Data ini perlu disimpan sementara agar tidak hilang ketika terjadi proses pergeseran data. Selanjutnya, variabel `j` diberi nilai `i - 1`, yang berarti menunjuk ke indeks sebelum data yang sedang dibandingkan.

Bagian `while j >= 0 and data_kopi[j]["harga"] > temp["harga"]` digunakan untuk membandingkan harga kopi sebelumnya dengan harga kopi yang sedang disimpan di variabel `temp`. Selama indeks `j` masih valid dan harga kopi sebelumnya lebih besar daripada harga kopi pada `temp`, maka data kopi tersebut akan digeser satu posisi ke kanan.

Perintah `data_kopi[j + 1] = data_kopi[j]` digunakan untuk menggeser data kopi yang memiliki harga lebih besar ke posisi sebelah kanan. Setelah itu, perintah `j -= 1` digunakan untuk mengurangi nilai `j` agar proses perbandingan dapat dilanjutkan ke data sebelumnya.

Setelah proses perbandingan selesai dan posisi yang sesuai ditemukan, perintah `data_kopi[j + 1] = temp` digunakan untuk menempatkan data kopi yang disimpan sementara ke posisi yang tepat. Dengan proses ini, data kopi akan tersusun berdasarkan harga dari yang termurah sampai yang termahal.

Selanjutnya, program memiliki fungsi `main()` yang digunakan sebagai fungsi utama. Di dalam fungsi ini, program pertama kali menampilkan judul program menggunakan perintah `print`. Judul tersebut berfungsi sebagai tampilan awal agar pengguna mengetahui bahwa program yang dijalankan adalah sistem pengurutan harga kopi coffee shop.

Setelah itu, program meminta pengguna memasukkan jumlah kopi menggunakan perintah `input`. Input tersebut diubah menjadi tipe data integer menggunakan `int`. Proses input jumlah kopi diletakkan di dalam blok `try` agar program dapat menangani kesalahan input. Jika pengguna memasukkan data yang bukan angka, maka blok `except ValueError` akan dijalankan dan program menampilkan pesan bahwa input tidak valid.

Jika input jumlah kopi tidak valid, perintah `return` digunakan untuk menghentikan fungsi `main()` sehingga program tidak melanjutkan proses berikutnya. Hal ini dilakukan agar program tidak mengalami error saat jumlah data yang dimasukkan tidak sesuai.

Setelah jumlah kopi berhasil dimasukkan, program membuat list kosong bernama `data_kopi`. List ini digunakan sebagai tempat penyimpanan seluruh data kopi yang akan dimasukkan oleh pengguna. Setiap data kopi nantinya akan disimpan dalam bentuk dictionary.

Program kemudian menjalankan perulangan `for i in range(n)` untuk meminta input data kopi sebanyak jumlah yang sudah dimasukkan pengguna. Pada setiap perulangan, program menampilkan keterangan data kopi ke berapa yang sedang diinput, kemudian meminta pengguna memasukkan nama kopi.

Setelah nama kopi dimasukkan, program meminta pengguna memasukkan harga kopi. Input harga kopi diletakkan di dalam perulangan `while True` agar program terus meminta harga sampai pengguna memasukkan angka yang valid. Jika input harga tidak valid, maka blok `except ValueError` akan dijalankan dan program menampilkan pesan kesalahan bahwa harga harus berupa angka.

Jika harga kopi yang dimasukkan sudah valid, perintah `break` digunakan untuk menghentikan perulangan input harga. Setelah itu, data kopi yang berisi nama dan harga akan dimasukkan ke dalam list `data_kopi` menggunakan perintah `append`.

Data kopi disimpan dalam bentuk dictionary dengan dua bagian, yaitu `nama` untuk menyimpan nama kopi dan `harga` untuk menyimpan harga kopi. Dengan bentuk ini, setiap data kopi memiliki informasi yang jelas dan mudah diakses saat proses pengurutan dilakukan.

Setelah seluruh data kopi selesai dimasukkan, program menampilkan daftar kopi sebelum diurutkan. Program menggunakan perulangan `for kopi in data_kopi` untuk mengambil setiap data kopi yang ada di dalam list, kemudian menampilkan nama dan harga kopi menggunakan perintah `print`.

Selanjutnya, program memanggil fungsi `insertion_sort_kopi(data_kopi, n)`. Pemanggilan fungsi ini bertujuan untuk mengurutkan data kopi berdasarkan harga dari yang termurah hingga yang termahal. Proses pengurutan dilakukan langsung pada list `data_kopi`.

Setelah proses pengurutan selesai, program menampilkan daftar kopi yang sudah diurutkan. Program kembali menggunakan perulangan untuk menampilkan setiap data kopi yang ada di dalam list. Hasil yang ditampilkan adalah data kopi yang sudah tersusun berdasarkan harga secara menaik.

Pada bagian akhir program terdapat kondisi `if __name__ == "__main__":`. Kondisi ini digunakan untuk memastikan bahwa fungsi `main()` hanya dijalankan ketika file Python dijalankan secara langsung. Perintah `main()` kemudian digunakan untuk menjalankan seluruh proses utama program.

## 4. Output Program

<img width="472" height="486" alt="image" src="https://github.com/user-attachments/assets/2a59b4b4-dafb-46f9-944d-fbb2b258b133" />

### Penjelasan Output Program

Pada output program, tampilan pertama yang muncul adalah judul program, yaitu sistem pengurutan harga kopi coffee shop. Setelah itu, pengguna diminta memasukkan jumlah data kopi yang ingin diinput ke dalam program.

Setelah jumlah kopi dimasukkan, program akan meminta pengguna mengisi data kopi satu per satu. Setiap data terdiri dari nama kopi dan harga kopi. Program akan terus meminta input harga sampai pengguna memasukkan angka yang valid, sehingga program dapat berjalan tanpa error.

Setelah semua data berhasil dimasukkan, program menampilkan daftar kopi sebelum diurutkan. Pada bagian ini, data kopi masih ditampilkan sesuai urutan input dari pengguna. Hal ini bertujuan untuk memperlihatkan kondisi awal data sebelum proses pengurutan dilakukan.

Kemudian program menjalankan proses pengurutan menggunakan algoritma **Insertion Sort**. Data kopi diurutkan berdasarkan nilai harga dari yang paling kecil sampai yang paling besar.

Setelah proses pengurutan selesai, program menampilkan daftar kopi setelah diurutkan dari harga termurah ke harga termahal. Output ini membuktikan bahwa program berjalan sesuai dengan studi kasus, yaitu mengurutkan harga kopi pada coffee shop tanpa terjadi error.

## 5. Link YouTube

Link video presentasi/demo program:
https://youtu.be/4aeqX816H3I
