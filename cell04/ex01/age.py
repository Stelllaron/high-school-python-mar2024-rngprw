#!/usr/bin/env python3

my_age =int(input("Please tell me your age : "))
print(f"You are currently {my_age} years old")
for future in [10, 20, 30] :
    future_age = my_age + future 
    print(f" In {future} years, you will be {future_age} years old.")

