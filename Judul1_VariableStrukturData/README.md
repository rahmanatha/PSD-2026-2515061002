# Sistem Antrian Mahasiswa Menggunakan Singly Linked List

## Judul Program

Sistem Antrian Mahasiswa Menggunakan Singly Linked List

## Identitas

Nama: Abdu Ar Rahman Athallah  
NPM: 2515061002

## Deskripsi Singkat

Program ini merupakan implementasi struktur data **Singly Linked List** menggunakan bahasa pemrograman Python. Studi kasus yang digunakan adalah sistem antrian mahasiswa. Program ini dapat digunakan untuk menambahkan mahasiswa ke dalam antrian, melayani mahasiswa pertama dalam antrian, mencari nama mahasiswa dalam antrian, dan menampilkan seluruh isi antrian.

Struktur data Singly Linked List digunakan karena setiap data mahasiswa disimpan dalam sebuah node. Setiap node memiliki data berupa nama mahasiswa dan referensi `next` yang menunjuk ke node berikutnya. Karena hanya memiliki satu arah referensi, penelusuran data dilakukan dari node pertama atau `head` sampai node terakhir yang menunjuk ke `None`.

## Struktur Data yang Digunakan

Struktur data yang digunakan pada program ini adalah **Singly Linked List**.

Singly Linked List adalah struktur data linear yang terdiri dari beberapa node. Setiap node memiliki dua bagian utama, yaitu:

1. `data`, yaitu bagian yang menyimpan nilai atau informasi.
2. `next`, yaitu bagian yang menyimpan referensi ke node berikutnya.

Pada program ini, data yang disimpan adalah nama mahasiswa. Node pertama disebut sebagai `head`. Jika `head` bernilai `None`, berarti linked list masih kosong. Jika sudah terdapat data, maka setiap node akan saling terhubung satu arah menggunakan referensi `next`.

## Fitur Program

Program ini memiliki beberapa fitur, yaitu:

1. Menambahkan mahasiswa ke dalam antrian.
2. Melayani atau menghapus mahasiswa pertama dari antrian.
3. Mencari nama mahasiswa dalam antrian.
4. Menampilkan seluruh isi antrian mahasiswa.
5. Keluar dari program.

## Source Code

```python
# ==============================================================
# Nama          : Abdu Ar Rahman Athallah
# NPM           : 2515061002
# Judul Program : Pengelolaan Data Mahasiswa Menggunakan Singly Linked List
# Struktur Data : Singly Linked List
# Deskripsi     : Program ini digunakan untuk menambah, menghapus,
#                 mencari, dan menampilkan data mahasiswa. Setiap
#                 mahasiswa disimpan sebagai node yang saling
#                 terhubung satu arah menggunakan referensi next.
# ==============================================================

class Node:
    def __init__(self, nama):
        self.nama = nama
        self.next = None


class SinglyLinkedList:
    def __init__(self):
        self.head = None

    def tambah_antrian(self, nama):
        node_baru = Node(nama)

        if self.head is None:
            self.head = node_baru
        else:
            sekarang = self.head
            while sekarang.next is not None:
                sekarang = sekarang.next
            sekarang.next = node_baru

        print(f"{nama} berhasil masuk ke antrian.")

    def layani_antrian(self):
        if self.head is None:
            print("Antrian masih kosong.")
        else:
            nama_dilayani = self.head.nama
            self.head = self.head.next
            print(f"{nama_dilayani} sudah dilayani dan keluar dari antrian.")

    def cari_antrian(self, nama):
        sekarang = self.head
        posisi = 1

        while sekarang is not None:
            if sekarang.nama.lower() == nama.lower():
                print(f"{nama} ditemukan di posisi antrian ke-{posisi}.")
                return
            sekarang = sekarang.next
            posisi += 1

        print(f"{nama} tidak ditemukan dalam antrian.")

    def tampilkan_antrian(self):
        if self.head is None:
            print("Antrian kosong.")
        else:
            sekarang = self.head
            print("\nDaftar Antrian:")
            while sekarang is not None:
                print(sekarang.nama, end=" -> ")
                sekarang = sekarang.next
            print("None")


# Program utama
antrian = SinglyLinkedList()

while True:
    print("\n=== MENU ANTRIAN MAHASISWA ===")
    print("1. Tambah antrian")
    print("2. Layani antrian pertama")
    print("3. Cari nama dalam antrian")
    print("4. Tampilkan antrian")
    print("5. Keluar")

    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        nama = input("Masukkan nama mahasiswa: ")
        antrian.tambah_antrian(nama)

    elif pilihan == "2":
        antrian.layani_antrian()

    elif pilihan == "3":
        nama = input("Masukkan nama yang dicari: ")
        antrian.cari_antrian(nama)

    elif pilihan == "4":
        antrian.tampilkan_antrian()

    elif pilihan == "5":
        print("Program selesai.")
        break

    else:
        print("Pilihan tidak valid.")
```

## Penjelasan Logika Program Perbaris

### 1. Bagian Komentar Program

```python
# ==============================================================
```

Baris ini digunakan sebagai pembatas agar tampilan komentar program terlihat lebih rapi.

```python
# Nama          : Abdu Ar Rahman Athallah
```

Baris ini berisi nama pembuat program.

```python
# NPM           : 2515061002
```

Baris ini berisi NPM pembuat program.

```python
# Judul Program : Pengelolaan Data Mahasiswa Menggunakan Singly Linked List
```

Baris ini menjelaskan judul program yang dibuat.

```python
# Struktur Data : Singly Linked List
```

Baris ini menjelaskan bahwa struktur data yang digunakan dalam program adalah Singly Linked List.

```python
# Deskripsi     : Program ini digunakan untuk menambah, menghapus,
#                 mencari, dan menampilkan data mahasiswa.
```

Baris ini menjelaskan fungsi utama program, yaitu mengelola data mahasiswa dalam bentuk antrian.

```python
#                 mahasiswa disimpan sebagai node yang saling
#                 terhubung satu arah menggunakan referensi next.
```

Baris ini menjelaskan bahwa setiap data mahasiswa disimpan sebagai node yang saling terhubung satu arah menggunakan referensi `next`.

### 2. Class Node

```python
class Node:
```

Baris ini digunakan untuk membuat class bernama `Node`. Class ini berfungsi sebagai cetakan untuk membuat simpul atau node pada Singly Linked List.

```python
    def __init__(self, nama):
```

Baris ini adalah constructor yang akan dijalankan secara otomatis ketika objek `Node` dibuat. Parameter `nama` digunakan untuk menerima data nama mahasiswa.

```python
        self.nama = nama
```

Baris ini digunakan untuk menyimpan data nama mahasiswa ke dalam atribut `nama`.

```python
        self.next = None
```

Baris ini digunakan untuk membuat atribut `next`. Nilai awalnya adalah `None` karena node baru belum menunjuk ke node berikutnya.

### 3. Class SinglyLinkedList

```python
class SinglyLinkedList:
```

Baris ini digunakan untuk membuat class `SinglyLinkedList`. Class ini berisi operasi-operasi yang dapat dilakukan pada linked list.

```python
    def __init__(self):
```

Baris ini adalah constructor dari class `SinglyLinkedList`.

```python
        self.head = None
```

Baris ini digunakan untuk membuat atribut `head`. `head` adalah penunjuk node pertama dalam linked list. Nilai awalnya adalah `None` karena linked list masih kosong.

### 4. Method tambah_antrian

```python
    def tambah_antrian(self, nama):
```

Baris ini digunakan untuk membuat method `tambah_antrian` yang berfungsi menambahkan data mahasiswa ke dalam antrian.

```python
        node_baru = Node(nama)
```

Baris ini membuat node baru dari class `Node` dengan isi data berupa nama mahasiswa yang dimasukkan oleh user.

```python
        if self.head is None:
```

Baris ini mengecek apakah linked list masih kosong. Jika `head` bernilai `None`, berarti belum ada data di dalam linked list.

```python
            self.head = node_baru
```

Jika linked list masih kosong, maka node baru langsung dijadikan sebagai node pertama atau `head`.

```python
        else:
```

Baris ini dijalankan jika linked list sudah memiliki data.

```python
            sekarang = self.head
```

Baris ini membuat variabel `sekarang` yang digunakan untuk menelusuri linked list mulai dari node pertama.

```python
            while sekarang.next is not None:
```

Baris ini melakukan perulangan selama node saat ini masih memiliki node berikutnya. Tujuannya adalah mencari node terakhir dalam antrian.

```python
                sekarang = sekarang.next
```

Baris ini memindahkan posisi penelusuran ke node berikutnya.

```python
            sekarang.next = node_baru
```

Setelah node terakhir ditemukan, baris ini menghubungkan node terakhir dengan node baru.

```python
        print(f"{nama} berhasil masuk ke antrian.")
```

Baris ini menampilkan pesan bahwa mahasiswa berhasil masuk ke dalam antrian.

### 5. Method layani_antrian

```python
    def layani_antrian(self):
```

Baris ini digunakan untuk membuat method `layani_antrian` yang berfungsi melayani mahasiswa pertama dalam antrian.

```python
        if self.head is None:
```

Baris ini mengecek apakah antrian masih kosong.

```python
            print("Antrian masih kosong.")
```

Jika antrian kosong, program menampilkan pesan bahwa antrian masih kosong.

```python
        else:
```

Baris ini dijalankan jika antrian memiliki data.

```python
            nama_dilayani = self.head.nama
```

Baris ini menyimpan nama mahasiswa yang berada pada node pertama atau `head`.

```python
            self.head = self.head.next
```

Baris ini memindahkan `head` ke node berikutnya. Dengan begitu, mahasiswa pertama dianggap sudah keluar dari antrian.

```python
            print(f"{nama_dilayani} sudah dilayani dan keluar dari antrian.")
```

Baris ini menampilkan pesan bahwa mahasiswa pertama sudah dilayani dan keluar dari antrian.

### 6. Method cari_antrian

```python
    def cari_antrian(self, nama):
```

Baris ini digunakan untuk membuat method `cari_antrian` yang berfungsi mencari nama mahasiswa dalam antrian.

```python
        sekarang = self.head
```

Baris ini membuat variabel `sekarang` untuk mulai menelusuri linked list dari node pertama.

```python
        posisi = 1
```

Baris ini membuat variabel `posisi` untuk mencatat urutan mahasiswa dalam antrian.

```python
        while sekarang is not None:
```

Baris ini melakukan perulangan selama node yang sedang diperiksa belum bernilai `None`.

```python
            if sekarang.nama.lower() == nama.lower():
```

Baris ini membandingkan nama pada node dengan nama yang dicari. Fungsi `lower()` digunakan agar pencarian tidak membedakan huruf besar dan kecil.

```python
                print(f"{nama} ditemukan di posisi antrian ke-{posisi}.")
```

Jika nama ditemukan, program menampilkan posisi mahasiswa tersebut dalam antrian.

```python
                return
```

Baris ini digunakan untuk menghentikan method setelah data ditemukan.

```python
            sekarang = sekarang.next
```

Jika data belum ditemukan, program berpindah ke node berikutnya.

```python
            posisi += 1
```

Baris ini menambah nilai posisi setiap kali program berpindah ke node berikutnya.

```python
        print(f"{nama} tidak ditemukan dalam antrian.")
```

Baris ini dijalankan jika seluruh node sudah diperiksa tetapi nama yang dicari tidak ditemukan.

### 7. Method tampilkan_antrian

```python
    def tampilkan_antrian(self):
```

Baris ini digunakan untuk membuat method `tampilkan_antrian` yang berfungsi menampilkan seluruh isi antrian.

```python
        if self.head is None:
```

Baris ini mengecek apakah antrian kosong.

```python
            print("Antrian kosong.")
```

Jika antrian kosong, program menampilkan pesan bahwa antrian kosong.

```python
        else:
```

Baris ini dijalankan jika antrian memiliki data.

```python
            sekarang = self.head
```

Baris ini membuat variabel `sekarang` untuk menelusuri linked list mulai dari `head`.

```python
            print("\nDaftar Antrian:")
```

Baris ini menampilkan judul output sebelum isi antrian ditampilkan.

```python
            while sekarang is not None:
```

Baris ini melakukan perulangan selama node yang sedang diperiksa belum bernilai `None`.

```python
                print(sekarang.nama, end=" -> ")
```

Baris ini menampilkan nama mahasiswa pada node saat ini, kemudian menambahkan tanda panah sebagai penghubung antar node.

```python
                sekarang = sekarang.next
```

Baris ini memindahkan penelusuran ke node berikutnya.

```python
            print("None")
```

Baris ini menampilkan `None` sebagai tanda akhir dari linked list.

### 8. Program Utama

```python
# Program utama
```

Baris ini merupakan komentar yang menandakan bahwa bagian berikutnya adalah program utama.

```python
antrian = SinglyLinkedList()
```

Baris ini membuat objek `antrian` dari class `SinglyLinkedList`.

```python
while True:
```

Baris ini membuat perulangan agar menu terus ditampilkan sampai user memilih keluar.

```python
    print("\n=== MENU ANTRIAN MAHASISWA ===")
```

Baris ini menampilkan judul menu program.

```python
    print("1. Tambah antrian")
```

Baris ini menampilkan pilihan menu untuk menambahkan mahasiswa ke dalam antrian.

```python
    print("2. Layani antrian pertama")
```

Baris ini menampilkan pilihan menu untuk melayani mahasiswa pertama dalam antrian.

```python
    print("3. Cari nama dalam antrian")
```

Baris ini menampilkan pilihan menu untuk mencari nama mahasiswa dalam antrian.

```python
    print("4. Tampilkan antrian")
```

Baris ini menampilkan pilihan menu untuk menampilkan seluruh isi antrian.

```python
    print("5. Keluar")
```

Baris ini menampilkan pilihan menu untuk keluar dari program.

```python
    pilihan = input("Pilih menu: ")
```

Baris ini meminta user untuk memasukkan pilihan menu.

```python
    if pilihan == "1":
```

Baris ini mengecek apakah user memilih menu nomor 1.

```python
        nama = input("Masukkan nama mahasiswa: ")
```

Baris ini meminta user memasukkan nama mahasiswa yang ingin ditambahkan ke antrian.

```python
        antrian.tambah_antrian(nama)
```

Baris ini memanggil method `tambah_antrian` untuk menambahkan nama mahasiswa ke dalam antrian.

```python
    elif pilihan == "2":
```

Baris ini mengecek apakah user memilih menu nomor 2.

```python
        antrian.layani_antrian()
```

Baris ini memanggil method `layani_antrian` untuk melayani mahasiswa pertama dalam antrian.

```python
    elif pilihan == "3":
```

Baris ini mengecek apakah user memilih menu nomor 3.

```python
        nama = input("Masukkan nama yang dicari: ")
```

Baris ini meminta user memasukkan nama mahasiswa yang ingin dicari.

```python
        antrian.cari_antrian(nama)
```

Baris ini memanggil method `cari_antrian` untuk mencari nama mahasiswa dalam antrian.

```python
    elif pilihan == "4":
```

Baris ini mengecek apakah user memilih menu nomor 4.

```python
        antrian.tampilkan_antrian()
```

Baris ini memanggil method `tampilkan_antrian` untuk menampilkan seluruh isi antrian.

```python
    elif pilihan == "5":
```

Baris ini mengecek apakah user memilih menu nomor 5.

```python
        print("Program selesai.")
```

Baris ini menampilkan pesan bahwa program telah selesai.

```python
        break
```

Baris ini digunakan untuk menghentikan perulangan sehingga program berhenti.

```python
    else:
```

Baris ini dijalankan jika user memasukkan pilihan selain angka 1 sampai 5.

```python
        print("Pilihan tidak valid.")
```

Baris ini menampilkan pesan bahwa pilihan yang dimasukkan tidak valid.

## Screenshot Source Code

<img width="902" height="799" alt="image" src="https://github.com/user-attachments/assets/d847fc28-ec5b-4d7c-a0d8-8e0f41759ffa" />

<img width="890" height="484" alt="image" src="https://github.com/user-attachments/assets/2edceefb-8d6c-4d05-810b-7c3890dee76f" />

<img width="898" height="638" alt="image" src="https://github.com/user-attachments/assets/2a739475-bdbb-4442-9893-ecd00a780e5d" />

## Contoh Output Program

```text
=== MENU ANTRIAN MAHASISWA ===
1. Tambah antrian
2. Layani antrian pertama
3. Cari nama dalam antrian
4. Tampilkan antrian
5. Keluar
Pilih menu: 1
Masukkan nama mahasiswa: Andi
Andi berhasil masuk ke antrian.

=== MENU ANTRIAN MAHASISWA ===
1. Tambah antrian
2. Layani antrian pertama
3. Cari nama dalam antrian
4. Tampilkan antrian
5. Keluar
Pilih menu: 1
Masukkan nama mahasiswa: Budi
Budi berhasil masuk ke antrian.

=== MENU ANTRIAN MAHASISWA ===
1. Tambah antrian
2. Layani antrian pertama
3. Cari nama dalam antrian
4. Tampilkan antrian
5. Keluar
Pilih menu: 4

Daftar Antrian:
Andi -> Budi -> None

=== MENU ANTRIAN MAHASISWA ===
1. Tambah antrian
2. Layani antrian pertama
3. Cari nama dalam antrian
4. Tampilkan antrian
5. Keluar
Pilih menu: 3
Masukkan nama yang dicari: Budi
Budi ditemukan di posisi antrian ke-2.

=== MENU ANTRIAN MAHASISWA ===
1. Tambah antrian
2. Layani antrian pertama
3. Cari nama dalam antrian
4. Tampilkan antrian
5. Keluar
Pilih menu: 2
Andi sudah dilayani dan keluar dari antrian.

=== MENU ANTRIAN MAHASISWA ===
1. Tambah antrian
2. Layani antrian pertama
3. Cari nama dalam antrian
4. Tampilkan antrian
5. Keluar
Pilih menu: 4

Daftar Antrian:
Budi -> None
```

## Screenshot Output Program

<img width="274" height="151" alt="image" src="https://github.com/user-attachments/assets/fcea63c0-11c0-4e93-8c63-d76bb0a579f7" />

## Penjelasan Output Program

Pada contoh output program, user memilih menu nomor 1 untuk menambahkan mahasiswa ke dalam antrian. Data pertama yang dimasukkan adalah `Andi`, kemudian data kedua yang dimasukkan adalah `Budi`. Setelah itu, user memilih menu nomor 4 untuk menampilkan isi antrian. Program menampilkan data dengan urutan `Andi -> Budi -> None`, yang berarti node pertama berisi data `Andi`, node kedua berisi data `Budi`, dan `None` menunjukkan akhir dari linked list.

Selanjutnya, user memilih menu nomor 3 untuk mencari nama `Budi`. Program berhasil menemukan `Budi` pada posisi antrian ke-2. Setelah itu, user memilih menu nomor 2 untuk melayani antrian pertama. Karena mahasiswa pertama adalah `Andi`, maka `Andi` keluar dari antrian. Ketika antrian ditampilkan kembali, isi antrian menjadi `Budi -> None`.

## Link Video Presentasi

Link video presentasi/demo program:

```text
https://youtu.be/ZPYvLYbXmuE
```

## Kesimpulan

Berdasarkan program yang telah dibuat, Singly Linked List dapat digunakan untuk mengelola data antrian mahasiswa secara dinamis. Setiap mahasiswa disimpan dalam bentuk node yang saling terhubung satu arah menggunakan referensi `next`.

Program ini menunjukkan beberapa operasi dasar pada Singly Linked List, yaitu menambahkan node baru di akhir, menghapus node pertama, mencari node berdasarkan nama, dan menampilkan seluruh node. Dengan menggunakan Singly Linked List, data tidak harus disimpan pada lokasi memori yang berurutan seperti array, karena setiap node cukup menyimpan referensi ke node berikutnya.
