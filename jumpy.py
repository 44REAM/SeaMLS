def is_jumpy(num):
    down = 0
    up = 0
    str_num = str(num)
    for i in range(len(str_num)-1):
        if int(str_num[i])<int(str_num[i+1]):
            up = 1
        elif int(str_num[i])>int(str_num[i+1]):
            down = 1
        if down and up:
            return 1
    return 0

max_number = 500
num = 100
n = 0
jumpy_list = []  

while n<max_number:
    if is_jumpy(num):
        jumpy_list.append(num)
        n+=1
    num+=1

print(len(jumpy_list))
print(sum(jumpy_list))

