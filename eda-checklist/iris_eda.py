import pandas as pd
import plotly.express as px
from sklearn.datasets import load_iris

# -----------------------------------
# 1. Load the Iris dataset
# -----------------------------------
iris = load_iris()

# Create DataFrame with feature names
df = pd.DataFrame(data=iris.data, columns=iris.feature_names)

# Add target column
df['species'] = iris.target

# Map numeric target values to actual species names
df['species'] = df['species'].map({
    0: iris.target_names[0],
    1: iris.target_names[1],
    2: iris.target_names[2]
})

# -----------------------------------
# 2. Display first few rows
# -----------------------------------
print("First 5 rows of the dataset:")
print(df.head())
print("\n" + "="*50 + "\n")

# Observation:
# The dataset contains flower measurements and a species column.

# -----------------------------------
# 3. Dataset information
# -----------------------------------
print("Dataset Info:")
print(df.info())
print("\n" + "="*50 + "\n")

# Observation:
# The dataset has 150 rows and 5 columns.
# Four columns are numerical and one is categorical.

# -----------------------------------
# 4. Summary statistics
# -----------------------------------
print("Summary Statistics:")
print(df.describe())
print("\n" + "="*50 + "\n")

# Observation:
# Summary statistics show count, mean, standard deviation,
# minimum, maximum, and quartile values for all numerical columns.

# -----------------------------------
# 5. Check for missing values
# -----------------------------------
print("Missing Values:")
print(df.isnull().sum())
print("\n" + "="*50 + "\n")

# Observation:
# No missing values are present in the dataset.

# -----------------------------------
# 6. Distribution of one feature
# Example: sepal length
# -----------------------------------
fig1 = px.histogram(
    df,
    x='sepal length (cm)',
    color='species',
    title='Distribution of Sepal Length by Species',
    marginal='box'
)
fig1.show()

# Observation:
# Setosa generally has smaller sepal length compared to Versicolor and Virginica.

# -----------------------------------
# 7. Relationship between two features
# Example: petal length vs petal width
# -----------------------------------
fig2 = px.scatter(
    df,
    x='petal length (cm)',
    y='petal width (cm)',
    color='species',
    title='Petal Length vs Petal Width'
)
fig2.show()

# Observation:
# There is a strong positive relationship between petal length and petal width.
# Setosa is clearly separated, while Versicolor and Virginica are closer.

# -----------------------------------
# 8. Species/Class distribution
# -----------------------------------
species_count = df['species'].value_counts()
print("Species Distribution:")
print(species_count)
print("\n" + "="*50 + "\n")

fig3 = px.bar(
    x=species_count.index,
    y=species_count.values,
    labels={'x': 'Species', 'y': 'Count'},
    title='Species Distribution'
)
fig3.show()

# Observation:
# All three species have equal number of samples (50 each).

# -----------------------------------
# 9. Correlation between numerical features
# -----------------------------------
correlation_matrix = df.drop(columns=['species']).corr()
print("Correlation Matrix:")
print(correlation_matrix)
print("\n" + "="*50 + "\n")

# Observation:
# Petal length and petal width have a very high positive correlation.

# -----------------------------------
# 10. Final insight
# -----------------------------------
print("EDA completed successfully.")

# Final Observation:
# Petal-related features are more useful for distinguishing species
# than sepal-related features.