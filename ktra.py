#bai4
input_str = input("Nhập danh sách các chuỗi (các phần tử ngăn cách bởi dấu cách): ")

input_list = input_str.split()
ky_tu= set()

for item in input_list:
    for char in item:
       ky_tu.add(char)
result_list = list(ky_tu)

print(result_list)

#bai2

def min_steps(x):
    
    a = [float('inf')] * (x + 1)
    a[0] = 0
    for i in range(x + 1):
        if a[i] != float('inf'):
           
            if i + 1 <= x:
                a[i + 1] = min(a[i + 1], a[i] + 1)
            if i + 2 <= x:
                a[i + 2] = min(a[i + 2], a[i] + 1)
            if i + 3 <= x:
                a[i + 3] = min(a[i + 3], a[i] + 1)
    
    return a[x]

x = int(input("Nhập tọa độ đích: "))
print(f"Số bước tối thiểu cần thiết: {min_steps(x)}")

#bai1

input_string = input().strip()
input_list = input_string.split()

numbers = [int(num) for num in input_list]


count_dict = {}
for num in numbers:
    if num in count_dict:
        count_dict[num] += 1
    else:
        count_dict[num] = 1

result = []
for num, count in count_dict.items():
    if count % 5 == 0 and count % 10 != 0:
        result.append(num)

print(*result)


#bai3

n = int(input("Nhập số lượng thành viên: "))

members = []

for _ in range(n):
    data = input().split()
    name = data[0]
    score = int(data[1])
    members.append((name, score))


scores = [score for _, score in members]


diem_cao = sorted(set(scores))
if len(diem_cao) > 1:
    score_t2 = diem_cao[1]
else:
    score_t2 = diem_cao[0]  

name_t2 = [name for name, score in members if score == score_t2]

for name in name_t2:
    print("người có điểm thấp thứ 2 trong nhóm là : " , name)





