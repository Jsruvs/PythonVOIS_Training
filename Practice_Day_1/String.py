#1 Write a program to count the number of vowels,consonants, digits, and special character in a given string.
s = "Hello123@#"

vowels = consonants = digits = special = 0

for ch in s:
    if ch.lower() in "aeiou":
        vowels += 1
    elif ch.isalpha():
        consonants += 1
    elif ch.isdigit():
        digits += 1
    else:
        special += 1

print("Vowels:", vowels)
print("Consonants:", consonants)
print("Digits:", digits)
print("Special Characters:", special)

#2 Given a string,reverse each word individually without changing the word order.

s = "Hello World Python"
words = s.split()
result = []

for word in words:
    result.append(word[::-1])

print(" After Reverse: ".join(result))

#3 check whether a given string is a palindrome using indexing and slicing

s = "malyalam"
if s == s[::-1]:
    print("Palindrome")
else:
    print("Not Palindrome")

#4 Write a program to find the frequency of each character in a string

s = "python"

freq = {}

for ch in s:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1

print(freq)

#5 Demonstrate string immutability by attempting to modify a character and handling the error.

s = "Python"
s[0] = "J"

   # try except
s = "Python"

try:
    s[0] = "J"
except TypeError as e:
    print("Error:", e)

 
