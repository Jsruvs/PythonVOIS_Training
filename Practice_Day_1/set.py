#1
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

print("Union:", A | B)
print("Intersection:", A & B)
print("Difference (A-B):", A - B)
print("Symmetric Difference:", A ^ B)

#2
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

common = A & B

A = A - common
B = B - common

print("A:", A)
print("B:", B)

#3

A = {1, 2}
B = {1, 2, 3, 4}

if A.issubset(B):
    print("A is a subset of B")
else:
    print("A is not a subset of B")

#4
s = {5, 10, 15, 20, 25}
num = 12

for i in s:
    if i > num:
        print(i)

#5
lst = [1, 2, 2, 3, 4, 4, 5]

unique_list = list(set(lst))

print(unique_list)

