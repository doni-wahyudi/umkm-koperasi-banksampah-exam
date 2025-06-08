class UMKMSystem:
    def __init__(self, nama_umkm):
        self.nama_umkm = nama_umkm
        self.anggota = []
        self.dana_pinjaman = 50000000
        print(f"Terimakasih telah menunggu, {nama_umkm} telah kami tambahkan di program kami.")
        
    def tambah_anggota(self, nama_anggota, jumlah_pinjaman):
        # anggota[nama] = jumlah_pinjaman
        self.anggota.append({"nama_anggota": nama_anggota, "jumlah_pinjaman": jumlah_pinjaman})
        self.dana_pinjaman = self.dana_pinjaman - jumlah_pinjaman
        # print(self.anggota)
    
    def hitung_pengembalian(self, nama_anggota, tahun_pengembalian):
        jumlah_pinjaman = 0
        for dict_anggota in self.anggota:
            # print(dict_anggota)
            # print(dict_anggota["nama_anggota"])
            if dict_anggota["nama_anggota"] == nama_anggota:
                jumlah_pinjaman = dict_anggota["jumlah_pinjaman"]
        # print(jumlah_pinjaman)
        
        total_pengembalian = jumlah_pinjaman + (jumlah_pinjaman * 0.05) * tahun_pengembalian
        # print(total_pengembalian)
            

class Koperasi(UMKMSystem):
    def __init__(self, nama_umkm):
        super().__init__(nama_umkm)
        self.transaksi = []

    def catat_transaksi(self, nama_anggota, jenis_transaksi, jumlah_transaksi):
        self.transaksi.append({'nama_anggota': nama_anggota, 'jenis_transaksi': jenis_transaksi, 'jumlah_transaksi': jumlah_transaksi})

    def hitung_keuntungan(self):
        transaksi_beli = 0
        transaksi_jual = 0
        for items in self.transaksi:
            # print(items)
            if items["jenis_transaksi"] == "jual":
                transaksi_jual = + items["jumlah_transaksi"]
            elif items["jenis_transaksi"] == "beli":
                transaksi_beli = + items["jumlah_transaksi"]

        total_keuntungan = transaksi_jual - transaksi_beli
        # print(transaksi_jual)
        # print(transaksi_beli)
        # print(total_keuntungan)


class BankSampah(UMKMSystem):
    def __init__(self, nama_umkm):
        super().__init__(nama_umkm)
        self.data_sampah = {}

        self.data_sampah = {"doni": {"plastik": 10, "kertas": 5}, "ihsan": {"kertas": 4, "plastik": 2}}
        # self.data_sampah = {"doni" : {"plastik" : 10,"kertas" : 5}}

    def catat_sampah(self, nama_anggota, jenis_sampah, jumlah):        
        if nama_anggota in self.data_sampah:
            for i in self.data_sampah:
                if i == nama_anggota:
                    if jenis_sampah in self.data_sampah[i]:
                        self.data_sampah[nama_anggota][jenis_sampah] = self.data_sampah[nama_anggota][jenis_sampah] + jumlah
                    else:
                        self.data_sampah[nama_anggota][jenis_sampah] = jumlah
        else:
            self.data_sampah[nama_anggota] = {jenis_sampah : jumlah}

        
    def hitung_nilai_tukar(self):
        total_per_anggota = {}
        total_nilai = 0
        for items in self.data_sampah:
            nilai_anggota = 0
            # print(items)
            for type in self.data_sampah[items]:
                # print(type)
                if type == "plastik":
                    # print(f"total nilai awal tipe {type} : ", nilai_anggota)
                    nilai_anggota = nilai_anggota + (5000 * self.data_sampah[items][type])
                    # print(f"jumlah {type} dikalikan 5000: ",self.data_sampah[items][type])
                    # print("total nilai ditambah : ", nilai_anggota)
                elif type == "kertas":
                    # print(f"total nilai awal tipe {type} : ", nilai_anggota)
                    nilai_anggota = nilai_anggota + (2000 * self.data_sampah[items][type])
                    # print(f"jumlah {type} dikalikan 2000: ",self.data_sampah[items][type])
                    # print("total nilai ditambah : ", nilai_anggota)
            total_nilai = total_nilai + nilai_anggota
            total_per_anggota[items] = nilai_anggota

            print(f"total nilai akhir {items} : ", nilai_anggota)
        print("total nilai semua : ", total_nilai)
        print(total_per_anggota)

    def pesan_edukasi(self, nama):
        total_sampah = 0
        for items in self.data_sampah:
            if items == nama:
                for jenis_sampah in self.data_sampah[nama]:
                    total_sampah = total_sampah + self.data_sampah[nama][jenis_sampah]
        if total_sampah > 20:
            print(f"Anda Hebat {nama} dapat mengumpulkan sampah sangat banyak dengan total {total_sampah}!\n"
                  + "Semoga kita bisa terus konsisten menjaga bumi dengan mengumpulkan lalu mengolah sampah.")
        elif total_sampah > 10:
            print(f"Terimakasih banyak {nama} atas kontribusi nya dalam memilah dan mengumpulkan sampah sebanyak {total_sampah}.\n"
                  + "Mari kita lebih giat lagi untuk mengolah sampah demi keberlanjutan hidup umat manusia.")
        else:
            print(f"Halo {nama}, Terimakasih telah mengumpulkan sampah sebanyak {total_sampah}.\n"
                  + "Ini menjadi awal yang baik karena kamu sudah peduli dengan lingkungan, Semoga kita bisa mengolah lebih banyak sampah lagi!")

# ===============================================================
# umkm_a = UMKMSystem("ETL")
# umkm_a.tambah_anggota("doni", 100000)
# umkm_a.tambah_anggota("ihsan", 200000)

# print(umkm_a.nama_umkm)
# print(umkm_a.anggota)
# print(umkm_a.dana_pinjaman)

# umkm_a.hitung_pengembalian("doni",1)
# ===============================================================
# umkm_b = Koperasi("Batch 9")

# umkm_b.tambah_anggota("doni", 100000)
# umkm_b.tambah_anggota("ihsan", 200000)

# print(umkm_b.nama_umkm)
# print(umkm_b.anggota)
# print(umkm_b.dana_pinjaman)

# umkm_b.hitung_pengembalian("doni",1)
# umkm_b.catat_transaksi("ihsan","jual",100000)
# umkm_b.catat_transaksi("ihsan","beli",70000)

# umkm_b.hitung_keuntungan()
# print(umkm_b.transaksi)
# print(umkm_b.jumlah_)
# ===============================================================
# umkm_c = BankSampah("Batch 10")
# umkm_c.catat_sampah("doni","plastik",30)
# umkm_c.catat_sampah("doni","kertas",5)
# umkm_c.catat_sampah("doni","organik",20)
# umkm_c.catat_sampah("ihsan","kertas",8)
# umkm_c.catat_sampah("ihsan","organik",2)
# umkm_c.catat_sampah("doni","kertas",15)

# umkm_c.hitung_nilai_tukar()
# umkm_c.pesan_edukasi('doni')
# print(umkm_c.data_sampah)
umkm_terdaftar = [] #nanti ini dan detail lain nya di read dan taro di file txt
nama_umkm = input("Selamat Datang di aplikasi UMKM System!\nMohon masukkan nama UMKM Anda: ")
if nama_umkm in umkm_terdaftar:
    opsi = input(f"Selamat Datang {nama_umkm}!\nPilih menu :") #kasih menu opsi dari tiap fungsi class, buat dulu pengecekan di tiap class nya apakah sudah terdaftar atau ada data nya
#nanti pilih menu nya buat ke fungsi tersendiri
else:
    opsi = input(f"Selamat Datang {nama_umkm}!\nSepertinya {nama_umkm} belum terdaftar di sistem kami, apakah kamu mau mendaftarkan UMKM-mu? (Y/N): ")
    nama_umkm = UMKMSystem(nama_umkm)