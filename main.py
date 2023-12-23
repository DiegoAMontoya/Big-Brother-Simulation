import random as ran

contestants = ['Camila','Diego','Dylan','Madison','Sydney','Eliana','Geoffrey','Evan','Ryan','Faith','Jaeden','Jaden','Gabby','Sara','Kaitlyn','Yogi']
vote_record = {}
evicted = []
HOH = False
rem_con = contestants[:]
for i in range(len(contestants)):
    vote_record[contestants[i]] = []

while len(rem_con)!=3:
    
    #HOH competition    
    HOH_elig = rem_con[:]
    if HOH in HOH_elig:
        HOH_elig.remove(HOH)
    ran.shuffle(HOH_elig)
    HOH = HOH_elig[0]
    
    #initial nominees
    nom_elig = rem_con[:]
    nom_elig.remove(HOH)
    ran.shuffle(nom_elig)
    noms = nom_elig[0:2]
    
    #voting
    
    

