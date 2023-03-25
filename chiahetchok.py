xau = input()
arr = xau.split()
a = int(arr[0])
k = int(arr[1])
n = int(arr[2])
kq = []
for x in range(k-(a%k),n-a+1,k):
    if (x + a) % k == 0:
        kq.append(str(x))
if len(kq) == 0:
    print(-1)
else:
    print(" ".join(kq))