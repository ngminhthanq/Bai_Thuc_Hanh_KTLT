class Hinhchunhat:
    def __init__(self, chieu_dai, chieu_rong):
        self.chieu_dai = chieu_dai  # Chiều dài của hình chữ nhật
        self.chieu_rong = chieu_rong  # Chiều rộng của hình chữ nhật

    def dien_tich(self):
        return self.chieu_dai * self.chieu_rong  # Tính diện tích hình chữ nhật

# Tạo đối tượng Hinhchunhat với chiều dài và chiều rộng
hinh = Hinhchunhat(5, 3)

# Gọi phương thức để tính diện tích và in ra kết quả
print("Diện tích hình chữ nhật là:", hinh.dien_tich())
