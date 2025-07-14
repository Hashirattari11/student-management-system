def get_marks():
    marks = []
    for i in range(1, 4):
        while True:
            try:
                mark = int(input("Enter mark {} (0 to 100): ".format(i)))
                if 0 <= mark <= 100:
                    marks.append(mark)
                    break
                else:
                    print("Invalid mark. Please enter between 0 and 100.")
            except ValueError:
                print("Invalid input. Please enter an integer.")
    return marks

# Function ko calculate kare ga
def get_average(marks):
    total = sum(marks)
    average = total / len(marks)
    return average

# Function ko dhonde ga jo top honge
def get_top_students(avg_dict):
    highest = max(avg_dict.values())
    top_students = []
    for name, avg in avg_dict.items():
        if avg == highest:
            top_students.append(name)
    return top_students, highest

# Main function ko manage student data
def student_marks_manager():
    students = {}     # Dictionary ma store student marks kare ga
    averages = {}     # Dictionary ma store student averages kare ga

    # Input data for 5 students
    for i in range(5):
        print("\nEnter details for student {}".format(i + 1))
        name = input("Enter student name: ")
        marks = get_marks()
        students[name] = marks

    print("\nStudent Averages:")
    for name in students:
        avg = get_average(students[name])
        averages[name] = avg
        print("{}: {:.2f}".format(name, avg))

    # Find and display top student(s)
    top_names, top_avg = get_top_students(averages)
    print("\nTop Student(s) with average {:.2f}:".format(top_avg))
    for student in top_names:
        print(student)

# Run the program
if __name__ == "__main__":
    student_marks_manager()
# Function to get 3 valid marks from user
def get_marks():
    marks = []
    for i in range(1, 4):
        while True:
            try:
                mark = int(input("Enter mark {} (0 to 100): ".format(i)))
                if 0 <= mark <= 100:
                    marks.append(mark)
                    break
                else:
                    print("Invalid mark. Please enter between 0 and 100.")
            except ValueError:
                print("Invalid input. Please enter an integer.")
    return marks

# Function to calculate average of a list of marks
def get_average(marks):
    total = sum(marks)
    average = total / len(marks)
    return average

# Function to find top student(s)
def get_top_students(avg_dict):
    highest = max(avg_dict.values())
    top_students = []
    for name, avg in avg_dict.items():
        if avg == highest:
            top_students.append(name)
    return top_students, highest

# Main function to manage student data
def student_marks_manager():
    students = {}     # Dictionary to store student marks
    averages = {}     # Dictionary to store student averages

    # Input data for 5 students
    for i in range(5):
        print("\nEnter details for student {}".format(i + 1))
        name = input("Enter student name: ")
        marks = get_marks()
        students[name] = marks

    print("\nStudent Averages:")
    for name in students:
        avg = get_average(students[name])
        averages[name] = avg
        print("{}: {:.2f}".format(name, avg))

    # Find and display top student(s)
    top_names, top_avg = get_top_students(averages)
    print("\nTop Student(s) with average {:.2f}:".format(top_avg))
    for student in top_names:
        print(student)
        break

# Run the program
if __name__ == "__main__":
    student_marks_manager()                                                                                                          