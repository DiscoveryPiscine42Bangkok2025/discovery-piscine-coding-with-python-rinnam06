# ?> cat greetings_for_all.py | cat -e
# # your method definition here
# greetings('Alexandra')
# greetings('Wil')
# greetings()
# greetings(42)

# ?> ./greetings_for_all.py | cat -e
# Hello, Alexandra.$
# Hello, Wil.$
# Hello, noble stranger.$
# Error! It was not a name.$
# ?>

def greetings(name="noble stranger"):
    if isinstance(name, str):
        print("Hello, %s." %name)
    else:
        print("Error! It was not a name.")

greetings('Alexandra')
greetings('Wil')
greetings()
greetings(42)
