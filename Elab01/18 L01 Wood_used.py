# wood_used โรงงานไม้
# โรงงานเฟอร์นิเจอร์แห่งหนึ่งรับผลิตโต๊ะสองขนาดคือขนาดใหญ่และขนาดเล็ก
# โต๊ะขนาดใหญ่ใช้ไม้แผ่น 2 แผ่น และไม้ท่อน 6 ท่อน
# โต๊ะขนาดเล็กใช้ไม้แผ่น 1 แผ่น และไม้ท่อน 4 ท่อน
# โรงงานต้องผลิตโต๊ะใหญ่ M โต๊ะ และโต๊ะเล็ก N โต๊ะ จงเขียนโปรแกรมที่รับค่ M และ N จากผู้ใช้และคำนวณว่าโรงานจะต้องใช้ไม้ทั้งหมดกี่แผ่น และกี่ท่อน ตามลำดับ

# ข้อมูลเข้า
# มีหนึ่งบรรทัด เป็นตัวเลขจำนวนเต็มสองตัวคั่นด้วยช่องว่าง เลขตัวแรกคือ M ตัวที่สองคือ N
# โดยที M และ N มีค่าไม่น้อยกว่าศูนย์และไม่เกิน 1,000,000 นอกจากนี้ M และ N จะไม่เป็นศูนย์พร้อมกัน

M = int(input("M: "))
N = int(input("N: "))
print(f"{(2*M)+N} {(6*M)+(4*N)}")