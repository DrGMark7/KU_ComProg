from collections import OrderedDict
import numpy as np
A = int(input("A: "))
B = int(input("B: "))
C = int(input("C: "))

D = {"A":A,"B":B,"C":C}

keys = list(D.keys())
values = list(D.values())
sorted_value_index = np.argsort(values)
sorted_dict = {keys[i]: values[i] for i in sorted_value_index}



