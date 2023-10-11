import fractions

frac1 = "4/8"
frac2 = "1/2"

split_frac1 = frac1.split('/')
split_frac2 = frac2.split('/')
int_split_frac1 = []
int_split_frac2 = []

for i in split_frac1:
    i = int(i)
    int_split_frac1.append(i)

for i in split_frac2:
    i = int(i)
    int_split_frac2.append(i)

x = int(split_frac1[1])
y = int(split_frac2[1])

if x > y:
    greater = x
else:
    greater = y
while True:
    if (greater % x == 0) and (greater % y == 0):
        lcm = greater
        break
    greater += 1

a = lcm // int_split_frac1[1]
b = lcm // int_split_frac2[1]

for i in range(len(int_split_frac1)):
    int_split_frac1[i] = int_split_frac1[i] * a

for i in range(len(int_split_frac2)):
    int_split_frac2[i] = int_split_frac2[i] * b

print(f'Сумма дробей: {int_split_frac1[0] + int_split_frac2[0]}/{lcm}')
print(f'Произведение дробей: {int_split_frac1[0] * int_split_frac2[0] // lcm}'
      f'/{int_split_frac1[1] * int_split_frac2[1] // lcm}')
c = fractions.Fraction(frac1)
d = fractions.Fraction(frac2)
print(f'Сумма дробей: {c + d}')
print(f'Произведение дробей: {c * d}')
