from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=1)

model.fit(X_train, y_train)

from sklearn.metrics import mean_absolute_error

preds = model.predict(X_test)

mae = mean_absolute_error(y_test, preds)

print(mae)
