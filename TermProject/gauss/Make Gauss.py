import random

# จำนวนตัวเลขที่ต้องการสร้าง
n = 50  # แก้ค่าตามที่ต้องการ

# สร้างไฟล์ข้อความ
with open('gauss20.txt', 'w') as file:
    for i in range(n):
        # สร้าง n ตัวเลขสุ่มและเขียนลงในไฟล์บนบรรทัดเดียวกัน
        random_numbers = [random.randint(1, 10) for _ in range(n + 1)]
        line = ' '.join(map(str, random_numbers))
        file.write(line + '\n')