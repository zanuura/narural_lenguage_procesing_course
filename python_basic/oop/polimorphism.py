'''
Polimorphisme adalah kemampuan untuk menggunakan satu fungsi
umum untuk kemudian bekerja secara beragam tergantung 
object yang diberikan 
'''


class Cat:

    def __init__(self):
        self.nama = 'Meong'
        self.tipe = 'Anggora'

    def forward(self):
        print("Kucing itu berlari...")


class Bird:

    def __init__(self):
        self.nama = 'Erago'
        self.tie = 'Elang'

    def forward(self):
        print("Burung itu terbang...")


def melaju(objek):
    objek.forward()


meong = Cat()
erago = Bird()

melaju(meong)
melaju(erago)
