import random as ran
import time
#elim
#race
#time
def veto(players):
    vtype =ran.randint(0,2)
    if vtype == 0:
        r_players = players
        roundnum = 0
        input("Each round, one person will be eliminated until there is one person remaining.\n")
        while True:
            roundnum +=1
            ran.shuffle(r_players)
            input("Round {}: {} has been eliminated.\n".format(roundnum,r_players[-1]))
            r_players = r_players[:-1]
            if len(r_players)==1:
                return r_players[0]
            
    elif vtype == 1:
        input("The players will race to collect pieces to put spell out the answer to a riddle.\n")
        ran.shuffle(players)
        return(players[0])
    
    elif vtype == 2:
        input("The players will individually race to find the differences between multiple pictures.\n")
        times = {}
        rawtime = []
        for i in players:
            while True:
                ptime = ran.randint(90,1200)
                if ptime not in rawtime:
                    rawtime.append(ptime)
                    times[ptime] = i
                    break
        ran.shuffle(rawtime)
        for i in rawtime:
            input("{} finishes with a time of {} minutes and {} seconds.\n".format(times[i],i//60,i%60))
        return times[min(rawtime)]
                    
                    
            
            
            