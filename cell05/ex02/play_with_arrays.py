# ?> ./play_with_arrays.py | cat -e
# [2, 8, 9, 48, 8, 22, -12, 2]$
# [10, 11, 50, 10, 24]$
# ?>

oarr = [2, 8, 9, 48, 8, 22, -12, 2]
narr = []
for i in oarr:
    num = i+2
    if num > 5:
        narr.append(num)
print(oarr)
print(narr)