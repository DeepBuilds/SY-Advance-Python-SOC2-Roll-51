import csv
import argparse

# Create command-line argument parser
parser = argparse.ArgumentParser()
parser.add_argument("filename", help="CSV file name")
args = parser.parse_args()

try:
    # Read course details from CSV file
    with open(args.filename, "r") as file:
        reader = csv.DictReader(file)
        courses = list(reader)

    # Display all course records
    print("\n--- Course Information ---")
    for course in courses:
        print(course)

    # Search by Course ID
    search_id = input("\nEnter Course ID to search: ")

    found = False

    for course in courses:
        if course["Course ID"] == search_id:
            print("\nCourse Found:")
            for key, value in course.items():
                print(key + ":", value)
            found = True
            break

    if not found:
        print("Course not found.")

except FileNotFoundError:
    print("File not found.")
except Exception as e:
    print("Error:", e)


# Sample Output:
# --- Course Information ---
# {'Course ID': 'C101', 'Course Name': 'Python Programming', 'Department': 'CSE', 'Credits': '4'}
# {'Course ID': 'C102', 'Course Name': 'Data Structures', 'Department': 'CSE', 'Credits': '4'}
# {'Course ID': 'C103', 'Course Name': 'Database Management', 'Department': 'CSE', 'Credits': '3'}
# {'Course ID': 'C104', 'Course Name': 'Computer Networks', 'Department': 'CSE', 'Credits': '3'}
#
# Enter Course ID to search: C102
#
# Course Found:
# Course ID: C102
# Course Name: Data Structures
# Department: CSE
# Credits: 4
