# # Stuktur syntax
# #  fungsi non-parameter
# def halo_dunia():
#     var = "halo dunia isekai"
#     print(var)

# # Pemanggilan fungsi

# halo_dunia()

# # Fungsi parameter

# def halo_name(name):
#     var = "halo {name} selamat datang di isekai"
#     print(var)

# nhalo_name('hammam')

# # Fungsi anonim

# double = lambda x: x * 2

# print(double(5))


# Function non-parameter
def halo_dunia():
    var = "Hallo python, halo duia!"
    print(var)

halo_dunia()

# Function parameter
def selamat_datang(name, asal):
    '''
    ini adalag fungsi untuk
    menyapa nama yang telah disebutkan
    '''
    var = f"Halo {name} dari {asal}, welcome!"
    print(var)

selamat_datang('Hammam', "Isekai")
selamat_datang('Muhajir', "Multiverse")
selamat_datang('Ahmad', "Another Universe")

def selamat_datang(*daftar_nama):

    var = 'Halo '
    for nama in daftar_nama:
        var += nama + ", "

    var += "Welcome"
    print(var)

selamat_datang('Ahmad', 'Hammam', 'Muhajir', 'Hanan')
print(selamat_datang.__doc__)

# anonim
double = lambda x: x * 3

print(double(5))

def selamat_datang(nama):
    '''
    ini adalah fungsi untuk menyapa
    nama yang sudah di sebutkan
    '''
    var = f'Halo {nama}, welcome'
    print(var)

selamat_datang('hammam')
print(selamat_datang.__doc__)

# BONUS : Scope & Return

# Return
def operasi(a, b, c):

    op1 = a * b
    op2 = op1 // c

    return op2

hasil = operasi(10, 5, 2)
print(hasil)

# Scope
a = 2

def operasi(a, b, c):

    op1 = a * b
    op2 = op1 // c

    print('a di dalam function : ', a)

    return op2

hasil = operasi(15, 5, 2)
print('a di luar funcrion : ', a)