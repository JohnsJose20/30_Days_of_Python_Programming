'''
Author:Krishnapriya
Date  :15/11/2024
Description:A python program that checks if a given word is a pallindrome.A pallindrome is a word thats reads the same forward and backward
word=input("enter a word:")
if word==word[::-1]:
    print(word,"is a pallindrom")
else:
    print(word,"is not a pallindrom")
