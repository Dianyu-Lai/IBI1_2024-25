class patients:
    #create a class with attributes
    def __init__(self, name, age , admission_date, medical_history):
        self.name=name
        self.age=age
        self.admission_date=admission_date
        self.medical_history=medical_history
    #create a method to print the details of the patient
    def print_details(self):
        print(f"Name: {self.name}, Age: {self.age}, Admission Date: {self.admission_date}, Medical History: {self.medical_history}")
#create an example
patient1 = patients('Sha Rui',18,'2025-01-01','too_smart')
patient1.print_details()
#another Example:
#patient2 = patients('Johnson',60,'2079-05-15','diabetes')
#patient2.print_details()