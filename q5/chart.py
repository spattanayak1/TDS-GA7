# chart.py
# Email: 24f2001293@ds.study.iitm.ac.in

import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# --------------------------
# 1. Generate synthetic data
# --------------------------
np.random.seed(42)
n_customers = 300
segments = ["High Value", "Medium Value", "Low Value"]

# Simulate realistic purchase amount distributions
data = {
    "Customer Segment": np.random.choice(segments, n_customers, p=[0.3, 0.4, 0.3]),
    "Purchase Amount": np.concatenate([
        np.random.normal(loc=500, scale=50, size=int(n_customers * 0.3)),  # High Value
        np.random.normal(loc=250, scale=30, size=int(n_customers * 0.4)),  # Medium Value
        np.random.normal(loc=100, scale=20, size=int(n_customers * 0.3)),  # Low Value
    ])
}

df = pd.DataFrame(data)

# ---------------------------------
# 2. Set Seaborn professional style
# ---------------------------------
sns.set_style("whitegrid")
sns.set_context("talk")  # Presentation-ready text sizes

# ---------------------------------
# 3. Create boxplot visualization
# ---------------------------------
plt.figure(figsize=(8, 8))  # 8 inches * 64 dpi = 512 px
palette = sns.color_palette("Set2")

sns.boxplot(
    data=df,
    x="Customer Segment",
    y="Purchase Amount",
    palette=palette,
    width=0.5
)

# ---------------------------------
# 4. Titles, labels, and formatting
# ---------------------------------
plt.title("Purchase Amount Distribution by Customer Segment", fontsize=16, weight="bold")
plt.xlabel("Customer Segment", fontsize=14)
plt.ylabel("Purchase Amount (USD)", fontsize=14)

# Optional: Improve layout for publication
sns.despine(trim=True)

# ---------------------------------
# 5. Save chart as exactly 512x512 px
# ---------------------------------
plt.savefig("chart.png", dpi=64, bbox_inches="tight")
plt.close()
