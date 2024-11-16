'''Author:Johns Jose
Date  :15/11/2024
Description:This is a Python program that checks 
if a given word is a palindrome. A palindrome is a word 
that reads the same forward and backward
'''

word = input("Enter a word: ")
if word == word[::-1]:
    print(f'"{word}" is a palindrome.')
else:
    print(f'"{word}" is not a palindrome.')

