# Qualification เข้าสู่วงการบอล
# เด็กชายบัซซี่มีความฝันอยากเป็นนักฟุตบอลอาชีพ หลังจากฝึกซ้อมฟุตบอลที่สนามเช่าอย่างเต็มที่แล้ว เขาจึงไปเข้าคัดตัวกับสโมสร นครราชสีมา F.C. ในขั้นแรกจะมีการตรวจร่างกายก่อน และหนึ่งในนั้นมีการวัดค่า BMI โดยมีเกณฑ์ดังนี้

# เกณฑ์ค่า BMI                           ผลการประเมิน
# ตั้งแต่ 30 ขึ้นไป                             You're in the obese range.
# ตั้งแต่ 25 ขึ้นไป แต่น้อยกว่า 30        You're in the overweight range.
# ตั้งแต่ 18.6 ขึ้นไป แต่น้อยกว่า 25     You're in the healthy weight range.
# น้อยกว่า 18.6                               You're in the underweight range.

# จงเขียนโปรแกรมที่รับค่า ส่วนสูง และน้ำหนัก แล้วคำนวณค่า BMI แล้วแสดงผลลัพธ์ตามเกณฑ์
    
# BMI=Weight(kg)./(Height(m).)2

w = float(input("Weight: "))
h = float(input("Height: "))
bmi = round((w/((h/100)**2)),1)
if bmi >= 30:
    t = "You're in the obese range."
elif bmi < 30 and bmi >= 25:
    t = "You're in the overweight range."
elif bmi < 25 and bmi >= 18.6:
    t = "You're in the healthy weight range."
else:
    t = "You're in the underweight range."
print(f"Your BMI is {bmi} {t}")