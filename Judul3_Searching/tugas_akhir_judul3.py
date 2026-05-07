# ================================================================
# Nama            : ABDU AR RAHMAN ATHALLAH
# NPM             : 2515061002
# Judul Program   : Pencarian Posisi Mahasiswa di Barisan Upacara
# Struktur Data   : List dan Binary Search
# Deskripsi       : Program ini digunakan untuk mencari posisi
#                   mahasiswa di barisan upacara berdasarkan tinggi
#                   badan. Data tinggi badan mahasiswa harus sudah
#                   terurut dari yang paling pendek ke paling tinggi.
#                   Proses pencarian dilakukan menggunakan algoritma
#                   Binary Search untuk mengetahui mahasiswa berada
#                   di barisan ke berapa, serta termasuk bagian depan
#                   atau belakang barisan.
# ================================================================


def binary_search_barisan(data_tinggi, n, target):
    kiri = 0
    kanan = n - 1
    posisi = -1

    while kiri <= kanan:
        tengah = kiri + (kanan - kiri) // 2

        print(f"Indeks tengah: {tengah}")
        print(f"Tinggi tengah: {data_tinggi[tengah]} cm")

        if data_tinggi[tengah] == target:
            posisi = tengah
            break
        elif data_tinggi[tengah] < target:
            print("Mencari di bagian kanan")
            kiri = tengah + 1
        else:
            print("Mencari di bagian kiri")
            kanan = tengah - 1

    return posisi


def tentukan_bagian_barisan(posisi, n):
    nomor_barisan = posisi + 1
    batas_tengah = n / 2

    if nomor_barisan <= batas_tengah:
        return "bagian depan"
    else:
        return "bagian belakang"


def main():
    print("=== Pencarian Posisi Mahasiswa di Barisan Upacara ===")

    try:
        n = int(input("Masukkan jumlah mahasiswa: "))
    except ValueError:
        print("Input tidak valid! Jumlah mahasiswa harus angka.")
        return

    data_tinggi = []

    print("\nMasukkan tinggi badan mahasiswa")
    print("dari yang paling pendek ke paling tinggi.")

    for i in range(n):
        while True:
            try:
                tinggi = int(
                    input(f"Tinggi mahasiswa ke-{i + 1} (cm): ")
                )
                data_tinggi.append(tinggi)
                break
            except ValueError:
                print("Input tidak valid! Tinggi harus angka.")

    print("\nData tinggi mahasiswa dalam barisan:")
    print(data_tinggi)

    while True:
        try:
            target = int(
                input("\nMasukkan tinggi mahasiswa yang dicari: ")
            )
            break
        except ValueError:
            print("Input tidak valid! Tinggi harus angka.")

    posisi = binary_search_barisan(data_tinggi, n, target)

    if posisi != -1:
        nomor_barisan = posisi + 1
        bagian = tentukan_bagian_barisan(posisi, n)

        print("\nHasil Pencarian:")
        print(f"Mahasiswa dengan tinggi {target} cm ditemukan.")
        print(f"Mahasiswa berada di barisan ke-{nomor_barisan}.")
        print(f"Mahasiswa berada pada {bagian} barisan.")
    else:
        print("\nHasil Pencarian:")
        print(f"Mahasiswa dengan tinggi {target} cm tidak ditemukan.")


if __name__ == "__main__":
    main()