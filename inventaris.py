class Inventaris:
    def __init__(self):
        # Dictionary untuk menyimpan seluruh produk.
        # ID produk digunakan sebagai kunci.
        self.produk = {}

    def tambah_produk(self, id_produk, nama_produk, harga, stok):
        # Periksa apakah ID sudah digunakan.
        if id_produk in self.produk:
            print(f"=> Gagal: Produk '{nama_produk}' (ID: {id_produk}) sudah terdaftar.")
            return

        # Periksa apakah harga dan stok valid.
        if harga < 0 or stok < 0:
            print("=> Gagal: Harga dan stok tidak boleh negatif.")
            return

        # Simpan produk ke dalam dictionary.
        self.produk[id_produk] = {
            "nama_produk": nama_produk,
            "harga": harga,
            "stok": stok
        }

        print(f"=> Produk '{nama_produk}' (ID: {id_produk}) berhasil ditambahkan.")

    def cari_produk(self, id_produk):
        # Cari produk menggunakan ID sebagai kunci.
        if id_produk in self.produk:
            return self.produk[id_produk]

        return None

    def hapus_produk(self, id_produk):
        # Periksa apakah produk tersedia.
        if id_produk in self.produk:
            del self.produk[id_produk]
            print(f"=> Produk (ID: {id_produk}) berhasil dihapus.")
            return

        print(f"=> Gagal: Produk (ID: {id_produk}) tidak ditemukan.")

    def tampilkan_produk(self):
        # Periksa apakah inventaris masih kosong.
        if not self.produk:
            print("=> Inventaris masih kosong.")
            return

        # Tampilkan seluruh produk.
        print("\n=== DAFTAR PRODUK ===")

        for id_produk, data in self.produk.items():
            print(f"ID    : {id_produk}")
            print(f"Nama  : {data['nama_produk']}")
            print(f"Harga : Rp{data['harga']:,}")
            print(f"Stok  : {data['stok']}")
            print("-" * 25)