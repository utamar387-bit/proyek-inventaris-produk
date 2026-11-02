from inventaris import Inventaris


def mode_demo():
    # Membuat objek inventaris.
    toko = Inventaris()

    # Menambahkan beberapa produk.
    toko.tambah_produk("P001", "Laptop ASUS", 7500000, 10)
    toko.tambah_produk("P002", "Mouse Logitech", 150000, 25)

    # Menampilkan seluruh produk.
    toko.tampilkan_produk()

    # Mencari produk berdasarkan ID.
    print("\n=== HASIL PENCARIAN ===")
    hasil = toko.cari_produk("P002")

    if hasil is not None:
        print("Produk ditemukan:", hasil)
    else:
        print("Produk tidak ditemukan.")

    # Menghapus produk berdasarkan ID.
    print("\n=== PENGHAPUSAN PRODUK ===")
    toko.hapus_produk("P001")

    # Menampilkan produk setelah penghapusan.
    toko.tampilkan_produk()


def mode_interaktif():
    # Membuat objek inventaris.
    def tampilkan_menu():
        """Menampilkan pilihan menu kepada pengguna."""
        print("\n" + "=" * 40)
        print("   SISTEM MANAJEMEN INVENTARIS")
        print("=" * 40)
        print("1. Tambah Produk")
        print("2. Cari Produk")
        print("3. Hapus Produk")
        print("4. Tampilkan Semua Produk")
        print("5. Keluar")
        print("=" * 40)


    def tambah_produk_menu(inventaris):
        """Menerima masukan dan menambahkan produk."""
        print("\n=== TAMBAH PRODUK ===")

        id_produk = input("Masukkan ID produk: ").strip().upper()
        nama_produk = input("Masukkan nama produk: ").strip()

        try:
            harga = int(input("Masukkan harga produk: "))
            stok = int(input("Masukkan stok produk: "))
        except ValueError:
            print("Gagal: Harga dan stok harus berupa angka bulat.")
            return

        if not id_produk or not nama_produk:
            print("Gagal: ID dan nama produk tidak boleh kosong.")
            return

        inventaris.tambah_produk(id_produk, nama_produk, harga, stok)


    def cari_produk_menu(inventaris):
        """Mencari produk berdasarkan ID."""
        print("\n=== CARI PRODUK ===")

        id_produk = input("Masukkan ID produk: ").strip().upper()

        hasil = inventaris.cari_produk(id_produk)

        if hasil is not None:
            print("\nProduk ditemukan!")
            print(f"ID    : {id_produk}")
            print(f"Nama  : {hasil['nama_produk']}")
            print(f"Harga : Rp{hasil['harga']:,}")
            print(f"Stok  : {hasil['stok']}")
        else:
            print("Produk tidak ditemukan.")


    def hapus_produk_menu(inventaris):
        """Menghapus produk berdasarkan ID."""
        print("\n=== HAPUS PRODUK ===")

        id_produk = input("Masukkan ID produk yang ingin dihapus: ").strip().upper()

        inventaris.hapus_produk(id_produk)


    def main():
        """Fungsi utama program."""
        inventaris = Inventaris()

        while True:
            tampilkan_menu()

            pilihan = input("Pilih menu (1-5): ").strip()

            if pilihan == "1":
                tambah_produk_menu(inventaris)

            elif pilihan == "2":
                cari_produk_menu(inventaris)

            elif pilihan == "3":
                hapus_produk_menu(inventaris)

            elif pilihan == "4":
                inventaris.tampilkan_produk()


            elif pilihan == "5":
                print("Terima kasih telah menggunakan program.")
                break

            else:
                print("Pilihan tidak valid. Silakan pilih angka 1-5.")

    if __name__ == "__main__":
        main()


def main():
    print("Selamat datang di Sistem Manajemen Inventaris Produk!")
    print("Pilih mode:")
    print("1. Mode Demo")
    print("2. Mode Interaktif")

    pilihan = input("Masukkan pilihan (1 atau 2): ").strip()

    if pilihan == "1":
        mode_demo()
    elif pilihan == "2":
        mode_interaktif()
    else:
        print("Pilihan tidak valid. Silakan pilih 1 atau 2.")

if __name__ == "__main__":
    main()