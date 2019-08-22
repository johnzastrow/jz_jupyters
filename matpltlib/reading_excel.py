import pandas as pd
from pandas import ExcelWriter
from pandas import ExcelFile

# The data are the following:
#  Sepal length  Sepal width  Petal length  Petal width    Species
# 0           5.1          3.5           1.4          0.2  l. setosa
# 1           4.9          3.0           1.4          0.2  l. setosa
# 2           4.7          3.2           1.3          0.2  l. setosa
# 3           4.6          3.1           1.5          0.2  l. setosa
# 4           5.0          3.6           1.4          0.2  l. setosa
# 5           5.4          3.9           1.7          0.4  l. setosa
# 6           4.6          3.4           1.4          0.3  l. setosa
# 7           5.0          3.4           1.5          0.2  l. setosa

# you will have to install xlrd if you get the following error when running the code:
#       ImportError: Install xlrd >= 1.0.0 for Excel support
# You may then use the PIP install method to install xlrd as follows:
# pip install xlrd

#(use "r" before the path string to address special character, such as '\'). Don't forget to put the file name at the end of the path + '.xlsx'
df = pd.read_excel(r'petals.xlsx')
print(df)

print("Column headings:")
print(df.columns)
print(df['Sepal width'])

# Optional Step: Selecting subset of column/s: do only Sepal Width and Petal length. make sure that the 
# column names specified in the code exactly match with the column names within the Excel file. Otherwise, 
# you’ll get NaN values.

data = pd.read_excel(r'petals.xlsx')
df2 = pd.DataFrame(data, columns= ['Petal length','Sepal width'])
print (df2)