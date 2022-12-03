# This is my first Python program

print("This application will calculate your date of birth based on your age!")

name = input("What's your name? ")

print("Hi " + name + " Nice to meet you!")

age = input("How old are you? " + name)

def dob_calculater(age):
    dob = 2022 - int(age)
    return dob


dob_calculater()

print(name + ", you were born in " + str(dob))
