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
