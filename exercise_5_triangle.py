
def is_triangle(a, b, c):
    if a+b >= c and b+c >= a and c+a >= b:
        print("Yes")
    else:
        print("No")

print("To verify if three sticks make a triangle")
a = input("Enter first side length: ")
b = input("Enter second side length: ")
c = input("Enter third side length: ")

print("\nResult is: ")
is_triangle(int(a), int(b), int(c))