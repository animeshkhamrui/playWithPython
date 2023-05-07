# 1) Make a Pandas DataFrame with two-dimensional list | Python

import pandas as pd

lst = [['Animesh', 25], ['Ankita', 30],
       ['Amita', 26], ['Aritri', 22]]

df = pd.DataFrame(lst, columns=['Name', 'Number'])
# print(df)


lst1 = [['tom', 'reacher', 25], ['krish', 'pete', 30],
        ['nick', 'wilson', 26], ['juli', 'williams', 22]]

df1 = pd.DataFrame(lst1, columns=['FName', 'LName', 'Age'],
                   dtype=float)
# print(df1)

# 2) Python | Creating DataFrame from dict of narray/lists

data = {'Category': ['Array', 'Stack', 'Queue'],
        'Marks': [20, 21, 19]
        }

df2 = pd.DataFrame(data)

# print(df2)


data1 = {'Category': ['Array', 'Stack', 'Queue'],
         'Student_1': [20, 21, 19], 'Student_2': [15, 20, 14]}

df2 = pd.DataFrame(data1)

# print(df2.transpose())

df3 = pd.DataFrame(data1, index=['Cat_1', 'Cat_2', 'Cat_3'])
print(df3)
