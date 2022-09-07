# Do not modify these lines
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__winc_id__ = '71dd124b4a6e4d268f5973db521394ee'
__human_name__ = 'strings'

# Add your code after this line
# 1 players that scored
player_1 = 'Ruud Gullit'
player_2 = 'Marco van Basten'
# 2 goals that scored
goal_0= 32
goal_1 = 54
# 3 scorers
scorers = player_1 + " " + str(goal_0) + ", "  + player_2 + " " + str(goal_1)
print(scorers)
# 4 Report
report = player_1 + ' scored in the ' + str(goal_0) + "nd minute" "\n" + player_2 + " scored in the " + str(goal_1) + "th minute"
print(report)
# Part 2
# 1 variable player
player = 'Jan Wouters'
# 2 first name and find method
find_space = player.find(" ")
first_name = player [0:find_space]
print(first_name)
# 3 last name len, find, len
last_name_len = len (player [player.find(" ") + 1:])
print(last_name_len)
# 4 isolate name short
name_short = player[0: 1] + '.' + player[player.find(" "):]
print(name_short)
# 5 chant
chant0 = (first_name + '!' + ' ') * len(first_name)
chant = chant0.strip ( )
print(chant)
# 6 good_chant
good_chant = True
chant ==  "jan! + jan! + jan! + jan! + jan!"