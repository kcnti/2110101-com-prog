data = {}

while(1):
    p = input().strip().split()
    
    if len(p) == 1:
        break
    rating = p[1].replace('+', '').replace('-', '')
    if rating in data:
        data[rating].append(p[0])
    else:
        data[rating] = [p[0]]

rating_data = {"None": 0}

while(1):
    t = 0
    p = input().strip().split()
    if len(p) == 1:
        break
    name = ""
    for i in range(len(p[0])):
        if p[0][i].isdigit():
            name = p[0][:i]
            break
    for i in data:
        for j in data[i]:
            if name == j:
                if i in rating_data:
                    rating_data[i] += int(p[1])
                else:
                    rating_data[i] = int(p[1])
                t = 1
    if not t:
        rating_data["None"] += int(p[1])

total = sum(list(rating_data.values()))

for rating_group in ['AAA','AA','A','BBB','BB','B','CCC','CC','C','D','None']:
    if rating_group in rating_data:
        if rating_group == "None" and rating_data["None"] == 0:
            continue
        if total == 0:
            print(rating_group, total, str(round(100, 2))+"%")
        else:
            print("{} {} {}%".format(rating_group, rating_data[rating_group], round(100/total*rating_data[rating_group], 2)))