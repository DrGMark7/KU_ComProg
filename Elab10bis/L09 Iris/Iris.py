import json
import os

def read_json(filename):
    with open(filename) as f:
        data = f.read()
        data = json.loads(data)
    return data

#Filename = str(input("File name: "))
Filename = os.path.dirname(os.path.abspath(__file__))+'\\Iris1.json'
#Type = str(input("type : "))
Type = 'sepalLength'
Data = read_json(Filename)

type_List , Type_List = [],[] 
for item in Data:
    type_List.append(item.get('species'))

for item in type_List:
    if item not in Type_List:
        Type_List.append(item)


Type_Dict = {score: 0 for score in Type_List}
Nums_Dict = {score: 0 for score in Type_List}
mean = {score: 0 for score in Type_List}

for item in Data:
    ID = item.get('species')
    if ID in Type_List:
        Type_Dict[ID] += item.get(Type)
        Nums_Dict[ID] += 1

Package = zip(Type_List,list(Type_Dict.values()),list(Nums_Dict.values()))
for i,j,k in Package:
    mean[i] = j/k

sorted(mean,reverse=True,key=lambda x:x[0])

for key,value in zip(mean.keys(),mean.values()):
    print(f'{key} = {value:.2f}')

    

