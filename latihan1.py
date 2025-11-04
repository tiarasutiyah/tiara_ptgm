# Deklarasi Class
class Siswa:
    # Atribut Class
    sekolah = "SMK PGRI 35 SOLOKANJERUK"

    # Konstruktor
    def __init__(self, nama, nis, kelas):
        self.nama = nama
        self.nis = nis
        self.kelas = kelas

    # Method
    def tampilkan_info(self):
        print(f"Nama      : {self.nama}")
        print(f"Nis       : {self.nis}")
        print(f"Kelas     : {self.kelas}")
        print(f"Sekolah   : {Siswa.sekolah}")


# Membuat Objek
b1 = Siswa("Tiara Sutiyah", 8405319, "XI RPL 3")

# Memanggil Method
b1.tampilkan_info()


