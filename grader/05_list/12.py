name_list = {
    "Robert": "Dick",
    "William": "Bill",
    "James": "Jim",
    "John": "Jack",
    "Margaret": "Peggy",
    "Edward": "Ed",
    "Sarah": "Sally",
    "Andrew": "Andy",
    "Anthony": "Tony",
    "Deborah": "Debbie"
}

n = int(input().strip())

for i in range(n):
    name = input().strip()
    if name in name_list:
        print(name_list[name])
    else:
        a = [k for k, v in name_list.items() if v == name]
        print(a[0]) if len(a) != 0 else print("Not found")