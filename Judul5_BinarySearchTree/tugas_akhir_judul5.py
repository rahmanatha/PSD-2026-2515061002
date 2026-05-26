class Node:
    def __init__(self, nomor):
        self.nomor = nomor
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def tambah(self, nomor):
        self.root = self._tambah(self.root, nomor)

    def _tambah(self, root, nomor):
        if root is None:
            return Node(nomor)

        if nomor < root.nomor:
            root.left = self._tambah(root.left, nomor)
        elif nomor > root.nomor:
            root.right = self._tambah(root.right, nomor)
        else:
            print("Nomor antrean sudah ada")

        return root

    def cari(self, nomor):
        return self._cari(self.root, nomor)

    def _cari(self, root, nomor):
        if root is None:
            return False

        if root.nomor == nomor:
            return True
        elif nomor < root.nomor:
            return self._cari(root.left, nomor)
        else:
            return self._cari(root.right, nomor)

    def tampil_urut(self):
        self._inorder(self.root)

    def _inorder(self, root):
        if root is not None:
            self._inorder(root.left)
            print(root.nomor, end=" ")
            self._inorder(root.right)


def main():
    bst = BST()

    while True:
        print("\n=== Sistem Antrean Pasien ===")
        print("1. Tambah nomor antrean")
        print("2. Cari nomor antrean")
        print("3. Tampilkan nomor antrean")
        print("4. Keluar")

        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            nomor = int(input("Masukkan nomor antrean: "))
            bst.tambah(nomor)
            print("Nomor antrean berhasil ditambahkan")

        elif pilihan == "2":
            nomor = int(input("Masukkan nomor yang dicari: "))

            if bst.cari(nomor):
                print("Nomor antrean ditemukan")
            else:
                print("Nomor antrean tidak ditemukan")

        elif pilihan == "3":
            print("Daftar nomor antrean:")
            bst.tampil_urut()
            print()

        elif pilihan == "4":
            print("Program selesai")
            break

        else:
            print("Pilihan tidak valid")


main()