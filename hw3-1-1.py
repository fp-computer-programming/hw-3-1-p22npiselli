# Author: Nolan (AMDG) 9/28/2021

x = int(input("Team 1 input number of wins: "))
y = int(input("Team 1 input number of ties: "))
a = int(input("Team 2 input number of wins: "))
b = int(input("Team 2 input number of ties: "))

if x + y > a + b:
    print("Team 1 has more points")
elif a + b > x + y:
    print("Team 2 has more points")
 