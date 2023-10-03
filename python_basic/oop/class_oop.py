# CLASS
class Cat:
    '''
    ini adalah class untuk kucing
    '''

    species = 'Kucing'

    def __init__(self, nama, tipe):
        self.nama = nama
        self.tipe = tipe

    def run(self, speed):
        print(f"Kucing {self.nama} berlari dg kecepatan {speed}")

    def play(self):
        print(f"Kucing {self.nama} bermain dengan kucing lainnya...")

    def eat(self):
        pass

# OBJECTS


class Employee():
    '''
    ini adalah untuk memanipulasi data employee 
    melalui kelas ini kita akan memanipulasi data yang ada seperti baca, hapus, dan tambah
    '''

    def __init__(self, lokasi_file):

        self.data_employee = open(f"{lokasi_file}", mode='r', encoding='utf-8')
        self.data_per_sesi = 10

    def baca(self):

        self.data_employee = self.data_employee[:self.data_per_sesi]
        return self.data_employee

    def hapus(self, baris, kolom):

        del self.data_employee[baris][kolom]

    def tambah(self, data_baru):
        nama, gaji, posisi, jabatan, domisili, = data_baru
        self.data_employee.append([nama, gaji, posisi, jabatan, domisili])


kinako = Cat('Kinako', 'Anggora')
minto = Cat('Minto', 'Persia')

kinako.run(speed='20')
minto.run(speed='30')

print(kinako.nama)
print(minto.nama)

# del kinako
# del minto

print(kinako)
print(minto)

# membuat object

# it = Employee(lokasi_file='./karyawan_it.xls')
# marketing = Employee(lokasi_file='./marketing.xls')
# product = Employee(lokasi_file='./product.xls')

# Abstract Object


class RandomForest():
    pass
