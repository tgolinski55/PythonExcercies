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
    
def array123(nums):
    for i in range(len(nums)):
        if i+2<len(nums):
            if nums[i]==1 and nums[i+1]==2 and nums[i+2]==3:
                return True
    return False
            
def string_match(a, b):
    index = 0
    counter = 0
    if len(a)>len(b):
        index = len(b)
    else:
        index = len(a)
    for i in range(index):
        if i+1 < index:
            if a[i]==b[i] and a[i+1]==b[i+1]:
                counter = counter+1
    return counter

### STRING 1 ###
def hello_name(name):
    return "Hello "+name+"!"

def make_abba(a,b):
    return a+b+b+a

def make_tags(tag, word):
    return "<"+tag+">"+word+"</"+tag+">"

def make_out_word(out, word):
    return out[0]+out[1]+word+out[2]+out[3]

def extra_end(str):
    end = str[-2:]
    return 3*end

def first_two(str):
    if len(str)>2:
        return str[:2]
    else:
        return str    

def first_half(str):
    mid = int(len(str)/2)
    return str[:mid]

def without_end(str):
    mid = str[1:]
    mid = mid[:-1]
    return mid

def combo_string(a,b):
    if len(a)>0 and len(b)>0:
        if len(a)>len(b):
            return b+a+b
        else:
            return a+b+a
    elif len(a)==0:
        return b
    elif len(b)==0:
        return a

def non_start(a, b):
    return a[1:]+b[1:]

def left2(str):
    starts = str[:2]
    return str[2:]+starts

### LIST 1 ###
def first_last6(nums):
    if nums[0]==6 or nums[len(nums)-1]==6:
        return True
    return False

def same_first_last(nums):
    if len(nums)>0:
        first = nums[0]
        last = nums[len(nums)-1]
        if first==last:
            return True
        else:
            return False
    else:
        return False

def make_pi():
    pir = [3,1,4]
    return pir

def common_end(a, b):
    if a[0]==b[0] or a[len(a)-1]==b[len(b)-1]:
        return True
    return False

def sum3(nums):
    sumVal = 0
    for n in range(len(nums)):
        sumVal += nums[n]
    return sumVal

def rotate_left3(nums):
    tempArr = [0,0,0]
    for n in range(len(nums)):
        if n == 0:
            tempArr[1] = nums[len(nums)-1]
        if n+1<=len(nums)-1 and n>0:
            tempArr[0] = nums[n]
        if n == len(nums)-1:
            tempArr[2] = nums[0]
    return tempArr

def reverse3(nums):
    tempArr = [0,0,0]
    for n in range(len(nums)):
        if n == 0:
            tempArr[0] = nums[len(nums)-1]
        if n+1<=len(nums)-1 and n>0:
            tempArr[1] = nums[n]
        if n == len(nums)-1:
            tempArr[2] = nums[0]
    return tempArr

def max_end3(nums):
    tempArr = [nums[0],nums[0],nums[0]]
    if nums[len(nums)-1]>nums[0]:
        tempArr = [nums[len(nums)-1],nums[len(nums)-1],nums[len(nums)-1]]
    return tempArr

def sum2(nums):
    sumVal = 0
    if len(nums)>1:
        return nums[0] + nums[1]
    elif len(nums) == 0:
        return 0
    elif len(nums)<2:
        for n in range(len(nums)):
            sumVal = sumVal + nums[n]
        return sumVal
            
def middle_way(a,b):
    midVal = [a[1],b[1]]
    return midVal

def make_ends(nums):
    first = nums[0]
    last = nums[len(nums)-1]
    tempArr = [first, last]
    return tempArr

def has23(nums):
    for n in range(len(nums)):
        if nums[n] == 2 or nums[n] == 3:
            return True
    return False

def cigar_party(cigars, is_weekend):
    if cigars>=40 and cigars<=60 and not is_weekend:
        return True
    if is_weekend and cigars>=40:
        return True
    return False

def date_fashion(you, date):
    val = 1
    if you>=8 or date>=8:
        val = 2
    if you<=2 or date<=2:
        val = 0
    return val
##Call the method
print(cigar_party(115, True))
