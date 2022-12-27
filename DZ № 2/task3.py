# Даны две строки. Посчитайте сколько раз каждый символ первой строки встречается во второй
# «one» «onetwonine» - o – 2, n – 3, e – 2

string1 = 'one'
string2 = 'onetwonine'
countO = 0
countN = 0
countE = 0
for i in string2: 
    if i == 'o': 
        countO += 1
    elif i == 'n':
        countN += 1
    elif i == 'e':
        countE += 1
print (f'o = {str(countO)}, n = {str(countN)} e = {str(countE)}')