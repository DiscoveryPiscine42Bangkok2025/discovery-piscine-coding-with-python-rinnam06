i = 0
while True:
    txt = ""
    if i == 0:
        txt = input("What you gotta say? : ")
    else:
        txt = input("I got that! Anything else? : ")

    if txt == "STOP":
        break
    i += 1
