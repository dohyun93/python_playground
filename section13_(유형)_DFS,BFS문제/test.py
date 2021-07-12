from collections import deque

dq = deque()
dq.append(3)
dq.append(1)
dq.append(4)

dq = sorted(dq)
print(dq)