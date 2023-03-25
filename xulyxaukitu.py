s1 = input().lower()
s2 = input().lower()
set1 = set(s1.split())
set2 = set(s2.split())
x = sorted(set1 & set2)
y = sorted(set1 | set2)
for i in y:
    print(i,end=" ")
print()
for i in x:
    print(i,end=" ")
print()
