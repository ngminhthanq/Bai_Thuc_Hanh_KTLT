print("Nguyen Minh Thắng","\nMSSV: 235752021610097")
class Circle:
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14159 * self.radius**2

    def circumference(self):
        return 2 * 3.14159 * self.radius

circle = Circle(5)

print(f"Diện tích hình tròn: {circle.area()}")
print(f"Chu vi hình tròn: {circle.circumference()}")

