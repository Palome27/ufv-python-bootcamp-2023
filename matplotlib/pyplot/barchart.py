import matplotlib.pyplot as plt

labels = ["A", "B", "C", "D"]
values = [10, 15, 8, 12]

# Create a bar chart
plt.bar(labels, values, color=["red", "blue", "green", "yellow"], label="Value bars")

# Add labels and title
plt.xlabel("Categories")
plt.ylabel("Values")
plt.title("Bar Chart with pyplot")
plt.legend()

# Display the plot
plt.show()
