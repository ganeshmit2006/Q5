import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Set random seed for reproducibility
np.random.seed(42)

# Set Seaborn style and context for professional appearance
sns.set_style("whitegrid")
sns.set_context("talk")

# Generate synthetic data for monthly revenue trends by segment
months = pd.date_range("2024-01-01", periods=12, freq="MS").strftime("%b")
segments = ["Standard", "Premium", "Enterprise"]

data = []
for segment in segments:
    base = {
        "Standard": 100_000,
        "Premium": 220_000,
        "Enterprise": 400_000,
    }[segment]
    trend = np.linspace(0, 30_000, 12)  # up to +30k/year trend
    seasonality = 8000 * np.sin(np.linspace(0, 2 * np.pi, 12))  # add seasonality
    noise = np.random.normal(0, 5000, 12)
    revenue = base + trend + seasonality + noise
    for i, month in enumerate(months):
        data.append({"Month": month, "Customer Segment": segment, "Revenue ($)": revenue[i]})

df = pd.DataFrame(data)

# Create the lineplot
plt.figure(figsize=(8, 8))  # 8 inches * 64 dpi = 512x512 pixels
sns.lineplot(
    data=df,
    x="Month",
    y="Revenue ($)",
    hue="Customer Segment",
    marker="o",
    palette="tab10",
    linewidth=2.5
)
plt.title("Monthly Revenue Trend by Customer Segment", fontsize=18, weight="bold")
plt.xlabel("Month", fontsize=14)
plt.ylabel("Revenue ($)", fontsize=14)
plt.legend(title="Customer Segment")


# Save as exactly 512x512 PNG
plt.savefig("chart.png", dpi=64)
plt.close()
