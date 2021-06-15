dr = [2, 2, -2, -2, 1, 1, -1, -1]
dc = [1, -1, 1, -1, 2, -2, 2, -2]

position = input()
r = ord(position[0]) - ord('a') + 1
c = int(position[1])
answer = 0
# 8 x 8 좌표평면. (1,1) ~ (8,8)
for i in range(len(dr)):
    nr = r + dr[i]
    nc = c + dc[i]
    if nr < 1 or nc < 1 or nr > 8 or nc > 8:
        continue
    answer += 1
print(answer)