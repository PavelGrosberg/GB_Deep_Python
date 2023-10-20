'''
Напишите функцию key_params, принимающую на вход только ключевые параметры и возвращающую словарь,
где ключ - значение переданного аргумента, а значение - имя аргумента.
Если ключ не хешируем, используйте его строковое представление.
'''


def key_params(**kwargs):
    res_dict = {}
    for k, v in kwargs.items():
        if isinstance(v, (bool, complex, float, list, dict)):
            v = str(v)
        res_dict[v] = k
    return res_dict


params = key_params(a=1, b='hello', c=[1, 2, 3], d={})
print(params)
