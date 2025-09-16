# Give me a number: 42
# This number is an integer.
# ?>
# ?> ./float.py
# Give me a number: 42.00
# This number is an integer.
# ?>
# ?> ./float.py
# Give me a number: 42.42
# This number is a decimal.

num = float(input("Give me a number: "))
if num.is_integer():
    print("This number is an integer.")
else:
    print("This number is a decimal.")