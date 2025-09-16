num1 = int(input("Enter the first number : "))
num2 = int(input("Enter the second number : "))

sum = num1 * num2
print("%d x %d = %d" %(num1, num2, sum))
if sum < 0:
    print("The result is negative.")
elif sum > 0:
    print("The result is positive.")
else:
    print("The result is positive and negative.")
