import csv

f = open('guns.csv','r')
csvreader = csv.reader(f)
guns=list(csvreader)

print(guns[0:5])
headers = guns[:1]
guns=guns[1:]

##Headers
print(headers)

##Datas
print(guns[0:5])

years = [gun[1] for gun in guns]
year_counts={}
for year in years:
    if year not in year_counts:
        year_counts[year]=0
    year_counts[year]+=1

print(year_counts)

import datetime

dates=[datetime.datetime(year = int(row[1]), month = int(row[2]), day=1) for row in guns]

date_counts={}
for date in dates:
    if date  not in date_counts:
        date_counts[date]=0
    date_counts[date]+=1

print(date_counts)

sex_counts={}
race_counts={}

for row in guns:
    sex=row[5]
    race=row[7]
    if sex not in  sex_counts:
        sex_counts[sex]=0
    if race not in race_counts:
        race_counts[race]=0
    sex_counts[sex]+=1
    race_counts[race]+=1

with open('census.csv','r') as f:
    populations = list(csv.reader(f))

mapping={}
mapping['Black']=40250635
mapping['Asian/Pacific Islander']=674625+15159516
mapping['White']=197318956
mapping['Hispanic']=44618105
mapping['Native American/Native Alaskan']=3739506

ratio={}
for race, count in race_counts.items():
    ratio[race]=count*100000/mapping[race]

ratio
