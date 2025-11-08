import matplotlib.pyplot as plt

#Define data
values = [40, 30, 15, 15]
labels = ["Rent", "Groceries", "Transport", "Savings"]
explode = [0.1, 0, 0, 0]

plt.pie(values, labels=labels, autopct="%.1f%%", explode=explode)
plt.title("Monthly Budget Pie Chart")
plt.show()
