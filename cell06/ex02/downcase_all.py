# ?> ./downcase_all.py
# none
# ?> ./downcase_all.py "HELLO WORLD" "I understood Arrays well!"
# hello world
# i understood arrays well!
# ?>

import sys

def downcase_it(txt):
    return txt.lower()

parameters = sys.argv[1:]

if len(parameters) == 0:
    print("none")
else:
    for i in parameters:
        print(downcase_it(i))