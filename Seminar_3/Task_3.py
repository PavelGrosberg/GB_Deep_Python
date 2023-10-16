from pprint import pprint
import itertools

items = {
    "ключи": 0.3,
    "кошелек": 0.2,
    "телефон": 0.5,
    "зажигалка": 0.1
}
max_weight = 1.0

result = []
result_dict = {}
backpack_weight = 0

combos = list(itertools.chain.from_iterable(itertools.combinations(items, r) for r in range(len(items) + 1)))

for i in range(len(combos)):
    for j in range(len(combos[i])):
        backpack_weight += items[combos[i][j]]
        if backpack_weight <= max_weight:
            result_dict[combos[i][j]] = items[combos[i][j]]
    backpack_weight = 0
    result_dict = {}
    result.append(result_dict)
result.pop()
pprint(result)
