# Step 1: Create a list of scores
scores = [78, 85, 92, 67, 89, 94, 56, 83]

# Step 2: Sort the list in ascending order
scores.sort()

# Step 3: Determine the lowest and highest scores
lowest_score = scores[0]
highest_score = scores[-1]

# Step 4: Calculate the average score
average_score = sum(scores) / len(scores)

# Display the sorted scores and the computed values
print("Sorted Scores:", scores)
print("Lowest Score:", lowest_score)
print("Highest Score:", highest_score)
print("Average Score:", round(average_score, 2))
