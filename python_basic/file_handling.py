# Read

# data = open('data/data_text.txt', mode='r')  # Membaca file
# print(data.read())

# # encoding
# data = open('data/data_text.txt', mode='r', encoding='utf-8')
# print(data.read())

# # Append

# data = open('data/data_text.txt', mode='a')  # Menambahkan file
# data.write('\n halo')
# data.write('\n hallo lagii')

# # Write

# data = open('data/data_text.txt', mode='w')  # Mengubah file
# data.write('\n halo')
# data.write('\n hallo lagii gaesss')

# # print(data)
# data.close()

# Best Practice
try:
    f = open('data/data_text.txt', mode='r', encoding='utf-8')
    print(f.read())
finally:
    f.close()

# Best practice

with open('data/data_text.txt', mode='r', encoding='utf-8') as f:
    print(f.read())
    f.close()
