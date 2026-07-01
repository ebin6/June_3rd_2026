class Animals:
    def __init__(self,n):
        self.name=n


class Dog(Animals):
    def __init__(self,n):
        super().__init__(n)
        print(self.name)
    
dg1=Dog("Ricky")
