from sklearn.metrics import mean_absolute_error

preds = model.predict(X_test)

mae = mean_absolute_error(y_test, preds)

print(mae)
