def args_total(*nums):
    sum = 0
    for num in nums:
        sum += num
    return sum
n = tuple(map(int, input().split()))
print(args_total(*n))
