# Defining Patient class and attributes
class Patient:
    def __init__(self, id, name, age, gender, admission_date, condition):
        self.id = id
        self.name = name
        self.age = age
        self.gender = gender
        self.admission_date = admission_date
        self.condition = condition
        
    def get_details(self):
        return (
            f"id: {self.id}\n"
            f"name: {self.name}\n"
            f"age: {self.age}\n"
            f"gender: {self.gender}\n"
            f"admitted: {self.admission_date}\n"
            f"condition: {self.condition}\n"
        )
# Created Multiple Patient Objects and Stored in an array
patient_list = [
    Patient(115, "Eniola Elvis", 34, "Female", "10-10-2024", "Insomnia"),
    Patient(15, "Emery Kevin", 23, "Male", "07-10-2014", "H-pylori"),
    Patient(137, "Ahmed Musa", 65, "Male", "04-09-2024", "Diabetes"),
]

# Define a Function to Count number of Patients
def count_patients(patient_list):
    return len(patient_list)

# Define a Function to List All Patient Names
def list_patient_names(patient_list):
    return [Patient.name for Patient in patient_list]

# Step 5: Definining a Function to Print Patient Details by ID
def print_patient_by_id(patient_list):
    try:
        search_id = int(input("Enter the patient ID: "))
        for patient in patient_list:
            if patient.id == search_id:
                print(patient.get_details())
                return
        print("Patient not found.")
    except ValueError:
        print("Invalid ID format. Please enter an integer.")

# Testing the Functions
print("total number of patients is:", count_patients(patient_list))
print("all patient names:",list_patient_names(patient_list))
print_patient_by_id(patient_list)
