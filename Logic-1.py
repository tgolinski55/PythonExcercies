def caught_speeding(speed, is_birthday):
    if is_birthday:
        if speed>65 and speed<=85:
            return 1
        if speed>=85:
            return 2
        if speed<=65:
            return 0
    else:
        if speed>60 and speed<=80:
            return 1
        if speed>80:
            return 2
        if speed<=60:
            return 0

def sorta_sum(a, b):
    sumVal = a+b
    if sumVal>=10 and sumVal<=19:
        return 20
    else:
        return sumVal
    
def alarm_clock(day, vacation):
    if vacation:
        if not day==0 and not day==6:
            return "10:00"
        else:
            return "off"
    else:
        if not day==0 and not day==6:
            return "7:00"
        else:
            return "10:00"

def love6(a, b):
    if a==6 or b==6:
        return True
    if abs(a-b)==6 or a+b==6:
        return True
    return False

def in1to10(n, outside_mode):
    if outside_mode:
        return (n<=1 or n>=10)
    else:
        return (n>=1 and n<=10)

def near_ten(num):
    vale = num%10
    if 10-vale <=2 or abs(vale-10) <=2 or vale<=2:
        return True
    return False