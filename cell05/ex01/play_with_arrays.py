# ?> ./play_with_arrays.py
# Original array: [2, 8, 9, 48, 8, 22, -12, 2]
# New array: [4, 10, 11, 50, 10, 24, -10, 4]
# ?>
oarr = [2, 8, 9, 48, 8, 22, -12, 2]
narr = []
for i in oarr:
    num = i+2
    narr.append(num)
print("Original array: " + str(oarr))
print("New array: " + str(narr))