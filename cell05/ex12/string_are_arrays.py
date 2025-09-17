# ?> ./string_are_arrays.py | cat -e
# none$
# ?> ./string_are_arrays.py "The character Z is not found in this string" | cat -e
# none$
# ?> ./string_are_arrays.py "The character z is found in this string" | cat -e
# z$
# ?> ./string_are_arrays.py "Zaz visits the zoo with Zazie" | cat -e
# zzz$
# ?>

import sys

parameters = sys.argv[1:]
count_alpha = 0

if len(parameters) != 1:
    print("none")
else:
    for i in parameters[0]:
        if i == 'z':
            count_alpha += 1

    if count_alpha == 0:
        print("none")
    else:
        for i in range(count_alpha):
            print('z', end='')
        print("")