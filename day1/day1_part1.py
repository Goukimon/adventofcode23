import string

def onlyDigits(s) :
        s = s.strip('\n').strip(string.ascii_lowercase)
        a = s[0]
        b = s[-1]
        if len(s) != 1 :
            return str(a+b)
        else :
            return str(a+a)

with open('input.txt') as f :
    lines = f.readlines()

total = 0
for line in lines :
    total = total + int(onlyDigits(line))

print(f"Sum of all calibration values : {total}")

