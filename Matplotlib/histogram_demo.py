import matplotlib.pyplot as plt
import numpy as np

ages= np.random.normal(35,  10,  100)
plt.hist(ages, bins=10, color="skyblue", edgecolor="black")

 #Add Inbels and title
plt.xlabel("Age Range")
plt.ylabel("Number of People")
plt.title("Age Distribution Histogram")

plt.show()