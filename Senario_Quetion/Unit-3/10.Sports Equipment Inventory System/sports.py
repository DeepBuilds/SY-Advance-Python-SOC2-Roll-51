import csv
import argparse

# Create command-line argument parser
parser = argparse.ArgumentParser()
parser.add_argument("filename", help="CSV file name")
args = parser.parse_args()

try:
    # Read equipment details from CSV file
    with open(args.filename, "r") as file:
        reader = csv.DictReader(file)
        equipment = list(reader)

    # Display all equipment information
    print("\n--- Sports Equipment Inventory ---")
    for item in equipment:
        print(item)

    # Search by Equipment ID
    search_id = input("\nEnter Equipment ID to search: ")

    found = False

    for item in equipment:
        if item["Equipment ID"] == search_id:
            print("\nEquipment Found:")
            for key, value in item.items():
                print(key + ":", value)
            found = True
            break

    if not found:
        print("Equipment not found.")

except FileNotFoundError:
    print("File not found.")
except Exception as e:
    print("Error:", e)


# Sample Output:
# --- Sports Equipment Inventory ---
# {'Equipment ID': 'E101', 'Equipment Name': 'Football', 'Sport': 'Football', 'Quantity': '10', 'Condition': 'Good'}
# {'Equipment ID': 'E102', 'Equipment Name': 'Cricket Bat', 'Sport': 'Cricket', 'Quantity': '5', 'Condition': 'Excellent'}
# {'Equipment ID': 'E103', 'Equipment Name': 'Tennis Racket', 'Sport': 'Tennis', 'Quantity': '8', 'Condition': 'Good'}
# {'Equipment ID': 'E104', 'Equipment Name': 'Basketball', 'Sport': 'Basketball', 'Quantity': '6', 'Condition': 'Average'}
#
# Enter Equipment ID to search: E102
#
# Equipment Found:
# Equipment ID: E102
# Equipment Name: Cricket Bat
# Sport: Cricket
# Quantity: 5
# Condition: Excellent
