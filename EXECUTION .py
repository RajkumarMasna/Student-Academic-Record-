import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
from scipy.stats import zscore

# Load the dataset using known working encoding
df = pd.read_csv("C:\\Users\\rajku\\Downloads\\py dta set project.csv")

# 1. Info about dataset
print("=== Dataset Info ===")
print(df.info())
print("\n=== Summary Statistics ===")
print(df.describe())
print("\n=== Missing Values ===")
print(df.isnull().sum())

# 2. Handling Missing Data
df = df.dropna()
print("\n=== After Handling Missing Values ===")
print(df.isnull().sum())

# 3. Pairplot to view relationships
sns.pairplot(df, hue='Gender')
plt.suptitle("Pairplot of Academic Performance", y=1.02)
plt.show()

# 4. Correlation Heatmap
plt.figure(figsize=(10, 6))
sns.heatmap(df.corr(numeric_only=True), annot=True, cmap='coolwarm')
plt.title("Correlation Heatmap")
plt.show()

# 5. Boxplots for outlier detection
plt.figure(figsize=(14, 6))
sns.boxplot(data=df[['CGPA100', 'CGPA200', 'CGPA300', 'CGPA400']])
plt.title("Boxplot of CGPAs Across Years")
plt.show()

# 6. Z-score outlier detection
z_scores = zscore(df[['CGPA', 'SGPA']])
outliers = (np.abs(z_scores) > 3).any(axis=1)
print(f"\nNumber of outliers (Z-score > 3): {outliers.sum()}")

# 7. Line plot: progression across years (average)
avg_cgpas = df[['CGPA100', 'CGPA200', 'CGPA300', 'CGPA400']].mean()
avg_cgpas.plot(kind='line', marker='o', title="Average CGPA Progression Over Years")
plt.xlabel("Year")
plt.ylabel("Average CGPA")
plt.grid(True)
plt.show()

# 8. Bar plot: Gender vs Average CGPA (warning fixed using hue)
gender_cgpa = df.groupby('Gender')['CGPA'].mean().reset_index()
sns.barplot(data=gender_cgpa, x='Gender', y='CGPA', hue='Gender', palette='Set2', legend=False)
plt.title("Average CGPA by Gender")
plt.show()

# 9. Column plot: Program Code vs Average CGPA
prog_cgpa = df.groupby('Prog Code')['CGPA'].mean().sort_values(ascending=False)
prog_cgpa.plot(kind='bar', color='skyblue', title="Average CGPA by Program")
plt.ylabel("Average CGPA")
plt.tight_layout()
plt.show()

# Pie Chart: Year of Graduation (YOG) Distribution
yog_counts = df['YoG'].value_counts()
plt.figure(figsize=(6, 6))
plt.pie(yog_counts, labels=yog_counts.index, autopct='%1.1f%%', colors=sns.color_palette('pastel'))
plt.title("Year of Graduation (YoG) Distribution")
plt.axis('equal')
plt.show()

# Regression Plot: SGPA vs CGPA
plt.figure(figsize=(8, 6))
sns.regplot(data=df, x='SGPA', y='CGPA', scatter_kws={"color": "blue"}, line_kws={"color": "red"})
plt.title("Regression Line: SGPA vs CGPA")
plt.xlabel("SGPA")
plt.ylabel("CGPA")
plt.grid(True)
plt.show()
