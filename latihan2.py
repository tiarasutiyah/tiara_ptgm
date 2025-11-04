class Kendaraan:
    def __init__(self, merk, kecepatan):
        self.merk = merk
        self.kecepatan = kecepatan 

class BMW(Kendaraan):
    def info(self):
        print(f"Mobil {self.merk} melaju {self.kecepatan} km/jam.")


class Honda(Kendaraan):
    def info(self):
        print(f"Motor {self.merk} melaju {self.kecepatan} km/jam.")


# Membuat objek dari subclass
b1 = BMW("BMW", 800)
p1 = Honda("Honda", 400)

# Memanggil method
b1.info()
p1.info()
