def ucln(a,b):
    if b == 0:
        return a
    return ucln(b,a%b)
xau = input()
arr = xau.split()
a,b = map(int,arr)
for x in range(a,b-1):
    for y in range(a+1,b):
        if ucln(x,y) == 1 and x < y:
            for z in range(y,b+1):
                if ucln(x,z) == 1 and ucln(y,z) == 1:
                    print(f"({x}, {y}, {z})")
