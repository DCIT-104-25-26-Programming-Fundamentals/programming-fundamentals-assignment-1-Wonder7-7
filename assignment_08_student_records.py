# =============================================================================
# PROGRAMMING FUNDAMENTALS — Assignment 8
# Topic: Lists of Dictionaries, Loops, and Functions
# =============================================================================
#
# TASK: Student Record Management System
#
# Build a console-based program that stores and manages student information.
# Each student record must contain:
#
#   - Name   : the student's full name (text)
#   - ID     : a unique student ID number (e.g. 20240001)
#   - Scores : a list of scores from multiple assessments (e.g. [75, 88, 90])
#
# -----------------------------------------------------------------------------
# FEATURES YOUR PROGRAM MUST SUPPORT
# -----------------------------------------------------------------------------
#
#   1. Add a Student
#      - Ask the user to enter the student's name and ID.
#      - Ask how many scores to enter, then collect each score one by one.
#      - Save the student record and confirm it was added.
#
#   2. Display All Students
#      - Print a formatted table showing every student's:
#          Name, ID, individual scores, and their average score.
#      - If no students have been added yet, print a message saying so.
#
#   3. Calculate Average Score for a Specific Student
#      - Ask the user to enter a student ID.
#      - Find the student and calculate the average of their scores.
#      - Display the result. If the ID is not found, print an error message.
#
#   4. Quit
#      - End the program.
#
# -----------------------------------------------------------------------------
# HOW THE MENU SHOULD LOOK
# -----------------------------------------------------------------------------
#
#   ================================
#      STUDENT RECORD SYSTEM MENU
#   ================================
#   1. Add student
#   2. Display all students
#   3. Calculate average score
#   4. Quit
#   Enter your choice (1-4):
#
# -----------------------------------------------------------------------------
# EXPECTED INTERACTION EXAMPLE
# -----------------------------------------------------------------------------
#
#   Enter your choice (1-4): 1
#   Student name: Alice Mensah
#   Student ID: 20240001
#   How many scores? 3
#   Enter score 1: 78
#   Enter score 2: 85
#   Enter score 3: 90
#   Student "Alice Mensah" added successfully.
#
#   Enter your choice (1-4): 2
#   --------------------------------------------------
#   Name           ID          Scores         Average
#   --------------------------------------------------
#   Alice Mensah   20240001    78, 85, 90     84.33
#   --------------------------------------------------
#
#   Enter your choice (1-4): 3
#   Enter student ID: 20240001
#   Alice Mensah's average score: 84.33
#
# -----------------------------------------------------------------------------
# REQUIREMENTS
# -----------------------------------------------------------------------------
# - Store all student records in a list of dictionaries.
#   Example structure:
#       student = {
#           "name": "Alice Mensah",
#           "id": 20240001,
#           "scores": [78, 85, 90]
#       }
# - Average scores should be rounded to 2 decimal places.
# - Each feature MUST be implemented in its own function (see scaffold below).
# - Handle invalid menu choices and missing student IDs gracefully.
#

# =============================================================================
# YOUR CODE BELOW — remove the # symbols from the scaffold and fill it in
# =============================================================================

def add_student(students):
    """Prompt for a name, ID, and scores, then add the student record."""
    name = input("Student name: ").strip()

    try:
        student_id = int(input("Student ID: "))
    except ValueError:
        print("Error: Student ID must be a whole number.")
        return

    try:
        count = int(input("How many scores? "))
        if count <= 0:
            print("Error: Number of scores must be positive.")
            return
    except ValueError:
        print("Error: Please enter a valid whole number.")
        return

    scores = []
    for i in range(1, count + 1):
        while True:
            raw = input(f"Enter score {i}: ")
            try:
                scores.append(float(raw))
                break
            except ValueError:
                print("  Please enter a valid number.")

    students.append({"name": name, "id": student_id, "scores": scores})
    print(f'Student "{name}" added successfully.')


def calculate_average(scores):
    """Return the average of a list of scores, rounded to 2 decimals."""
    return round(sum(scores) / len(scores), 2)


def display_students(students):
    """Print a formatted table of every student's name, ID, scores, average."""
    if not students:
        print("No students have been added yet.")
        return

    # Format scores without trailing ".0" for whole numbers, e.g. 78 instead of 78.0
    def format_score(score):
        return str(int(score)) if score == int(score) else str(score)

    rows = []
    for student in students:
        scores_str = ", ".join(format_score(s) for s in student["scores"])
        average = calculate_average(student["scores"])
        rows.append((student["name"], str(student["id"]), scores_str, str(average)))

    # Size each column to fit its widest value (with a minimum width for readability).
    name_width = max(15, max(len(r[0]) for r in rows) + 2)
    id_width = max(12, max(len(r[1]) for r in rows) + 2)
    scores_width = max(15, max(len(r[2]) for r in rows) + 2)

    line_width = name_width + id_width + scores_width + 8
    print("-" * line_width)
    print(f"{'Name':<{name_width}}{'ID':<{id_width}}{'Scores':<{scores_width}}{'Average'}")
    print("-" * line_width)

    for name, sid, scores_str, average in rows:
        print(f"{name:<{name_width}}{sid:<{id_width}}{scores_str:<{scores_width}}{average}")

    print("-" * line_width)


def find_student_by_id(students, student_id):
    """Return the student dict with the given ID, or None if not found."""
    for student in students:
        if student["id"] == student_id:
            return student
    return None


def calculate_average_for_student(students):
    """Ask for a student ID and print their average score."""
    try:
        student_id = int(input("Enter student ID: "))
    except ValueError:
        print("Error: Student ID must be a whole number.")
        return

    student = find_student_by_id(students, student_id)
    if student is None:
        print("Error: No student found with that ID.")
        return

    average = calculate_average(student["scores"])
    print(f"{student['name']}'s average score: {average}")


def print_menu():
    print("\n================================")
    print("   STUDENT RECORD SYSTEM MENU")
    print("================================")
    print("1. Add student")
    print("2. Display all students")
    print("3. Calculate average score")
    print("4. Quit")


def main():
    students = []

    while True:
        print_menu()
        choice = input("Enter your choice (1-4): ").strip()

        if choice == "1":
            add_student(students)
        elif choice == "2":
            display_students(students)
        elif choice == "3":
            calculate_average_for_student(students)
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a number from 1 to 4.")


if __name__ == "__main__":
    main()