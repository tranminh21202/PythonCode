ok = True
while ok:
    n = int(input())
    dem = 0
    if n == 0:
        ok = False
        break
    elif n == 1:
        print(1)
    else:
        while n != 1:
            if n % 2 == 0:
                n /= 2
                dem += 1
            else:
                n = n*3+1
                dem += 1
        print(dem + 1)
