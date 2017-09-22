import json
from urllib.request import urlopen

players = json.load(urlopen('http://frisbeer.win/frisbeer/API/players'))
games = json.load(urlopen('http://frisbeer.win/frisbeer/API/games'))

def score(game, pId):
    player = 0
    score = 0
    if game["team1_score"] == 1 or game["team2_score"] == 1:
        score = 1
    if pId in game["team1"] and (game["team1_score"] > game["team2_score"]):
        player = 1
    elif pId in game["team2"] and (game["team1_score"] < game["team2_score"]):
        player = 1
    return player, score

names = {}
total_games = 0
rounds3 = 0
rounds2 = 0

for game in games:
        total_games += 1
        if game["team1_score"] == 1 or game["team2_score"] == 1:
            rounds3 += 1
        else:
            rounds2 += 1

prosentage = 0
for player in players:
        names[player["name"]] = player["id"]
        victory = 0
        played = 0
        for game in games:
            if player["id"] in game["team1"] or player["id"] in game["team2"]:
                played += 1
                res, trash= score(game, player["id"])
                victory += res
        if played != 0:
            prosentage += round(victory / played, 3) * 100

prosentage = round(prosentage / len(names), 1)

print("Total amount of games played is {}".format(total_games))
print("Avarage win prosentage is {} %".format(prosentage))
print("{} % or {} of games played lasted 3 rounds\n\n".format(int(round(rounds3 / total_games, 2) * 100), rounds3))


while 1:
    name = input("Give name. (q to exit): ")
    if name in names:
        played = 0
        won = 0
        won3 = 0
        pRounds3 = 0
        pId = names[name]
        for game in games:
            if pId in game["team1"] or pId in game["team2"]:
                played += 1
                result, third = score(game, pId)
                if result == 1:
                    won += 1
                    won3 += third
                    pRounds3 += third
                else:
                    pRounds3 += third
        print("Games played by {}: {}".format(name, played))
        if played != 0:
            print("Games won: {} ({} %)\nThird rounds played: {}\nThird rounds won: {}\n\n".format(won, int(round(won/played,2)*100), pRounds3, won3))
        else:
            print("\n\n")

    elif name == "q":
        break
    else:
        print("Bad name\n\n")
