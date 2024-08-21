n = int(input())
student_marks = {}
for _ in range(n):
    line = input().split()
    name = line[0]
    marks = list(map(float, line[1:]))  
    student_marks[name] = marks
query_name = input()
marks = student_marks[query_name]
average = sum(marks) / len(marks)
print(f"{average:.2f}")