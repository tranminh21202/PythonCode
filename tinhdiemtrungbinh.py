from math import ceil
class SV:
    def __init__(self, ma, hoten, diem1, diem2, diem3):
        self.ma = "SV{:02d}".format(ma)
        self.hoten = hoten
        self.diem1 = diem1
        self.diem2 = diem2
        self.diem3 = diem3
        self.tb = (diem1*3+diem2*3+diem3*2)/8
        self.xh = 0

    def __str__(self):
        return self.ma + " " + self.hoten + " " + "{:.2f}".format(ceil(self.tb*100)/100) + " " + str(self.xh)
    
def chuanHoa(xau):
    return " ".join(i.title() for i in xau.strip().split())

n = int(input())
ds = []
for i in range(n):
    hoten = chuanHoa(input())
    diem1 = int(input())
    diem2 = int(input())
    diem3 = int(input())
    a = SV((i+1), hoten, diem1, diem2, diem3)
    ds.append(a)
ds = sorted(ds,key=lambda x:(-x.tb,x.ma))
p = 1
dem = 1
while i < len(ds)-1:
    if ds[i].tb > ds[i+1].tb:
        ds[i].xh = p
        p += 1
        i += 1
    elif ds[i].tb == ds[i+1].tb:
        j = i
        while ds[j].tb == ds[j+1].tb:
            ds[j].xh = ds[j+1].xh = p
            dem += 1
            j += 1
        p += dem
        i += dem
        dem = 1
for i in ds:
    print(i)


