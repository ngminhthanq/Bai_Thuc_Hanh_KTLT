class Circle(object):
    def __init__(self, r):
        self.radius = r  # Lưu bán kính của hình tròn

    def area(self):
        return self.radius**2 * 3.14  # Tính diện tích hình tròn

# Tạo một đối tượng Circle với bán kính là 2
aCircle = Circle(2)

# Gọi phương thức area để tính diện tích và in ra kết quả
print("diện tích là: ",aCircle.area())
