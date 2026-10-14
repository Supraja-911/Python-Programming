patients = {}

while True:
    print(" Hospital Patient Record Management")
    print("1. Add Patient Record")
    print("2. View All Patient Records")
    print("3. Update Patient Record")
    print("4. Delete Patient Record")
    print("5. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        patient_id = input("Enter Patient ID: ")

        if patient_id in patients:
            print("Patient ID already exists!")
        else:
            name = input("Enter Patient Name: ")
            age = input("Enter Patient Age: ")
            disease = input("Enter Disease: ")
            doctor = input("Enter Doctor Name: ")

            patients[patient_id] = {
                "Name": name,
                "Age": age,
                "Disease": disease
            }

            print("Patient record added successfully!")

    elif choice == "2":
        if not patients:
            print("No patient records found.")
        else:
            print("Patient Records")
            for patient_id, details in patients.items():
                print("Patient ID:", patient_id)
                for key, value in details.items():
                    print(key + ":", value)

    elif choice == "3":
        patient_id = input("Enter Patient ID to update: ")

        if patient_id in patients:
            print("1. Name")
            print("2. Age")
            print("3. Disease")

            field_choice = input("Select field to update: ")

            fields = {
                "1": "Name",
                "2": "Age",
                "3": "Disease"
            }

            if field_choice in fields:
                field = fields[field_choice]
                new_value = input(f"Enter new {field}: ")
                patients[patient_id][field] = new_value
                print("Patient record updated successfully!")
            else:
                print("Invalid field choice.")
        else:
            print("Patient ID not found.")

    elif choice == "4":
        patient_id = input("Enter Patient ID to delete: ")

        if patient_id in patients:
            del patients[patient_id]
            print("Patient record deleted successfully!")
        else:
            print("Patient ID not found.")

    elif choice == "5":
        print("Exiting the system. Goodbye!")
        break

    else:
        print("Invalid choice. Please try again.")
