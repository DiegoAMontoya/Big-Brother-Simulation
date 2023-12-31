import random as ran
import time
#elim/wall
#race
#craphoot
#quiz
#head to head
def hoh(players):
    htype =ran.randint(0,3)
    if htype == 0:
        r_players = players
        input("The players will hold onto a button as long as they can. The last person standing wins.\n")
        while True:
            ran.shuffle(r_players)
            input("{}. {} has been eliminated.\n".format(len(r_players),r_players[-1]))
            r_players = r_players[:-1]
            if len(r_players)==1:
                return r_players[0]
            
    elif htype == 1:
        input("The players will race to find items hidden in a ball pit.\n")
        ran.shuffle(players)
        return(players[0])
    
    elif htype == 2:
        input("The players will hit a ball down a ramp to earn points. The highest point value wins.\n")
        scores = {}
        rawscore = []
        for i in players:
            while True:
                pscore = ran.randint(1,50)
                if pscore not in rawscore:
                    rawscore.append(pscore)
                    scores[pscore] = i
                    break
        ran.shuffle(rawscore)
        for i in rawscore:
            input("{} scored {} points.\n".format(scores[i],i))
        return scores[max(rawscore)]
    elif htype == 3:
        input("The players will watch a video and answer true/false questions about it. The last person standing wins.\n")
        r_players = players
        qnum = 0
        while True:
            qnum +=1
            print("Question {}:\n".format(qnum))
            right = []
            wrong = []
            answer = {}
            for i in r_players:
                answer[i] = ran.randint(1,5)
            ran.shuffle(r_players)            
            answer[r_players[0]] = 5 #ensure at least 1 person is right
            r_players.sort()
            for i in r_players:
                if answer[i] >= 3:
                    right.append(i)
                else:
                    wrong.append(i)
            print("{} answered correctly.\n".format(right))
            if len(wrong) == 0:
                input("We move on to the next question.\n")
            else:
                input("{} has been eliminated.\n".format(wrong))
            for i in wrong:
                r_players.remove(i)
            if len(r_players)==1:
                return r_players[0]
            
        
        