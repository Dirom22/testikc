x = int(input("Введите сумму вклада "))
p = float(input("Введите процентную ставку "))
y = int(input("Введите желаемую сумму вклада "))

i = 0
while x <= y:
    i += 1
    x = int(x + p * x / 100)
print(i)
