# ?> ./round_up.py
# Give me a number: 41.42
# 42
# ?>
# ?> ./round_up.py
# Give me a number: 42
# 42
# ?>
# ?> ./round_up.py
# Give me a number: 0.001
# 1
# ?>

num = float(input("Give me a number: "))
if num == int(num):
    print(int(num))
else:
    print(int(num)+1)
