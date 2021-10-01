import math
def pythagoreanTheorem():
    get_a = int(input("What's 'a':"))
    get_b = int(input("What's 'b':"))
    solve_for_c = (get_a ** 2) + (get_b ** 2)
    c = f"C = {int(math.sqrt(solve_for_c))}"
    return c

equation = input("What math equation are you solving today? ")
if (equation == "pythagorean theorem" or "Pythgorean theorem" or "Pythagorean Theorem"):
    print(pythagoreanTheorem())
else:
    print("Something is wrong. Make sure pythagorean theorem is spelt right and make sure it is all lower case!")
    