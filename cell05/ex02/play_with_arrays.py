#!/usr/bin/python3
array = [2,8,9,48,8,22,-12,2]
new_array = [x + 2 for x in array if x > 5]
print(f"Original array: {array}")
print(f"New array: {new_array}")
