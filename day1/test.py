ref = ['one','two','three','four','five','six','seven','eight','nine']

if 'one' in ref :
    print("OK")
else :
    print("KO")

l1 = []
l2 = []
l3 = []
l4 = []
l5 = []
for d in ref :
    l1.append(d[0])
    l2.append(d[0]+d[1])
    l3.append(d[0]+d[1]+d[2])
    if len(d) >= 4 :
        l4.append(d[0]+d[1]+d[2]+d[3])
    if len(d) == 5 :
        l5.append(d[0]+d[1]+d[2]+d[3]+d[4])

for i in range(10) :
    print(i)