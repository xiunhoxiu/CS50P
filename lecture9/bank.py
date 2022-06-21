balance = 0

def main():
    balance = 0
    print("Balance:", balance)
    deposit(100)
    withdraw(50)
    print("New Balance:", balance)

def deposit(n):
    global balance
    balance += n


def withdarw(n):
    global balance
    balance -= n

if __name__ == "__main__":
    main()