class NV:
    def __init__(self, ma, ten, lt, th):
        self.ma = "TS0" + str(ma)
        self.ten = ten
        if lt > 10:
            lt = lt/10
        if th > 10:
            th = th/10
        self.tb = (lt + th)/2
        if self.tb < 5:
            self.kq = "TRUOT"
        elif self.tb >=5 and self.tb < 8:
            self.kq = "CAN NHAC"
        elif self.tb >=8 and self.tb < 9.5:
            self.kq = "DAT"
        else:
            self.kq = "XUAT SAC"
    def __str__(self):
        return self.ma + " " + self.ten + " " + "{:.2f}".format(self.tb) + " " + self.kq

t = int(input())
ds = []
for i in range(t):
    ten = input()
    lt = float(input())
    th = float(input())
    a = NV((i+1), ten, lt, th)
    ds.append(a)
ds = sorted(ds,key=lambda x:-x.tb)
for i in ds:
    print(i)
