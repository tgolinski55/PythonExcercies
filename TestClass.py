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

def diff21(n):
    if n<=21:
        return 21-n
    else:
        return -2*(21-n)

def parrot_trouble(talking, hour):
    if talking and (hour<7 or hour>20):
        return True
    else:
        return False

def makes10(a, b):
    if a ==10 or b == 10:
        return True
    elif a+b==10:
        return True
    else:
        return False

def near_hundred(n):
    if abs(100-n)<=10:
        return True
    elif abs(200-n)<=10:
        return True
    else:
        return False     

def pos_neg(a, b, negative):
    if negative and a<=0 and b<=0:
        return True
    elif not negative and ((a>0 and b<=0) or (a<=0 and b>0)):
        return True
    else:
        return False
        
def not_string(str):
    if str.startswith("not"):
        return str
    else:
        return "not "+str

def array_front9(nums):
    index = len(nums)
    if index > 4:
        index = 4
    for i in range(index):
      if nums[i]==9:
        return True
    return False
    


##Call the method
print(array_front9({1,2,3,4}))
