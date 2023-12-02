import re

with open('input.txt') as f :
    lines = f.readlines()

class Game:
    def __init__(self,id,red,blue,green):
        self.id = id
        self.red = red
        self.blue = blue
        self.green = green

    def __str__(self):
        return f"Game {self.id} : RED {self.red},BLUE {self.blue},GREEN {self.green}"


    def power(self):
        return max(self.red)*max(self.blue)*max(self.green)

gamelist = []

for line in lines :
    line = line.replace(' ','')
    match_id = re.search(r'[0-9]+:',line)
    id = int(match_id.group(0).strip(':'))
    turn_list = line.split(';')

    red = []
    blue = []
    green = []
    
    for turn in turn_list :
        match_blue = re.search(r'[0-9]+b',turn)
        match_red = re.search(r'[0-9]+r',turn)
        match_green = re.search(r'[0-9]+g',turn)
        
        if match_blue == None :
            turn_blue = 0
        else :
            turn_blue = int(match_blue.group(0).strip('b'))
        if match_red == None :
            turn_red = 0
        else :
            turn_red = int(match_red.group(0).strip('r'))
        if match_green == None :
            turn_green = 0
        else :
            turn_green = int(match_green.group(0).strip('g'))
        
        red.append(turn_red)
        blue.append(turn_blue)
        green.append(turn_green)
    
    gamelist.append(Game(id,red,blue,green))

total_power = 0
for game in gamelist :
    total_power += game.power()

print(f"Power of all games : {total_power}")