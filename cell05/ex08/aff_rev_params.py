# ?> ./aff_rev_params.py | cat -e
# none$
# ?> ./aff_rev_params.py "coucou" | cat -e
# none$
# ?> ./aff_rev_params.py "Python" "piscine" "hello" | cat -e
# hello$
# piscine$
# Python$
# ?>

import sys

count = len(sys.argv) - 1
if count < 2:
    print("none")
else:
    for i in reversed(sys.argv[1:]):
        print(i)