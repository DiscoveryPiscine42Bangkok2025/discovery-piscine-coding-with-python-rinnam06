# ?> ./aff_first_param.py | cat -e
# none$
# ?> ./aff_first_param.py "Code Ninja" "Numerique" "42" | cat -e
# Code Ninja$
# ?>

import sys

count = len(sys.argv) - 1
if count == 0:
    print("none")
else:
    print(sys.argv[1])