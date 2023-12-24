import random as ran
vote_record = {}
evicted = []
HOHs = []
vetos = []
init_noms = []
fin_noms = []



contestants = ['Camila','Diego','Dylan','Madison',
               'Sydney','Eliana','Geoffrey','Evan',
               'Ryan','Faith','Jaeden','Jaden',
               'Gabby','Sara','Kaitlyn','Yogi']

HOH = False
rem_con = contestants[:]
for i in contestants:
    vote_record[i] = []




while len(rem_con)!=3:
    
    #HOH competition    
    HOH_elig = rem_con[:]
    if HOH in HOH_elig:
        HOH_elig.remove(HOH)
    ran.shuffle(HOH_elig)
    HOH = HOH_elig[0]
    HOHs.append(HOH)
    
    #initial nominees
    nom_elig = rem_con[:]
    nom_elig.remove(HOH)
    ran.shuffle(nom_elig)
    noms = nom_elig[0:2]
    init_noms.append(noms)
    
    #veto selection and comp
    veto_play = [HOH]+noms
    elig_veto = rem_con[:]
    ran.shuffle(elig_veto)
    for i in elig_veto:
        if i not in veto_play:
            veto_play.append(i)
            if len(veto_play)==6:
                break
    ran.shuffle(veto_play)
    v_win = veto_play[0]
    vetos.append(v_win)
    
    #veto ceremony and rep nom
    if v_win != HOH:
        #1 = use, 0 = not using
        use = ran.randint(0, 1)
        if (use == 1 and len(rem_con) !=4) or v_win in noms:
            save = v_win
            if v_win in noms:
                noms.remove(v_win)
            else:
                select = ran.randint(0,1)
                save = noms[select]
                noms.remove(save)
            imm = noms + [save] + [v_win]
            ran.shuffle(nom_elig)
            for i in nom_elig:
                if i not in imm:
                    noms.append(i)
                    break
    fin_noms.append(noms)   
    #voting
    vote_num = [0 for i in noms]
    for i in rem_con:
        if i in noms:
            vote_record[i].append('NOM')
        elif i == HOH:
            vote_record[i].append('HOH')
        else:
            vote = ran.randint(0,len(noms)-1)
            vote_num[vote]+=1
            vote_record[i].append(noms[vote])
            
    #HOH vote if tied
    if vote_num[0]==vote_num[1]:
        vote = ran.randint(0,len(noms)-1)
        vote_num[vote]+=1
        vote_record[HOH][-1]= noms[vote]+'*'  
        
    #removes most voted for nominee
    elimdex = vote_num.index(max(vote_num))
    evicted.append(noms[elimdex])
    rem_con.remove(noms[elimdex])
   
#final 3
ran.shuffle(rem_con)
p1_w =  rem_con[0]
p2_players = rem_con[1:3]
ran.shuffle(p2_players)
p2_w = p2_players[0]
p3_players = [p1_w,p2_w]
ran.shuffle(p3_players)
HOH = p3_players[0]
HOHs.append(HOH)
noms = rem_con[:]
noms.remove(HOH)
init_noms.append(noms)

for i in noms:
    vote_record[i].append('NOM')
vote = ran.randint(0,len(noms)-1)
vote_num[vote]+=1
vote_record[HOH].append(noms[vote]+'*')
evicted.append(noms[vote])
rem_con.remove(noms[vote])

#finale
finalist = rem_con[:]
jury_num = len(evicted)//2
if jury_num %2 != 1:
    jury_num += 1
jury = evicted[len(evicted)-jury_num:]

for i in range(len(evicted)):
    if len(vote_record[rem_con[0]])-len(vote_record[evicted[i]]):
        for c in range(len(vote_record[rem_con[0]])-len(vote_record[evicted[i]])):
            vote_record[evicted[i]].append('    ')
            
vote_num = [0 for i in finalist]
for i in jury:
    vote = ran.randint(0,len(finalist)-1)
    vote_num[vote]+=1
    vote_record[i].append(finalist[vote])
            

elimdex = vote_num.index(min(vote_num))
for i in rem_con:
    if i != finalist[elimdex]:
        vote_record[i].append('Winner')
    else:
        vote_record[i].append('Runner-up')
evicted.append(finalist[elimdex])
rem_con.remove(finalist[elimdex])
    
for i in rem_con:
    print("{}:{}".format(i,vote_record[i]))
for i in range(len(evicted)):
    print("{}:{}".format(evicted[-i-1],vote_record[evicted[-i-1]]))

#prep for spreadsheet
final_plac = rem_con
for i in range(len(evicted)):
    final_plac.append(evicted[-i-1])
for i in range(len(evicted)):
    if len(vote_record[final_plac[0]])-len(vote_record[evicted[i]]):
        for c in range(len(vote_record[final_plac[0]])-len(vote_record[evicted[i]])):
            vote_record[evicted[i]].append('    ')

records = [HOHs,init_noms,vetos,fin_noms]
for i in records:
    if len(vote_record[final_plac[0]])-len(i):
        for c in range(len(vote_record[final_plac[0]])-len(i)):
            i.append('    ')        

#make spreadsheet export
from openpyxl import Workbook
from openpyxl.styles import Font, Alignment, PatternFill
wb = Workbook()
sheet = wb.active
episodes = list(range(1,len(vote_record[rem_con[0]])+1))
alphabet = ['B','C','D','E','F','G','H','I','J','K','L','M','N',
            'O','P','Q','R','S','T','U','V','W','X','Y','Z','AA','AB','AC','AC']    

trowFill = PatternFill(start_color='00EAECF0',
                   end_color='00EAECF0',
                   fill_type='solid')
voteFill = PatternFill(start_color='00F8F9Fa',
                   end_color='00F8F9Fa',
                   fill_type='solid')
HOHFill = PatternFill(start_color='00ccffcc',
                   end_color='00ccffcc',
                   fill_type='solid')
nomFill = PatternFill(start_color='00959ffd',
                   end_color='00959ffd',
                   fill_type='solid')
naFill = PatternFill(start_color='00A9A9A9',
                   end_color='00A9A9A9',
                   fill_type='solid')
winnerFill = PatternFill(start_color='0073fb76',
                   end_color='0073fb76',
                   fill_type='solid')
ruFill = PatternFill(start_color='00d1e8ef',
                   end_color='00d1e8ef',
                   fill_type='solid')

sheet["A1"] = "Contestants"
sheet["A2"] = "HOH"
sheet["A3"] = "Nominations (pre-veto)"
sheet["A4"] = "Veto Winner"
sheet["A5"] = "Nominations (post-veto)" 
for i in range(1,6):
    sheet["A{}".format(i)].fill = trowFill
    sheet["A{}".format(i)].font = Font(bold=True)
    sheet["A{}".format(i)].alignment = Alignment(horizontal="center")
rows = {}
columns = {}

for i in range(len(final_plac)):
    rows[final_plac[i]] = i+7
for i in range(len(alphabet)):
    columns[i] = alphabet[i]
    
for i in range(len(episodes)):
    sheet["{}1".format(columns[i])] = "Week {}".format(episodes[i])    
    sheet["{}1".format(columns[i])].fill = trowFill
    sheet["{}1".format(columns[i])].font = Font(bold=True)
    sheet["{}1".format(columns[i])].alignment = Alignment(horizontal="center")
    for c in range(len(records)):
        sheet["{}{}".format(columns[i],c+2)] = str(records[c][i])
        sheet["{}{}".format(columns[i],c+2)].alignment = Alignment(horizontal="center")
        if str(records[c][i]) == '    ':
            sheet["{}{}".format(columns[i],c+2)].fill = naFill
        else:
            sheet["{}{}".format(columns[i],c+2)].fill = voteFill
for i in range(len(final_plac)):
    sheet["A{}".format(rows[final_plac[i]])] = final_plac[i]
    sheet["A{}".format(rows[final_plac[i]])].fill = trowFill
    sheet["A{}".format(rows[final_plac[i]])].font = Font(bold=True)
    sheet["A{}".format(rows[final_plac[i]])].alignment = Alignment(horizontal="center")  
     
    for c in range(len(vote_record[final_plac[i]])):
        sheet["{}{}".format(columns[c],rows[final_plac[i]])] = vote_record[final_plac[i]][c]
        sheet["{}{}".format(columns[c],rows[final_plac[i]])].alignment = Alignment(horizontal="center")
        if vote_record[final_plac[i]][c] == 'NOM':
            sheet["{}{}".format(columns[c],rows[final_plac[i]])].fill = nomFill
        elif vote_record[final_plac[i]][c] == 'HOH' or '*' in vote_record[final_plac[i]][c]:
            sheet["{}{}".format(columns[c],rows[final_plac[i]])].fill = HOHFill
        elif vote_record[final_plac[i]][c] == 'Winner':
            sheet["{}{}".format(columns[c],rows[final_plac[i]])].fill = winnerFill  
            sheet["{}{}".format(columns[c],rows[final_plac[i]])].font = Font(bold=True)  
        elif vote_record[final_plac[i]][c] == 'Runner-up':
            sheet["{}{}".format(columns[c],rows[final_plac[i]])].fill = ruFill              
        elif vote_record[final_plac[i]][c] == '    ':
            sheet["{}{}".format(columns[c],rows[final_plac[i]])].fill = naFill
        else:
            sheet["{}{}".format(columns[c],rows[final_plac[i]])].fill = voteFill    
  
    
    
    
    
wb.save(filename="bbsim.xlsx")    
















