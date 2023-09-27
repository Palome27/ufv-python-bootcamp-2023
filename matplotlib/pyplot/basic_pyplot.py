import matplotlib.pyplot as plt

x = [0, 1, 2, 3, 4]
y1 = [0, 1, 4, 9, 16]
y2 = [0, 2, 8, 18, 32]

# Create line plots
plt.plot(x, y1, label="y = x^2", color="blue", marker="o")
plt.plot(x, y2, label="y = 2x^2", color="red", linestyle="--")

# Add labels and title
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.title("Line Plots with pyplot")
plt.legend()

# Display the plot
plt.show()
