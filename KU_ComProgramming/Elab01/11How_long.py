# [How long] เมื่อไหร่จะคืน
# น้องได้ทวงเพื่อนที่ยืมหนังสือไป 7 ปีแล้ว ไม่ยอมคืนสักที ซึ่งเพื่อนตอบกลับมา 3 ประโยคแล้วบอกว่า "ขอยืมอีก ( ความยาวของประโยค 1 บวก ความยาวประโยค 2 จากนั้นคูณ ความยาวประโยค 3 ) ชั่วโมง"

# น้องที่อยากรู้ว่าเมื่อไหร่จะได้หนังสือคืนจึงลองคำนวณตามที่เพื่อนบอก

a = len(str(input("First sentence: ")))
b = len(str(input("Second sentence: ")))
c = len(str(input("Third sentence: ")))
print((a+b)*c)