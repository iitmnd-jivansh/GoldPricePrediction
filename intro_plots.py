import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

# Load data
df = pd.read_csv("merged.csv")

# Convert Month column to datetime & sort
df['Month'] = pd.to_datetime(df['Month'])
df = df.sort_values('Month').reset_index(drop=True)

# Show head
print("\nFirst 5 rows:")
print(df.head())

# Correlation matrix (now includes RealRate)
cols = ['Gold', 'FedRate', 'inflation', 'Index' ]
corr = df[cols].corr()

print("\nCorrelation Matrix:")
print(corr)

# ================
# Time Series Plots
# ================
plt.figure(figsize=(14, 12))

plt.subplot(5, 1, 1)
plt.plot(df['Month'], df['Gold'])
plt.title("Gold price")
plt.ylabel("$")

plt.subplot(5, 1, 2)
plt.plot(df['Month'], df['FedRate'])
plt.title("Federal Funds Rate (%)")
plt.ylabel("%")

plt.subplot(5, 1, 3)
plt.plot(df['Month'], df['inflation'])
plt.title("CPI Inflation Rate (YoY)")
plt.ylabel("%")

plt.subplot(5, 1, 4)
plt.plot(df['Month'], df['Index'])
plt.title("S&P price")
plt.ylabel("$")

plt.tight_layout()
plt.show()

# ==========
# Heatmap
# ==========
plt.figure(figsize=(6, 5))
plt.imshow(corr, cmap='coolwarm', interpolation='nearest')
plt.colorbar(label="Correlation coefficient")
plt.xticks(range(len(cols)), cols, rotation=45, ha='right')
plt.yticks(range(len(cols)), cols)
plt.title("Correlation Heatmap (incl. RealRate)")
plt.tight_layout()
plt.show()

