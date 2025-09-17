# ?> ./methods_everywhere.py | cat -e
# none$
# ?> ./methods_everywhere.py 'lol' 'physically' 'backpack' | cat -e
# lolZZZZZ$
# physical$
# backpack$
# ?>

import sys

def shrink(txt):
    return txt[:8]
    

def enlarge(txt):
    num = 8 - len(txt)
    for i in range(num):
        txt = txt + 'Z'
    return txt



parameters = sys.argv[1:]

if len(parameters) < 1:
    print("none")
else:
    for i in parameters:
        if len(i) < 8:
            print(enlarge(i))
        else:
            print(shrink(i))