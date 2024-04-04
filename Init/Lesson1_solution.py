def calculate_average_score(scores):
    total_score = sum(scores.values())
    average_score = total_score / len(scores)
    return average_score

# Test case
scores = {'Alice': 85, 'Bob': 92, 'Charlie': 78, 'David': 90}
assert calculate_average_score(scores) == 86.25

def find_max_value(numbers):
    max_value = max(numbers)
    return max_value

# Test case
numbers = [10, 25, 7, 42, 15]
assert find_max_value(numbers) == 42
