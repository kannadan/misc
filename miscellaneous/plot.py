# -*- coding: utf-8 -*-
import json
from urllib.request import urlopen
from yattag import Doc, indent
import numpy as np
import codecs

doc, tag, text = Doc().tagtext()

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

total_games = 0
rounds3 = 0

for game in games:
        total_games += 1
        if game["team1_score"] == 1 or game["team2_score"] == 1:
            rounds3 += 1

playerList = []

for player in players:
    stats = [0, 0, 0, 0, 0, 0] # [played, won, played third round, won on third round, rounds played, rounds won]
    pId = player["id"]

    for game in games:
        if pId in game["team1"] or pId in game["team2"]:
            stats[0] += 1
            result, third = score(game, pId)
            if result == 1:
                stats[1] += 1
                stats[2] += third
                stats[3] += third
            else:
                stats[2] += third
            if third == 1:
                stats[4] += 3
                if result == 1:
                    stats[5] += 2
                else:
                    stats[5] += 1
            else:
                stats[4] += 2
                if result == 1:
                    stats[5] += 2
                else:
                    stats[5] += 0
    if stats[4] != 0:
        stats.append(round((stats[5]/stats[4])*100, 1))
    else:
        stats.append(0)
    stats.insert(0, player["score"])
    stats.insert(0, player["rank"])
    stats.insert(0, player["name"])
    #[name, rank, score, played, won, played third round, won on third round, rounds played, rounds won, rounds won %]
    if stats[3] != 0:
        stats.insert(5, round((stats[4]/stats[3]) * 100, 1))
    else:
        stats.insert(5, 0)
    #[name, rank, score, played, won, win %, played third round, won on third round, rounds played, rounds won, rounds won %]
    playerList.append(stats)
prosentage = 0
prosTotal = 0

for player in playerList:
    if player[3] > 4:
        prosentage += player[5]
        prosTotal += 1
prosentage = round(prosentage / prosTotal, 1)
beerTotal = rounds3*8*6 + (total_games - rounds3)*8*4
playerList = sorted(playerList, key = lambda x: int(x[2]))[::-1]
playerTotal = len(playerList)


file = codecs.open("tilasto.html", "w", encoding='utf8')
file.write("<!doctype html>\n\n")

with tag("html"):
    with tag("head"):
        with tag("meta", charset="utf-8"):
            pass
        with tag("title"):
            text("Tilastot")
    with tag("body"):
        with tag("h1"):
            text("Frisbeer kauden 2017 tilastoja")
        with tag("h2"):
            text("Pelejä on pelattu: {}".format(total_games))
        with tag("h2"):
            text("Kaljoja on tuhottu: {}".format(beerTotal))
        with tag("h2"):
            text("Rekisteröityjä pelaajia oli yhteensä: {}".format(playerTotal))
        with tag("h2"):
            text("Kolmanteen erään meni {} peliä".format(rounds3))
        with tag("h2"):
            text("Keskiarvoinen voittoprosentti yli neljä peliä pelanneilla oli {} %".format(prosentage))
        with tag("table", border="1"):
            with tag("tr"):
                #[name, rank, score, played, won, win %, played third round, won on third round, rounds played, rounds won, rounds won %]
                with tag("th"):
                    text("Name")
                with tag("th"):
                    text("Rank")
                with tag("th"):
                    text("Score")
                with tag("th"):
                    text("Played")
                with tag("th"):
                    text("Won")
                with tag("th"):
                    text("Win %")
                with tag("th"):
                    text("Played on a third round")
                with tag("th"):
                    text("Won on a third round")
                with tag("th"):
                    text("Rounds played")
                with tag("th"):
                    text("Rounds won")
                with tag("th"):
                    text("% of rounds won")
            for player in playerList:
                with tag("tr"):
                    for value in player:
                        with tag("td"):
                            text(value)

file.write(indent(doc.getvalue()))
file.close()
