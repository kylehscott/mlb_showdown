import random
import csv

set_year = "2001.csv"
# x = current batter in lineup
x = 81 - 2
y = 51 - 2
f = open(set_year)
csv_f = csv.reader(f)

# x = Player ID
no = []
set_name = []
player_name = []
team = []
pts = []
year = []
OB = []
spd = []
pos = []
bat = []
PU_min = []
PU_max = []
SO_min = []
SO_max = []
GB_min = []
GB_max = []
FB_min = []
FB_max = []
BB_min = []
BB_max = []
S_min = []
S_max = []
SP_min = []
SP_max = []
DB_min = []
DB_max = []
TR_min = []
TR_max = []
HR_min = []
HR_max = []

out = 0
home_score = 0
away_score = 0

#,Set,Name,Team,Pts.,Yr.,OB/C,Spd/IP,Pos,H,PU,SO,GB,FB,W,S,S+,DB,TR,HR

for row in csv_f:
  no.append(row[0])
  set_name.append(row[1])
  player_name.append(row[2])
  team.append(row[3])
  pts.append(row[4])
  year.append(row[5])
  OB.append(row[6])
  spd.append(row[7])
  pos.append(row[8])
  bat.append(row[9])
  PU_min.append(row[10])
  PU_max.append(row[11])
  SO_min.append(row[12])
  SO_max.append(row[13])
  GB_min.append(row[14])
  GB_max.append(row[15])
  FB_min.append(row[16])
  FB_max.append(row[17])
  BB_min.append(row[18])
  BB_max.append(row[19])
  S_min.append(row[20])
  S_max.append(row[21])
  SP_min.append(row[22])
  SP_max.append(row[23])
  DB_min.append(row[24])
  DB_max.append(row[25])
  TR_min.append(row[26])
  TR_max.append(row[27])
  HR_min.append(row[28])
  
opp_lineup = []
lineup = [57, 31, 200, 221, 392, 309, 456, 321, 334]
bench = [400, 320, 420]

x = 0

roll = random.randint(1,20)

#print roll
#print player_name[lineup[x]]
print "Batter:", no[lineup[x]], set_name[lineup[x]], player_name[lineup[x]], team[lineup[x]], pts[lineup[x]], year[lineup[x]], OB[lineup[x]], spd[lineup[x]], pos[lineup[x]], bat[lineup[x]]
print "Pitcher:", no[y], set_name[y], player_name[y], team[y], pts[y], year[y], OB[y], spd[y], pos[y], bat[y]

def roll_result(roll):
  print "Outcome:", roll
  if int(OB[x]) <= (int(OB[y]) + int(roll)):
    # batter roll
    print "Advantage:", player_name[lineup[x]]
    roll = random.randint(1,20)
    print roll
    if int(SO_min[x]) <= roll <= int(SO_max[x]):
      return "SO"
    elif int(GB_min[x]) <= roll <= int(GB_max[x]):
      return "GB"
    elif int(FB_min[x]) <= roll <= int(FB_max[x]):
      return "FB"
    elif int(BB_min[x]) <= roll <= int(BB_max[x]):
      return "BB"
    elif int(S_min[x]) <= roll <= int(S_max[x]):
      return "1B"
    elif int(SP_min[x]) <= roll <= int(SP_max[x]):
      return "1B+"
    elif int(DB_min[x]) <= roll <= int(DB_max[x]):
      return "2B"
    elif int(TR_min[x]) <= roll <= int(TR_max[x]):
      return "3B"
    elif int(HR_min[x]) <= roll:
      return "HR"
    else:
      return "Oops"
  else:
    # pitcher roll
    print "Advantage: ", player_name[lineup[y]]
    roll = random.randint(1,20)
    print roll
    if int(PU_min[y]) <= roll <= int(PU_max[y]):
      return "PU"
      out += 1
    elif int(SO_min[y]) <= roll <= int(SO_max[y]):
      return "SO"
      out += 1
    elif int(GB_min[y]) <= roll <= int(GB_max[y]):
      return "GB"
      out += 1
    elif int(FB_min[y]) <= roll <= int(FB_max[y]):
      return "FB"
      out += 1
    elif int(BB_min[y]) <= roll <= int(BB_max[y]):
      return "BB"
    elif int(S_min[y]) <= roll <= int(S_max[y]):
      return "1B"
    elif int(DB_min[y]) <= roll <= int(DB_max[y]):
      return "2B"
    elif int(HR_min[y]) <= roll:
      return "HR"
    else:
      return "Oops"

comm = raw_input("What would you like to do? ")

if comm =="roll":
  print roll_result(roll)
elif comm == "sub":
  for i in lineup:
    print player_name[i]  
  sub = raw_input("Who would you like to replace? ")
  for i in lineup:
    if player_name[i] == sub:
      lineup.remove(i), bench.append(i)
  for i in bench:
    print player_name[i]
  new_sub = raw_input("Who would you like to put in? ")
  for i in bench:
    if player_name[i] == new_sub:
      bench.remove(i), lineup.append(i)

print "Lineup"
for i in lineup:
    print player_name[i]
print "Bench"
for i in bench:
    print player_name[i] 
    
if x < 8:
  x += 1
else:
  x = 0