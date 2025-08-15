# Employee Performance Analysis (24f2001293@ds.study.iitm.ac.in)
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import mpld3
from io import StringIO

# Sample data as a string
data_str = """employee_id,department,region,performance_score,years_experience,satisfaction_rating
EMP001,R&D,Africa,79.3,11,4.7
EMP002,IT,Middle East,78.18,2,4.4
EMP003,HR,Asia Pacific,92.06,11,4.4
EMP004,Sales,Africa,86.59,1,4.9
EMP005,IT,Latin America,67.39,2,3.2"""

# Load data from string
data = pd.read_csv(StringIO(data_str))

# Frequency count for "Operations" department
operations_count = data[data['department'] == 'Operations'].shape[0]
print(f"Frequency count of 'Operations' department: {operations_count}")

# Create histogram for department distribution
plt.figure(figsize=(8,5))
sns.countplot(data=data, x='department', palette='viridis', order=data['department'].value_counts().index)
plt.title('Department Distribution of Employees')
plt.xlabel('Department')
plt.ylabel('Number of Employees')
plt.xticks(rotation=45)
plt.tight_layout()

# Save histogram as HTML using mpld3
html_str = mpld3.fig_to_html(plt.gcf())
with open("department_distribution.html", "w") as f:
    f.write(html_str)

print("HTML file 'department_distribution.html' generated successfully.")
