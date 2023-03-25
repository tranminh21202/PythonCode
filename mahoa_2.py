ok = True
P = ['A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','_','.']
while ok:
    xau = input()
    arr = xau.split()
    k = int(arr[0])
    if k == 0:
        break
    s = arr[1]
    kq = ""
    for x in s:
        kq = P[(P.index(x)+k)%28] + kq
    print(kq)
