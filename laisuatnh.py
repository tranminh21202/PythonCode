t = int(input())
while t > 0:
    xau = input()
    arr = xau.split()
    n,x,m = map(float,arr)
    nam = 0
    while n < m:
        lai = float(n * x / 100)
        n += lai
        nam += 1
    print(nam)
    t -= 1