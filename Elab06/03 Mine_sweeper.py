Grid_size = list(map(int, input("Grid Size: ").split()))
Number_mine = int(input("Number of mine(s): "))

index_mine = []
for i in range(Number_mine):
    index_mine.append(list(map(int, input(f"Mine#{i+1}: ").split())))

# สร้างแผนที่ Minesweeper และกำหนดค่าเริ่มต้นให้เป็น "0"
Genarate_map = [[0 for _ in range(Grid_size[0])] for _ in range(Grid_size[1])]

for i in index_mine:
    # ตำแหน่งของรัศมีแรงระเบิด
    x, y = i

    # ตั้งค่าตำแหน่งที่ป้อนเข้าไปเป็น "X"
    Genarate_map[y][x] = "X"

    # ตรวจสอบตำแหน่งของจุดที่อยู่รอบๆ รัศมีแรงระเบิด
    for dx in [-1, 0, 1]:
        for dy in [-1, 0, 1]:
            new_x, new_y = x + dx, y + dy
            # ตรวจสอบว่าตำแหน่งใหม่อยู่ในขอบเขตของแผนที่
            if 0 <= new_x < Grid_size[0] and 0 <= new_y < Grid_size[1]:
                # ตรวจสอบว่าตำแหน่งใหม่ไม่ใช่รัศมีแรงระเบิด
                if Genarate_map[new_y][new_x] != "X":
                    # เปลี่ยนค่าที่ตำแหน่งใหม่เป็น "1"
                    Genarate_map[new_y][new_x] += 1

# แสดงแผนที่ Minesweeper ที่สร้างขึ้น
for row in Genarate_map:
    for i in row:
        print(str(i),end=" ")
    print()



