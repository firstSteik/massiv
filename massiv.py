from array import array
a = array('h', [1, 2, 2, 3, 3, 3, 4, 4, 4, 4, 5, 5, 6])
for i in a:
    if a.count(i) > 2:
        a.remove(i)
print(a)
