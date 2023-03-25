ok = True
while ok:
    n = int(input())
    ds = []
    if n == 0:
        ok = False
        break
    else:
        while n > 0:
            t = int(input())
            ds.append(t)
            n -= 1
        x = min(ds)
        y = max(ds)
        if x == y:
            print("BANG NHAU")
        else:
            print(x,y)
