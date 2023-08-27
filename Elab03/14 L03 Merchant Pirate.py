wA = float(input("weight of cargo to A: "))
wB = float(input("weight of cargo to B: "))
wC = float(input("weight of cargo to C: "))
wO = float(input("weight of cargo to O: "))
pA = float(input("price of cargo to A: "))
pB = float(input("price of cargo to B: "))
pC = float(input("price of cargo to C: "))
pO = float(input("price of cargo to O: "))
pS = float(input("price of supply: "))
dOA = float(input("distance O to A: "))
dAB = float(input("distance A to B: "))
dBC = float(input("distance B to C: "))
dCO = float(input("distance C to O: "))
from math import *
def travel_speed(w):
    return 90/(30+w)+5

from math import ceil

def travel_time(s, d):
    hours = d/s
    day = ceil(hours/24)
    return day

def cal_sub_profit(distance, net_weight, sell_weight, cargo_price_per_ton, supply_price_per_day):
    speed = travel_speed(net_weight)
    cargo_price = sell_weight*cargo_price_per_ton
    supply_price = travel_time(speed,distance)*supply_price_per_day
    return cargo_price - supply_price

def calculate_profit():
    w_net = wA+wB+wC+wO
    profit = cal_sub_profit(dOA,w_net,wA,pA,pS)
    
    w_net = wB+wC+wO
    profit = profit + cal_sub_profit(dAB,w_net,wB,pB,pS)
    
    w_net = wC+wO
    profit = profit + cal_sub_profit(dBC,w_net,wC,pC,pS)

    w_net = wO
    profit = profit + cal_sub_profit(dCO,w_net,wO,pO,pS)

    return profit

print(f"result profit is {calculate_profit():.3f}")