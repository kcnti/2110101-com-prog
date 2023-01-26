def is_mobile_number(number):

    initnumber = ['06', '08', '09']

    if not number[:2] in initnumber or len(number) != 10:
        return False
    else:
        return True

exec(input())