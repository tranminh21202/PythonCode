def phantich(n):
    ds = []
    while n % 2 == 0:
        ds.append(2)
        n //= 2
    i = 3
    while n > 1:
        if n % i == 0:
            n //= i
            ds.append(i)
        else:
            i += 2
    if len(ds) == 0:
        ds.append(n)
    return sum(ds)

n = int(input())
tong = 0
while n > 0:
    x = int(input())
    tong += phantich(x)
    n -= 1
print(tong)
