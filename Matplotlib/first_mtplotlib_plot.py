import matplotlib.pyplot as plt

x_values = [1,2,3,4,5]
y_values = [2,4,6,8,10]

plt.plot(x_values, y_values)

plt.xlabel("X Axis Values")
plt.ylabel("Y Axis Values")
plt.title("My First Matplotlib Plot")
plt.plot(x_values, y_values, color = "green", marker = "o")
plt.grid()
plt.show()
