import matplotlib.pyplot as plt

categories = ["Math","Science","English","History","Geography"] # x-axis
scores = [88,92,80,75,85] # y-axis

plt.bar(categories,scores,color = "orange")
plt.xlabel("Subjects")
plt.ylabel("Scores")
plt.title("Exams scores by subjects")

plt.grid()
plt.show()
