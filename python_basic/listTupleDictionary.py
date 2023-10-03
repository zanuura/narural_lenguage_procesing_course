#  List

fruit_list = ['Apple', 'Banana', 'Coconut', 'Durian', 'Orange', 'Mango']

apple = fruit_list[0]
print(apple)

fruits = fruit_list[0:4]
print(fruits)

print(fruit_list[2])
fruit_list[2] = 'Dragon fruit'
print(fruit_list[2])

# Menambahkan elemet pada list
# append
fruit_list.append("Purple")
print(fruit_list)
# insert
fruit_list.insert(3, "More Apple")
print(fruit_list)
# extend
fruit_list2 = ['coco', 'chocolate']
fruit_list.extend(fruit_list2)
print(fruit_list)

# Menghapus element
# remove
fruit_list.remove('Apple')
print(fruit_list)
# pop
fruit_list.pop(2)
print(fruit_list)
# del
del fruit_list[-1]
print(fruit_list)

# Tuple
# Bersifat immutable atau permanen(tidak bisa di rubah)

stuff_list = ('Laptop', 'Monitor', 'SmartPhone',)
print(stuff_list)
print(stuff_list[1])

# Dictionary

profile = {
    'nama': 'Hammam',
    'gender': 'Male',
    'age': 20,
}

print(profile)

# Praktik Bagian 1

list1 = ['watermelon', 'coconut', 'apple', 'banana', ]
list2 = [6, 7, 8, 9, 1, 2, 3, 4, 5,]
list3 = [True, False, True]
list4 = [True, 'abc', 10, False]
print(list1)
print(list2)
print(list3)
print(list4)

print(list1 + list2)

list2.sort()

print(list2)

list1.sort()

print(list1)

list2.reverse()
print(list2)

list1.reverse()
print(list1)

list2c = list2.copy()
list2c.reverse()
print(list2c)

# Dictionary

profile_user = {
    'name': 'Hammam',
    'age': 20,
    'gender': 'Male',
    'weight': 50,
    'height': 165,
}

for key, value in profile_user.items():
    print(key, value)

for key, value in profile_user.items():
    print(key, profile_user[key])


# SET

A = {1, 2, 3, 4, 5, 6, 7, 8, 9}
B = {10, 11, 12, 13, 14, 15, 16}

# UNION
print(A | B)

# INTERSECTION
print(A & B)

# DIFFERENCE
print(A - B)
print(B - A)

# SYMETRIC DIFFERENCE
print(A ^ B)
