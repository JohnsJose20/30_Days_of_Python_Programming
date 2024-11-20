"""
Author: Kritthik
Date: 20-11-2024
"""

while True:
    custom = input("Enter your name or quit the process by typing stop: ")
    if custom == "stop":
        print("Process is stopped")
        break
    else:
        print("Welcome", custom, "\b!")

