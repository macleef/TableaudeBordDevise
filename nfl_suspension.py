import csv
f_nfl_sus=open('nfl-suspensions-data.csv', 'r')
nfl_suspensions=list(csv.reader(f_nfl_sus))

nfl_suspensions=nfl_suspensions[1:]

years={}
for data in nfl_suspensions:
    year=data[5]
    if year in years:
        years[year]+=1
    else:
        years[year]=1

print(years)

teams=[row[1] for row in nfl_suspensions]
unique_teams=set(teams)

games=[row[2] for row in nfl_suspensions]
unique_games=set(games)

class Suspensions():
    def __init__(self, ligne):
        self.name=ligne[0]
        self.team=ligne[1]
        self.games=ligne[2]
        try:
            self.year=int(ligne[5])
        except Exception:
            self.year=0

    def get_year(self):
        print(self.year)

ligne3=Suspensions(nfl_suspensions[22])
ligne3.get_year()


