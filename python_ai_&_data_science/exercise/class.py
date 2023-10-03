class Cat:
    def __init__(self, nama, tipe):
        self.nama = nama
        self.tipe = tipe
        self.kaki = 4

    def run(self):
        var = f"Kucing {self.nama} sedang berlari"
        print(var)

    def jump(self):
        var = f"Kucing {self.nama} sedang melompat"
        print(var)

    def getNama(self):
        return self.nama

    def setNama(self, namaBaru):
        self.nama = namaBaru


persia = Cat("tom", "persia")
print(persia.nama)
persia.nama = "jojo"

# Setter Getter
# print(persia.getNama())
# persia.setNama("jojo")

print(persia.nama)

# print(persia.tipe)
# print(persia.kaki)
# persia.run()
# persia.jump()

# anggora = Cat("coco", "anggora")
# anggora.jump()
