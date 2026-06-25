def show_balance(balance):
    print("===================================")
    print(f"Your balance is ${balance:.2f}")
    print("===================================")

    print()

def deposit():
    amount = float(input("Enter an amount to be deposited: "))

    if amount < 0:
        print("===================================")
        print("Please enter valid amount")
        print("===================================")

        
        return 0
    else:
        print("===================================")
        return amount
        print("===================================")

def withdraw(balance):
    w_amount = float(input("Enter an amount for withdrawal: "))
    if w_amount < 0:
        print("===================================")
        print("Please enter valid amount")
        print("===================================")
        return 0
    elif w_amount > balance:
        print("===================================")
        print("Insufficient Funds")
        print("===================================")
        return 0
    else:
        print("===================================")
        return w_amount
        print("===================================")

def main():
    balance = 0
    is_running = True

    while is_running:
        print("===================================")
        print("       Welcome to HDFC Bank        ")
        print("===================================")

        print("1. Show balance")
        print("2. Deposit")
        print("3. Withdraw")
        print("4. Exit")

        choice = input("Choose your option (1-4):  ")

        if choice == '1':
            show_balance(balance)

        elif choice == '2':
            balance += deposit()

        elif choice == '3':
            balance -= withdraw(balance)

        elif choice == '4':
            is_running = False

        else:
            print("That is not a valid choice")


    print("Thank you! Have a nice day!")

if __name__ == '__main__':
    main()

