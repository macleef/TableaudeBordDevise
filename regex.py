import csv
import re

f = open("askreddit-2015.csv", "r")
reader = csv.reader(f)
posts = list(reader)
posts[0:5]
posts = posts[1:]

of_reddit_count = 0
regex = 'of [Rr]eddit'
for post in posts:
    if re.search(regex, post[0]):
        of_reddit_count += 1

print(of_reddit_count)

serious_count = 0
for post in posts:
    regex = '[\[\()]serious[\]\)]'
    if re.search(regex, post[0]) is not None:
        serious_count += 1

print(serious_count)

serious_start_count=0
serious_end_count=0
serious_count_final=0

for post in posts:
    regex = '^[\[\()][Ss]erious[\]\)]'
    if re.search(regex, post[0]) is not None:
        serious_start_count += 1
        
for post in posts:
    regex = '[\[\()][Ss]erious[\]\)]$'
    if re.search(regex, post[0]) is not None:
        serious_end_count += 1
        
for post in posts:
    regex = '^[\[\()][Ss]erious[\]\)]|[\[\()][Ss]erious[\]\)]$'
    if re.search(regex, post[0]) is not None:
        serious_count_final += 1
        
posts_new=[]
for post in posts:
    regex = '[\[\()][Ss]erious[\]\)]'
    post[0]= re.sub(regex, '[Serious]', post[0])
    posts_new.append(post)
