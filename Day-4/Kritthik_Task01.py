"""
Author: Kritthik
Date: 15-11-2024
"""
custom = input("Enter a word: ")
rev = reversed(custom)

if list(custom) == list(rev):
    print("The given word is a palindrome")
else:
    print("The given word is not a palindrome")