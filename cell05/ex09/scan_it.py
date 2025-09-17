# ?> ./scan_it.py | cat -e
# none$
# ?> ./scan_it.py "the" | cat -e
# none$
# ?> ./scan_it.py "the" "the quick brown fox jumps over the lazy dog" | cat -e
# 2$
# ?>

import sys

parameters = sys.argv[1:]

if len(parameters) != 2:
    print("none")
else:
    keyword, txt = parameters
    count_word = txt.count(keyword)

    if count_word == 0:
        print("none")
    else:
        print(count_word)