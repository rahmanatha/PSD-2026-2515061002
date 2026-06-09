class hash_map:
    def __init__(self, size=10):
        self.size = size
        self.table = [[] for _ in range(size)]

    def hash_function(self, key):
        total = 0
        for huruf in key:
            total += ord(huruf)
        return total % self.size

    def tambah(self, key, value):
        index = self.hash_function(key)
        bucket = self.table[index]

        for data in bucket:
            if data[0] == key:
                data[1] = value
                return "data berhasil diperbarui"

        bucket.append([key, value])
        return "data berhasil ditambahkan"

    def cari(self, key):
        index = self.hash_function(key)
        bucket = self.table[index]

        for data in bucket:
            if data[0] == key:
                return data[1]

        return None

    def hapus(self, key):
        index = self.hash_function(key)
        bucket = self.table[index]

        for data in bucket:
            if data[0] == key:
                bucket.remove(data)
                return True

        return False

    def tampilkan_semua(self):
        kosong = True

        for bucket in self.table:
            for data in bucket:
                kode = data[0]
                barang = data[1]

                print("-------------------------")
                print("kode barang :", kode)
                print("nama barang :", barang[0])
                print("stok        :", barang[1])
                print("harga       :", barang[2])

                kosong = False

        if kosong:
            print("belum ada data barang")

    def tampilkan_table(self):
        print("\nisi hash table:")
        for i in range(self.size):
            print(f"index {i}: ", end="")

            if len(self.table[i]) == 0:
                print("kosong")
            else:
                for data in self.table[i]:
                    print(f"[{data[0]}] -> ", end="")
                print("none")


def menu():
    print("\n=== sistem data barang toko ===")
    print("1. tambah barang")
    print("2. cari barang")
    print("3. hapus barang")
    print("4. tampilkan semua barang")
    print("5. tampilkan hash table")
    print("0. keluar")


def main():
    data_barang = hash_map()

    while True:
        menu()
        pilih = input("pilih menu: ")

        if pilih == "1":
            kode = input("masukkan kode barang: ").upper()
            nama = input("masukkan nama barang: ")
            stok = int(input("masukkan stok barang: "))
            harga = int(input("masukkan harga barang: "))

            barang = [nama, stok, harga]
            pesan = data_barang.tambah(kode, barang)
            print(pesan)

        elif pilih == "2":
            kode = input("masukkan kode barang yang dicari: ").upper()
            barang = data_barang.cari(kode)

            if barang is not None:
                print("\ndata barang ditemukan")
                print("nama barang :", barang[0])
                print("stok        :", barang[1])
                print("harga       :", barang[2])
            else:
                print("data barang tidak ditemukan")

        elif pilih == "3":
            kode = input("masukkan kode barang yang dihapus: ").upper()

            if data_barang.hapus(kode):
                print("data barang berhasil dihapus")
            else:
                print("data barang tidak ditemukan")

        elif pilih == "4":
            data_barang.tampilkan_semua()

        elif pilih == "5":
            data_barang.tampilkan_table()

        elif pilih == "0":
            print("program selesai")
            break

        else:
            print("pilihan tidak valid")


if __name__ == "__main__":
    main()