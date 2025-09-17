# ?> ./parameter_matching.py
# none
# ?> ./parameter_matching.py "Hello"
# What was the parameter? Bonjour
# Nope, sorry...
# ?> ./parameter_matching.py "Hello"
# What was the parameter? Hello
# Good job!
# ?>

import sys

parameters = sys.argv[1:]

if len(parameters) != 1:
    print("none")
else:
    prompt = input("What was the parameter? ")
    if prompt == parameters[0]:
        print("Good job!")
    else:
        print("Nope, sorry...")