class Mobil():

    def __init__(self, plat):

        self.__plat = plat
        self.__tipe = "Civic"
        self.__bensin = 40

    # Getter

    def lihatMaksimumBensin(self):
        print(f"Maksimum bensin yaitu {self.__bensin} liter")

    # Setter

    def aturMaksimumBensin(self, bensin):
        self.__bensin = bensin


civic = Mobil(plat="D 6576 HX")

# print(civic.plat)
# print(civic.tipe)
# print(civic.bensin)

civic.__bensin = 60

civic.lihatMaksimumBensin()

civic.aturMaksimumBensin(1000)

civic.lihatMaksimumBensin()
