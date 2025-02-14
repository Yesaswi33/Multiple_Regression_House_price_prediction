from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_absolute_error,mean_squared_error,r2_score,accuracy_score
import joblib
# Load Preprocessed Data
X_train, X_test, y_train, y_test, scaler = joblib.load("data/preprocessed_data.pkl")

# Train Model
model = LinearRegression()
model.fit(X_train, y_train)



y_pred=model.predict(X_test)


mae= mean_absolute_error(y_test,y_pred)
mse= mean_squared_error(y_test,y_pred)
r2=r2_score(y_test,y_pred)

print(f"Mean Absolute error is : {mae}")
print(f"Mean Square error is : {mse}")
print(f"R2 Score is : {r2}")


# Save Model
joblib.dump(model, "trained_model.pkl")