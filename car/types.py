some_list = [1, 2, 3, 4]
some_tuple = (5, 6, 7, 8, some_list)

print(some_tuple)
some_list.append(555)
print(some_tuple)
some_list.append("pop")
print(some_tuple)

a = 1
b = 1
some_list = [1, 2, 3, 4]
some_list_second = [1, 2, 3, 4]

print(some_list == some_list_second)
print(some_list is some_list_second)

print(a == b)
print(a is b)

print(id(a), id(b))
