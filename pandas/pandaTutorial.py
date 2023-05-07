import pandas as pd
print(pd.__version__)

newObj = {
    'cars': ['BMW', 'FORD', 'TATA', 'LS'],
    'quantity': [2, 4, 6, 8]
}

myTable = pd.DataFrame(newObj)
# print('#',myTable)

# print(myTable.loc[0])

# print(myTable.loc[[0,1]])

myList = [1, 2, 3, 4, 5]

# mySerise = pd.Series(myList)

mySerise = pd.Series(myList, index=['one', 'two', 'three', 'four', 'five'])

# print(mySerise)

# print(mySerise["three"])

calories = {"day1": 420, "day2": 380, "day3": 390}

myData = pd.Series(calories)

# print(myData)

mydata = pd.Series(calories, index=['day1', 'day3'])

# print(mydata)

csvdata = pd.read_csv('C:\\Users\\Piklu PC\\Downloads\\data.csv')

print(csvdata)
