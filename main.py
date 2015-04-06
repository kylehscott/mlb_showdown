from collections import deque
import csv, random

set_year = "2001.csv"
f = open(set_year)
csv_f = csv.reader(f)

"""
Working commands:
roll
walk
box
sub
pitch sub
end
"""

"""
To-do list:
Fix walks moving runner on 2nd and/or 3rd
Changed Var names
Restructuring "roll_result"
Pitchers box score
Save box score to .txt file
Import teams from .txt file
Create more in-depth stats (2B's, 3B's, IBB, etc.)
Add advanced gameplay (Steals, advancing on flyballs, etc.)
*MAYBE*
Bunting
*LATER*
Building front end graphics
Create pack system
"""

# Player values are stored here
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
# Function to add values from CSV to current game
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
  
  
# Variables for current game
home_team = "Toronto"
away_team = "Texas"

inning = 0
out = 0
home_score = []
away_score = [0]

bases = deque(["none", "none", "none"])
base_term = ["3rd:", "2nd:", "1st:"]

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

# Adds players to box score
for i in home_lineup:
  bat_box_home.append({"ID": i, "AB": 0, "R": 0, "H": 0, "RBI": 0, "BB": 0, "SO": 0, "PA": 0})
for i in away_lineup:
  bat_box_away.append({"ID": i, "AB": 0, "R": 0, "H": 0, "RBI": 0, "BB": 0, "SO": 0, "PA": 0})
  
cur_box = bat_box_away

roll = random.randint(1,20)

# Possible outcomes for an At-Bat
class Atbat(object):
  
  def __init__(self):
    global bases
    global out
    
  def put_out(self, x):
    global out
    cur_box[x]["AB"] += 1
    cur_box[x]["PA"] += 1
    out += 1
    print "Outcome: PU"

  def strike_out(self, x):
    global out
    cur_box[x]["AB"] += 1
    cur_box[x]["SO"] += 1
    cur_box[x]["PA"] += 1
    out += 1
    print "Outcome: SO"
    
  def ground_ball(self, x):
    global out
    cur_box[x]["AB"] += 1
    cur_box[x]["PA"] += 1
    out += 1
    print "Outcome: GB"
    
  def fly_ball(self, x):
    global out
    cur_box[x]["AB"] += 1
    cur_box[x]["PA"] += 1
    out += 1
    print "Outcome: FB"
    
  def walk(self, x):
    cur_box[x]["BB"] += 1
    cur_box[x]["PA"] += 1    
    if bases[2] == "none":
      bases.popleft(2)
      bases.append((lineup[x]))
    elif bases[0] and bases[2] != "none":
      bases.popleft(1)
      bases.append((lineup[x]))
    elif bases[2] != "none":
      bases.append((lineup[x]))
    print "Outcome: BB"

  def single(self, x):
    cur_box[x]["AB"] += 1
    cur_box[x]["H"] += 1
    cur_box[x]["PA"] += 1
    bases.append((lineup[x]))
    print "Outcome: 1B"
    
  def single_plus(self, x):
    cur_box[x]["AB"] += 1
    cur_box[x]["H"] += 1
    cur_box[x]["PA"] += 1
    bases.extend(("none", lineup[x]))
    print "Outcome: 1B+"
  
  def double(self, x):
    cur_box[x]["AB"] += 1
    cur_box[x]["H"] += 1
    cur_box[x]["PA"] += 1      
    bases.extend((lineup[x], "none"))
    print "Outcome: 2B"

  def triple(self, x):
    cur_box[x]["AB"] += 1
    cur_box[x]["H"] += 1
    cur_box[x]["PA"] += 1
    bases.extend((lineup[x], "none", "none"))
    print "Outcome: 3B"
  
  def home_run(self, x):
    cur_box[x]["AB"] += 1
    cur_box[x]["H"] += 1
    cur_box[x]["PA"] += 1
    bases.extend((lineup[x], "none", "none", "none"))
    print "Outcome: HR"
  
ab = Atbat()

# Defines players statline
def player_statline(i):
  print player_name[lineup[i]], "Stats:", "AB:", cur_box[i]["AB"], "R:", cur_box[i]["R"], "H:", cur_box[i]["H"], "RBI:", cur_box[i]["RBI"], "BB:", cur_box[i]["BB"], "SO:", cur_box[i]["SO"], "PA:", cur_box[i]["PA"]

#Idea on how to improve
"""Pass pitcher or batter through function. IF x == pitcher, PU is used, ELIF x == batter, 3B, etc. is used"""
# Roll function to decide what happens during the at bat
def roll_result(roll):
  global out
  cur_bat = lineup[x]
  print "Outcome:", roll
  # Checks to see who gets advantage
  if int(OB[lineup[x]]) >= (int(OB[y]) + int(roll)):
    # batter roll
    print "Advantage: Batter"
    roll = random.randint(1,20)
    print "Roll:", roll

    if int(SO_min[cur_bat]) <= roll <= int(SO_max[cur_bat]):
      ab.strike_out(x)

    elif int(GB_min[cur_bat]) <= roll <= int(GB_max[cur_bat]):
      ab.ground_ball(x)

    elif int(FB_min[cur_bat]) <= roll <= int(FB_max[cur_bat]):
      ab.fly_ball(x)

    elif int(BB_min[cur_bat]) <= roll <= int(BB_max[cur_bat]):
      ab.walk(x)

    elif int(S_min[cur_bat]) <= roll <= int(S_max[cur_bat]):
      ab.single(x)

    elif int(SP_min[cur_bat]) <= roll <= int(SP_max[cur_bat]):
      ab.single_plus(x)

    elif int(DB_min[cur_bat]) <= roll <= int(DB_max[cur_bat]):
      ab.double(x)

    elif int(TR_min[cur_bat]) <= roll <= int(TR_max[cur_bat]):
      ab.triple(x)

    elif int(HR_min[cur_bat]) <= roll:
      ab.home_run(x)
    
  else:
    # pitcher roll
    print "Advantage: Pitcher"
    roll = random.randint(1,20)
    print "Roll:", roll

    if int(PU_min[y]) <= roll <= int(PU_max[y]):
      ab.put_out(x)
    
    elif int(SO_min[y]) <= roll <= int(SO_max[y]):
      ab.strike_out(x)

    elif int(GB_min[y]) <= roll <= int(GB_max[y]):
      ab.ground_ball(x)

    elif int(FB_min[y]) <= roll <= int(FB_max[y]):
      ab.fly_ball(x)

    elif int(BB_min[y]) <= roll <= int(BB_max[y]):
      ab.walk(x)

    elif int(S_min[y]) <= roll <= int(S_max[y]):
      ab.single(x)

    elif int(DB_min[y]) <= roll <= int(DB_max[y]):
      ab.double(x)

    elif int(TR_min[y]) <= roll <= int(TR_max[y]):
      ab.triple(x)

    elif int(HR_min[y]) <= roll:
      ab.home_run(x)

# Checks to see if a runner has scored, if so, adds RBI's and Run's to appropiate player
def base_rot(run):
  global score
  global x
  for i in range(run):
    if bases[0] == "none":
      del bases[0]
    else:
      for i in range(len(cur_box)):
        if cur_box[i]["ID"] == bases[0]:
          cur_box[i]["R"] += 1
      cur_box[x - 1]["RBI"] += 1
      score[int(inning)] += 1
      del bases[0]

# Running game    
while inning < 9:
  # Checks to see if anyone has scored
  if len(bases) > 3:
    base_rot(len(bases) - 3)
  # Rotates batting order  
  if x == 9:
    x = 0
  #Changes sides
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
    

  # Prints info every At-Bat  
  print away_team + ":", sum(away_score)
  print home_team + ":", sum(home_score)
  print "Batter:", player_name[lineup[x]], "OB:", OB[lineup[x]], "Pos:", pos[lineup[x]]
  print "Pitcher:", player_name[y], "Ct:", OB[y]
  print "Inning", int(inning + 1)
  print "Outs", out
  print "Bases: 1st:"

  # Prints who's on base
  for i in range(2, -1, -1):
    if bases[i] != "none":
      print base_term[i], player_name[int(bases[i])],
    else:
      print base_term[i], "none",

  # Prints game stats for current player
  print " "
  player_statline(x - 1)
  print " "

  
  # User input stuff
  comm = raw_input("What would you like to do? ")
  
  # Rolls dice for current AB
  if comm.lower() == "roll":
    roll = random.randint(1,20)
    roll_result(roll)
    print " "
    x += 1
  
  # Intintial walk
  elif comm.lower() == "walk":
    ab.walk(x)
      
  # Batter substitution    
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
        
  # pitching substitute
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
    bxpl = raw_input("Input player name: ")
    if bxpl.lower() == "all":
      for i in range(len(cur_box)):
        player_statline(i)
        print " "
    else: 
      for i in range(len(cur_box)):
        if player_name[cur_box[i]["ID"]].lower() == bxpl.lower():
          player_statline(i)
          print " "
    
  # Ends current session    
  elif comm.lower() == "end":
    break
  # Invalid command  
  else:
    print "Invalid command"