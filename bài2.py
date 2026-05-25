transaction = " nguyEN vAN a | PYTHON-01 | 15000000 | paid"

# xoá khoảng trắng
transaction = transaction.strip()

# tách theo |
parts = transaction.split("|")

# chuẩn hóa dữ liệu 
student_name = parts[0].strip().title()
course_code = parts[1].strip()
amount = parts[2].strip()
status = parts[3].strip().upper()

# in ra kết quả
print("Học viên :", student_name )
print("khoá học :", course_code)
print("số tiền :", amount)
print("trạng thái :", status)