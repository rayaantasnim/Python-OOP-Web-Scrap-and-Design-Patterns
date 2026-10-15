class Shape:
    def __init__(self, name):
        self.name = name

    def area(self, *side):
        if self.name == "square":
            return side[0] * side[0]

        elif self.name == "rectangle":
            return side[0] * side[1]

        elif self.name == "circle":
            return 3.1416 * side[0] * side[0]

        elif self.name == "triangle":
            return 0.5 * side[0] * side[1]

        elif self.name == "trapezoid":
            return 0.5 * (side[0] + side[1]) * side[2]


shape_name = input("Enter the shape name: ").lower()

if shape_name == "square":
    side = float(input("Enter the side length: "))
    shape_obj = Shape(shape_name)
    print(f"The area of this {shape_name} is: {shape_obj.area(side)}")

elif shape_name == "rectangle":
    length = float(input("Enter the length: "))
    width = float(input("Enter the width: "))
    shape_obj = Shape(shape_name)
    print(f"The area of this {shape_name} is: {shape_obj.area(length, width)}")

elif shape_name == "circle":
    radius = float(input("Enter the radius: "))
    shape_obj = Shape(shape_name)
    print(f"The area of this {shape_name} is: {shape_obj.area(radius)}")

elif shape_name == "triangle":
    base = float(input("Enter the base: "))
    height = float(input("Enter the height: "))
    shape_obj = Shape(shape_name)
    print(f"The area of this {shape_name} is: {shape_obj.area(base, height)}")

elif shape_name == "trapezoid":
    base1 = float(input("Enter the first base: "))
    base2 = float(input("Enter the second base: "))
    height = float(input("Enter the height: "))
    shape_obj = Shape(shape_name)
    print(f"The area of this {shape_name} is: {shape_obj.area(base1, base2, height)}")

else:
    print("Invalid Shape.")