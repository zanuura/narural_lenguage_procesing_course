# Logical error

try:
    nilai = 10
    pembagi = 0
    hasil = nilai / pembagi
    print(hasil)
except Exception as e:
    print("Oops! terjadi ", e.__class__, ".")

try:
    nilai = 10
    pembagi = 0
    hasil = nilai / pembagi
    print(hasil)
except ZeroDivisionError:
    print("Oops terjadi ZeroDivisionError")
except ValueError:
    print("Oops terjadi ValueError")
except:
    print("Oops terjadi error yang tidak di ketahui")


class valueTooSmallError(Exception):
    pass


class ValueTooLargeError(Exception):
    pass


number = 10

while True:

    try:
        i_num = int(input("Tebak angka : "))

        if i_num < number:
            raise valueTooSmallError
        elif i_num > number:
            raise ValueTooLargeError
        break

    except valueTooSmallError:
        print('Angka yang kamu tebak terlalu kecil, coba lagi')
        print()
    except ValueTooLargeError:
        print('Angka yang kamu tebak terlalu besar, coba lagi')
        print()

print('Betul kamu berhasil menebak angka yang benar')
