from collections import deque
t = int(input())
st = deque()
st.append([int(input()), 1])
cnt = 0
for i in range(1,t):
    x = int(input())
    while len(st) > 0:
        top = st.pop()
        if top[0] > x:
            cnt += 1
            st.append(top)
            st.append([x, 1])
            break
        elif top[0] == x:
            cnt += top[1]
            if len(st) > 0:
                cnt += 1
            st.append([x, top[1] + 1])
            break
        else:
            cnt += top[1]
    if len(st) == 0:
        st.append([x, 1])
print(cnt)