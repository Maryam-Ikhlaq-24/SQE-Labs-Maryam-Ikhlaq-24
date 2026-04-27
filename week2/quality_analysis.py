import numpy as np
import matplotlib.pyplot as plt

# Ratings (your actual values)
APP1_RATINGS = [5, 4, 5, 4, 5, 5, 5, 5]  # Chrome
APP2_RATINGS = [5, 4, 5, 4, 5, 5, 4, 5]  # Edge

# Labels
labels = [
    "Functional",
    "Performance",
    "Compatibility",
    "Usability",
    "Reliability",
    "Security",
    "Maintainability",
    "Portability"
]

# Convert to numpy
angles = np.linspace(0, 2 * np.pi, len(labels), endpoint=False).tolist()

# Close the loop
APP1_RATINGS += APP1_RATINGS[:1]
APP2_RATINGS += APP2_RATINGS[:1]
angles += angles[:1]

# Plot
plt.figure()
ax = plt.subplot(111, polar=True)

# Plot data
ax.plot(angles, APP1_RATINGS, label="Google Chrome")
ax.plot(angles, APP2_RATINGS, label="Microsoft Edge")

# Fill (optional)
ax.fill(angles, APP1_RATINGS, alpha=0.1)
ax.fill(angles, APP2_RATINGS, alpha=0.1)

# Labels
ax.set_xticks(angles[:-1])
ax.set_xticklabels(labels)

# Title
plt.title("ISO 25010 Quality Comparison (Mobile Browsers)")

# Legend
plt.legend(loc='upper right')

# Save image
plt.savefig("radar_chart.png")

# Show chart
plt.show()