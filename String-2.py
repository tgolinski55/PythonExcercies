def double_char(str):
    word = ""
    for n in range(len(str)):
        word+=str[n]+str[n]
    return word

def count_hi(str):
    count = 0
    for n in range(len(str)-1):
        if str[n]=="h" and str[n+1]=="i":
            count += 1
    return count

def cat_dog(str):
    catCount = 0
    dogCount = 0
    for i in range(len(str)-2):
        if str[i:i+3]=="cat":
            catCount += 1
        if str[i:i+3]=="dog":
            dogCount += 1
    if catCount == dogCount:
        return True
    else:
        return False

# Return the number of times that the string "code" appears anywhere in the given string, except we'll accept any letter for the 'd', so "cope" and "cooe" count.

# count_code('aaacodebbb') → 1
# count_code('codexxcode') → 2
# count_code('cozexxcope') → 2

def count_code(str):
    countStr = 0
    for i in range(len(str)-3):
        if str[i:i+2]=="co" and str[i+3]=="e":
            countStr += 1
    return countStr

print(count_code("cozexxcope"))