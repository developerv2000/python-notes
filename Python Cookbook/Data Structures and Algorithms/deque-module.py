from collections import deque

q = deque(maxlen=3)
q.append(1)
q.append(2)
q.append(3)
print(q)  # deque([1, 2, 3], maxlen=3)

q.append(4)
print(q)  # deque([2, 3, 4], maxlen=3)

q.appendleft(8)
print(q)  # deque([8, 2, 3], maxlen=3)

q.popleft()
print(q)  # deque([2, 3], maxlen=3)
