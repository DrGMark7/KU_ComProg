# [full_divide] เพิ่มความกล้าหาญ
# เขียนโปรแกรมที่รับค่าตัวตั้งและตัวหาร เพื่อแสดงผลการหารในรูปของผลหารและเศษ
#     ตัวตั้ง = ตัวหาร * ผลหาร + เศษ

a = int(input("Input Dividend: "))
b = int(input("Input Divider: "))
print(f"{a} = {b} * {int(a//b)} + {int(a%b)}")