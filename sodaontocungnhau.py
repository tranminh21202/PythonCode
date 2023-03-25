t = int(input())
def ucln(a,b):
    if b == 0:
        return a
    return ucln(b,a%b)
while t > 0:
    xau = input()
    xaumoi = ""
    for x in range(0,len(xau)):
        xaumoi = xau[x] + xaumoi
    a = int(xau)
    b = int(xaumoi)
    c = ucln(a,b)
    if c == 1:
        print("YES")
    else:
        print("NO")
    t -= 1