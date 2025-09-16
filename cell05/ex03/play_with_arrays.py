# ?> ./play_with_arrays.py | cat -e
# [2, 8, 9, 48, 8, 22, -12, 2]$
# {24, 10, 11, 50}$
# ?>

oarr = [2, 8, 9, 48, 8, 22, -12, 2]
narr = []
for i in oarr:
    num = i+2
    if num > 5:
        narr.append(num)
print(oarr)
print(set(narr))