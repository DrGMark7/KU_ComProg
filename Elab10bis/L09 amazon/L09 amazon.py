import json
import os

def read_json(filename):
    data = []
    with open(filename) as file:
        for line in file:
            try:
                json_data = json.loads(line)
                data.append(json_data)
            except:
                pass
    return data

#Filename = str(input("file name: "))
Filename = os.path.dirname(os.path.abspath(__file__))+'\\amazon1.json'
Request = int(input("input: "))

Data = read_json(Filename)

class Amazon_database:
    def __init__(self,data) -> None:
        self.data = data
        self.num_review = len(self.data)
        self.num_reviewer, self.reviewer = 0 , []
        self.num_product , self.product  = 0 , []
        self.user_per_review = None
        self.proID_per_review = None
        self.proID_per_Score = None
        self.category = []

        for item in self.data:
            self.reviewer.append(item['reviewerID'])
            self.product.append(item['productName'])
            self.category.append(item['category'].split(' > '))

    def get_number_review(self):  #* 1 
        return self.num_review
    
    def get_number_reviewer(self):
        self.num_reviewer = len(set(self.reviewer))
        return self.num_reviewer
    
    def get_number_product(self):
        self.num_product = len(set(self.product))
        return self.num_product
    
    def get_number_main_product(self):
        main_category = []
        for item in self.category:
            main_category.append(item[0])
        
        return len(set(main_category))
    
    def get_number_sub1_product(self):
        sub1_category = []
        for item in self.category:
            sub1_category.append(item[1])

        return len(set(sub1_category))
    
    def get_most_reviewer(self):
        self.user_per_review = {name: 0 for name in self.reviewer}
        for item in self.data:
            ID = item.get('reviewerID')
            if ID in self.reviewer:
                self.user_per_review[ID] += 1

        most_reviewer = max(self.user_per_review.values())
        for key,value in self.user_per_review.items():
            if value == most_reviewer:
                return key

    def get_name_pop_productID(self):

        self.proID_per_Score = {name: 0 for name in self.product}
        self.proID_per_review = {name: 0 for name in self.product}

        for item in self.data:
            ID = item.get('productName')
            if ID in self.product:
                self.proID_per_Score[ID] += item.get('overall')
                self.proID_per_review[ID] += 1
        
        mean = {name: 0 for name in self.product}
        Package = zip(list(self.proID_per_Score.values()),list(self.proID_per_review.values()),list(self.proID_per_Score.keys()))
        for score,time,keys in Package:
            mean[keys] = score/time

        most_Score = max(mean.values())
        Product_most_score = []
        for key,value in mean.items():
            if value == most_Score:
               Product_most_score.append(key)
        
        Check = {name: 0 for name in Product_most_score}
        for item in self.data:
            ID = item.get('productName')
            if ID in Product_most_score:
                Check[ID] += 1

        Best_Product = max(Check.values())
        for key,value in Check.items():
            if value == Best_Product:
               return key

    def get_best_averagescore(self):
        
        self.proID_per_Score = {name: 0 for name in self.product}
        self.proID_per_review = {name: 0 for name in self.product}

        for item in self.data:
            ID = item.get('productName')
            if ID in self.product:
                self.proID_per_Score[ID] += len(item.get('reviewText').split())
                self.proID_per_review[ID] += 1
        
        mean = {name: 0 for name in self.product}
        Package = zip(list(self.proID_per_Score.values()),list(self.proID_per_review.values()),list(self.proID_per_Score.keys()))
        for score,time,keys in Package:
            mean[keys] = score/time

        most_Score = max(mean.values())
        for key,value in mean.items():
            if value == most_Score:
               return key
        

    #* 8 : name product is len(review) / len(product) 

AWS = Amazon_database(Data)

if Request == 1:
    print(AWS.get_number_review())
elif Request == 2:
    print(AWS.get_number_reviewer())
elif Request == 3:
    print(AWS.get_number_product())
elif Request == 4:
    print(AWS.get_number_main_product())
elif Request == 5:
    print(AWS.get_number_sub1_product())
elif Request == 6:
    print(AWS.get_most_reviewer())
elif Request == 7:
    print(AWS.get_name_pop_productID())
elif Request == 8:
    print(AWS.get_best_averagescore())
else:
    print('')