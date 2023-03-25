t = int(input())
while t > 0:
    n = int(input())
    kq = 0.0
    if n % 2 == 0:
        for x in range(2,n+1,2):
            kq += float(1/x)
    else:
        for x in range(1,n+1,2):
            kq += float(1/x)
    print(f"{kq:.6f}")
    t -= 1