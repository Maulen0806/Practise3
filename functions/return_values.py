def func(num):
    for i in (2,3,5):
        while num % i == 0:
            num //= i
    return num == 1
n = int(input())
if func(n):
    print("Valid")
else:
    print("Not valid")
