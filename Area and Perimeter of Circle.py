import math

class Circle:
    
    def __init__(self, radius):
        
        if not isinstance(radius, (int, float)) or radius < 0:
            raise ValueError("Radius must be a non-negative number.")
        self.radius = radius

    def area(self):
        
        return math.pi * (self.radius ** 2)

    def perimeter(self):
       
        return 2 * math.pi * self.radius

# Take input from the user
try:
    user_radius = float(input("Enter the radius of the circle: "))
    
    # Create a Circle object
    my_circle = Circle(user_radius)

    # Calculate and print the area and perimeter
    print(f"Area of the circle: {my_circle.area():.2f}")
    print(f"Perimeter of the circle: {my_circle.perimeter():.2f}")

except ValueError as e:
    print(f"Error: {e}")