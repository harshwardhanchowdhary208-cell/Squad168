n=int(input())
res = 0
while n > 0 or res > 9:
    if n == 0:
        n = res
        res = 0
    res += n % 10
    n //= 10
print(res)
