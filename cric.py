import pandas as pd
import matplotlib.pyplot as plt

final = pd.read_csv('1237181.csv')

inningOne = final[final.innings == 1]

wicket = inningOne.wicket_type

inningOne_formatted = inningOne[['runs_off_bat', 'extras']]
inning1_runBall = inningOne_formatted.sum(1)

currentRun = []
for i in range(inning1_runBall.count()):
    if (i == 0):
        currentRun.append(inning1_runBall[i])
    else:
        currentRun.append(currentRun[i-1] + inning1_runBall[i])

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


finalFOW = []
for i in range(finalRuns.score.count()):
    if (finalRuns.fow[i] == True):
        finalFOW.append(finalRuns.score[i])
    else:
        finalFOW.append(None)

# over = []
# for i in range(finalRuns.score.count()):
#     over.append(i/6)

# finalRuns['over'] = over

fig, ax = plt.subplots()

ax.plot(finalRuns.score)
ax.plot(finalFOW, 'r.', markersize = 10)

ax.set_title("Delhi Capitals")
ax.set_xlabel("Balls")
ax.set_ylabel("Runs")

plt.show()
