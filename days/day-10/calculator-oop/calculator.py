class Calculator:
    def __init__(self):
        self.operation_map={
        '+':self.add,
        '-':self.subtract,
        '*':self.multiply,
        '/':self.divide,
   }
    def add(self,a,b):
        return a+b
    def subtract(self,a,b):
        return a-b
    def multiply(self,a,b):
        return a*b
    def divide(self,a,b):
        return a/b
    def compute(self,a,b,operation):
        return self.operation_map[operation](a,b)
    
