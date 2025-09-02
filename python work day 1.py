#reverse a given string without using bulit in reverse functions
def reverse_string(s):
    if len(s) == 0:
        return s
    return reverse_string(s[1:]) + s[0]

s = input("enter name: ")
print(reverse_string(s))


#Check if a string is a palindrome
s = input("enter the plaindrome: ")
is_palindrome = True
for i in range(len(s) // 2):
    if s[i] != s[len(s) - i - 1]:
        is_palindrome = False
        break

if is_palindrome:
    print("Palindrome")
else:
    print("Not Palindrome")

#Count the number of vowels and consonants in a string
text = input("Enter a string: ").lower()
vowels = sum(1 for ch in text if ch in "aeiou")
consonants = sum(1 for ch in text if ch.isalpha() and ch not in "aeiou")
print("Vowels:", vowels, "Consonants:", consonants)

#Remove all spaces from a given string
text = input("Enter a string: ")
text = text.replace(" ", "")
print(text)


#Count the frequency of each character in a string
text = input("Enter a string: ")
freq = {}
for ch in text:
    freq[ch] = freq.get(ch, 0) + 1
print(freq)
