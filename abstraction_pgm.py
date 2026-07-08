from abc import abstractmethod,ABC

class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass
    
    def display(self):
        pass

class Bike(Vehicle):
    def start(self):
        print("Starting bike")

ob=Bike()
ob.start()

