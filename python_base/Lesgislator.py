
#%%
import csv

f = open ('legislators.csv')
legislators = list (csv.reader(f))
gender = []
for row in legislators:
    gender.append(row[3])
    

gender = set(gender)
print(gender)


#%%
for row in legislators:
    if row[3] == '':
        row[3] = 'M'
gender = []
for row in legislators:
    gender.append(row[3])
    

gender = set(gender)
print(gender)


#%%
birth_years=[]
for row in legislators:
    birth = row[2]
    year = birth.split('-')[0]
    birth_years.append(year)
int_years=[]
for date in birth_years:
    try:
        date=int(date)
    except Exception:
        date=0
    int_years.append(date)
    


#%%
import csv

f = open ('legislators.csv')
legislators = list (csv.reader(f))

for data in legislators:
    birth_year=data[2].split('-')[0]
    try:
        birth_year=int(birth_year)
    except Exception:
        birth_year=0
    data.append(birth_year)

legislators[0][7]="birth_year"
last_value=1
for item in legislators:
    if item[7]==0:
        item[7]=last_value
    last_value=item[7]
    
print(legislators)


#%%
name_counts={}
for item in legislators:
    name=item[1]
    year=item[7]
    if item[3] == 'F' and year > 1950:        
        if name in name_counts:
            name_counts[name]+=1
        else :
            name_counts[name]=1
            
print(name_counts)
        


##TRAINING
male_name_counts={}
for item in legislators:
    name=item[1]
    year=item[7]
    if item[3] == 'M' and year > 1940:        
        if name in male_name_counts:
            male_name_counts[name]+=1
        else :
            male_name_counts[name]=1

print(male_name_counts)            
top_male_count=None
top_male_names=[]
for name, number in male_name_counts.items():
    if top_male_count is None or male_name_counts[name] > top_male_count:
        top_male_count=male_name_counts[name]
        
for name, count in male_name_counts.items():
    if count==top_male_count:
        top_male_names.append(name)
print(top_male_names)




#%%



