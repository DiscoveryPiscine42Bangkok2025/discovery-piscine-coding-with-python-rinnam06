# ?> ./append_it.py | cat -e
# none$
# ?> ./append_it.py "parallel" "egoism" "human" | cat -e
# parallelism$
# humanism$
# ?>

import sys

parameters = sys.argv[1:]

if len(parameters) == 0:
    print("none")
else:
    for i in parameters:
        if i[-3:] != "ism":
            print("%sism" %i)