months = {
    "1": "January",
    "2": "February",
    "3": "March",
    "4": "April",
    "5": "May",
    "6": "June",
    "7": "July",
    "8": "August",
    "9": "September",
    "10": "October",
    "11": "November",
    "12": "December",
}

n = input().split('/')
d, m, y = n[0], months[n[1]], n[2]

print("{} {}, {}".format(m, d, y))