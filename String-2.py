def double_char(str):
    word = ""
    for n in range(len(str)):
        word+=str[n]+str[n]
    return word

print(double_char("Word"))