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
