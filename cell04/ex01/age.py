age = int(input("Please tell me your age: "))

for i in range(0, 4):
    if i == 0:
        print("You are currently %d years old." %age)
    else:
        print("In %d years, you'll be %d years old." %(i*10, age+(i*10)))
