n = int(input())
students = []

for i in range(n) :
    name, korean, english, math = input().split()
    students.append((name, int(korean), int(english), int(math)))


students.sort(key=lambda x : (-x[1], x[2], -x[3], x[0]))
for i in range(n) :
    print(students[i][0])
    
# 국어점수 기준 정렬

# diff = []
# start = students[0][1]

# # 국어점수 바뀌는 부분 찾기
# for i in range(1, n) :
#     if students[i][1] != start :
#         diff.append(i)
#         start = students[i][1]

# # 영어점수 기준 정렬
# idxStart = 0
# for d in diff :
#     students[idxStart:d] = sorted(students[idxStart:d], key=lambda x : x[2])
#     idxStart = d;

# # 영어점수 바뀌는 부분 찾기
# diff = []
# start = students[0][2]

# for i in range(1, n) :
#     if students[i][2] != start :
#         diff.append(i)
#         start = students[i][2]
        
# # 수학점수 기준 정렬
# idxStart = 0
# for d in diff :
#     students[idxStart:d] = sorted(students[idxStart:d], key=lambda x : -x[3])
#     idxStart = d;


# print(students)