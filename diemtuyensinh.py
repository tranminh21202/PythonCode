class Diem_Tuyen:
    def __init__(self,n,hoten,diem,dantoc,khuvuc):
        self.ma = "TS{:02d}".format(n)
        self.hoten = hoten
        self.diem = diem
        self.dantoc = dantoc
        self.khuvuc = khuvuc
    
    def get_tong(self):
        if self.dantoc == "Kinh":
            if self.khuvuc == 1:
                return self.diem + 1.5
            elif self.khuvuc == 2:
                return self.diem + 1
            elif self.khuvuc == 3:
                return self.diem
        else:
            if self.khuvuc == 1:
                return self.diem + 1.5 + 1.5
            elif self.khuvuc == 2:
                return self.diem + 1 + 1.5
            elif self.khuvuc == 3:
                return self.diem + 1.5
            
    def get_tt(self):
        if self.get_tong() >= 20.5:
            return "Do"
        else:
            return "Truot"
        
    def __str__(self):
        return f"{self.ma} {self.hoten} {'{:.1f}'.format(self.get_tong())} {self.get_tt()}"

ds = []
i = 1
t = int(input())
while t > 0:
    hoten = ' '.join(input().strip().title().split())
    diem = float(input())
    dantoc = input()
    khuvuc = int(input())
    a = Diem_Tuyen(i,hoten,diem,dantoc,khuvuc)
    ds.append(a)
    i += 1
    t -= 1
ds.sort(key=lambda a:(-a.get_tong(),a.ma))
for x in ds:
    print(x)
