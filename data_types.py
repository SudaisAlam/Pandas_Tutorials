import pandas as pd

Data = pd.read_csv('/Users/sudaisalam/Downloads/titanic/train.csv')

#for Specific 
print(Data.Survived.dtype)

#For whole Dataset
print(Data.dtypes) 

# Changing data types
print(Data.Survived.astype('float64'))
