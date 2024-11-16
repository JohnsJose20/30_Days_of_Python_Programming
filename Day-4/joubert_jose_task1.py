'''
Author:joubert jose
Date  :15/11/2024
Description:This is a Python program that checks if a given
word is a palindrome. A palindrome is a word that reads the same forward and backward
'''
word=input("enter a word:")
word2=word[::-1]
if word==word2:
    print(word,"is palindrome")
else:
    print(word,"is not palindrome")
