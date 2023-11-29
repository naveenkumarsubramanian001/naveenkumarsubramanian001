This project serves as a foundation for a basic vehicle parking management system. Depending on specific requirements, additional features and enhancements can be incorporated, such as graphical interfaces, real-time status updates, or integration with databases for persistent storage. This project is particularly useful for learning basic file handling, data manipulation, and program flow control in Python.
Vehicle Data CSV File:

The project utilizes a CSV file (vehicle_data.csv) to store information about vehicles, mapping registration numbers to categories.
The CSV file has two columns: "Registration Number" and "Category."
Parking Slots:

The program simulates a parking lot with a specified number of slots (in this case, 10 slots).
Parking slots are represented as a list, and each slot can hold a vehicle category.
Functionality:

Read Vehicle Data:
Reads vehicle data from the CSV file during program initialization.
Park Vehicle:
Accepts a registration number as input, finds the corresponding vehicle category, and parks the vehicle in an available slot.
If all slots are occupied, it notifies the user that parking is full.
Exit Vehicle:
Accepts a slot number as input, removes the vehicle from the slot, and marks the slot as available.
If the slot is invalid or already empty, it notifies the user.
Quit:
Exits the program.