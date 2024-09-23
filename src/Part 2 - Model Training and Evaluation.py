import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
import matplotlib.pyplot as plot

# Load the dataset
data = pd.read_csv('../data/data.csv')

# Fill missing values with the forward fill method
updated_data = data.ffill()

# Convert date column to datetime format
updated_data['Date'] = pd.to_datetime(updated_data['Date'])

# Set 'Date' column as the index
updated_data.set_index('Date', inplace=True)

# features variable
features = updated_data[['ConsumerPrices', 'UNEM', 'GDP', 'GovExp', 'HouseExp']]

# target variable
target = updated_data['GFCF']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(features, target, test_size=0.2, random_state=42)

# Initialize and train the model
model = LinearRegression()
model.fit(X_train, y_train)

# Make predictions on the test set
y_predict = model.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, y_predict)
r2 = r2_score(y_test, y_predict)

print(f"Mean Squared Error: {mse}")
print(f"R-squared: {r2}")

# Plot actual vs predicted GDP values
plot.figure(figsize=(10, 6))
plot.plot(y_test.index, y_test, label='Actual GFCF')
plot.plot(y_test.index, y_predict, label='Predicted GFCF', linestyle='-.')
plot.xlabel('Date')
plot.ylabel('GFCF')
plot.title('Actual vs Predicted GFCF')
plot.legend()
plot.show()

