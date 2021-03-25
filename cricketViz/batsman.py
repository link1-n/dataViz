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
    
    battedStats = {}
    ball = []
    for name in batted:
        runs = 0
        balls = 0
        for i in range(innings.runs.count()):
            if (name == innings.striker[i]):
                runs += innings.runs_off_bat[i]
                balls += 1
        battedStats[f'{name}'] = runs
        ball.append(balls)
            
    batsmanData = pd.DataFrame(list(battedStats.items()), columns = ['batsman', 'runs'])
    batsmanData['balls_played'] = ball
    print(batsmanData)


batsmanData(1)