import json
import os

def read_json(filename):
    with open(filename) as f:
        data = f.read()
        data = json.loads(data)
    return data

#* Filename = str(input("Filename : "))
Filename = os.path.dirname(os.path.abspath(__file__))+'\\test1.json'
Data_name = str(input("Data : "))

Data = read_json(Filename)

def Search(Data,name):

    for i in range(len(Data)):
        item , check = Data[i],False
        Keys = list(item.keys())
        for key in Keys:
            if item[key] == name:
                check = True
        if check == True:
            print('Found in blacklist')
            for j in range(len(Keys)):
                print(f'{Keys[j]} : {item[Keys[j]]}')
            return ''
        else:
            continue

    return print('Not found in blacklist')
            

Search(Data,Data_name)