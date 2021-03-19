import pandas as pd
import matplotlib.pyplot as plt

match = pd.read_csv('1237181.csv')

def runs(inning):
    innings = match[match.innings == inning]
    innings = innings.reset_index()
    del innings['index']
    wicket = innings.wicket_type
    innings_formatted = innings[['runs_off_bat', 'extras']].sum(1)

    currentRun = []
    for i in range(innings_formatted.count()):
        if (i == 0):
            currentRun.append(innings_formatted[i])
        else:
            currentRun.append(currentRun[i-1] + innings_formatted[i])

    finalRuns = pd.DataFrame(currentRun, columns = ['score']);
    finalRuns['wicket'] = wicket 

    fow = []
    for i in range(finalRuns.score.count()):
        if (type(finalRuns.wicket[i]) == str):
            fow.append(True)
        else:
            fow.append(False)

    finalRuns['fow'] = fow
    del finalRuns['wicket']

    return finalRuns

def fow(runs):
    finalFOW = []
    for i in range(runs.score.count()):
        if (runs.fow[i] == True):
            finalFOW.append(runs.score[i])
        else:
            finalFOW.append(None)
    
    return finalFOW

inn1 = runs(1)
inn2 = runs(2)

inn1_fow = fow(inn1)
inn2_fow = fow(inn2)

fig, ax = plt.subplots()

ax.plot(inn1.score, 'b')
ax.plot(inn1_fow, 'r.', markersize = 10)

ax.plot(inn2.score, 'g')
ax.plot(inn2_fow, 'r.', markersize = 10)

ax.set_title(f"{match.batting_team[0]} Vs. {match.bowling_team[0]}")
ax.set_xlabel("Balls")
ax.set_ylabel("Runs")
ax.legend([match.batting_team[0], 'Wicket', match.bowling_team[0]])

plt.show()
