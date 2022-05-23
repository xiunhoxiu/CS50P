def hello(to="world"):  # assigning world if not assigned an argument from user.
    print("hello,", to)

hello()
name = input("What's your name? ")
hello(name)