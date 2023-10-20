import model


def get_balance(balance):
    print(f'Balance: {balance}')


def run():
    while True:
        print("1. Deposit")
        print("2. Withdraw")
        print("3. Balance")
        print("4. Exit")
        choice = input("Enter your choice: ")
        if choice == '1':
            amount = int(input('How much (must be a multiple of 100): '))
            print(f'Пополнение карты на {amount} у.е.')
            model.deposit(amount)
        elif choice == '2':
            pass
        elif choice == '3':
            get_balance(model.balance)
        elif choice == '4':
            model.richness()
            get_balance(model.balance)
            break
