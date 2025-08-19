import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Set random seed for reproducibility
np.random.seed(42)

# Set Seaborn style and context
sns.set_style("whitegrid")
sns.set_context("talk")

# Generate synthetic website performance data
n_samples = 300
data = pd.DataFrame({
    "page_load_time": np.random.normal(3, 0.5, n_samples),           # in seconds
    "server_response_time": np.random.normal(0.2, 0.05, n_samples),  # in seconds
    "time_to_first_byte": np.random.normal(0.1, 0.02, n_samples),    # in seconds
    "total_requests": np.random.poisson(50, n_samples),
    "error_rate": np.clip(np.random.normal(0.02, 0.01, n_samples), 0, 1),
    "user_satisfaction_score": np.random.normal(7, 1.5, n_samples),  # scale 1-10
})

# Compute correlation matrix
corr = data.corr()

# Create figure and heatmap
plt.figure(figsize=(8, 8))  # 8 inches * 64 dpi = 512 pixels
heatmap = sns.heatmap(
    corr,
    annot=True,
    fmt=".2f",
    cmap="coolwarm",
    square=True,
    linewidths=0.5,
    cbar_kws={"shrink": 0.8}
)

# Add title
plt.title("Website Performance Correlation Matrix", fontsize=16)

# Save figure with required dimensions
plt.savefig("chart.png", dpi=64, bbox_inches="tight")