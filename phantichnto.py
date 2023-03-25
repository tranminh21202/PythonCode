import math
t = int(input())
while t>0:
    n = int(input())
    dem = 0
    print(f"{1}", end="")
    while n % 2 == 0:
        n /= 2
        dem += 1
    if dem > 0:
        print(f" * {2}^{dem}", end="")
        dem = 0
    if n != 1:
        for x in range(3,int(n)+1,2):
            while n % x == 0:
                dem += 1
                n //= x
            if dem > 0:
                print(f" * {x}^{dem}", end="")
                dem = 0
            else:
                continue
    print("")
    t -= 1