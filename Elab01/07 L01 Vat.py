# เวลาเราไปร้านอาหารนั้น เราก็จะต้องจ่ายภาษีเพิ่มขึ้นจากค่าอาหารเดิมเป็นจำนวน 7% โดยที่เราก็ไม่รู้เลยว่าร้านอาหารนั้นคิดถูกหรือผิด
# เนื่องจากน้องๆเก่งทางด้านเขียนโปรแกรม พี่ๆจึงอยากให้น้องเขียนโปรแกรมรับจำนวนเงินที่รวมภาษีแล้ว
# นำมาคำนวณว่าในจำนวนเงินนั้นเป็นค่าอาหารจริงกี่บาท และภาษีกี่บาท
# ให้หาค่าภาษีจาก ภาษี = ราคารวมภาษี - ราคาไม่รวมภาษี
# เนื่องจากโจทย์ไม่สามารถ format float ได้ ขอให้น้องหาค่า ราคาไม่รวมภาษี จาก ราคา = ราคารวมภาษี /107 *100

sp = float(input(f"summary price : "))
f = sp/107*100
print(f"food : {f}")
print(f"vat : {sp-f}")