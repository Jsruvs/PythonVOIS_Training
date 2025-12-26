# ===============================
# MAIN PROGRAM : Student Management System
# ===============================

# 1. Importing user-defined modules
import student                  # normal import
from marks import add_marks, calculate_average   # from ... import
import report as rpt             # module alias

# 2. Importing reusable module
from utils import grade

# 3. Importing predefined modules
import datetime
import random
import math

# ===============================
# MAIN EXECUTION STARTS
# ===============================

print("===== STUDENT MANAGEMENT SYSTEM =====")

# Display current date using datetime module
print("Date:", datetime.date.today())

# Generate random roll number
roll_no = random.randint(1, 100)
print("Generated Roll No:", roll_no)

# Add student details
student.add_student(roll_no, "Aman Gupta")

# Add marks
add_marks(roll_no, [75, 82, 88])

# Calculate average marks
avg = calculate_average(roll_no)
avg = math.ceil(avg)   # rounding using math module

# Generate grade
student_grade = grade(avg)

# Generate report
report_obj = rpt.Report()
final_report = report_obj.generate(
    student.get_student(roll_no),
    avg
)

# Display output
print("\n----- STUDENT REPORT -----")
print(final_report)
print("Grade:", student_grade)

print("\n===== PROGRAM END =====")
