# ?> ./upcase_it.py | cat -e
# none$
# ?> ./upcase_it.py "initiation" | cat -e
# INITIATION$
# ?> ./upcase_it.py 'This exercise is quite easy!' | cat -e
# THIS EXERCISE IS QUITE EASY!$
# ?>

import sys

count = len(sys.argv) - 1
if count != 1:
    print("none")
else:
    print(sys.argv[1].upper())