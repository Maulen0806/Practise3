def func(n):
    return lambda a: a ** n
n1 = int(input())
n2 = int(input())
power = func(n2)
print(power(n1))
