def func(*n):
    return sorted(n, key=lambda a: len(a))
n = list(map(str, input().split()))
print(func(*n))
