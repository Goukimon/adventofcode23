import string
import time

def check_around(x,y,double_tab):
    top_check = []
    bot_check = []
    mid_check = []

    top_check.append(double_tab[x-1][y-1])
    top_check.append(double_tab[x-1][y])
    top_check.append(double_tab[x-1][y+1])

    bot_check.append(double_tab[x+1][y-1])
    bot_check.append(double_tab[x+1][y])
    bot_check.append(double_tab[x+1][y+1])

    mid_check.append(double_tab[x][y-1])
    mid_check.append(double_tab[x][y])
    mid_check.append(double_tab[x][y+1])

    top_left = [x-1,y-1]
    top_mid = [x-1,y]
    top_right = [x-1,y+1]
    left = [x,y-1]
    mid = [x,y]
    right = [x,y+1]
    bot_left = [x+1,y-1]
    bot_mid = [x+1,y]
    bot_right = [x+1,y-1]

    #places_to_check = ''.join(top_check) + '\n' + ''.join(mid_check) + '\n' + ''.join(bot_check)

    return([top_left,top_mid,top_right],[left,mid,right],[bot_left,bot_mid,bot_right])

def check_left(t,full_engine) :
    val = t[0][1]
    val = 

with open('smol.txt') as f :
    lines = f.readlines()

full_engine = []

for line in lines :
    engine_line = []
    line = line.strip("\n")
    line = list(line)
    for char in line :
        engine_line.append(char)
    
    full_engine.append(engine_line)

#print(full_engine)

for i in range(len(full_engine)) :
    for j in range(len(full_engine[i])) :
        if full_engine[i][j] not in '.'+string.digits :
            print(check_around(i,j,full_engine))

