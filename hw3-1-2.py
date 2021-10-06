# Author: Nolan (AMDG) 9/28/2021

x = int(input("Input your first card's worth: "))
y = int(input("Input your second card's worth: "))

if x + y <= 21:
    print("you are safe")
else:
    print("you are not safe")