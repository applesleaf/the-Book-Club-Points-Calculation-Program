# Part 2: Book Club Points Calculation

# Ask for the number of books purchased this month
num_books = int(input("Enter the number of books purchased this month: "))

# Determine the number of points awarded based on the number of books purchased
if num_books < 2:
    points = 0
elif num_books < 4:
    points = 5
elif num_books < 6:
    points = 15
elif num_books < 8:
    points = 30
else:
    points = 60

# Display the number of points awarded
print(f"Number of points awarded: {points}")