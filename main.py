from collections import deque
import random
import csv

set_year = "2001.csv"
f = open(set_year)
csv_f = csv.reader(f)


#Method for counting total box scores
"""  total_runs = 0
  for r in cur_box:
    s = 0
    global total_runs
    total_runs += cur_box[s]["AB"]
    s += 1
  
  print total_runs"""

#Current function commands
#roll
#sub
#end

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

home_team = "Toronto"
away_team = "Texas"

inning = 0
out = 0
home_score = []
away_score = [0]

bases = deque(["none", "none", "none"])

home_lineup = [99, 82,98, 85, 84, 100, 88, 93, 78]
home_bench = [77, 79, 80, 81]
home_pitcher = 92
home_bullpen = [462, 221]
away_lineup = [546, 529, 525, 542, 534, 526, 528, 530, 532]
away_bench = [531, 539, 540, 544, 545]
away_pitcher = 543
away_bullpen = []
lineup = away_lineup
bench = away_bench
bullpen = home_bullpen
home_x = 0
away_x = 0
score = away_score
x = away_x
y = home_pitcher

bat_box_home = []
bat_box_away = []

for i in home_lineup:
  bat_box_home.append({"ID": i, "AB": 0, "R": 0, "H": 0, "RBI": 0, "BB": 0, "SO": 0, "PA": 0})
for i in away_lineup:
  bat_box_away.append({"ID": i, "AB": 0, "R": 0, "H": 0, "RBI": 0, "BB": 0, "SO": 0, "PA": 0})
  
cur_box = bat_box_away

roll = random.randint(1,20)

#print roll
#print player_name[batt]

def roll_result(roll):
  global out
  print "Outcome:", roll
  if int(OB[lineup[x]]) >= (int(OB[y]) + int(roll)):
    # batter roll
    print "Advantage: Batter"
    roll = random.randint(1,20)
    print "Roll:", roll
    if int(SO_min[lineup[x]]) <= roll <= int(SO_max[lineup[x]]):
      cur_box[x]["AB"] += 1
      cur_box[x]["SO"] += 1
      cur_box[x]["PA"] += 1
      out += 1
      return "Outcome: SO"
    elif int(GB_min[lineup[x]]) <= roll <= int(GB_max[lineup[x]]):
      cur_box[x]["AB"] += 1
      cur_box[x]["PA"] += 1
      out += 1
      return "Outcome: GB"
    elif int(FB_min[lineup[x]]) <= roll <= int(FB_max[lineup[x]]):
      cur_box[x]["AB"] += 1
      cur_box[x]["PA"] += 1
      out += 1
      return "Outcome: FB"
    elif int(BB_min[lineup[x]]) <= roll <= int(BB_max[lineup[x]]):
      cur_box[x]["BB"] += 1
      cur_box[x]["PA"] += 1
      if bases[2] == "none":
        bases.popleft()
        bases.append((lineup[x]))
      else:
        bases.append((lineup[x]))
      return "Outcome: BB"
    elif int(S_min[lineup[x]]) <= roll <= int(S_max[lineup[x]]):
      cur_box[x]["AB"] += 1
      cur_box[x]["H"] += 1
      cur_box[x]["PA"] += 1
      bases.append((lineup[x]))
      return "Outcome: 1B"
    elif int(SP_min[lineup[x]]) <= roll <= int(SP_max[lineup[x]]):
      cur_box[x]["AB"] += 1
      cur_box[x]["H"] += 1
      cur_box[x]["PA"] += 1
      bases.extend(("none", lineup[x]))
      return "Outcome: 1B+"
    elif int(DB_min[lineup[x]]) <= roll <= int(DB_max[lineup[x]]):
      cur_box[x]["AB"] += 1
      cur_box[x]["H"] += 1
      cur_box[x]["PA"] += 1      
      bases.extend((lineup[x], "none"))
      return "Outcome: 2B"
    elif int(TR_min[lineup[x]]) <= roll <= int(TR_max[lineup[x]]):
      cur_box[x]["AB"] += 1
      cur_box[x]["H"] += 1
      cur_box[x]["PA"] += 1
      bases.extend((lineup[x], "none", "none"))
      return "Outcome: 3B"
    elif int(HR_min[lineup[x]]) <= roll:
      cur_box[x]["AB"] += 1
      cur_box[x]["H"] += 1
      cur_box[x]["PA"] += 1
      bases.extend((lineup[x], "none", "none", "none"))
      return "Outcome: HR"
  else:
    # pitcher roll
    print "Advantage: Pitcher"
    roll = random.randint(1,20)
    print "Roll:", roll
    if int(PU_min[y]) <= roll <= int(PU_max[y]):
      cur_box[x]["AB"] += 1
      cur_box[x]["PA"] += 1
      out += 1
      return "Outcome: PU"
    elif int(SO_min[y]) <= roll <= int(SO_max[y]):
      cur_box[x]["AB"] += 1
      cur_box[x]["SO"] += 1
      cur_box[x]["PA"] += 1
      out += 1
      return "Outcome: SO"
    elif int(GB_min[y]) <= roll <= int(GB_max[y]):
      cur_box[x]["AB"] += 1
      cur_box[x]["PA"] += 1
      out += 1
      return "Outcome: GB"
    elif int(FB_min[y]) <= roll <= int(FB_max[y]):
      cur_box[x]["AB"] += 1
      cur_box[x]["PA"] += 1
      out += 1
      return "Outcome: FB"
    elif int(BB_min[lineup[x]]) <= roll <= int(BB_max[lineup[x]]):
      cur_box[x]["BB"] += 1
      cur_box[x]["PA"] += 1
      if bases[2] == "none":
        bases.popleft()
        bases.append((lineup[x]))
      else:
        bases.append((lineup[x]))
      return "Outcome: BB"
    elif int(S_min[lineup[x]]) <= roll <= int(S_max[lineup[x]]):
      cur_box[x]["AB"] += 1
      cur_box[x]["H"] += 1
      cur_box[x]["PA"] += 1
      bases.append((lineup[x]))
      return "Outcome: 1B"
    elif int(DB_min[y]) <= roll <= int(DB_max[y]):
      cur_box[x]["AB"] += 1
      cur_box[x]["H"] += 1
      cur_box[x]["PA"] += 1
      bases.extend((lineup[x], "none"))
      return "Outcome: 2B"
    elif int(HR_min[y]) <= roll:
      cur_box[x]["AB"] += 1
      cur_box[x]["H"] += 1
      cur_box[x]["PA"] += 1
      bases.extend((lineup[x], "none", "none", "none"))
      return "Outcome: HR"

def base_rot(run):
  global score
  global x
  for i in range(run):
    if bases[0] == "none":
      del bases[0]
    else:
      cur_box[run - 1]["R"] += 1
      cur_box[x - 1]["RBI"] += 1
      score[int(inning)] += 1
      del bases[0]

    
while inning < 9:
  if len(bases) > 3:
    base_rot(len(bases) - 3)
  if x == 9:
    x = 0
  if out == 3 and lineup == away_lineup:
    bases = deque(["none", "none", "none"])
    lineup = home_lineup
    away_x = x
    bat_box_away = cur_box
    home_score.append(0)
    x = home_x
    y = away_pitcher
    cur_box = bat_box_home
    score = home_score
    out = 0
    inning += 0.5
  elif out == 3 and lineup == home_lineup:
    bases = deque(["none", "none", "none"])
    lineup = away_lineup
    home_x = x
    bat_box_home = cur_box
    away_score.append(0)
    x = away_x
    y = home_pitcher
    cur_box = bat_box_away
    score = away_score
    out = 0
    inning += 0.5
    

    
  print away_team + ":", sum(away_score)
  print home_team + ":", sum(home_score)
  print "Batter:", player_name[lineup[x]], "OB:", OB[lineup[x]], "Pos:", pos[lineup[x]]
  print "Pitcher:", player_name[y], "Ct:", OB[y]
  print "Inning", int(inning + 1)
  print "Outs", out
  print "Bases: 1st:", bases[2], "2nd:", bases[1], "3rd:", bases[0]
  for run in bases:
    if run != "none":
      print player_name[run]
    elif run == "none":
      print run
  print "Stats:", "AB:", cur_box[x]["AB"], "R:", cur_box[x]["R"], "H:", cur_box[x]["H"], "RBI:", cur_box[x]["RBI"], "BB:", cur_box[x]["BB"], "SO:", cur_box[x]["SO"], "PA:", cur_box[x]["PA"]
  print " "

  

  comm = raw_input("What would you like to do? ")

  if comm.lower() == "roll":
    roll = random.randint(1,20)
    print roll_result(roll)
    print " "
    x += 1
      
  elif comm.lower() == "sub":
    for i in lineup:
      print player_name[i]  
    sub = raw_input("Who would you like to replace? ")
    for i in lineup:
      if player_name[i].lower() == sub.lower():
        lineup_pos = lineup.index(player_name.index(sub))
        lineup.remove(i)
    for i in bench:
      print player_name[i]
    new_sub = raw_input("Who would you like to put in? ")
    for i in bench:
      if player_name[i].lower() == new_sub.lower():
        bench.remove(i), lineup.insert(lineup_pos, i)
        print bench
  #pitching substitute
  elif comm.lower() == "pitch sub":
    print "Current pitcher:", player_name[y]
    print ""
    for i in bullpen:
      print player_name[i]
    sub = raw_input("Who would you like to put in? ")
    for i in bullpen:
      if  sub.lower() == player_name[i].lower():
        home_pitcher = i
        y = home_pitcher
  elif comm.lower() == "box":
    print cur_box
  elif comm.lower() == "end":
    break
  else:
    print "Invalid command"