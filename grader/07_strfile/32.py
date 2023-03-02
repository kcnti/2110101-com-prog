def no_lowercase(t): # return True if no lowercase, otherwise return False 
    return False if [i for i in t if i.islower()] else True
 
def no_uppercase(t): 
    return False if [i for i in t if i.isupper()] else True
 
def no_number(t): 
    return False if [i for i in t if i.isdigit()] else True
 
def no_symbol(t): 
    return False if [i for i in t if not i.isalnum()] else True
 
def character_repetition(t): 
    return True if [i for i in range(len(t)-3) if t[i:i+4].count(t[i]) == 4] else False
 
def number_sequence(t): 
    import string
    nums = string.digits + '0'
    rev_nums = nums[::-1]
    for i in range(len(t)-3):
        if t[i:i+4].lower() in nums or t[i:i+4].lower() in rev_nums:
            return True
    return False
 
def letter_sequence(t):
    import string
    alphabet = string.ascii_lowercase
    rev_alphabet = alphabet[::-1]
    for i in range(len(t)-3):
        if t[i:i+4].lower() in alphabet or t[i:i+4].lower() in rev_alphabet:
            return True
    return False
 
def keyboard_pattern(t):
    keyboard = '!@#$%^&*()_+\nqwertyuiop\nasdfghjkl\nzxcvbnm'
    for i in range(len(t)-3):
        if t[i:i+4].lower() in keyboard:
            return True
    for i in range(len(t)-3):
        if t[i:i+4].lower() in keyboard[::-1]:
            return True
    return False
 
#----------------------------- 
passw = input().strip() 
errors = [] 
if len(passw) < 8: 
    errors.append("Less than 8 characters") 
 
if no_lowercase(passw): 
    errors.append("No lowercase letters") 
 
if no_uppercase(passw): 
    errors.append("No uppercase letters")

if no_number(passw):
    errors.append("No numbers") 

if no_symbol(passw):
    errors.append("No symbols")

if character_repetition(passw):
    errors.append("Character repetition")

if number_sequence(passw):
    errors.append("Number sequence")

if letter_sequence(passw):
    errors.append("Letter sequence")

if keyboard_pattern(passw):
    errors.append("Keyboard pattern")
 
if len(errors) == 0: 
    print("OK")
else: 
    print('\n'.join(errors))