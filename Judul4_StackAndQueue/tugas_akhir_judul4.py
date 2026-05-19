class StackRiwayat:
    def __init__(self):
        self.stack = []

    def push(self, file):
        self.stack.append(file)

    def pop(self):
        if len(self.stack) == 0:
            print("Riwayat print kosong.")
        else:
            print(f"Riwayat terakhir dihapus: {self.stack.pop()}")

    def display(self):
        if len(self.stack) == 0:
            print("Riwayat print kosong.")
        else:
            print("Riwayat file yang sudah diprint:")
            for file in reversed(self.stack):
                print("-", file)


class QueuePrint:
    def __init__(self):
        self.queue = []

    def enqueue(self, file):
        self.queue.append(file)
        print(f"File '{file}' masuk antrean print.")

    def dequeue(self):
        if len(self.queue) == 0:
            print("Antrean print kosong.")
            return None
        else:
            file = self.queue.pop(0)
            print(f"File '{file}' sedang diprint.")
            return file

    def display(self):
        if len(self.queue) == 0:
            print("Antrean print kosong.")
        else:
            print("Antrean file print:")
            for file in self.queue:
                print("-", file)


def main():
    antrean = QueuePrint()
    riwayat = StackRiwayat()

    while True:
        print("\n=== SISTEM ANTREAN PRINT TUGAS ===")
        print("1. Tambah file ke antrean")
        print("2. Print file")
        print("3. Tampilkan data")
        print("4. Hapus riwayat terakhir")
        print("5. Keluar")

        pilih = input("Pilih menu: ")

        if pilih == "1":
            file = input("Masukkan nama file: ")
            antrean.enqueue(file)

        elif pilih == "2":
            file_diprint = antrean.dequeue()
            if file_diprint is not None:
                riwayat.push(file_diprint)

        elif pilih == "3":
            antrean.display()
            riwayat.display()

        elif pilih == "4":
            riwayat.pop()

        elif pilih == "5":
            print("Program selesai.")
            break

        else:
            print("Pilihan tidak valid.")


if __name__ == "__main__":
    main()