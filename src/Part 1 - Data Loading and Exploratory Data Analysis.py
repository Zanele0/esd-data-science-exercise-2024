
# Full Name: Zanele Malope
import pandas as pd
import matplotlib.pyplot as plot

# Load the dataset
data = pd.read_csv('../data/data.csv')

# Print the first 10 rows of the dataset
print("First 10 rows of the dataset:")
print(data.head(26))

# Printing summary statistics
print("\n Summary statistics:")
print(data.describe())

# Checking for missing values and printing the number of missing values per calumn
print("\nMissing values per column:")
print(data.isnull().sum())

# Fill the missing values (NaN) with the forward fill method
updated_data = data.ffill()

# Convert the date column to datetime format
updated_data['Date'] = pd.to_datetime(updated_data['Date'])

# Setting Date column as index
updated_data.set_index('Date', inplace=True)

# Plotting the time series data
plot.figure(figsize=(14, 8))
plot.subplot(3, 2, 1)
plot.plot(updated_data['GDP'], label='GDP')
plot.title('GDP over Time')
plot.legend()

plot.subplot(3, 2, 2)
plot.plot(updated_data['ConsumerPrices'], label='Consumer Prices', color='orange')
plot.title('Consumer Prices over Time')
plot.legend()

plot.subplot(3, 2, 3)
plot.plot(updated_data['UNEM'], label='Unemployment Rate', color='green')
plot.title('Unemployment Rate over Time')
plot.legend()

plot.subplot(3, 2, 4)
plot.plot(updated_data['GFCF'], label='Gross Fixed Capital Formation', color='red')
plot.title('Gross Fixed Capital Formation over Time')
plot.legend()

plot.subplot(3, 2, 5)
plot.plot(updated_data['GovExp'], label='Government Expenditure', color='purple')
plot.title('Government Expenditure over Time')
plot.legend()

plot.subplot(3, 2, 6)
plot.plot(updated_data['HouseExp'], label='Household Expenditure', color='brown')
plot.title('Household Expenditure over Time')
plot.legend()

plot.tight_layout()
plot.show()




 
