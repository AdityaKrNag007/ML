importances = model_RF.feature_importances_
features_check = X_train.columns

feat_df = pd.DataFrame({
    "Feature": features_check,
    "Importance": importances
}).sort_values("Importance", ascending=False)

feat_df
