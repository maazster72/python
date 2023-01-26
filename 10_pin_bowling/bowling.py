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
        player = {"name":player,"score":0}
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
    


def ball(num):
    string = "Ball {}"
    print(string.format(num))
    score = input("Enter number of pins knocked down: ")
    return score

def start_game():
    print("\n* Welcome to 10-pin bowling! *\n")

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
main()