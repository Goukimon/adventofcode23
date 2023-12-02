import string
from tabnanny import check
import time
from enum import Enum

ref = ['one','two','three','four','five','six','seven','eight','nine']

l1 = []
for d in ref :
    l1.append(d[0])

def onlyDigits(s) :
        s = s.strip(string.ascii_lowercase)
        a = s[0]
        b = s[-1]
        print(f"Only digits : {s}")
        if len(s) != 1 :
            return str(a+b)
        else :
            return str(a+a)
        
def isBanned(check,i,s) :
    if len(check) == 3 and len(s)-i >= 5 :
        if ''+s[i+3]+s[i+4] == 'ty' :
            return True
    if len(check) == 3 and len(s)-i >= 7 :
        if ''+s[i+3]+s[i+4]+s[i+5]+s[i+6] == 'teen' :
            return True
    if len(check) == 4 and len(s)-i >= 6 :
        if ''+s[i+4]+s[i+5] == 'ty' :
            return True
    if len(check) == 4 and len(s)-i >= 8 :
        if ''+s[i+4]+s[i+5]+s[i+6]+s[i+7] == 'teen' :
            return True
    if len(check) == 5 and len(s)-i >= 7 :
        if ''+s[i+5]+s[i+6] == 'ty' :
            return True
    if len(check) == 5 and len(s)-i >= 9 :
        if ''+s[i+5]+s[i+6]+s[i+7]+s[i+8] == 'teen' :
            return True
    return False

def noMoreText(s) :

    s = list(s)
    for i in range(len(s)) :
            if s[i] in l1 :
                if len(s)-i >= 3 :
                    check = ''+s[i]+s[i+1]+s[i+2]
                    if check == 'one' :
                        s[i] = '1'
                    if check == 'two' :
                        s[i] = '2'
                    if check == 'six' :
                        s[i] = '6'
                if len(s)-i >= 4 :
                    check = ''+s[i]+s[i+1]+s[i+2]+s[i+3]
                    if check == 'four' :
                        s[i] = '4'
                    if check == 'five' :
                        s[i] = '5'
                    if check == 'nine' :
                        s[i] = '9'
                if len(s)-i >= 5 :
                    check = ''+s[i]+s[i+1]+s[i+2]+s[i+3]+s[i+4]
                    if check == 'three' :
                        s[i] = '3'
                    if check == 'seven' :
                        s[i] = '7'
                    if check == 'eight' :
                        s[i] = '8'

    s = ''.join(s)
    print(f"Post replace : {s}")
    return onlyDigits(s)



#------------------------------------------------------------------------------------------------------------------
with open('input.txt') as f :
    lines = f.readlines()

total = 0

for line in lines :
    line = line.strip('\n')
    print(f"OG line : {line}")
    if ('one' in line) or ('two' in line) or ('three' in line) or ('four' in line) or ('five' in line) or ('six' in line) or ('seven' in line) or ('eight' in line) or ('nine' in line) :
        total += int(noMoreText(line))
    else : 
        total += int(onlyDigits(line))
    print('-------------------------------------')

print(f"Sum of all calibration values, including text values : {total}")
