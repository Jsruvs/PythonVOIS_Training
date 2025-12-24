#1 write a program to remove duplicate elements from a list without using set.

lst = [1, 2, 2, 3, 4, 4, 5]
unique_list = []

for item in lst:
    if item not in unique_list:
        unique_list.append(item)
print(unique_list)

#2 Given a list of numbers, create a new list containing only even numbers using list comprehension

numbers = [1, 2, 3, 4, 5, 6, 7, 8]
even_numbers = [n for n in numbers if n % 2 == 0]
print(even_numbers)

#3 Write a program to find the second largest element in a list

lst = [10, 20, 30, 40, 20]
unique_lst = list(set(lst))
unique_lst.sort()

print("Second Largest:", unique_lst[-2])

#4 Create a nested list and calculate the sum of each inner list

<<<<<<< HEAD
lst = [[1, 2, 3], [4, 5, 6], [7, 8,7]]
for inner_list in lst:
    total = sum(inner_list)
    print("sum:", total)
=======
list = [[1, 2, 3], [4, 5, 6], [7, 8,7]]
for inner_list in list:
    print("Sum:", sum(inner_list))
>>>>>>> 03dc96e696b4dd49321817cac8ad650c33a8becb

#5 Demonstrate shallow copy and deep copy of a list with mutable elements.

import copy


lst1 = [[1, 2], [3, 4]]
shallow = copy.copy(lst1)

shallow[0][0] = 99

print("Original:", lst1)
print("Shallow:", shallow)

  #deep copy
deep = copy.deepcopy(lst1)

deep[0][0] = 10

print("Original:", lst1)
print("Deep:", deep)

