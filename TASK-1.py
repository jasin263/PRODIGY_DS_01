#Task 1
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Generate a sample dataset
np.random.seed(42)

# Define the size of the dataset
n = 1000

# Generate data
years = np.random.choice(range(1950, 2023), size=n, replace=True)
ages = np.random.randint(0, 100, size=n)
genders = np.random.choice(['Male', 'Female'], size=n, replace=True)
frequencies = np.random.poisson(lam=50, size=n)

# Create the DataFrame
population_data = pd.DataFrame({
    'Year': years,
    'Age': ages,
    'Gender': genders,
    'Frequency': frequencies
})

# Display the first few rows of the dataset
print(population_data.head())

# Distribution of Ages
plt.figure(figsize=(10, 6))
sns.histplot(data=population_data, x='Age', bins=30, kde=True)
plt.title('Distribution of Ages')
plt.xlabel('Age')
plt.ylabel('Count')
plt.show()

# Distribution of Genders
plt.figure(figsize=(8, 6))
sns.countplot(data=population_data, x='Gender')
plt.title('Distribution of Genders')
plt.xlabel('Gender')
plt.ylabel('Count')
plt.show()

