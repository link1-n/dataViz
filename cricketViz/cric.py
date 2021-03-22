import pandas as pd
import matplotlib.pyplot as plt
import math

match = pd.read_csv('1237181.csv')

def inningData(inningNum):

    innings = match[match.innings == inningNum][['ball', 'batting_team', 'bowling_team', 'runs_off_bat', 'extras', 'wicket_type', 'player_dismissed']]
    innings['runs'] = innings['runs_off_bat'] + innings['extras']
    innings = innings.reset_index()
    del innings['index']

    count = innings.ball.count()

    over = []
    for i in range(count):
        over.append(int(math.modf(innings.ball[i])[1]))

    innings['over'] = over

    currentRun = []
    for i in range(count):
        if (i == 0):
            currentRun.append(innings.runs[i])
        else:
            currentRun.append(currentRun[i-1] + innings.runs[i])

    innings['score'] = currentRun
    
    fow = []
    for i in range(innings.score.count()):
        if (type(innings.wicket_type[i]) == str):
            fow.append(True)
        else:
            fow.append(False)

    innings['fow'] = fow

    return innings
