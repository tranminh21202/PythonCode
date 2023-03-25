def sosanh(s1,s2):
    list1 = []
    list2 = []
    for x in range(0,len(s1)):
        list1.append(s1[x])
    list1.sort()
    for x in range(0,len(s2)):
        list2.append(s2[x])
    list2.sort()
    if len(list1) != len(list2):
        return False
    for x in range(0,len(list1)):
        if list1[x] != list2[x]:
            return False
    return True
t = int(input())
i = 1
while i <= t:
    s1 = input()
    s2 = input()
    if sosanh(s1,s2):
        print(f"Test {i}: YES")
    else:
        print(f"Test {i}: NO")
    i += 1