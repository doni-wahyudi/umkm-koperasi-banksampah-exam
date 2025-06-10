class UMKMSystem:
    anggota = [] 
    dana_pinjaman = 50000000

    def __init__(self, nama_umkm):
        self.umkm = nama_umkm

    def tambah_anggota(self, nama_anggota, jumlah_pinjaman):
        if self.dana_pinjaman - jumlah_pinjaman > 0:
            self.dana_pinjaman = self.dana_pinjaman - jumlah_pinjaman
            if len(self.anggota) > 0:
                for i in nama_umkm.anggota:
                    if i["nama_anggota"] == nama_anggota:
                        self.anggota[self.anggota.index(i)] = {"nama_anggota": nama_anggota, "jumlah_pinjaman": jumlah_pinjaman}
                        print(f"{nama_anggota} telah sukses terupdate jumlah pinjaman menjadi Rp. {jumlah_pinjaman:,}")
                        break
                else:
                    self.anggota.append({"nama_anggota": nama_anggota, "jumlah_pinjaman": jumlah_pinjaman})
                    print(f"{nama_anggota} telah sukses terdaftar sebagai anggota {self.umkm} dengan jumlah pinjaman Rp. {jumlah_pinjaman:,}")
            else:
                self.anggota.append({"nama_anggota": nama_anggota, "jumlah_pinjaman": jumlah_pinjaman})
                print(f"{nama_anggota} telah sukses terdaftar sebagai anggota {self.umkm} dengan jumlah pinjaman Rp. {jumlah_pinjaman:,}")
        else:
            print(f"Mohon maaf, dana pinjaman pada UMKM {self.umkm} telah mencapai limit.\n"
                  +"Anda dapat menggunakannya kembali ketika anggota lain sudah mengembalikan, Terimakasih.")
            self.anggota.append({"nama_anggota": nama_anggota, "jumlah_pinjaman": 0})
            print(f"{nama_anggota} telah sukses terdaftar sebagai anggota {self.umkm} dengan jumlah pinjaman Rp. 0")
    
    def hitung_pengembalian(self, nama_anggota, tahun_pengembalian):
        for dict_anggota in self.anggota:
            if dict_anggota["nama_anggota"] == nama_anggota:
                jumlah_pinjaman = dict_anggota["jumlah_pinjaman"]
        
        total_pengembalian = jumlah_pinjaman + (jumlah_pinjaman * 0.05) * tahun_pengembalian
        
        print(f"Total pengembalian dari {nama_anggota} selama {tahun_pengembalian} Tahun sebesar (Rp.): {int(total_pengembalian):,}")
                    

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
            if items["jenis_transaksi"].lower() == "jual":
                transaksi_jual = transaksi_jual + items["jumlah_transaksi"]
            elif items["jenis_transaksi"].lower() == "beli":
                transaksi_beli = transaksi_beli + items["jumlah_transaksi"]

        total_keuntungan = transaksi_jual - transaksi_beli
        return total_keuntungan


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
                if type.lower() == "plastik":
                    nilai_anggota = nilai_anggota + (5000 * self.data_sampah[items][type])
                elif type.lower() == "kertas":
                    nilai_anggota = nilai_anggota + (2000 * self.data_sampah[items][type])
            total_nilai = total_nilai + nilai_anggota
            total_per_anggota[items] = nilai_anggota
            print(f"Total nilai tukar {items} (Rp.): {nilai_anggota:,}")
        print(f"Total nilai tukar semua anggota (Rp.): {total_nilai:,}")

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
            print("\nSilahkan pilih menu:\n1. UMKM System\n2. Koperasi\n3. Bank Sampah\n4. Laporan\n5. Keluar")

            pilih_menu = int(input("Pilih (1/2/3/4): "))
            if pilih_menu == 1:
                print("\nUMKM System\n-----------\nSilahkan pilih kegiatan:\n1. Tambah Anggota\n2. Hitung Pengembalian\n3. Kembali")
                
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
                else:
                    print("Mohon Pilih menu yang tertera.")

            elif pilih_menu == 2:
                print("\nKoperasi\n-----------\nSilahkan pilih kegiatan:\n1. Daftar Koperasi\n2. Catat Transaksi\n3. Hitung Keuntungan\n4. Kembali")
                menu_koperasi = int(input("Pilih (1/2/3/4): "))

                if menu_koperasi == 1:
                    if isinstance(koperasi, Koperasi):
                        print("UMKM Anda sudah terdaftar dalam program Koperasi.")
                    else:
                        koperasi = Koperasi(nama_umkm)
                        print("Selamat Anda kini menjadi bagian dalam program Koperasi!")
                elif menu_koperasi == 2:
                    nama_anggota = input("Masukkan nama anggota: ")
                    jenis_transaksi = input("Masukkan jenis transaksi (Jual/Beli): ")
                    jumlah_transaksi = int(input("Masukkan jumlah transaksi: "))
                    koperasi.catat_transaksi(nama_anggota, jenis_transaksi, jumlah_transaksi)
                elif menu_koperasi == 3:
                    print(f"Total Keuntungan Koperasi sebesar (Rp.): {koperasi.hitung_keuntungan():,}")
                elif menu_koperasi == 4:
                    pass
                else:
                    print("Mohon Pilih menu yang tertera.")
                
            elif pilih_menu == 3:
                print("\nBank Sampah\n-----------\nSilahkan pilih kegiatan:\n1. Daftar Bank Sampah\n2. Catat Sampah\n3. Hitung Nilai Tukar\n4. Kembali")
                menu_bank_sampah = int(input("Pilih (1/2/3/4/5): "))

                if menu_bank_sampah == 1:
                    if isinstance(bank_sampah, BankSampah):
                        print("UMKM Anda sudah terdaftar dalam program Bank Sampah.")
                    else:
                        bank_sampah = BankSampah(nama_umkm)
                        print("Selamat Anda kini menjadi bagian dalam program Bank Sampah!")
                elif menu_bank_sampah == 2:
                    nama_anggota = input("Masukkan nama anggota: ")
                    jenis_sampah = input("Masukkan jenis sampah: ")
                    jumlah_sampah = int(input("Masukkan jumlah sampah: "))
                    bank_sampah.catat_sampah(nama_anggota, jenis_sampah, jumlah_sampah)
                elif menu_bank_sampah == 3:
                    bank_sampah.hitung_nilai_tukar()
                elif menu_bank_sampah == 4:
                    pass
                else:
                    print("Mohon Pilih menu yang tertera.")
            elif pilih_menu == 4:
                print(f"\nLaporan\n-----------\nBerikut Laporan lengkap dari UMKM {nama_umkm.umkm}:\n")
                for items in nama_umkm.anggota:
                    nama = items["nama_anggota"]
                    pinjaman = items["jumlah_pinjaman"]
                    print(f"Nama Anggota: {nama}\nJumlah Pinjaman (Rp.): {pinjaman:,}")
                print(f"\nTransaksi Koperasi:")
                for items in koperasi.transaksi:
                    print(f"Nama: {items['nama_anggota']}, Transaksi: {items['jenis_transaksi']}, Nominal (Rp.): {items['jumlah_transaksi']:,}")
                print(f"Total Keuntungan Koperasi sebesar (Rp.): {koperasi.hitung_keuntungan():,}")
                
                bank_sampah.hitung_nilai_tukar()
                for items in bank_sampah.data_sampah:
                    nama = items
                    bank_sampah.pesan_edukasi(nama)

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