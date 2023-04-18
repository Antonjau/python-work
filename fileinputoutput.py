#!/usr/bin/python3
name = input("whats your name?")

#file = open("names.txt", "a")
#file.write(f"{name}\n")
#file.close()
with open("names.txt", "a") as file:
    file.write(f"{name}\n")
    