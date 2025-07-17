import pandas as pd
import matplotlib.pyplot as plt

# Read the CSV data into a DataFrame
data = pd.read_csv("data1.csv")  # Replace with actual file path or use StringIO

'''# Bar Graph: Comparing all columns for each type
data.set_index("type", inplace=True)  # Set 'type' as index for better visualization
data.plot(kind="bar", figsize=(12, 8))
plt.title("Bar Graph of Different Factors of All Models")
plt.xlabel("Type")
plt.ylabel("Values")
plt.legend(title="Metrics")
plt.xticks(rotation=45)
plt.ylim(-5, 110)
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.savefig("bb.png", dpi=900)
plt.show()

# Line Graph: Trends across types
data.plot(kind="line", marker="o", figsize=(12, 8))  # Line plot with markers
plt.title("Line Graph of Different Factors of All Models")
plt.xlabel("Type")
plt.ylabel("Values")
plt.legend(title="Metrics")
plt.ylim(-5, 110)
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.xticks(rotation=45)
plt.savefig("cc.png", dpi=900)
plt.show()'''


# Plot
runs = list(range(1, 9))
transformer_fer = [71.2, 70.8, 73.5, 75.6, 72.0, 74.9, 72.5, 75.3]
emo_echo = [77.8, 80.1, 74.9, 82.0, 76.3, 77.1, 79.2, 78.4]

plt.figure(figsize=(10, 6))
plt.scatter(runs, transformer_fer, color='red', label='Transformer-based FER', s=100, marker='o')
plt.scatter(runs, emo_echo, color='blue', label='Emo Echo (Ours)', s=100, marker='o')

# Line connections for better visual trace
plt.plot(runs, transformer_fer, color='red', alpha=0.6)
plt.plot(runs, emo_echo, color='blue', alpha=0.6)

# Labels and styling
plt.title('Accuracy Comparison: Transformer-based FER vs Emo Echo', fontsize=14)
plt.xlabel('Run Number')
plt.ylabel('Accuracy (%)')
plt.xticks(runs)
plt.ylim(65, 85)
plt.grid(axis="y", linestyle="--", alpha=0.7)
plt.legend()

# Show plot
plt.savefig("dd.png", dpi=900)
plt.show()

