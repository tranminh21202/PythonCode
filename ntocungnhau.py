def ucln(a,b):
    if b == 0:
        return a
    return ucln(b,a%b)
xau = input()
arr = xau.split()
n,k = map(int,arr)
o = k - 1
dem = 1
for x in range(10**o,10**k):
    if ucln(n,x) == 1 and dem < 10:
        print(x,end=" ")
        dem += 1
    elif ucln(n,x) == 1 and dem == 10:
        print(x,end="\n")
        dem = 1
print("")
