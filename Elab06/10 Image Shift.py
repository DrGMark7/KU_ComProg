H = int(input("Enter horizontal shift size: "))
V = int(input("Enter vertical shift size: "))
print("Enter image:")

image = []
while True:
    data = str(input(""))
    if data == "-1":
        break
    else:
        image.append(list(data))



def shift_image(image,h,v):
    new_image = []
    if h != 0 and v != 0:
        for _ in range(V):
            new_image.append("0"*len(image[0]))
        for row in image[:-V]:
            new_row = []
            for _ in range(H):
                new_row.append('0')
            for j in row[:-H]:
                new_row.append(j)
            new_image.append(new_row)
    elif h == 0 and v == 0:
        new_image = image
    else:
        if h == 0:
            for _ in range(V):
                new_image.append("0"*len(image[0]))
            for row in image[:-V]:
                new_image.append(row)
        else:
            for row in image:
                new_row = []
                for _ in range(H):
                    new_row.append('0')
                for j in row[:-H]:
                    new_row.append(j)
                new_image.append(new_row) 

    return new_image

print("After shift:")
for i in shift_image(image,H,V):
    print(''.join(i))

    