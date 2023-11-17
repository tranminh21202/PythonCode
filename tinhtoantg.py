class TG:
    def __init__(self, ma, ten, vao, ra):
        self.ma = ma
        self.ten = ten
        h1,p1 = vao.split(":")
        h2,p2 = ra.split(":")
        if int(p1) <= int(p2):
            self.gio = int(h2)-int(h1)
            self.phut = int(p2)-int(p1)
        else:
            self.gio = int(h2) - int(h1) - 1
            self.phut = 60 - int(p1)
    def __str__(self):
        return self.ma + " " + self.ten + " " + str(self.gio) + " gio " + str(self.phut) + " phut"
    
t = int(input())
ds = []
for i in range(t):
    ma = input()
    ten = input()
    vao = input()
    ra = input()
    a = TG(ma,ten,vao,ra)
    ds.append(a)
ds = sorted(ds,key=lambda x:(-x.gio,-x.phut))
for i in ds:
    print(i)