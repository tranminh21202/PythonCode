class ChuyenCan:
    def __init__(self,masv,ten,lop):
        self.masv = masv
        self.ten = ten
        self.lop = lop
        self.cc=10
        self.note=""
    def __str__(self):
        return "{} {} {} {} {}".format(self.masv,self.ten,self.lop,self.cc,self.note)
a=[]
n=int(input())
for i in range(n):
    a.append(ChuyenCan(input(),input(),input()))
for i in range(n):
    ip=input().split()
    diem=ip[1].count('m')+2*ip[1].count('v')
    for j in a:
        if ip[0]==j.masv:
            j.cc=max(0,j.cc-diem)
            if j.cc==0:
                j.note="KDDK"
            break
for i in a:
    print(i)