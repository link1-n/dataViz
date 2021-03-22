import pandas as pd
import matplotlib.pyplot as plt
import math

match = pd.read_csv('1237181.csv')

def runBarG(inningNum):
    innings = match[match.innings == inningNum][['ball', 'batting_team', 'runs_off_bat', 'extras', 'wicket_type', 'player_dismissed']]
    innings['runs'] = innings['runs_off_bat'] + innings['extras']
    innings = innings.reset_index()
    del innings['index']

    over = []
    for i in range(innings.ball.count()):
        over.append(int(math.modf(innings.ball[i])[1]))

    innings['over'] = over

    overRuns = {}
    for i in range(20):
        inningsOver = innings[innings.over == i]
        
        inningsOver = inningsOver.reset_index()
        del inningsOver['index']

        overRuns[f'{i+1}'] = inningsOver.runs.sum()

    return overRuns


inn1 = runBarG(1)
inn2 = runBarG(2)

fn = [inn1, inn2]

fig, ax = plt.subplots(2)

for i, obj in enumerate(fn):
    ax[i].bar(obj.keys(), obj.values())    
    ax[i].set_title(f"{i}")

plt.suptitle("Yes")

plt.show()
