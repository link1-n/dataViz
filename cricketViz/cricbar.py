import pandas as pd
import matplotlib.pyplot as plt
import math

match = pd.read_csv('1237181.csv')

def runBarG(inningNum):
    innings = match[match.innings == inningNum][['ball', 'batting_team', 'runs_off_bat', 'extras', 'wicket_type', 'player_dismissed']]
    innings['runs'] = innings['runs_off_bat'] + innings['extras']

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

fig, ax = plt.subplots()

for i in range(2):
    for obj in [inn1, inn2]:
        ax[i].bar(obj.keys(), inn2.values())

plt.suptitle("Yes")

plt.show()
