from sklearn.ensemble import GradientBoostingRegressor

model_GB = GradientBoostingRegressor(random_state=1)
model_GB.fit(X_train, y_train)

preds_GB_val = model_GB.predict(X_test)
