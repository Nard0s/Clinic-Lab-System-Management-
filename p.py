import tkinter as tk
from tkinter import filedialog
import datetime

class ClinicLabManagementSystem:
    def __init__(self, window):
        self.window = window
        self.window.title("ClinicLab Management System")

        # Dictionary to store patient data
        self.patients = {}

        # Create GUI frames
        self.create_add_patient_frame()
        self.create_add_test_frame()
        self.create_get_patient_info_frame()
        self.create_file_handling_frame()

    def create_add_patient_frame(self):
        frame_add_patient = tk.Frame(self.window)
        frame_add_patient.pack(pady=10)

        tk.Label(frame_add_patient, text="Add Patient").grid(row=0, columnspan=2)
        tk.Label(frame_add_patient, text="Patient ID").grid(row=1, column=0)
        self.entry_patient_id = tk.Entry(frame_add_patient)
        self.entry_patient_id.grid(row=1, column=1)

        tk.Label(frame_add_patient, text="Name").grid(row=2, column=0)
        self.entry_name = tk.Entry(frame_add_patient)
        self.entry_name.grid(row=2, column=1)

        tk.Label(frame_add_patient, text="Age").grid(row=3, column=0)
        self.entry_age = tk.Entry(frame_add_patient)
        self.entry_age.grid(row=3, column=1)

        tk.Label(frame_add_patient, text="Gender").grid(row=4, column=0)
        self.entry_gender = tk.Entry(frame_add_patient)
        self.entry_gender.grid(row=4, column=1)

        self.lbl_patient_status = tk.Label(frame_add_patient, text="")
        self.lbl_patient_status.grid(row=5, columnspan=2)

        btn_add_patient = tk.Button(frame_add_patient, text="Add Patient", command=self.add_patient)
        btn_add_patient.grid(row=6, columnspan=2, pady=5)

    def create_add_test_frame(self):
        frame_add_test = tk.Frame(self.window)
        frame_add_test.pack(pady=10)

        tk.Label(frame_add_test, text="Add Test Result").grid(row=0, columnspan=2)
        tk.Label(frame_add_test, text="Patient ID").grid(row=1, column=0)
        self.entry_patient_id_test = tk.Entry(frame_add_test)
        self.entry_patient_id_test.grid(row=1, column=1)

        tk.Label(frame_add_test, text="Test Name").grid(row=2, column=0)
        self.entry_test_name = tk.Entry(frame_add_test)
        self.entry_test_name.grid(row=2, column=1)

        tk.Label(frame_add_test, text="Test Result").grid(row=3, column=0)
        self.entry_test_result = tk.Entry(frame_add_test)
        self.entry_test_result.grid(row=3, column=1)

        self.lbl_test_status = tk.Label(frame_add_test, text="")
        self.lbl_test_status.grid(row=4, columnspan=2)

        btn_add_test_result = tk.Button(frame_add_test, text="Add Test Result", command=self.add_test_result)
        btn_add_test_result.grid(row=5, columnspan=2, pady=5)

    def create_get_patient_info_frame(self):
        frame_get_patient_info = tk.Frame(self.window)
        frame_get_patient_info.pack(pady=10)

        tk.Label(frame_get_patient_info, text="Get Patient Info").grid(row=0, columnspan=2)
        tk.Label(frame_get_patient_info, text="Patient ID").grid(row=1, column=0)
        self.entry_patient_id_info = tk.Entry(frame_get_patient_info)
        self.entry_patient_id_info.grid(row=1, column=1)

        self.lbl_patient_info = tk.Label(frame_get_patient_info, text="")
        self.lbl_patient_info.grid(row=2, columnspan=2)

        btn_get_patient_info = tk.Button(frame_get_patient_info, text="Get Info", command=self.get_patient_info)
        btn_get_patient_info.grid(row=3, columnspan=2, pady=5)

    def create_file_handling_frame(self):
        frame_file_handling = tk.Frame(self.window)
        frame_file_handling.pack(pady=10)

        btn_load_data = tk.Button(frame_file_handling, text="Load Data", command=self.load_data)
        btn_load_data.grid(row=0, column=0, padx=5)

        btn_save_data = tk.Button(frame_file_handling, text="Save Data", command=self.save_data)
        btn_save_data.grid(row=0, column=1, padx=5)

    def add_patient(self):
        patient_id = self.entry_patient_id.get()
        name = self.entry_name.get()
        age = self.entry_age.get()
        gender = self.entry_gender.get()

        if patient_id in self.patients:
            self.lbl_patient_status.config(text="Patient ID already exists!", fg="red")
        else:
            self.patients[patient_id] = {'name': name, 'age': age, 'gender': gender, 'tests': []}
            self.lbl_patient_status.config(text=f"Patient {name} added successfully.", fg="green")

        self.entry_patient_id.delete(0, tk.END)
        self.entry_name.delete(0, tk.END)
        self.entry_age.delete(0, tk.END)
        self.entry_gender.delete(0, tk.END)

    def add_test_result(self):
        patient_id = self.entry_patient_id_test.get()
        test_name = self.entry_test_name.get()
        result = self.entry_test_result.get()

        if patient_id not in self.patients:
            self.lbl_test_status.config(text="Patient ID not found!", fg="red")
        else:
            test_date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            test = {'test_name': test_name, 'test_date': test_date, 'result': result}
            self.patients[patient_id]['tests'].append(test)
            self.lbl_test_status.config(text=f"Test result for {test_name} added to patient {patient_id}.", fg="green")

        self.entry_patient_id_test.delete(0, tk.END)
        self.entry_test_name.delete(0, tk.END)
        self.entry_test_result.delete(0, tk.END)

    def get_patient_info(self):
        patient_id = self.entry_patient_id_info.get()

        if patient_id not in self.patients:
            self.lbl_patient_info.config(text="Patient ID not found!", fg="red")
        else:
            patient_info = self.patients[patient_id]
            info = (f"Patient ID: {patient_id}\n"
                    f"Name: {patient_info['name']}\n"
                    f"Age: {patient_info['age']}\n"
                    f"Gender: {patient_info['gender']}\n"
                    "Tests:\n")
            for test in patient_info['tests']:
                info += (f"  Test Name: {test['test_name']}, Date: {test['test_date']}, Result: {test['result']}\n")
            self.lbl_patient_info.config(text=info, fg="black")

        self.entry_patient_id_info.delete(0, tk.END)

    def save_data(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
        if file_path:
            with open(file_path, "w") as file:
                for patient_id, patient_data in self.patients.items():
                    file.write(f"Patient ID: {patient_id}\n")
                    file.write(f"Name: {patient_data['name']}\n")
                    file.write(f"Age: {patient_data['age']}\n")
                    file.write(f"Gender: {patient_data['gender']}\n")
                    file.write("Tests:\n")
                    for test in patient_data['tests']:
                        file.write(f"  Test Name: {test['test_name']}, Date: {test['test_date']}, Result: {test['result']}\n")
                    file.write("\n")

    def load_data(self):
        file_path = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
        if file_path:
            self.patients = {}
            current_patient_id = None
            with open(file_path, "r") as file:
                lines = file.readlines()
                for line in lines:
                    if line.startswith("Patient ID: "):
                        current_patient_id = line.split(": ")[1].strip()
                        self.patients[current_patient_id] = {}
                    elif line.startswith("Name: "):
                        self.patients[current_patient_id]['name'] = line.split(": ")[1].strip()
                    elif line.startswith("Age: "):
                        self.patients[current_patient_id]['age'] = line.split(": ")[1].strip()
                    elif line.startswith("Gender: "):
                        self.patients[current_patient_id]['gender'] = line.split(": ")[1].strip()
                    elif line.startswith("  Test Name: "):
                        if 'tests' not in self.patients[current_patient_id]:
                            self.patients[current_patient_id]['tests'] = []
                        test_name = line.split(": ")[1].split(", Date: ")[0].strip()
                        test_date = line.split("Date: ")[1].split(", Result: ")[0].strip()
                        test_result = line.split("Result: ")[1].strip()
                        self.patients[current_patient_id]['tests'].append({'test_name': test_name, 'test_date': test_date, 'result': test_result})

window = tk.Tk()
app = ClinicLabManagementSystem(window)
window.mainloop()
