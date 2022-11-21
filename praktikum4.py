a = ["b", "a", "k", "s", "o"]

print(a[3])
print(a[2:4])
print(a[4:])
print(a[:])

a[3] = 19
a[3:] = 19, 15

print(a[3])
print(a[3:])
print(a[:])

b = [19,15]
a.append(["a"])
a.append([23, 21, 25])
print(a[:])

c = a + b
a.extend(b)
print(a[:])