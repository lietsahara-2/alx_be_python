class Calculator:
   
    @staticmethod
    def add(a, b): #Returns the sum of two numbers. Use the @staticmethod decorator.
        return a+b
    
    @classmethod
    def multiply(cls, a, b):# Returns the product of two numbers. Use the @classmethod decorator.
        print(f"Calculation type: {cls.calculation_type}")
        return a*b
    #Define a class attribute calculation_type with a value of "Arithmetic Operations" that the multiply class method will reference.
    calculation_type = "Arithmetic Operations"
    def __init__(self, calculation_type):
        self.calculation_type = calculation_type