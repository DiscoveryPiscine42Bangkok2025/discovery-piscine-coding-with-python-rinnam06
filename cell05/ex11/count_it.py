# ?> ./count_it.py | cat -e
# none$
# ?> ./count_it.py "Game" "of" "Thrones" | cat -e
# parameters: 3$
# Game: 4$
# of: 2$
# Thrones: 7$
# ?>

import sys

parameters = sys.argv[1:]

if len(parameters) == 0:
    print("none")
else:
    print("parameters: %d" %len(parameters))
    for i in parameters:
        count = 0
        for j in i:
            count += 1
        print("%s: %d" %(i, count))