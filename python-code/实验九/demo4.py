def count(string):
    capital=little=digit=other=0
    for i in string:
        if 'A'<=i<='Z':
            capital+=1
        elif 'a'<=i<='z':
            little+=1
        elif '0'<=i<='9':
            digit+=1
        else:
            other+=1
    return(capital,little,digit,other)
s='capital=little=digit=other=0'
print(count(s))