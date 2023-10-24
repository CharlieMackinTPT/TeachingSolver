import pandas as pd
from math import comb

csvFile = 'teachingData.csv' 
df = pd.read_csv(csvFile)

for index, row in df.iterrows():
    categoryName = str(col['Category'])
    firstObject = str(input("What do you put on the white board?"))
    if str(row[firstObject]) == '1':
	    print(f"Is it" + str(row['categoryName'])+ "?")
    else:
        print(f"")