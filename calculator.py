# This function calculates the grade for a student based on their marks.
def grade_calculator(marks):
    if marks >= 91 and marks <= 100:
        return "A+"
    elif marks >= 81 and marks <= 90:
        return "A"
    elif marks >= 71 and marks <= 80:
        return "B"
    elif marks >= 61 and marks <= 70:
        return "C"
    elif marks >= 41 and marks <= 60:
        return "D"
    else:
        return "F"


subjects = ["Bangla", "English", "Math", "Science"]

marks = []

# Loop through the subjects and take input from the user
for subject in subjects:
    mark = int(input(f"Enter the mark for {subject}: "))
    marks.append(mark)
    
# Calculate the average of the marks
average = sum(marks) / len(marks)

grade = grade_calculator(average)

print("The grade is:", grade)