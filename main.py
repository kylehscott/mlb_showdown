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
Pitchers box score
Positional stuff
Save box score to .txt file
Import teams from .txt file
Create more in-depth stats (2B's, 3B's, IBB, etc.)
Replace lineup[bat_pos]
*MAYBE*
Add advanced gameplay (Steals, advancing on flyballs, etc.)
Bunting
Change Var names
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
away_team = "Texas"
home_team = "Toronto"

inning = 0
out = 0
away_score = [0]
home_score = []

bases = ["none", "none", "none"]
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
home_bat_pos = 0
away_bat_pos = 0
score = away_score
# Batter position in lineup
bat_pos = away_bat_pos
y = home_pitcher

bat_box_home = []
bat_box_away = []
pit_box_home = []
pit_box_away = []

# Adds players to box score
for i in home_lineup:
  bat_box_home.append({"ID": i, "PA": 0, "AB": 0, "R": 0, "H": 0, "2B": 0, "3B": 0, "HR": 0, "RBI": 0, "BB": 0, "SO": 0})
for i in away_lineup:
  bat_box_away.append({"ID": i, "PA": 0, "AB": 0, "R": 0, "H": 0, "2B": 0, "3B": 0, "HR": 0, "RBI": 0, "BB": 0, "SO": 0})
pit_box_home.append({"ID": i,})
  
bat_box = bat_box_away

def box_find(ID):
  global bat_box
  for i in range(len(bat_box)):
    if bat_box[i]["ID"] == ID:
      return bat_box[i]

# Possible outcomes for an At-Bat
class Atbat(object):
  
  def __init__(self):
    global bases
    global out
    
  def put_out(self, ID):
    global out
    box_find(ID)["AB"] += 1
    box_find(ID)["PA"] += 1
    out += 1
    print "Outcome: PU"

  def strike_out(self, ID):
    global out
    box_find(ID)["AB"] += 1
    box_find(ID)["SO"] += 1
    box_find(ID)["PA"] += 1
    out += 1
    print "Outcome: SO"
    
  def ground_ball(self, ID):
    global out
    box_find(ID)["AB"] += 1
    box_find(ID)["PA"] += 1
    out += 1
    print "Outcome: GB"
    
  def fly_ball(self, ID):
    global out
    box_find(ID)["AB"] += 1
    box_find(ID)["PA"] += 1
    out += 1
    print "Outcome: FB"
    
  def walk(self, ID):
    box_find(ID)["BB"] += 1
    box_find(ID)["PA"] += 1    
    if bases[2] == "none":
      bases.pop()
      bases.append(ID)
    elif bases [0] != "none" and bases[1] != "none" and bases[2] != "none":
      bases.append(ID)
    elif bases[0] and bases[2] != "none":
      bases.remove("none")
      bases.append(ID)
    elif bases[2] != "none":
      bases.append(ID)
    print "Outcome: BB"

  def single(self, ID):
    box_find(ID)["PA"] += 1
    box_find(ID)["AB"] += 1
    box_find(ID)["H"] += 1
    bases.append(ID)
    print "Outcome: 1B"
    
  def single_plus(self, ID):
    box_find(ID)["PA"] += 1
    box_find(ID)["AB"] += 1
    box_find(ID)["H"] += 1
    bases.extend(["none", ID])
    print "Outcome: 1B+"
  
  def double(self, ID):
    box_find(ID)["PA"] += 1
    box_find(ID)["AB"] += 1
    box_find(ID)["H"] += 1
    box_find(ID)["2B"] += 1      
    bases.extend([ID, "none"])
    print "Outcome: 2B"

  def triple(self, ID):
    box_find(ID)["PA"] += 1
    box_find(ID)["AB"] += 1
    box_find(ID)["H"] += 1
    box_find(ID)["3B"] += 1
    bases.extend([ID, "none", "none"])
    print "Outcome: 3B"
  
  def home_run(self, ID):
    box_find(ID)["PA"] += 1
    box_find(ID)["AB"] += 1
    box_find(ID)["H"] += 1
    box_find(ID)["HR"] += 1
    bases.extend([ID, "none", "none", "none"])
    print "Outcome: HR"
  
ab = Atbat()

# Defines players statline
def player_statline(i):
  print player_name[i], "Stats:", "AB:", box_find(i)["AB"], "R:", box_find(i)["R"], "H:", box_find(i)["H"], "RBI:", box_find(i)["RBI"], "BB:", box_find(i)["BB"], "SO:", box_find(i)["SO"], "PA:", box_find(i)["PA"]

# Roll function to decide what happens during the at bat
def roll_result():
  global out
  cur_bat = lineup[bat_pos]
  roll = random.randint(1,20)
  print "Outcome:", roll
  # Checks to see who gets advantage
  if int(OB[cur_bat]) >= (int(OB[y]) + int(roll)):
    adv = cur_bat
    print "Advantage: Batter"
  else:
    adv = y
    print "Advantage: Pitcher"

  roll = random.randint(1,20)
  print "Roll:", roll

  if int(PU_min[adv]) <= roll <= int(PU_max[adv]):
    ab.put_out(cur_bat)    
    
  elif int(SO_min[adv]) <= roll <= int(SO_max[adv]):
    ab.strike_out(cur_bat)

  elif int(GB_min[adv]) <= roll <= int(GB_max[adv]):
    ab.ground_ball(cur_bat)

  elif int(FB_min[adv]) <= roll <= int(FB_max[adv]):
    ab.fly_ball(cur_bat)

  elif int(BB_min[adv]) <= roll <= int(BB_max[adv]):
    ab.walk(cur_bat)

  elif int(S_min[adv]) <= roll <= int(S_max[adv]):
    ab.single(cur_bat)

  elif int(SP_min[adv]) <= roll <= int(SP_max[adv]):
    ab.single_plus(cur_bat)

  elif int(DB_min[adv]) <= roll <= int(DB_max[adv]):
    ab.double(cur_bat)

  elif int(TR_min[adv]) <= roll <= int(TR_max[adv]):
    ab.triple(cur_bat)

  elif int(HR_min[adv]) <= roll:
    ab.home_run(cur_bat)

# Checks to see if a runner has scored, if so, adds RBI's and Run's to appropiate player
def base_rot(run):
  global score
  global bat_pos
  for i in range(run):
    if bases[0] == "none":
      del bases[0]
    else:
      for i in range(len(bat_box)):
        if bat_box[i]["ID"] == bases[0]:
          bat_box[i]["R"] += 1
      bat_box[bat_pos - 1]["RBI"] += 1
      score[int(inning)] += 1
      del bases[0]

# Running game    
while inning < 9:
  # Checks to see if anyone has scored
  if len(bases) > 3:
    base_rot(len(bases) - 3)
  # Rotates batting order  
  if bat_pos == 9:
    bat_pos = 0
  #Changes sides
  if out == 3 and lineup == away_lineup:
    bases = deque(["none", "none", "none"])
    lineup = home_lineup
    away_bat_pos = bat_pos
    bat_box_away = bat_box
    home_score.append(0)
    bat_pos = home_bat_pos
    y = away_pitcher
    bat_box = bat_box_home
    score = home_score
    out = 0
    inning += 0.5
  elif out == 3 and lineup == home_lineup:
    bases = deque(["none", "none", "none"])
    lineup = away_lineup
    home_bat_pos = bat_pos
    bat_box_home = bat_box
    away_score.append(0)
    bat_pos = away_bat_pos
    y = home_pitcher
    bat_box = bat_box_away
    score = away_score
    out = 0
    inning += 0.5
    

  # Prints info every At-Bat  
  print away_team + ":", sum(away_score)
  print home_team + ":", sum(home_score)
  print "Batter:", player_name[lineup[bat_pos]], "OB:", OB[lineup[bat_pos]], "Pos:", pos[lineup[bat_pos]]
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
  player_statline(lineup[bat_pos - 1])
  print " "

  
  # User input stuff
  comm = raw_input("What would you like to do? ")
  
  # Rolls dice for current AB
  if comm.lower() == "roll":
    roll = random.randint(1,20)
    roll_result()
    print " "
    bat_pos += 1
  
  # Intintial walk
  elif comm.lower() == "walk":
    ab.walk(lineup[bat_pos])
    bat_pos += 1
      
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
    bat_box.insert(lineup_pos + 1, {"ID": i, "PA": 0, "AB": 0, "R": 0, "H": 0, "2B": 0, "3B": 0, "HR": 0, "RBI": 0, "BB": 0, "SO": 0})
    for i in bench:
      if player_name[i].lower() == new_sub.lower():
        bench.remove(i), lineup.insert(lineup_pos, i)
        
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
      for i in range(len(bat_box)):
        player_statline(bat_box[i]["ID"])
        print " "
    elif bxpl.lower() == "bat_box":
      print bat_box
    else: 
      for i in range(len(bat_box)):
        if player_name[bat_box[i]["ID"]].lower() == bxpl.lower():
          player_statline(i)
          print " "
    
  # Ends current session    
  elif comm.lower() == "end":
    break
  # Invalid command  
  else:
    print "Invalid command"