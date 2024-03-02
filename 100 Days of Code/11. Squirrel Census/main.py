import pandas as pd 
squirrelcsv = pd.read_csv("./11. Squirrel Census/2018_Central_Park_Squirrel_Census.csv")
countgrey = 0
countcinnamon = 0
countblack = 0
for squirrel in squirrelcsv["Primary Fur Color"]:
    if squirrel == "Gray":
        countgrey += 1
    if squirrel == "Cinnamon":
        countcinnamon += 1
    if squirrel == "Black":
        countblack += 1

squirrelcount = {
    "Fur Color": ["grey","red","black"],
    "Count":[countgrey,countcinnamon,countblack]
}
final = pd.DataFrame(squirrelcount)
final.to_csv("./11. Squirrel Census/squirrel_count.csv")
