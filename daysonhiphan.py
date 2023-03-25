n = int(input())
list1 = list(map(int,input().split()))
dem = 0
for x in range(0,n-1):
    if list1[x] != list1[x+1]:
        dem += 1
print(dem)