import numpy as np

# Take fitness data for 7 days
steps = []

for i in range(7):
    value = int(input(f"Enter steps for Day {i + 1}: "))
    steps.append(value)

steps = np.array(steps)

print("\n--- Fitness Analysis ---")

print("Total steps in week:", np.sum(steps))
print("Average steps per day:", np.mean(steps))
print("Maximum steps:", np.max(steps))
print("Minimum steps:", np.min(steps))

best_day = np.argmax(steps) + 1
print("Best day:", best_day)