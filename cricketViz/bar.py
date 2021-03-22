import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
from cric import inningData

match = pd.read_csv('1237181.csv')

def overData(inningNum):
    innings = inningData(inningNum)
    
    overRuns = []
    overWickets = []
    for i in range(20):
        inningsOver = innings[innings.over == i]
        
        inningsOver = inningsOver.reset_index()
        del inningsOver['index']

        overRuns.append(inningsOver.runs.sum())
        
        count = 0
        for j in range(inningsOver.ball.count()):
            if (inningsOver.fow[j] == True):
                count += 1
        overWickets.append(count)

    overData = pd.DataFrame(list(zip(overRuns, overWickets)), columns = ['runs', 'number_wickets'])


    return overData


inn1 = overData(1)
inn2 = overData(2)

fn = [inn1, inn2]

fig, ax = plt.subplots(2)

for i, obj in enumerate(fn):
    obj.index.name = 'index'

    ax[i].bar(obj.index, obj.runs)   
    ax[i].set_title(f"{i}")

    for j in range(20):
        for k in range(obj.number_wickets[j]):
            cc = plt.Circle((i, (obj.runs[i] + k + 1)), 0.5, color = 'g') 
            ax[i].add_artist( cc )

    for axis in [ax[i].xaxis, ax[i].yaxis]:
        axis.set_major_locator(ticker.MaxNLocator(integer=True))

plt.suptitle("Yes")

plt.show()
