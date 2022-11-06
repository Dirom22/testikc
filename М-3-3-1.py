a = int(input())
b = int(input())
c = int(input())

p = 0
s = 0
def area(a, b, c):
    p = (a + b + c) / 2
    s = (p * (p - a) * (p - b) * (p - c)) **0.5
    return s

print(area(a, b, c))
