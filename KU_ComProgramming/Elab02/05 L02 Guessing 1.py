#จงเขียนโปรแกรมสำหรับเล่นเกมทายตัวเลข โดยกำหนดให้โปรแกรมสร้างเลขเป้าหมาย (target) ที่มีค่าตั้งแต่ 0 - 100 แล้วรับตัวเลขจากผู้เล่นที่ทายเข้ามา กำหนดให้เป้าหมายเท่ากับ 72
target = 72
x = float(input("Enter your guess (0 - 100): "))
if x in range(0,101,1):
    if x == target:
        print("Congratulations, your guess is correct.")
    else:
        print("Sorry, your guess is wrong, try again later.")
else:
    print("Sorry, out of range, try again later.")