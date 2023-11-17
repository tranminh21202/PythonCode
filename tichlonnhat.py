n = int(input())
a = [int(x) for x in input().split()]
a.sort()
print(max(a[0]*a[1], max(a[-1]*a[-2], max(a[0]*a[1]*a[-1], a[-1]*a[-2]*a[-3]))))