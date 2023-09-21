 
"""Median calculator."""
"""ENTER YOUR SOLUTION HERE!"""

while True:

print("Enter a list of numbers separated by commas: ")
list = [float(value) for value in input().split(",")]
length = len(list)
list.sort()
if length  % 2 == 0:
        number1 = list[length // 2]
        number2 = list[(length // 2) - 1]
        print((number1 + number2)/ 2)
else:
        print(list[(length // 2)])




