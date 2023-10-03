count = 0

# while loop
while (count < 1000):
    print("Nilai count: ", count)
    count = count + 1 # untuk while loop ini harus ada agar tidak ada looping forever

print("Good By")

# for loop
list_angka = [1,2,3,4,5]

for x in list_angka:
    print("Instruksi berjalan...")
    print(x)

print(range(10))

print(list(range(10)))

list_range = list(range(1, 100, 8))

print(list_range)

for x in list(range(11, 200, 5)):
    print(x)

# nested loop

i = 20

while (i < 200):

    j = 2
    print(i/j)
    while (j <= (i/j)):
        print("loop di dalam loop! ", (i/j))
        j = j + 1
        i = i + 1

print('Selamata tinggal')

# break and continue

for val in "String":

    if val == "i":
        continue

    print(val)

print("loop berakhir")

# for else

daftar_murid = ["angga", "mahdi", "royan", "farhan"]

nama_murid = 'farhan'

for nama in daftar_murid:

    if nama == nama_murid:
        print(nama)
        break

else:
    print("nama murid tidak ditemukan")