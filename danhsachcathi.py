class Ca_Thi:
    def __init__(self,n,ngaythi,giothi,phong):
        self.maca = "C{:03d}".format(n)
        self.ngaythi = ngaythi
        self.giothi = giothi
        self.phong = phong
    def __str__(self):
        return f"{self.maca} {self.ngaythi} {self.giothi} {self.phong}"
ds = []
with open("CATHI.in") as read:
    lines = read.readlines()
t = int(lines[0])
dem = 1
for x in range(1,len(lines),3):
    ngaythi = lines[x].rstrip()
    giothi = lines[x+1].rstrip()
    phong = lines[x+2].rstrip()
    a = Ca_Thi(dem,ngaythi,giothi,phong)
    ds.append(a)
    dem += 1
ds.sort(key=lambda a:(a.ngaythi,a.giothi,a.maca))
for x in ds:
    print(x)
