import random
import csv
#testing
my_list = []
x = 81 - 2
y = 51 - 2
f = open('2001.csv')
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

  
roll = random.randint(1,20)

print roll
print "Batter:", no[x], set_name[x], player_name[x], team[x], pts[x], year[x], OB[x], spd[x], pos[x], bat[x]
print "Pitcher:", no[y], set_name[y], player_name[y], team[y], pts[y], year[y], OB[y], spd[y], pos[y], bat[y]
def roll_result(roll):
  if int(OB[x]) <= (int(OB[y]) + int(roll)):
    roll = random.randint(1,20)
    print roll
    if int(PU_min[x]) <= roll <= int(PU_max[x]):
      return "PU"
    elif int(SO_min[x]) <= roll <= int(SO_max[x]):
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
    roll = random.randint(1,20)
    if int(PU_min[y]) <= roll <= int(PU_max[y]):
      return "PU"
    elif int(SO_min[y]) <= roll <= int(SO_max[y]):
      return "SO"
    elif int(GB_min[y]) <= roll <= int(GB_max[y]):
      return "GB"
    elif int(FB_min[y]) <= roll <= int(FB_max[y]):
      return "FB"
    elif int(BB_min[y]) <= roll <= int(BB_max[y]):
      return "BB"
    elif int(S_min[y]) <= roll <= int(S_max[y]):
      return "1B"
    elif int(SP_min[y]) <= roll <= int(SP_max[y]):
      return "1B+"
    elif int(DB_min[y]) <= roll <= int(DB_max[y]):
      return "2B"
    elif int(TR_min[y]) <= roll <= int(TR_max[y]):
      return "3B"
    elif int(HR_min[y]) <= roll:
      return "HR"
    else:
      return "Oops"
    
print roll_result(roll)
