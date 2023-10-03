# class Cat:
#     def __init__(self, nama, tipe):
#         self.nama = nama
#         self.tipe = tipe
#         self.kaki = 4

#     def run(self):
#         var = f"Kucing {self.nama} sedang berlari"
#         print(var)

#     def jump(self):
#         var = f"Kucing {self.nama} sedang melompat"
#         print(var)

#     def getNama(self):
#         return self.nama

#     def setNama(self, namaBaru):
#         self.nama = namaBaru


# persia = Cat("tom", "persia")
# print(persia.nama)
# persia.nama = "jojo"

# # Setter Getter
# # print(persia.getNama())
# # persia.setNama("jojo")

# print(persia.nama)

# # print(persia.tipe)
# # print(persia.kaki)
# # persia.run()
# # persia.jump()

# # anggora = Cat("coco", "anggora")
# # anggora.jump()


class Mobil:

    def __init__(self, merk, tahun, warna, harga):
        self.merk = merk
        self.tahun = tahun
        self.warna = warna
        self.harga = harga

    def run(self):
        print(f"Mobil {self.merk} melaju")

    def getMerk(self):
        return self.merk

    def setMerk(self, merkBaru):
        self.merk = merkBaru


class Suv(Mobil):

    def __init__(self, merk, warna, tahun, harga):

        super().__init__()

        self.merk = merk
        self.warna = warna
        self.tahun = tahun
        self.harga = harga

    def run(self):
        print(f"Mobil {self.merk} melaju")

    def getMerk(self):
        return self.merk

    def setMerk(self, merkBaru):
        self.merk = merkBaru


honda = Mobil(merk='honda', tahun='2022', warna='hitam', harga='2000')

toyota = Mobil(merk='toyota', tahun='2012', warna='biru', harga='5000')

nissan = Mobil(merk='nissan', tahun='2023', warna='putih', harga='22000')

print(honda.getMerk())
print(toyota.getMerk())
print(nissan.getMerk())

honda.setMerk('Honda New')

print(honda.getMerk())
print(toyota.getMerk())
print(nissan.getMerk())

# jeep = Suv(merk='Jeep', warna='Orange', tahun='2023', harga='8989787')

# print(jeep.getMerk())
