import csv
# Function to read vehicle data from CSV file
def read_vehicle_data(file_path):
    with open(file_path, 'r') as file:
        reader = csv.reader(file)
        vehicle_data = {rows[0]: rows[1] for rows in reader}
    return vehicle_data

# Function to initialize parking slots
def initialize_parking_slots(num_slots):
    return [None] * num_slots

# Function to find the category of a vehicle
def find_vehicle_category(vehicle_data, registration_number):
    return vehicle_data.get(registration_number, "Unknown")

# Function to park a vehicle
def park_vehicle(parking_slots, category):
    for i, slot in enumerate(parking_slots):
        if slot is None:
            parking_slots[i] = category
            return i + 1  # Return the slot number (1-indexed)
    return None  # No available slots

# Function to exit a vehicle from the parking slot
def exit_vehicle(parking_slots, slot_number):
    if 1 <= slot_number <= len(parking_slots) and parking_slots[slot_number - 1] is not None:
        exited_category = parking_slots[slot_number - 1]
        parking_slots[slot_number - 1] = None
        return exited_category
    return None  # Invalid slot number or slot is already empty

# Main program
if __name__ == "__main__":
    # Replace 'vehicle_data.csv' with the actual path to your CSV file
    vehicle_data_file_path = 'vehicle_data.csv'
    parking_slots_count = 10
    parking_slots = initialize_parking_slots(parking_slots_count)
    vehicle_data = read_vehicle_data(vehicle_data_file_path)

    while True:
        print("\n1. Park Vehicle\n2. Exit Vehicle\n3. Quit")
        choice = input("Enter your choice (1/2/3): ")

        if choice == '1':
            reg_number = input("Enter vehicle registration number: ")
            category = find_vehicle_category(vehicle_data, reg_number)
            if category != "Unknown":
                slot = park_vehicle(parking_slots, category)
                if slot is not None:
                    print(f"Vehicle parked in slot {slot}")
                else:
                    print("Parking slots are full.")
            else:
                print("Vehicle category not found.")

        elif choice == '2':
            slot_to_exit = int(input("Enter the slot number to exit: "))
            exited_category = exit_vehicle(parking_slots, slot_to_exit)
            if exited_category is not None:
                print(f"Vehicle of category {exited_category} exited from slot {slot_to_exit}")
            else:
                print("Invalid slot number or slot is already empty.")

        elif choice == '3':
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please enter 1, 2, or 3.")
