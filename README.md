# TH_TEST1_CNPM
# Kiểm tra CNPM

## Thông tin cá nhân
- **Họ và tên:** Nguyễn Thị Hiền  
- **Lớp:** Tin 2B  
- **Mã SV:** 24S10200278

# Hàm tính UCLN bằng thuật toán Euclid
def ucln(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Hàm tính BCNN
def bcnn(a, b):
    return a * b // ucln(a, b)

# Nhập hai số
num1 = int(input("Nhập số thứ nhất: "))
num2 = int(input("Nhập số thứ hai: "))

# Tính BCNN
print(f"BCNN của {num1} và {num2} là: {bcnn(num1, num2)}")

# Nhập 3 cạnh
a = float(input("Nhập cạnh a: "))
b = float(input("Nhập cạnh b: "))
c = float(input("Nhập cạnh c: "))

# Kiểm tra điều kiện tam giác
if a + b > c and a + c > b and b + c > a:
    print("Đây là 3 cạnh hợp lệ của một tam giác.")

    # Kiểm tra tam giác đều
    if a == b == c:
        print("Tam giác đều")
    # Kiểm tra tam giác cân
    elif a == b or a == c or b == c:
        # Kiểm tra vuông cân
        sides = sorted([a, b, c])
        if abs(sides[0]**2 + sides[1]**2 - sides[2]**2) < 1e-8:
            print("Tam giác vuông cân")
        else:
            print("Tam giác cân")
    else:
        # Kiểm tra vuông hay nhọn/tù
        sides = sorted([a, b, c])  # sắp xếp để sides[2] là cạnh lớn nhất
        if abs(sides[0]**2 + sides[1]**2 - sides[2]**2) < 1e-8:
            print("Tam giác vuông")
        elif sides[0]**2 + sides[1]**2 > sides[2]**2:
            print("Tam giác nhọn")
        else:
            print("Tam giác tù")
else:
    print("3 cạnh này không tạo thành tam giác.")
