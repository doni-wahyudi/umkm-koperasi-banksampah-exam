class UMKMSystem:
    def __init__(self, nama_umkm):
        self.nama_umkm = nama_umkm
        self.anggota = []
        self.dana_pinjaman = 50000000
        
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

            # for item in dict_anggota:
            #     print(item)
            #     if item[nama_anggota] == nama_anggota:
            #         jumlah_pinjaman = item[jumlah_pinjaman]
            # print(list_anggota)
            # for key, values in list_anggota.items():
            #     if key == nama_anggota:
            #         jumlah_pinjaman = values

    # def hitung_pengembalian(self, nama_anggota, tahun_pengembalian):
    #     jumlah_pinjaman = 0
    #     for list_anggota in self.anggota:
    #         # print(list_anggota)
    #         for key, values in list_anggota.items():
    #             if key == nama_anggota:
    #                 jumlah_pinjaman = values
            

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

        self.data_sampah = {"doni" : {"plastik" : 10,"kertas" : 5}, "ihsan" : {"kertas" : 4, "plastik":2}}
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
umkm_c = BankSampah("Batch 10")
# umkm_c.catat_sampah("doni","plastik",30)
# umkm_c.catat_sampah("doni","kertas",5)
# umkm_c.catat_sampah("doni","organik",20)
# umkm_c.catat_sampah("ihsan","kertas",8)
# umkm_c.catat_sampah("ihsan","organik",2)
# umkm_c.catat_sampah("doni","kertas",15)

umkm_c.hitung_nilai_tukar()

print(umkm_c.data_sampah)