numbers = [7, 5.5, 2, 4, 3, 3.5, 5, 6, 1, 1, 1.1, 10, 8, 9, 8.5]
STUDENT_ID = "12349"  

print(f"Initial list: {numbers}\n")

# Ascending sort
# We use the sort() method, which modifies the list in place in ascending order
numbers.sort()
print("1. Result of ascending sort:")
print(numbers, "\n")

# Descending sort
# We use the reverse=True argument to flip the order to descending
numbers.sort(reverse=True)
print("2. Result of descending sort:")
print(numbers, "\n")

# Indicating the element that matches the last digit of the student ID and its index
# We extract the last character from the STUDENT_ID constant and convert it to an integer
last_digit = int(STUDENT_ID[-1])
print(f"3. Searching for the element based on the student ID ({STUDENT_ID}):")
print(f"The last digit of your student ID is: {last_digit}")

# Checking if this digit exists in our list and point out its position
if last_digit in numbers:
    # The .index() method returns the position of the first occurrence of the element (0-based indexing)
    found_index = numbers.index(last_digit)
    print(f"Success! The number {last_digit} is in the list at index: {found_index}")
else:
    print(f"Information: The number {last_digit} is not in the list.")
print()

# Indicating how many numbers are in the list
# We use the built-in len() function, which returns the number of items in a collection
total_elements = len(numbers)
print("4. Counting the elements in the list:")
print(f"There are exactly {total_elements} numbers in the list.")
