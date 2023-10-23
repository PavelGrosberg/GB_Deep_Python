names = ["Alice", "Bob", "Charlie"]
salary = [5000, 6000, 7000]
bonus = ["10%", "5%", "15%"]

result = {name: salary * (float(bonus.strip('%')) / 100) for name, salary, bonus in zip(names, salary, bonus)}
print(result)
