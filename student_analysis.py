# Import necessary libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

# Step 1: Load the dataset into a pandas DataFrame
# Embedded dataset as a dictionary
data = {
    'student_id': list(range(1, 51)),  # 50 students
    'math': np.random.randint(0, 101, 50),  # Random scores 0-100
    'science': np.random.randint(0, 101, 50),
    'english': np.random.randint(0, 101, 50),
    'study_hours': np.random.randint(0, 21, 50)  # Random study hours 0-20
}
df = pd.DataFrame(data)

# Step 2: Print basic dataset info and first few rows
print("Dataset Info:")
print(df.info())
print("\nFirst few rows:")
print(df.head())

# Step 3: Calculate and print the average score per subject (math, science, english)
avg_math = df['math'].mean()
avg_science = df['science'].mean()
avg_english = df['english'].mean()
print(f"\nAverage Math Score: {avg_math:.2f}")
print(f"Average Science Score: {avg_science:.2f}")
print(f"Average English Score: {avg_english:.2f}")

# Step 4: Calculate total marks per student
df['total_marks'] = df['math'] + df['science'] + df['english']

# Step 5: Identify and print the top 10 students based on total marks
top_10_students = df.nlargest(10, 'total_marks')[['student_id', 'total_marks']]
print("\nTop 10 Students by Total Marks:")
print(top_10_students)

# Step 6: Create a bar chart of average scores per subject
subjects = ['Math', 'Science', 'English']
averages = [avg_math, avg_science, avg_english]
plt.figure(figsize=(8, 5))
plt.bar(subjects, averages, color=['blue', 'green', 'red'])
plt.title('Average Scores per Subject')
plt.xlabel('Subject')
plt.ylabel('Average Score')
plt.ylim(0, 100)
plt.show()

# Step 7: Create a scatter plot of study hours vs total marks
plt.figure(figsize=(8, 5))
plt.scatter(df['study_hours'], df['total_marks'], alpha=0.7)
plt.title('Study Hours vs Total Marks')
plt.xlabel('Study Hours')
plt.ylabel('Total Marks')
plt.grid(True)
plt.show()

# Step 8: Calculate and print the correlation between study hours and total marks
correlation = df[['study_hours', 'total_marks']].corr()
print(f"\nCorrelation between Study Hours and Total Marks: {correlation:.2f}")

# Step 9: Create a heatmap of the correlation
# Calculate the full correlation matrix for numerical columns
corr_matrix = df[['math', 'science', 'english', 'study_hours', 'total_marks']].corr()
plt.figure(figsize=(8, 6))
sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', fmt='.2f')
plt.title('Correlation Heatmap')
plt.show()
