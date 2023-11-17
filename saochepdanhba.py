class DB:
    def __init__(self, hoten, sdt, ngay):
        self.hoten = hoten
        self.sdt = sdt
        self.ngay = ngay
        self.ten = hoten.split()[-1]

    def getStr(self):
        return self.hoten + ": " + self.sdt + " " + self.ngay
    
r = open("SOTAY.txt", "r")
lines = r.read().split("\n")
ds = []
while len(lines) > 0:
    tmp = lines[0]
    lines.pop(0)
    if tmp[:4] == "Ngay":
        ngay = tmp[5:]
    elif len(lines) > 0:
        sdt = lines[0]
        lines.pop(0)
        a = DB(tmp, sdt, ngay)
        ds.append(a)
ds = sorted(ds,key=lambda x:(x.ten,x.hoten))
op = open("DIENTHOAI.txt","w")
for x in ds:
    op.write(x.getStr() + "\n")