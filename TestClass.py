def Welcome():
    return print("This is going to be an amazing adventure!")

def sleep_in(weekday, vacation):
    if not weekday or vacation:
        return True
    else:
        return False

def monkey_trouble(a_smile, b_smile):
    if a_smile and b_smile:
        return True
    elif not a_smile and not b_smile:
        return True
    else:
        return False

def sum_double(a, b):
    if not a == b:
        return a+b
    else:
        return 2*(a+b)

##Call the method
print(sum_double(2,2))
    
