# Nhập 3 cạnh
a = float(input("Nhập cạnh a: "))
b = float(input("Nhập cạnh b: "))
c = float(input("Nhập cạnh c: "))

# Kiểm tra điều kiện tam giác
if a + b > c and a + c > b and b + c > a:
    print("Đây là 3 cạnh hợp lệ của một tam giác.")
else:
    print("3 cạnh này không tạo thành tam giác.")
