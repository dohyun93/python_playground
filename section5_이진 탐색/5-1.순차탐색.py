def sequentialSearch(people, name):
    for idx in range(len(people)):
        if name == people[idx]:
            return idx

data = input().split()

numPeople = int(data[0])
findName = data[1]

people = input().split()

answer = sequentialSearch(people, findName)
print(f"정답은 {answer+1}번째에 있는 {people[answer]} 입니다.")