import view

RICHNESS_SUM = 10_000
RICHNESS_PERCENT = 5
MULTIPLICITY = 100
balance = 0


def richness():
    global balance
    if balance >= RICHNESS_SUM:
        balance = balance - (balance * RICHNESS_PERCENT / 100)


def check_multiplicity(amount) -> bool:
    if amount % MULTIPLICITY == 0:
        return True
    return False


def deposit(amount):
    global balance
    if not check_multiplicity(amount):
        print('Value is not MULTIPLICITY')
    else:
        balance += amount
        view.get_balance(balance)
        return balance
