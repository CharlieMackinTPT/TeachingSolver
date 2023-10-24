import pandas as pd
from math import comb

csvFile = 'teachingData.csv' 
df = pd.read_csv(csvFile)

firstObject = str(input("What do you put on the white board?")).lower().title()
print(firstObject)

for index, row in df.iterrows():
    categoryName = str(row['Category'])
    if str(row[firstObject]) == '1':
	    print("Is it " + str(categoryName)+ "?")