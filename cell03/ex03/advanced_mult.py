# for i in range(0, 11):
#     print("Table de %d: " %i, end="")
#     for j in range (0, 11):
#         print(i*j, end=" ")
#     print("")

i=0
while i < 11:
    print("Table de %d: " %i, end="")
    j=0 
    while j < 11:
        print(i*j, end=" ")
        j += 1
    i += 1
    print("")