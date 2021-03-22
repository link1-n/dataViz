from cric import inningData
import matplotlib.pyplot as plt

def fow(runs):
    finalFOW = []
    for i in range(runs.score.count()):
        if (runs.fow[i] == True):
            finalFOW.append(runs.score[i])
        else:
            finalFOW.append(None)
    
    return finalFOW

inn1 = inningData(1)
inn2 = inningData(2)

inn1_fow = fow(inn1)
inn2_fow = fow(inn2)

fig, ax = plt.subplots()

ax.plot(inn1.score, 'b')
ax.plot(inn1_fow, 'r.', markersize = 10)

ax.plot(inn2.score, 'g')
ax.plot(inn2_fow, 'r.', markersize = 10)

ax.set_title(f"{inn1.batting_team[0]} Vs. {inn1.bowling_team[0]}")
ax.set_xlabel("Balls")
ax.set_ylabel("Runs")
ax.legend([inn1.batting_team[0], 'Wicket', inn1.bowling_team[0]])

plt.show()