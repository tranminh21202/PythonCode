mod = 1000000007
def pow(a, b) :
    if b == 0 : return 1
    x = pow(a, int(b / 2))
    x = (x * x) % mod
    if b % 2 == 1 : x *= a
    return x % mod

def sodb(n, k) :
    if k <= 1 : return k
    x = 0
    while (k >> x) ^ 1 : x += 1
    return (pow(n, x) + sodb(n, k ^ (1 << x))) % mod

for t in range(int(input())) :
    n, k = map(int,input().split())
    print(sodb(n, k))