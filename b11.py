s = "abcd1234"
a = "abc"
b = "d12"
c = "1234"
# Tìm kiếm xâu con
# Cách 1: Dùng toán tử in
x = a in s
# Cách 2: Dùng hàm find()
y = s.find(b, 0, 5)
z = s.find(c)
print(x)
print(y)
print(z)

# Một số lệnh cơ bản với xâu
# Lệnh split() dùng để tách xâu thành các mảng ký tự
s = "a b c d1 234"
x = s.split( )
print(x)

f = "1;2;3;4;5;6;7;8;9"
y = f.split(";")
print(y)

# Thay thế giá trị bằng replace
txt = "i like bananas"
x = txt.replace("bananas", "apples")
print(x)

txt1 = "1 + 1 + 1 = 3"
y = txt1.replace("+", "-", 1)
print(y)

ho = "Dao"
ten_dem = "Trung"
ten = "Kien"
print(ho + ten_dem + ten)

# Bài 1: Cho chuỗi sau, yêu cầu người dùng nhập vào 1 chuỗi, kiểm tra xem chuỗi đó có phải là chuỗi con trong đề bài hay không
txt = "TRONGTUONG,NHANKIET,DANGPHUONG,QUOCAN,GIALINH,HOANGHUNG"
x = input("Nhập vào 1 chuỗi: ")
if x in txt:
    print("Có")
else:
    print("Không")

# Bài 2: Cho username:password là MindX:12345. Yêu cầu người dùng nhập vào username và password, kiểm tra xem có khớp với đề bài hay không. Nếu khớp username và password thì thông báo ĐĂNG NHẬP THÀNH CÔNG.
account = "MindX:12345"
user_and_pass = account.split(":")
print(user_and_pass)
username = user_and_pass[0]
password = user_and_pass[1]

input_username = input("Nhập vào username: ")
input_password = input("Nhập vào password: ")
if input_username == username and input_password == password:
    print("ĐĂNG NHẬP THÀNH CÔNG!!!")
else:
    print("ĐĂNG NHẬP THẤT BẠI!!!")
