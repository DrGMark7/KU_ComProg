class Coin:
    def __init__(self, value = 1):
      self.value = value

    def __str__(self):
      return f'{self.value} Baht Coin'


class BankNote:
    def __init__(self, value = 20):
      self.value = value

    def __str__(self):
      return f'{self.value} Baht Banknote'
    

amount = int(input("Input amount : "))

baht = [1000, 500, 100, 50, 20, 10 , 5, 2 ,1]

for value in baht:
    if amount//value > 0:
        if value >= 20:
            print(f"You get {amount//value} of {BankNote(value)}")
            amount = amount - amount//value * value

        else:
            print(f"You get {amount//value} of {Coin(value)}")
            amount = amount - amount//value * value

# Amount = int(input("Input amount : "))

# Currency,coin,banknote = [1000,500,100,50,20,10,5,2,1],[],[]
# if Amount >= 0:
#     current_cash = Amount
# else:
#     current_cash = 0

# for i in Currency:
#     if i in [10,5,2,1]:
#         times = current_cash // i
#         current_cash -= times*i
#         coin.append(times)
#     elif i in [1000,500,100,50,20]:
#         times = current_cash // i
#         current_cash -= times*i
#         banknote.append(times)
#     else:
#         pass


# def print_cash(coin,banknote):
#     cash_currency = banknote + coin
#     for i,j in zip(cash_currency,range(len(cash_currency))):
#         if j in [0,1,2,3] and i != 0:
#             print(f"You get {i} of {BankNote(Currency[j])}")
#         elif j in [4,5,6,7,8] and i != 0:
#             print(f"You get {i} of {Coin(Currency[j])}")
#         else:
#             pass
    
# print_cash(coin,banknote)