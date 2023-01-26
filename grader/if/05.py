n = int(input())

number_type = "positive"
state = "even"

if n%2 != 0:
    state = "odd"

if n == 0:
    number_type = "zero"
elif n < 0:
    number_type = "negative"

print(number_type)
print(state)