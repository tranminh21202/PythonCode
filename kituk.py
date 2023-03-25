t = int(input())
while t>0:
    n,k = map(int,input().split())
    if k%2==1:
        print("A")
    else:
        dem = 0
        while k%2==0:
            k >>= 1
            dem += 1
        print(chr(65+dem))
    t-=1