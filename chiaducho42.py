test = 10
kq = []
chia = []
while test > 0:
    xau = input()
    arr = xau.split()
    for x in arr:
        chia.append(int(x))
    test -= len(arr)
for x in chia:
    tmp = x % 42
    if tmp not in kq:
        kq.append(tmp)
print(len(kq))