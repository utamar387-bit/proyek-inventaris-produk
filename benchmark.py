import time


# ==========================================
# 1. MEMBUAT STRUKTUR DATA LINKED LIST
# ==========================================

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def tambah(self, data):
        # Membuat node baru.
        node_baru = Node(data)

        # Jika Linked List masih kosong.
        if self.head is None:
            self.head = node_baru
            self.tail = node_baru
        else:
            # Hubungkan node terakhir ke node baru.
            self.tail.next = node_baru
            self.tail = node_baru

    def cari(self, id_produk):
        # Mulai pencarian dari node pertama.
        sekarang = self.head

        while sekarang is not None:
            if sekarang.data["id_produk"] == id_produk:
                return sekarang.data

            sekarang = sekarang.next

        return None

    def hapus(self, id_produk):
        sekarang = self.head
        sebelumnya = None

        while sekarang is not None:
            if sekarang.data["id_produk"] == id_produk:

                # Jika node yang dihapus berada di awal.
                if sebelumnya is None:
                    self.head = sekarang.next
                else:
                    # Lewati node yang akan dihapus.
                    sebelumnya.next = sekarang.next

                # Jika node terakhir dihapus, perbarui tail.
                if sekarang is self.tail:
                    self.tail = sebelumnya

                return True

            sebelumnya = sekarang
            sekarang = sekarang.next

        return False


# ==========================================
# 2. MENYIAPKAN DATA PENGUJIAN
# ==========================================

JUMLAH_PRODUK = 5000
ULANGAN_CARI = 1000
ULANGAN_HAPUS = 20


def buat_data():
    # Membuat data produk dengan ID unik.
    return [
        {
            "id_produk": f"P{i:05d}",
            "nama_produk": f"Produk {i}",
            "harga": 10000 + i,
            "stok": 10
        }
        for i in range(JUMLAH_PRODUK)
    ]


def buat_list(data):
    return list(data)


def buat_linked_list(data):
    linked = LinkedList()

    for produk in data:
        linked.tambah(produk)

    return linked


def buat_dictionary(data):
    return {
        produk["id_produk"]: produk
        for produk in data
    }


# ==========================================
# 3. MENGUKUR WAKTU PENAMBAHAN
# ==========================================

def ukur_penambahan():
    data = buat_data()

    # Mengukur penambahan ke Python List.
    awal = time.perf_counter()
    list_produk = []

    for produk in data:
        list_produk.append(produk)

    waktu_list = time.perf_counter() - awal

    # Mengukur penambahan ke Linked List.
    awal = time.perf_counter()
    linked = LinkedList()

    for produk in data:
        linked.tambah(produk)

    waktu_linked = time.perf_counter() - awal

    # Mengukur penambahan ke Dictionary.
    awal = time.perf_counter()
    dictionary = {}

    for produk in data:
        dictionary[produk["id_produk"]] = produk

    waktu_dict = time.perf_counter() - awal

    return waktu_list, waktu_linked, waktu_dict


# ==========================================
# 4. MENGUKUR WAKTU PENCARIAN
# ==========================================

def ukur_pencarian():
    data = buat_data()

    list_produk = buat_list(data)
    linked = buat_linked_list(data)
    dictionary = buat_dictionary(data)

    # Produk target berada di posisi terakhir.
    target = f"P{JUMLAH_PRODUK - 1:05d}"

    # Mengukur pencarian pada List.
    awal = time.perf_counter()

    for _ in range(ULANGAN_CARI):
        hasil = None

        for produk in list_produk:
            if produk["id_produk"] == target:
                hasil = produk
                break

        assert hasil is not None

    waktu_list = time.perf_counter() - awal

    # Mengukur pencarian pada Linked List.
    awal = time.perf_counter()

    for _ in range(ULANGAN_CARI):
        hasil = linked.cari(target)
        assert hasil is not None

    waktu_linked = time.perf_counter() - awal

    # Mengukur pencarian pada Dictionary.
    awal = time.perf_counter()

    for _ in range(ULANGAN_CARI):
        hasil = dictionary.get(target)
        assert hasil is not None

    waktu_dict = time.perf_counter() - awal

    return waktu_list, waktu_linked, waktu_dict


# ==========================================
# 5. MENGUKUR WAKTU PENGHAPUSAN
# ==========================================

def ukur_penghapusan():
    data = buat_data()

    # Menghapus produk terakhir agar pencarian pada
    # List dan Linked List memerlukan penelusuran penuh.
    target = f"P{JUMLAH_PRODUK - 1:05d}"

    total_list = 0
    total_linked = 0
    total_dict = 0

    for _ in range(ULANGAN_HAPUS):

        # Persiapan data dilakukan sebelum pengukuran.
        list_produk = buat_list(data)
        awal = time.perf_counter()

        indeks = next(
            (
                i for i, produk in enumerate(list_produk)
                if produk["id_produk"] == target
            ),
            None
        )

        if indeks is not None:
            list_produk.pop(indeks)

        total_list += time.perf_counter() - awal

        # Persiapan Linked List dilakukan sebelum pengukuran.
        linked = buat_linked_list(data)
        awal = time.perf_counter()

        linked.hapus(target)

        total_linked += time.perf_counter() - awal

        # Persiapan Dictionary dilakukan sebelum pengukuran.
        dictionary = buat_dictionary(data)
        awal = time.perf_counter()

        dictionary.pop(target, None)

        total_dict += time.perf_counter() - awal

    return (
        total_list / ULANGAN_HAPUS,
        total_linked / ULANGAN_HAPUS,
        total_dict / ULANGAN_HAPUS
    )


# ==========================================
# 6. MENAMPILKAN HASIL PENGUJIAN
# ==========================================

def tampilkan_hasil(judul, hasil):
    print(f"\n=== {judul} ===")
    print(f"{'Struktur Data':<20}{'Waktu (ms)':>15}")
    print("-" * 35)

    nama_struktur = [
        "Python List",
        "Linked List",
        "Dictionary"
    ]

    for nama, waktu in zip(nama_struktur, hasil):
        print(f"{nama:<20}{waktu * 1000:>15.6f}")


def main():
    print("PENGUJIAN KOMPLEKSITAS STRUKTUR DATA")
    print(f"Jumlah produk: {JUMLAH_PRODUK}")
    print(f"Ulangan pencarian: {ULANGAN_CARI}")
    print(f"Ulangan penghapusan: {ULANGAN_HAPUS}")

    hasil_tambah = ukur_penambahan()
    hasil_cari = ukur_pencarian()
    hasil_hapus = ukur_penghapusan()

    tampilkan_hasil("PENAMBAHAN PRODUK", hasil_tambah)
    tampilkan_hasil("PENCARIAN PRODUK", hasil_cari)
    tampilkan_hasil("PENGHAPUSAN PRODUK", hasil_hapus)


if __name__ == "__main__":
    main()