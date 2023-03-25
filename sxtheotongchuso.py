def sum(n):
    sum = 0
    tmp = str(n)
    for x in range(0,len(tmp)):
        sum += int(tmp[x])
    return sum
t = int(input())
while t > 0:
    n = int(input())
    ds = list(map(int,input().split()))
    dict = {}
    for x in ds:
        tmp = sum(x)
        dict[x] = tmp
    kq = sorted(dict.values())
    print()
    t -= 1