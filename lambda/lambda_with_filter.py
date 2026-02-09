def func(*n):
    return list(filter(lambda a: a % 2 == 0, n))
n = list(map(int, input().split()))
print(func(*n))
