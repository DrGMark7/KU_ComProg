import json
import os

def read_json(filename):
    new_data = []
    with open(filename) as f:
        data = f.read()
        data = json.loads(data)
        for i in range(1,int(list(data.keys())[-1])+1,1):
            item = data.get(str(i))
            if item == None:
                pass
            else:
                new_data.append(item)
    return new_data

#* Filename = str(input("Filename : "))
Filename = os.path.dirname(os.path.abspath(__file__))+'\\championinfo.json'

Case = int(input("Case : "))

if Case == 0:
    Character = list(map(int, input("Character : ").split(',')))
else:
    Character = str(input("Character : ")).split(',')

Data = read_json(Filename)

def search_by_char(char):
    dis_data = []

    for item in Data:
        if Case == 0:
            for c in char:
                if item.get('id') == c:
                    dis_data.append(item)
        elif Case == 1:
            for c in char:
                if item.get('name')[0] == c:
                    dis_data.append(item)
        elif Case == 2:
            for c in char:
                List_check = (item.get('title')).split()
                for word in ['the', 'The']:
                    try:
                        List_check.remove(word)
                    except ValueError:
                        pass
                if c == List_check[0][0]:
                    dis_data.append(item)

    return dis_data


Searched = search_by_char(Character)

for i in Searched:
    print(f'{i.get("id")}\t---\t{i.get("name")}\t---\t{i.get("title")}')