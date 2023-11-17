class HD:
    def __init__(self, ma, ten, moi, cu):
        self.ma = "KH{:02d}".format(ma)
        self.ten = ten
        t = moi-cu
        if t >= 0 and t <= 50:
            t = t*100
            t = t + t*0.02
        elif t >= 51 and t <= 100:
            t = 50*100 + (t-50)*150
            t = t + t*0.03
        elif t > 100:
            t = 50*100 + 50*150 + (t-100)*200
            t = t + t*0.05
        self.tong = round(t)

    def __str__(self):
        return self.ma + " " + self.ten + " " + str(self.tong)
    
t = int(input())
ds = []
for i in range(t):
    ten = input()
    cu = int(input())
    moi = int(input())
    a = HD((i+1), ten, moi, cu)
    ds.append(a)
ds = sorted(ds,key=lambda x:(-x.tong))
for i in ds:
    print(i)