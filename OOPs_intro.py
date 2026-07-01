class Students:
    institute="OneTeam"

    def __init__(self,name,place):
        self.name=name
        self.place=place

    def display(self):
        print(f"Hello {self.name}, Welcome to {self.institute} you are from {self.place}")


std1=Students("Ebin","Vypin")

std2=Students("Sooraj","Kochi")


std1.display()
std2.display()