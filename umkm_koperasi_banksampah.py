class UMKMSystem:
    anggota = []
    dana_pinjaman = 50000000

    def __init__(self, nama_umkm):
        self.umkm = nama_umkm
        
    def tambah_anggota(self, nama_anggota, jumlah_pinjaman):
        self.anggota.append({"nama_anggota": nama_anggota, "jumlah_pinjaman": jumlah_pinjaman})
        
        print(f"{nama_anggota} telah sukses terdaftar sebagai anggota {self.umkm} dengan jumlah pinjaman {jumlah_pinjaman:,}")
        
        if self.dana_pinjaman - jumlah_pinjaman > 0:
            self.dana_pinjaman = self.dana_pinjaman - jumlah_pinjaman
        else:
            print(f"Mohon maaf, dana pinjaman pada UMKM {self.umkm} telah mencapai limit.\n"
                  +"Anda dapat menggunakannya kembali ketika anggota lain sudah mengembalikan, Terimakasih.")
    
    def hitung_pengembalian(self, nama_anggota, tahun_pengembalian):
        jumlah_pinjaman = 0
        for dict_anggota in self.anggota:
            if dict_anggota["nama_anggota"] == nama_anggota:
                jumlah_pinjaman = dict_anggota["jumlah_pinjaman"]
        
        total_pengembalian = jumlah_pinjaman + (jumlah_pinjaman * 0.05) * tahun_pengembalian
        
        print(f"Total pengembalian dari {nama_anggota} selama {tahun_pengembalian} Tahun sebesar: {int(total_pengembalian):,}")
                    

class Koperasi(UMKMSystem):
    def __init__(self, nama_umkm):
        super().__init__(nama_umkm.umkm)
        self.transaksi = []

    def catat_transaksi(self, nama_anggota, jenis_transaksi, jumlah_transaksi):
        self.transaksi.append({'nama_anggota': nama_anggota, 'jenis_transaksi': jenis_transaksi, 'jumlah_transaksi': jumlah_transaksi})
        print("Transaksi telah sukses tercatat.")

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
        # print(transaksi_beli)
        # print(transaksi_jual)
        print(f"Total Keuntungan Koperasi sebesar (Rp.): {total_keuntungan:,}")


class BankSampah(UMKMSystem):
    def __init__(self, nama_umkm):
        super().__init__(nama_umkm.umkm)
        self.data_sampah = {}

    def catat_sampah(self, nama_anggota, jenis_sampah, jumlah):        
        if nama_anggota in self.data_sampah:
            for i in self.data_sampah:
                if i == nama_anggota:
                    if jenis_sampah in self.data_sampah[i]:
                        self.data_sampah[nama_anggota][jenis_sampah] = self.data_sampah[nama_anggota][jenis_sampah] + jumlah
                    else:
                        self.data_sampah[nama_anggota][jenis_sampah] = jumlah
        else:
            self.data_sampah[nama_anggota] = {jenis_sampah: jumlah}
        
        print("\nData Bank sampah telah tercatat.")
        self.pesan_edukasi(nama_anggota)
    
    def hitung_nilai_tukar(self):
        total_per_anggota = {}
        total_nilai = 0
        for items in self.data_sampah:
            nilai_anggota = 0
            for type in self.data_sampah[items]:
                if type == "plastik":
                    nilai_anggota = nilai_anggota + (5000 * self.data_sampah[items][type])
                elif type == "kertas":
                    nilai_anggota = nilai_anggota + (2000 * self.data_sampah[items][type])
            total_nilai = total_nilai + nilai_anggota
            total_per_anggota[items] = nilai_anggota

            print(f"Total nilai tukar {items} : ", nilai_anggota)
        print("Total nilai tukar semua anggota : ", total_nilai)

    def pesan_edukasi(self, nama):
        total_sampah = 0
        for items in self.data_sampah:
            if items == nama:
                for jenis_sampah in self.data_sampah[nama]:
                    total_sampah = total_sampah + self.data_sampah[nama][jenis_sampah]
        if total_sampah > 50:
            print(f"\n{nama} telah mengumpulkan {total_sampah} kg sampah.\n"
                  + "Anda adalah pahlawan lingkungan sejati!")
        elif total_sampah > 20:
            print(f"\n{nama} telah mengumpulkan {total_sampah} kg sampah.\n"
                  + "Mari bersama berkontribusi lebih banyak untuk bumi!")
        elif total_sampah > 0:
            print(f"\n{nama} telah mengumpulkan {total_sampah} kg sampah.\n"
                  + "Semoga ini menjadi awal yang baik untuk kita bisa mengumpulkan lebih banyak sampah lagi!")
        else:
            print(f"\n{nama} belum mengumpulkan sampah.\nMari kita mulai mengumpulkan sampah agar Bumi kembali bersih!")


def menu(nama_umkm):
    global koperasi, bank_sampah
    while True:
        try:
            print("\nSilahkan pilih menu:")
            print("1. UMKM System")
            print("2. Koperasi")
            print("3. Bank Sampah")
            print("4. Laporan")
            print("5. Keluar")
            pilih_menu = int(input("Pilih (1/2/3/4): "))
            if pilih_menu == 1:
                print("\nUMKM System\n-----------\nSilahkan pilih kegiatan:")
                print("1. Tambah Anggota")
                print("2. Hitung Pengembalian")
                print("3. Kembali")
                # print("4. Laporan")
                menu_umkm = int(input("Pilih (1/2/3): "))

                if menu_umkm == 1:
                    if isinstance(bank_sampah, BankSampah) and len(bank_sampah.data_sampah) > 0:
                        nama_anggota = input("Masukkan nama anggota: ")
                        jumlah_pinjaman = int(input("Masukkan jumlah pinjaman: "))
                        nama_umkm.tambah_anggota(nama_anggota, jumlah_pinjaman)
                    else:
                        print(f"Notes: {nama_umkm.umkm} belum aktif dalam program Bank Sampah sehingga belum dapat menggunakan dana pinjaman.\n")
                        nama_anggota = input("Masukkan nama anggota: ")
                        jumlah_pinjaman = 0
                        nama_umkm.tambah_anggota(nama_anggota, jumlah_pinjaman)
                elif menu_umkm == 2:
                    nama_anggota = input("Masukkan nama anggota: ")
                    tahun_pengembalian = int(input("Masukkan tahun pengembalian (1,2,dst): "))
                    nama_umkm.hitung_pengembalian(nama_anggota, tahun_pengembalian)
                elif menu_umkm == 3:
                    pass
                # elif menu_umkm == 4:
                #     print(nama_umkm.anggota)
                else:
                    print("Mohon Pilih menu yang tertera.")

            elif pilih_menu == 2:
                print("Koperasi\n-----------\nSilahkan pilih kegiatan:")
                print("1. Daftar Koperasi")
                print("2. Catat Transaksi")
                print("3. Hitung Keuntungan")
                print("4. Kembali")
                menu_koperasi = int(input("Pilih (1/2/3/4): "))

                if menu_koperasi == 1:
                    if isinstance(koperasi, Koperasi):
                        print("Anda sudah terdaftar dalam program Koperasi")
                    else:
                        koperasi = Koperasi(nama_umkm)
                elif menu_koperasi == 2:
                    nama_anggota = input("Masukkan nama anggota: ")
                    jenis_transaksi = input("Masukkan jenis transaksi (Jual/Beli): ")
                    jumlah_transaksi = int(input("Masukkan jumlah transaksi: "))
                    koperasi.catat_transaksi(nama_anggota, jenis_transaksi, jumlah_transaksi)
                elif menu_koperasi == 3:
                    koperasi.hitung_keuntungan()
                elif menu_koperasi == 4:
                    pass
                else:
                    print("Mohon Pilih menu yang tertera.")
                
            elif pilih_menu == 3:
                print("Bank Sampah\n-----------\nSilahkan pilih kegiatan:")
                print("1. Daftar Bank Sampah")
                print("2. Catat Sampah")
                print("3. Hitung Nilai Tukar")
                print("4. Informasi Data Bank Sampah")
                print("5. Kembali")
                menu_bank_sampah = int(input("Pilih (1/2/3/4/5): "))

                if menu_bank_sampah == 1:
                    if isinstance(bank_sampah, BankSampah):
                        print("Anda sudah terdaftar dalam program Bank Sampah")
                    else:
                        bank_sampah = BankSampah(nama_umkm)
                elif menu_bank_sampah == 2:
                    nama_anggota = input("Masukkan nama anggota: ")
                    jenis_sampah = input("Masukkan jenis sampah: ")
                    jumlah_sampah = int(input("Masukkan jumlah sampah: "))
                    bank_sampah.catat_sampah(nama_anggota, jenis_sampah, jumlah_sampah)
                elif menu_bank_sampah == 3:
                    bank_sampah.hitung_nilai_tukar()
                elif menu_bank_sampah == 4:
                    nama_anggota = input("Masukkan nama anggota: ")
                    print(bank_sampah.data_sampah[nama_anggota])
                elif menu_bank_sampah == 5:
                    pass
                else:
                    print("Mohon Pilih menu yang tertera.")
            elif pilih_menu == 4:
                print(f"\nBerikut Laporan lengkap dari UMKM {nama_umkm.umkm}:\n")
                for items in nama_umkm.anggota:
                    nama = items["nama_anggota"]
                    pinjaman = items["jumlah_pinjaman"]
                    print(f"Nama: {nama}\nJumlah Pinjaman: {pinjaman}\n")
                for items in koperasi.transaksi: #masih ada yg kurang pas output sama looping nya
                    transaksi_beli = 0
                    transaksi_jual = 0
                    if items["jenis_transaksi"] == "jual":
                        transaksi_jual = items["jumlah_transaksi"]
                    elif items["jenis_transaksi"] == "beli":
                        transaksi_beli = items["jumlah_transaksi"]
                    nama = items["nama_anggota"]
                    total_keuntungan = transaksi_jual - transaksi_beli
                    print(f"Transaksi:\nNama: {nama}\nTransaksi Jual: {transaksi_jual}\nTransaksi Beli: {transaksi_beli}\nTotal Keuntungan: {total_keuntungan}")
                koperasi.hitung_keuntungan()
                
                bank_sampah.hitung_nilai_tukar()
                for items in bank_sampah.data_sampah:
                    nama = items
                    bank_sampah.pesan_edukasi(nama)
                    # transaksi = items["jenis_transaksi"]
                    # jumlah = items["jumlah_transaksi"]

            elif pilih_menu == 5:
                break
            else:
                print("Mohon Pilih menu yang tertera.")
        except Exception as e:
            print(e)

try:
    nama_umkm = input("Selamat Datang di aplikasi UMKM System!\nMohon masukkan nama UMKM Anda: ")
    print(f"Selamat Datang {nama_umkm}!")
    nama_umkm = UMKMSystem(nama_umkm)
    koperasi = None
    bank_sampah = None
    menu(nama_umkm)
except Exception as e:
    print(e)