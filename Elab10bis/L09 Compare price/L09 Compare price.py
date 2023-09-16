import json
import os

def read_json(filename):
    with open(filename) as f:
        data = f.read()
        data = json.loads(data)
    return data


Filename = os.path.dirname(os.path.abspath(__file__))+'\\test3.json'
Data = read_json(Filename)

Product = input()

Filter_data = []
for i in Data:
    if i.get('Product type') == Product:
        Filter_data.append(i)

def get_cost(Filter_data):
    return int(Filter_data['Cost'])
sorted_data = sorted(Filter_data, key=get_cost,reverse=False)

print(f'{sorted_data[0].get("Brand")} : {sorted_data[0].get("Cost")}')

