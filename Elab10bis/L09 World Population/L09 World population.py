import json
import os

def read_json(filename):
    with open(filename) as f:
        data = f.read()
        data = json.loads(data)
    return data

class World_Population:
    def __init__(self,data) -> None:
        self.data = data
        self.country_name = []
        self.population = []
        self.WorldRate = []

        self.name_country_start_C = []

        for country in self.data:
            self.country_name.append(country.get('country'))
            self.population.append(int(country.get('population')))
            self.WorldRate.append(float(country.get('World')))

    def get_num_country(self):
        return len(self.country_name)

    def get_num_population(self):
        return sum(self.population)
    
    def get_country_by_char(self):

        Result = []
        for country in self.country_name:
            if country[0] == 'C':
                self.name_country_start_C.append(country)
            if len(country) > 5:
                Result.append(country)
        return len(Result)

    def get_country_start_C(self):
        return len(self.name_country_start_C)

    def get_num_population_by_range(self,Range):

        Range_A,Range_B,Result = Range[0],Range[-1],[]
        if Range_A == 0:
            Range_A = min(self.population)
        if Range_B == 0:
            Range_B = max(self.population)

        for p in self.population:
            if Range_A <= p <= Range_B:
                Result.append(p)

        return len(Result)
    
    def get_country_by_pop(self,Range):

        Result = []
        for i in range(Range[0]-1,Range[-1]):
            Rate = self.WorldRate[i]
            Result.append(Rate)
        return f'{sum(Result)*100:.2f}'

Filename = os.path.dirname(os.path.abspath(__file__))+'\\worldpopulation.json'
#Filename = str(input("File Name :"))
Data = read_json(Filename)
World_Pop = World_Population(Data)
Input = int(input('Input : '))
if Input == 1:
    print(World_Pop.get_num_country())
elif Input == 2:
    print(World_Pop.get_num_population())
elif Input == 3:
    World_Pop.get_country_by_char()
    print(World_Pop.get_country_start_C())
    print(World_Pop.get_country_by_char())
elif Input == 4:
    print(World_Pop.get_num_population_by_range([500000000,0]))
    print(World_Pop.get_num_population_by_range([250000000,750000000]))
    print(World_Pop.get_num_population_by_range([0,10000000]))
elif Input == 5:
    print(World_Pop.get_country_by_pop([1,20]))
    print(World_Pop.get_country_by_pop([50,150]))
