class Numbers:
    def __init__(self,a,b):
        self.num1=a
        self.num2=b

    def __add__(self, other):
        return(self.num1+other.num1,self.num2+other.num2)
    
ob1=Numbers(12,3)
ob2=Numbers(34,8)

print(ob1+ob2)
