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

print(count_hi("WordHihihihihihHi"))