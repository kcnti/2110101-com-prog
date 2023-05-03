star2movies = {} 
n = int(input()) 
for i in range(n): 
    title, star1, star2 = input().split(",") 
    title = title.strip(); star1 = star1.strip(); star2 = star2.strip() 
    if star1 in star2movies:
        star2movies[star1].append(title)
    elif not star1 in star2movies:
        star2movies[star1] = [title]

    if star2 in star2movies:
        star2movies[star2].append(title)
    elif not star2 in star2movies:
        star2movies[star2] = [title]

stars = [e.strip() for e in input().split(",")] # read the last input line
for star in stars:
    if star in star2movies: 
        print(star, "->", ", ".join(star2movies[star]))
    else: 
        print(star, "->", "Not found") 