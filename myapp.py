# Nhập 3 cạnh
a = float(input("Nhập cạnh a: "))
b = float(input("Nhập cạnh b: "))
c = float(input("Nhập cạnh c: "))

# Kiểm tra điều kiện tam giác
if a + b > c and a + c > b and b + c > a:
    print("Đây là 3 cạnh hợp lệ của một tam giác.")
else:
    print("3 cạnh này không tạo thành tam giác.")
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
