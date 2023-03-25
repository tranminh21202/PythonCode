t = int(input())
kq = []
while t > 0:
    xau = input().upper()
    if xau not in kq:
        kq.append(xau)
    t -= 1
print(len(kq))