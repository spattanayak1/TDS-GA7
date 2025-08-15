# File: employee_performance_analysis.py
# Author: Karthik M
# Verification Email: 24f2001293@ds.study.iitm.ac.in

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import mpld3
from io import StringIO

# Sample employee data
data = """employee_id,department,region,performance_score,years_experience,satisfaction_rating
EMP001,R&D,Africa,79.3,11,4.7
EMP002,IT,Middle East,78.18,2,4.4
EMP003,HR,Asia Pacific,92.06,11,4.4
EMP004,Sales,Africa,86.59,1,4.9
EMP005,IT,Latin America,67.39,2,3.2
EMP006,Operations,Asia,88.0,5,4.5
EMP007,Operations,Europe,91.2,8,4.6
EMP008,Sales,Latin America,74.5,3,4.1
EMP009,R&D,Middle East,82.1,7,4.3
EMP010,HR,Africa,90.0,10,4.8
"""

# Load data
df = pd.read_csv(StringIO(data))

# Frequency count for "Operations" department
operations_count = df[df['department'] == 'Operations'].shape[0]
print(f"Number of employees in Operations department: {operations_count}")

# Plot department distribution
plt.figure(figsize=(8,5))
sns.countplot(data=df, x='department', palette='viridis')
plt.title('Employee Distribution by Department')
plt.xlabel('Department')
plt.ylabel('Number of Employees')
plt.xticks(rotation=45)
plt.tight_layout()

# Convert plot to HTML and embed email
html_plot = mpld3.fig_to_html(plt.gcf())
html_with_email = f"""
<html>
<head>
<title>Employee Department Histogram</title>
</head>
<body>
<h3>Verification Email: 24f2001293@ds.study.iitm.ac.in</h3>
{html_plot}
</body>
</html>
"""

# Save HTML
with open("employee_department_histogram.html", "w") as f:
    f.write(html_with_email)

print("Histogram saved as employee_department_histogram.html with email embedded.")
