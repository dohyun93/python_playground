import sys
N = int(input())
students = []

for i in range(N):
    data = input().split()
    students.append((data[0], int(data[1])))

sortedStudents = sorted(students, key=lambda students: students[1])
# [참고] 큰 점수대로 정렬하려면 아래처럼.
# sortedStudents = sorted(students, key=lambda students: students[1], reverse=True)

for student in sortedStudents:
    print(student[0], end=' ')
