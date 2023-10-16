'''
В большой текстовой строке text подсчитать количество встречаемых слов и вернуть 10 самых частых. Не учитывать знаки
препинания и регистр символов.

Слова разделяются пробелами, апостроф не считается за пробел. Такие слова как dont, its, didnt итд (после того, как
убрали знак препинания апостроф) считать одним словом.

На выходе:
[('hello', 3), ('world', 1), ('python', 1), ('again', 1)]
'''

text = 'Hello world. Hello Python. Hello again.'

punctuation = r"""!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~"""
digits = '0123456789'

for punctuation in punctuation:
    text = text.replace(punctuation, ' ')
    for digit in digits:
        text = text.replace(digit, '')

text = text.lower().split()
uniq_text = []
res = []

for i in text:
    if i not in uniq_text:
        uniq_text.append(i)

for i in uniq_text:
    res.append((i, text.count(i)))

res.sort(key=lambda a: a[1], reverse=True)

print(res[:10])
