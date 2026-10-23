# Laboratory3 Task1
# Program to solve the quadratic equation ax^2 + bx + c = 0

# While loop to ensure three valid numbers are entered
while True:
    try:
        print("Please enter the coefficients for the quadratic equation.")
        a = float(input("Enter a: "))
        b = float(input("Enter b: "))
        c = float(input("Enter c: "))
        break  # Exit the loop if the inputs are correct
    except ValueError:
        print("That is not a valid number! Please try again.\n")

print(f"\nSolving the equation: {a}x^2 + ({b})x + ({c}) = 0")

# Case 1: Linear equation (a == 0)
if a == 0:
    if b == 0:
        if c == 0:
            print("Identity equation (infinitely many solutions).")
        else:
            print("Contradictory equation (no solutions).")
    else:
        x = -c / b
        print(f"This is a linear equation. One solution: x = {x}")

# Case 2: Quadratic equation (a != 0)
else:
    # Calculating the discriminant (dt)
    dt = b**2 - 4 * a * c
    print(f"dt is: {dt}")

    # Conditional statement to check the number of solutions in the real numbers set
    if dt > 0:
        # Two solutions
        x1 = (-b - dt**0.5) / (2 * a)
        x2 = (-b + dt**0.5) / (2 * a)
        print(f"dt > 0. The equation has two solutions: x1 = {x1} and x2 = {x2}")
    elif dt == 0:
        # One solution
        x0 = -b / (2 * a)
        print(f"dt = 0. The equation has one solution: x0 = {x0}")
    else:
        # No real solutions
        print("dt < 0. The equation has no solutions in the set of real numbers.")
