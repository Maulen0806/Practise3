def func(*n):
    return list(map(lambda a: a ** 2, n))
n = list(map(int, input().split()))
print(func(*n))
