'''
author:karthika tb
date:16-11-2024
description:A Python program that checks if a given word is a palindrome.
 A palindrome is a word that reads the same forward and backward.
'''
str1=input("enter a word:")
str2=str1[::-1]
if str1==str2:
    print(str1,"is palindrome")
else:
    print(str1,"is not palindrome")


