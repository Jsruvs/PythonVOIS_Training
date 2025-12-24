#1
t = (10, 5, 20, 3, 15)

maximum = max(t)
minimum = min(t)

print("Maximum:", maximum)
print("Minimum:", minimum)


#2
lst = [("a", 1), ("b", 2), ("c", 3)]

d = {}
for key, value in lst:
    d[key] = value

print(d)

#3
t = (1, 2, 3, 2, 4, 2, 5)
element = 2

count = 0
for i in t:
    if i == element:
        count += 1

print("Occurrence of", element, "=", count)

#4
t = (1, 2, [10, 20, 30])

t[2][0] = 99

print(t)

#5
t1 = (1, 2, 3)
t2 = (4, 5, 6)

t1, t2 = t2, t1

print("t1:", t1)
print("t2:", t2)


#
