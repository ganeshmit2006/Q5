import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

np.random.seed(42)

sns.set_style("whitegrid")
sns.set_context("talk")

months = pd.date_range("2024-01-01", periods=12, freq="MS").strftime("%b")
segments = ["Standard", "Premium", "Enterprise"]

data = []

for segment in segments:
    base = {"Standard": 100000, "Premium": 220000, "Enterprise": 400000}[segment]
    trend = np.linspace(0, 30000, 12)
    seasonality = 8000 * np.sin(np.linspace(0, 2 * np.pi, 12))
    noise = np.random.normal(0, 5000, 12)
    revenue = base + trend + seasonality + noise
    for i, month in enumerate(months):
        data.append({"Month": month, "Customer Segment": segment, "Revenue ($)": revenue[i]})

df = pd.DataFrame(data)

plt.figure(figsize=(8, 8))

lineplot = sns.lineplot(
    data=df,
    x="Month",
    y="Revenue ($)",
    hue="Customer Segment",
    marker="o",
    linewidth=2.5,
    #cbar_kws={"shrink": 0.8}
)

# Enforce square aspect ratio for each data point segment (approximates heatmap cells)
##lineplot.set(aspect="equal")

# Add grid lines resembling heatmap cell borders
#plt.grid(True, linewidth=0.5)

plt.title("Monthly Revenue Trend by Customer Segment", fontsize=16, weight="bold")
plt.xlabel("Month", fontsize=14)
plt.ylabel("Revenue ($)", fontsize=14)
plt.legend(title="Customer Segment")

# Shrink padding around figure to prevent tight bbox over-cropping
#plt.subplots_adjust(left=0.12, right=0.92, top=0.9, bottom=0.12)

#plt.savefig("chart.png", dpi=64, bbox_inches='tight')
#plt.close()

plt.savefig("temp.png", dpi=64, bbox_inches='tight')
plt.close()
from PIL import Image
im = Image.open("temp.png")
im = im.resize((512, 512), Image.LANCZOS)
im.save("chart.png")
