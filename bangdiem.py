from decimal import Decimal, ROUND_HALF_UP
class BD:
    def __init__(self, ma, ten, toan, viet, anh, ly, hoa, sinh, su, dia, cd, cn):
        self.ma = "HS{:02d}".format(ma)
        self.ten = ten
        self.toan = toan
        self.viet = viet
        self.anh = anh
        self.ly = ly
        self.hoa = hoa
        self.sinh = sinh
        self.su = su
        self.dia = dia
        self.cd = cd
        self.cn = cn
        tmp = ((toan*2) + (viet*2) + anh + ly + hoa + sinh + su + dia + cd + cn)/12
        self.tb = tmp.quantize(Decimal("0.1"), ROUND_HALF_UP)
        if self.tb >= 9:
            self.xh = "XUAT SAC"
        elif self.tb >= 8 and self.tb <= 8.9:
            self.xh = "GIOI"
        elif self.tb >= 7 and self.tb <= 7.9:
            self.xh = "KHA"
        elif self.tb >= 5 and self.tb <= 6.9:
            self.xh = "TB"
        elif self.tb < 5:
            self.xh = "YEU"
    def __str__(self):
        return self.ma + " " + self.ten + " " + str(self.tb) + " " + str(self.xh)
    
t = int(input())
ds = []
for i in range(t):
    ten = input()
    toan,viet,anh,ly,hoa,sinh,su,dia,cd,cn = (Decimal(x) for x in input().split())
    a = BD((i+1), ten, toan, viet, anh, ly, hoa, sinh, su, dia, cd, cn)
    ds.append(a)
ds = sorted(ds,key=lambda x:(-x.tb, x.ma))
for x in ds:
    print(x)