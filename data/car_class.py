class Origin():
    def __init__(self, origin):
        self.origin = origin
    
class Company(Origin):
    def __init__(self, origin, company):
        super().__init__(origin)
        self.company = company

class Car(Company):
    def __init__(self, origin, company, model, fuel):
        super().__init__(origin, company)
        self.model = model
        self.fuel = fuel

class Consumer(Car):
    def __init__(self, origin, company, model, fuel, age, pur_count):
        super().__init__(origin, company, model, fuel)
        self.age = age
        self.pur_count = pur_count
        
    def __str__(self):
        return f"origin={self.origin}, company={self.company}, model={self.model}, fuel={self.fuel}, age={self.age}, pur_count={self.pur_count}"