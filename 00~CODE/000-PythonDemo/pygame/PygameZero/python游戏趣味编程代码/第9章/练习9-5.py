def printStars(n,m,ch):
    str = ''    
    for i in range(m):
        str = str + ch
    for i in range(n):
        print(str)

printStars(2,4, '+')
printStars(3,6, '@')