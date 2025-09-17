# ?> ./free_range.py | cat -e
# none$
# ?> ./free_range.py 10 14 | cat -e
# [10, 11, 12, 13, 14]$
# ?>

import sys

parameters = sys.argv[1:]

if len(parameters) != 2:
    print("none")
else:
    start = int(parameters[0])
    end = int(parameters[1])
    num_list = list(range(start, end + 1))
    print(num_list)