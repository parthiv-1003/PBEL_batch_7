#function 

def HBTY(name, age):
    print("Hello World")
    print("HBTY :" + name)
    print("Age:" + str(age))
HBTY("john", 23)


class CAR:
    #attributes 
    def _inti_(self, brand, model, year):
        self.model = model
        self.year = year
    #method

    def start_engine(self):
        print("Engine Started ")

    def display(self):
        print(f"Car ")