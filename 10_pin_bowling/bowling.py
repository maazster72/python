"""
This program keeps track of a 10-pin bowling game for a group of players
"""

def check_no_of_players_valid(num):
    if(num < 1):
        return False
    else:
        return True

def set_no_of_players():
    num = int(input("Enter the number of players: "))
    while(check_no_of_players_valid(num) != True):
        num = int(input("Please enter a valid number of players: "))
    else:
        return num

def set_players():
    no_of_players = set_no_of_players()
    players = []
    for i in range(no_of_players):
        player = input("Please enter name of player %s: " % str(i+1))
        player = {"name":player,"score":0,"strike": False,"spare":False}
        players.append(player)
    return players

def set_leaderboard(players):
    players = sorted(players, key=lambda p: p['score'])
    return players

def display_leaderboard(players):
    leaderboard = set_leaderboard(players)
    print("\nLeaderboard")
    print("-----------")
    for i in range(len(leaderboard)):
        display = "{0}. {1} Score: {2}"
        print(display.format(i+1,leaderboard[i]['name'],leaderboard[i]['score']))

def display_frame(num):
    if(num != 10):
        if(num != 1):
            string = "\nFrame #{}"
            string = string.format(num)
            print(string)
            print("---------")
        else:
            print("\nFirst Frame")
            print("---------")
    else:
        print("\nLast Frame")
        print("---------")

def display_player_turn(player):
    player_name = player['name']
    string = '\n* {}\'s turn *'
    string = string.format(player_name)
    print(string)

def check_valid_score(score):
    if(score < 0):
        return False
    else:
        return True
    
def ball(num):
    string = "Ball {}"
    print(string.format(num))
    score = int(input("Enter number of pins knocked down: "))
    while(check_valid_score(int(score)) != True):
        score = int(input("Please enter a valid number: "))
    return score

def frame_normal_roll(player):
    strike = player['strike']
    spare = player['spare']

    score = ball('1')
    if(score != 10):
        score += ball('2')
        if(score == 10):
            spare = True
    else:
        strike = True
    frame_roll = {'score':score,'strike':strike,'spare':spare}
    return frame_roll

def frame(num, players):
    display_frame(num)
    for j in range(len(players)):
        display_player_turn(players[j])
        frame_roll = frame_roll()

def start_game():
    print("\n* Welcome to 10-pin bowling! *\n")

# def frame(player, frame, bonus_strike,bonus_spare,score_prev_round):
#     if(frame != 10):
#         if(bonus_strike):
#             score = score_prev_round
#             for i in range

def main():
    start_game()
    players = set_players()
    display_leaderboard(players)
    for i in range(1,11):
        display_frame(i)
        for j in range(len(players)):
            display_player_turn(players[j])
        display_leaderboard(players)

# def strike():


# def frame_normal(player):
#     score = ball(1)
#     if(score == 10):

# def game(players):


# print(set_players(set_no_of_players()))
#main()
print(frame_normal_roll())