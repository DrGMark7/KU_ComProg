# เขียนโปรเเกรมเพื่อเเสดงเงินสุทธิที่ได้จากการฝากธนาคารแสดงเป็นทศนิยม 2 ตำแหน่ง ซึ่งสามารถคำนวณได้จากสูตรข้างล่างนี้

    
# A=P(1+r/n)nt
# เมื่อ P คือเงินตั้งต้น
#     r คืออัตราดอกเบี้ย
#     n คือจำนวนครั้งการจ่ายดอกเบี้ยทบต่อต่อปี
#     t เป็นจำนวนปี

p = float(input("Input principal amount (P): "))
r = float(input("Input annual nominal interest rate (r): "))
n = float(input("Input # of times the interest is compounded per year (n): "))
t = float(input("Input # of years (t): "))
print(f"Final amount: {p*((1+(r/n))**(n*t)):.2f}")