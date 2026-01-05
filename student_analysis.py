import pandas as pd
import matplotlib.pyplot as plt

# Load the dataset
data = pd.read_csv('student_data.csv')

# Show first 5 rows
print("Dataset:\n", data)

# Calculate average marks per student
data['Average'] = data[['Math','Physics','Chemistry','English','Biology']].mean(axis=1)
print("\nAverage Marks per Student:\n", data[['Student','Average']])

# Highest and lowest marks in each subject
print("\nHighest Marks:\n", data[['Math','Physics','Chemistry','English','Biology']].max())
print("\nLowest Marks:\n", data[['Math','Physics','Chemistry','English','Biology']].min())

# Visualization
plt.figure(figsize=(8,5))
plt.bar(data['Student'], data['Average'], color='skyblue')
plt.title('Average Marks per Student')
plt.xlabel('Students')
plt.ylabel('Average Marks')
plt.show()
