X['Sex'] = X['Sex'].map({'male':0, 'female':1})
X['Embarked'] = X['Embarked'].map({'S':0, 'C':1, 'Q':2})

# only numbers can be considered in pattern recognision , so we convert male --> 0 and female --> 1 so it can predict better with more info
# similar for every other text feature like 'Embarked'
