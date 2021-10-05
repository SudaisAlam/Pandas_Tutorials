import pandas as pd

Data = pd.read_csv('/Users/sudaisalam/Downloads/titanic/train.csv')

print(pd.concat([Data.Name, Data.Survived]))
print(Data[['Name', 'Age']].join(Data.Survived, lsuffix='_self', rsuffix='_tojoin'))# better!