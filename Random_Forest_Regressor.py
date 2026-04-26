from sklearn.ensemble import RandomForestRegressor

model = RandomForestRegressor(random_state=1)
model.fit(X, y)

preds = model.predict(X1)   #X1 is the other dataframe you want to predict the value in whilst training from dataframe X

