class DsPhim:
    def __init__(self, ma, tl, tg, ten, st):
        self.ma = "P{:03d}".format(ma)
        self.tl = tl
        self.tg = tg
        self.ten = ten
        self.st = int(st)
        self.ngay = int(tg[:2])
        self.thang = int(tg[3:5])
        self.nam = int(tg[6:])
    def __str__(self):
        return self.ma + " " + self.tl + " " + self.tg + " " + self.ten + " " + str(self.st)
    
n,m = (int(x) for x in input().split())
tl = []
ds = []
for i in range(n):
    tl.append(input())
for i in range(m):
    ma = input()
    tg = input()
    ten = input()
    st = int(input())
    ds.append(DsPhim((i+1), tl[int(ma[2:])-1], tg, ten, st))
ds = sorted(ds, key=lambda x: (x.nam, x.thang, x.ngay, x.ten, -x.st))
for i in ds:
    print(i)

