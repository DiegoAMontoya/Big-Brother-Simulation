import random as ran

contestants = ['Camila','Diego','Dylan','Madison',
               'Sydney','Eliana','Geoffrey','Evan',
               'Ryan','Faith','Jaeden','Jaden',
               'Gabby','Sara','Kaitlyn','Yogi']
vote_record = {}
evicted = []
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
    
    #initial nominees
    nom_elig = rem_con[:]
    nom_elig.remove(HOH)
    ran.shuffle(nom_elig)
    noms = nom_elig[0:2]
 
    veto_play = [HOH]+noms
    elig_veto = rem_con[:]
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

sheet["A1"] = "Contestants"
sheet["A1"].fill = trowFill
sheet["A1"].font = Font(bold=True)
sheet["A1"].alignment = Alignment(horizontal="center")
rows = {}
columns = {}

for i in range(len(final_plac)):
    rows[final_plac[i]] = i+2
for i in range(len(alphabet)):
    columns[i] = alphabet[i]
    
for i in range(len(episodes)):
    sheet["{}1".format(columns[i])] = "Week {}".format(episodes[i])    
    sheet["{}1".format(columns[i])].fill = trowFill
    sheet["{}1".format(columns[i])].font = Font(bold=True)
    sheet["{}1".format(columns[i])].alignment = Alignment(horizontal="center")       
    
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
        elif vote_record[final_plac[i]][c] == '    ':
            sheet["{}{}".format(columns[c],rows[final_plac[i]])].fill = naFill
        else:
            sheet["{}{}".format(columns[c],rows[final_plac[i]])].fill = voteFill    
wb.save(filename="bbsim.xlsx")    
















