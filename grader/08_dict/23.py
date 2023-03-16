n = int(input())

name_list = {}
name_list2 = {}

for i in range(n):
    firstname, lastname, phone = input().strip().split()
    name_list[firstname + ' ' + lastname] = phone
    name_list2[phone] = firstname + ' ' + lastname


n = int(input())

for i in range(n):
    find = input().strip()
    if find in name_list:
        print(find, '-->', name_list[find])
        continue
    elif find in name_list2:
        print(find, '-->', name_list2[find])
    else:
        print(find, '-->', "Not found")
