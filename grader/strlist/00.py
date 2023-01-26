def get_id_info(id):
    year = id//100000000
    group = (id%100000000)//10000000
    running_number = (id%10000000)//1000
    faculty_code = id%100
    return year, group, running_number, faculty_code

print(get_id_info(6532018321))
