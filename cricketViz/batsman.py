import matplotlib.pyplot as plt
import pandas as pd
from cric import inningData

def batsmanData(inningNum):
    innings = inningData(inningNum)
    batted = []
    for i, name in enumerate(innings.striker):
        if (i == 0):
            batted.append(name)
        else:
            if(name in batted):
                pass
            else:
                batted.append(name)

    for i, name in enumerate(innings.non_striker):
        if(name in batted):
            pass
        else:
            batted.append(name)

    wides = innings.wides.isnull()
    noballs = innings.noballs.isnull()
    
    extraBool = []
    for i in range(innings.score.count()):
        if (wides[i] == False or noballs[i] == False):
            extraBool.append(True)
        else:
            extraBool.append(False)

    innings['extraBool'] = extraBool
    
    battedStats = {}
    ball = []
    for name in batted:
        runs = 0
        balls = 0
        for i in range(innings.runs.count()):
            if (name == innings.striker[i]):
                runs += innings.runs_off_bat[i]

                if(innings.extraBool[i] == False):
                    balls += 1
        battedStats[f'{name}'] = runs
        ball.append(balls)
            
    batsmanData = pd.DataFrame(list(battedStats.items()), columns = ['batsman', 'runs'])
    
    batsmanData['balls_played'] = ball
    batsmanData['sr'] = (batsmanData.runs/batsmanData.balls_played)*100
    for i in range(batsmanData.batsman.count()):
        if(batsmanData.balls_played[i] == 0):
            batsmanData.sr[i] = 0

    batsmanData['sr'] = batsmanData['sr'].astype(int)

    return batsmanData



fig, ax = plt.subplots(2)

for innNum in [1, 2]:
    inn = batsmanData(innNum)

    ax[innNum-1].barh(inn.batsman, inn.runs)
    ax[innNum-1].set_xlabel("Runs")
    ax[innNum-1].set_ylabel("Batsman")
    ax[innNum-1].set_title(f"{inningData(innNum).batting_team[0]}")

plt.suptitle("Batsmen")
plt.tight_layout()
plt.show()