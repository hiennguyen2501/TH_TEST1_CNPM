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
