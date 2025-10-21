import matplotlib.pyplot as plt


with open("log.txt", "r") as f:
    data = [float(line.strip()) for line in f if line.strip()]


plt.hist(data, bins=10, color = "skyblue", edgecolor="black")

plt.title("Time Perception Accuracy")
plt.xlabel("Seconds Guessed")
plt.ylabel("Frequency")

plt.legend()

plt.show()
