class patients:
    def __init__(self, name, age , admission_date, medical_history):#create a class with attributes
        self.name=name
        self.age=age
        self.admission_date=admission_date
        self.medical_history=medical_history
    def print_details(self):
        print(f"Name: {self.name}, Age: {self.age}, Admission Date: {self.admission_date}, Medical History: {self.medical_history}")
#create an example
patient1=patients('Sha Rui',18,'2025-01-01','too_smart')
patient1.print_details()