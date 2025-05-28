print("Chào mừng bạn đến với Python!")  # Bài 1
ten, tuoi = "Tòng", 20; print("Xin chào", ten); print("Bạn", tuoi, "tuổi.")  # Bài 2
print("Xin chào", input("Nhập tên của bạn: "))  # Bài 3
print("Tổng là:", int(input("Nhập a: ")) + int(input("Nhập b: ")))  # Bài 4
print("Chẵn" if int(input("Nhập số: ")) % 2 == 0 else "Lẻ")  # Bài 5
import math; r = float(input("Bán kính: ")); print("CV:", 2*math.pi*r, "DT:", math.pi*r**2)  # Bài 6
print("Điểm TB:", round((float(input("Toán: "))+float(input("Văn: "))+float(input("Anh: ")))/3, 2))  # Bài 7
[print("Lặp", i) for i in range(1, 6)]  # Bài 8
i = 1; exec("print('Lần', i); i += 1\n"*5)  # Bài 9
n = int(input("Nhập số: ")); [print(f"{n} x {i} = {n*i}") for i in range(1, 11)]  # Bài 10
