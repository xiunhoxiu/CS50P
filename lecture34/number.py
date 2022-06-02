def main():
    x = get_int("What's x?")
    print(f"you've typed x is {x}")

def get_int(prompt):
    while(True):
        try:
            return int(input(prompt))
        except ValueError:
            pass  ## stay in the loop without telling user what's wrong


main()
