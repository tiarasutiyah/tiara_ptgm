# Deklarasi Class Induk
class Kendaraan:
    def __init__(self, merk, kecepatan):
        self.merk = merk
        self.kecepatan = kecepatan 

# Subclass Kucing
class BMW(Kendaraan):
    def info(self):
        print(f"Mobil {self.merk} melaju {self.kecepatan} km/jam.")


# Subclass Anjing
class Porsche(Kendaraan):
    def info(self):
        print(f"Mobil {self.merk} melaju {self.kecepatan} km/jam.")


# Membuat objek dari subclass
b1 = BMW("BMW", 800)
p1 = Porsche("Porsche", 400)

# Memanggil method
b1.info()
p1.info()