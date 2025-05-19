import pandas as pd
import matplotlib.pyplot as plt

# Load CSV file
df = pd.read_csv('economic_data.csv')

# Plot the data
plt.figure(figsize=(10, 5))
plt.plot(df['Year'], df['Inflation Rate'], marker='o', label='Inflation Rate (%)', color='red')
plt.plot(df['Year'], df['Interest Rate'], marker='o', label='Interest Rate (%)', color='blue')

# Customize plot
plt.title('Inflation vs Interest Rate (2015–2024)')
plt.xlabel('Year')
plt.ylabel('Percentage (%)')
plt.grid(True)
plt.legend()
plt.tight_layout()

# Show plot
plt.show()
