class Fraction:
    def __init__(self,numerator,denominator) -> None:
        self.numerator = numerator
        self.denominator = denominator
        self.min_numerator = 0
        self.min_denominator = 0

    def resize(self):
        List_1 ,List_2 = [],[]
        for i,j in zip(range(1,self.numerator+1),range(1,self.denominator+1)):
            if self.numerator % i == 0:
                List_1.append(i)
            if self.denominator % j == 0:
                List_2.append(j)

        same_factor = list(set(List_1).intersection(set(List_2)))
        try:
            min_factor = same_factor[-1]
        except:
            min_factor = 1

        if self.numerator == 0:
            self.denominator  = 1

        self.min_numerator = self.numerator / min_factor
        self.min_denominator = self.denominator / min_factor

    def __str__(self) -> str:
        self.resize()
        return f"{round(self.min_numerator)} / {round(self.min_denominator)}"
    
    def evaluate(self):
        return self.numerator / self.denominator
    
    def multiply(self, n):
        self.numerator = self.numerator*n
        self.resize()
        return self

    
    def add(self, n):
        new_add = n * self.denominator
        self.numerator += new_add
        self.resize()
        return self


    def __add__(self, Fraction2):    
        new_denominator = self.denominator * Fraction2.denominator
        new_numerator1 = self.numerator * Fraction2.denominator
        new_numerator2 = Fraction2.numerator * self.denominator 

        result = Fraction(new_numerator1 + new_numerator2, new_denominator)
        return result

    def __mul__(self, Fraction2):
        new_numerator = self.numerator * Fraction2.numerator 
        new_denominator = self.denominator * Fraction2.denominator
        
        result = Fraction(new_numerator, new_denominator)
        return result


print((Fraction(1,2) + Fraction(3,4)).multiply(0))
        

    
