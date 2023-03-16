n = int(input())

name_list = {}
name_list2 = {}

for i in range(n):
    firstname, lastname = input().strip().split()
    name_list[firstname] = lastname
    name_list2[lastname] = firstname

n = int(input())

for i in range(n):
    find = input().strip()
    if find in name_list:
        print(name_list[find])
    elif find in name_list2:
        print(name_list2[find])
    else:
        print("Not found")
