import pandas as pd
from math import comb

csvFile = 'teachingData.csv' 
df = pd.read_csv(csvFile)

firstObject = str(input("What do you put on the white board?")).lower().title()
print(firstObject)

count = 0
for index, row in df.iterrows():
	categoryName = str(row['Category'])
	if str(row[firstObject]) == '1':
		print("Is it " + str(categoryName)+ "?")
		count = count + 1

secondObject = str(input("What do you put on the white board next?")).lower().title()

count = 0
for index, row in df.iterrows():
	categoryName = str(row['Category'])
	if str(row[firstObject]) == '1' and str(row[secondObject])=='1':
		print("Is it " + str(categoryName)+ "?")
		count = count + 1
	
if(count<1):
	print("There are no results for these combinations")
	exit(0)

thirdObject = str(input("What do you put on the white board next?")).lower().title()

count = 0
for index, row in df.iterrows():
	categoryName = str(row['Category'])
	if str(row[firstObject]) == '1' and str(row[secondObject])== '1' and  str(row[secondObject]) == '1':
		print("Is it " + str(categoryName)+ "?")
		count = count + 1
	
if(count<1):
	print("There are no results for these combinations")
	exit(0)