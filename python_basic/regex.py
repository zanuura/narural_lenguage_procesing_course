import re

teks = "radix"
x = re.match("^r...x$", teks)
print(x)

# split
teks = "Saya senang belajar regex"
x = re.split("\s", teks)
print(x)

# subtitue
teks = '''
        Ada 3 tipe looop atau perulangan di bahasa pemrograman python 
        yaitu while loop, for loop, dan nested loop 2012
        '''
x = re.sub('\d+', "", teks)
print(x)

# search
teks = 'Hujan deras di daerah bandung'
results = re.search("^Hujan.*bandung$", teks)

if results:
    print("YES! We have a match.")
else:
    print("No Match!")

# findall
teks = '23 oct 2019 23 oct, 2019 october, 2019 oct 26, 2020'
x = re.findall("\d{2} [a-z]{3} \d{4}", teks)
print(x)

# sensor
teks = 'harga 1 mobile antik tersebut yaitu $1000'
x = re.sub("\$\d+", '#######', teks)
print(x)

teks = 'Akan dialihkan ke http://google.com'
x = re.sub("http[s]?\://\S+", "____", teks)
print(x)

teks = 'Luar biasa! banyak anak-anak muda traveling tahun ini, begini tanggapan lesti #travel #_lesti #viral #gadget'
x = re.findall("#[_]*[a-z]+", teks)
print(x)
