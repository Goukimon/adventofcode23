import string
import time
from enum import Enum

ref = ['one','two','three','four','five','six','seven','eight','nine']
unique_chrs = {'t', 'w', 's', 'i', 'x', 'g', 'u', 'h', 'n', 'e', 'f', 'o', 'v', 'r'}

def onlyDigits(s) :
        s = s.strip(string.ascii_lowercase)
        a = s[0]
        b = s[-1]
        print(f"Only digits : {s}")
        if len(s) != 1 :
            return str(a+b)
        else :
            return str(a+a)

def noMoreText(s) :

    indices1 = s.index(ref[0])
    indices2 = s.index(ref[1])
    indices3 = s.index(ref[2])
    indices4 = s.index(ref[3])
    indices5 = s.index(ref[4])
    indices6 = s.index(ref[5])
    indices7 = s.index(ref[6])
    indices8 = s.index(ref[7])
    indices9 = s.index(ref[8])

    # Avancer dans la string.
    # Si caractère hors de l'ensemble : delete le buffer.
    # Si caractere dans l'ensemble : add to buffer, add next one.
    # Quand buffersize == 3, commencer les checks pour remplacer
    # Si on atteint les critiques, checks les x suivants pour voir si ty ou teen existe.

    """
    s = s.replace('one','1')
    s = s.replace('two','2')
    s = s.replace('three','3')
    s = s.replace('five','5')
    s = s.replace('four','4')
    s = s.replace('six','6')
    s = s.replace('seven','7')
    s = s.replace('nine','9')
    s = s.replace('eight','8')
    s = s.replace('4ty','')
    s = s.replace('4teen','')
    s = s.replace('4ty','')
    s = s.replace('4teen','')
    s = s.replace('6ty','')
    s = s.replace('6teen','')
    s = s.replace('7ty','')
    s = s.replace('7teen','')
    s = s.replace('9ty','')
    s = s.replace('9teen','')
    s = s.replace('8y','')
    s = s.replace('8een','')
    """
    print(f"Post replace : {s}")
    return 0
    #return onlyDigits(s)



#------------------------------------------------------------------------------------------------------------------
with open('smol.txt') as f :
    lines = f.readlines()

total = 0

tout = ''.join(ref)
allchars = set(list(tout))
print(allchars)

for line in lines :
    line = line.strip('\n')
    print(f"OG line : {line}")
    if ('one' in line) or ('two' in line) or ('three' in line) or ('four' in line) or ('five' in line) or ('six' in line) or ('seven' in line) or ('eight' in line) or ('nine' in line) :
        total = total + int(noMoreText(line))
    else : 
        total = total + int(onlyDigits(line))
    print('-------------------------------------')
    time.sleep(3)

print(f"Sum of all calibration values, including text values : {total}")

#53655 is too low
