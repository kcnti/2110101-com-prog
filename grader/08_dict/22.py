total_sale = 0

n = int(input())

ice_cream_list = {}

for i in range(n):
    name, price = input().strip().split()
    ice_cream_list[name] = int(price)

n = int(input())

sales = {}

for i in range(n):
    name, amount = input().strip().split()
    if name in ice_cream_list:
        sale = int(amount)*ice_cream_list[name]
        total_sale += sale
        if name in sales:
            sales[name] += sale
        else:
            sales[name] = sale

if not total_sale:
    print("No ice cream sales")
else:
    print("Total ice cream sales:", float(total_sale))
    top_sale = []
    max_sale = 0
    for i in sales:
        if sales[i] > max_sale:
            max_sale = sales[i]
    for i in sales:
        if sales[i] == max_sale:
            top_sale.append(i)
    print('Top sales:', ', '.join(sorted(top_sale)))