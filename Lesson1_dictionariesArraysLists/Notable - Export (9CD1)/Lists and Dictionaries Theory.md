---
title: Lists and Dictionaries Theory
created: '2024-04-04T21:21:56.053Z'
modified: '2024-04-04T21:25:23.608Z'
---

# Lists and Dictionaries Theory

Task 1: Dictionaries

Write a function called calculate_average_score that takes a dictionary of student names and their corresponding scores as input and returns the average score of all students. Include Tests to check that they work. Look at the sample code. For task 1 and 2 you will online need to create one ```defFunction()``` and suitable tests.

Task 2: Lists

Task:
Write a function called find_max_value that takes a list of numbers as input and returns the maximum value from the list.

Example:

```
guest_list = []

def add_guest(guest):
    guest_list.append(guest)

def remove_guest(guest):
    if guest in guest_list:
        guest_list.remove(guest)
        return True
    else:
        return False

def total_guests():
    return len(guest_list)

def display_guest_list():
    return guest_list

# Unit tests
add_guest("Alice")
add_guest("Bob")
add_guest("Charlie")

assert total_guests() == 3
assert remove_guest("Bob") == True
assert total_guests() == 2
assert display_guest_list() == ['Alice', 'Charlie']

```
