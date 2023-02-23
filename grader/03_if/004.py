n = input()
initnumber = ['06', '08', '09']

error = 'Not a mobile number'
success = 'Mobile number'

if not n[:2] in initnumber or len(n) != 10:
    print(error)
else:
    print(success)
