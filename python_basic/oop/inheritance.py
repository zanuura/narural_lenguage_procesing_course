# kosep oop yang meeariksan semua funsionalitas dari kelas induk

# Parent class
class Animal:

    def __init__(self):
        self.tipe = 'Mamalia'
        self.kecepatan = 'Lambat'

    def grow(self):
        print(f"Mamalia ini bertumbuh...")

# Child class


class Cat(Animal):

    def __init__(self, nama, tipe):

        super().__init__()

        self.nama = nama
        self.tipe = tipe

    def run(self):
        print(f"Kucing {self.nama} berlari...")


class Dog(Animal):
    pass


kinako = Cat(nama='Kinako', tipe='Anggora')
minto = Cat(nama='Minto', tipe='Persia')

print(kinako.kecepatan)
print(kinako.tipe)
print(kinako.run())

print(minto.kecepatan)
print(minto.tipe)
print(minto.run())
