X = pd.get_dummies(X)

#👉 It converts text columns → numbers automatically

#What it actually does

#Example:

#Before:

#Contract
#Month-to-month
#One year
#Two year

#After:

#Contract_Month-to-month   Contract_One year   Contract_Two year
#1                         0                   0
#0                         1                   0
#0                         0                   1

#👉 Creates separate columns (0/1)
