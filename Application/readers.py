import json

time_d = {}
players_d = {}


def read_time():
    global time_d
    file = open('Data/time.json')
    time_d = json.load(file)


def read_players():
    global players_d
    file = open('Data/players.json')
    players_d = json.load(file)


def write_time():
    global time_d
    with open('Data/time.json', 'w') as outfile:
        json.dump(time_d, outfile)


def write_players():
    global players_d
    with open('Data/players.json', 'w') as outfile:
        json.dump(players_d, outfile)
