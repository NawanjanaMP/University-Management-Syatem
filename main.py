# main.py

from models.person import Staff
from models.faculty import Professor, Lecturer, TA
from models.student import SecureStudentRecord
from models.course import Course
from models.department import Department

def main():
    """Main function to demonstrate the University Management System."""
    print("--- 1. Setting up University Structure ---")
    
    # Create Departments
    cs_dept = Department("Computer Science")
    
    # Create Courses
    cs101 = Course("CS101", "Intro to Programming", 3, 100)
    cs201 = Course("CS201", "Data Visualization", 3, 50, prerequisites=["CS101"])
    cs301 = Course("CS301", "Machine Learning", 3, 30, prerequisites=["CS201"])
    
    cs_dept.add_course(cs101)
    cs_dept.add_course(cs201)
    cs_dept.add_course(cs301)
    
    # Create People
    prof_ada = Professor("Milena Fernandz", 101, "milena@uni.edu", "Computer Science")
    lect_blaise = Lecturer("Shamaan Chamaal", 102, "shamaanc@uni.edu", "Computer Science")
    ta_charles = TA("Adam Zampa", 103, "adamz@uni.edu", "Computer Science")
    staff_grace = Staff("Hendrick Nicoly", 201, "hendrickn@uni.edu", "Admissions Officer")
    student_alan = SecureStudentRecord("Nawanjana Madhushankha", 301, "nawanjanam@uni.edu", "Computer Science")

    cs_dept.add_faculty(prof_ada)
    
    print("\n--- 2. Polymorphism Demonstration ---")
    people = [prof_ada, lect_blaise, ta_charles, staff_grace, student_alan]
    
    print("\n--- Getting Responsibilities ---")
    for person in people:
        print(f"{person.name} ({person.__class__.__name__}): {person.get_responsibilities()}")

    print("\n--- Calculating Faculty Workload ---")
    faculty_members = [prof_ada, lect_blaise, ta_charles]
    for member in faculty_members:
        print(f"{member.name} ({member.__class__.__name__}): {member.calculate_workload()}")

    print("\n--- 3. Course Enrollment & Prerequisite System ---")
    
    # Attempt 1: Enroll in advanced course without prereqs (should fail)
    try:
        student_alan.enroll_course(cs301, student_alan.completed_courses)
    except PermissionError as e:
        print(f"Enrollment failed as expected: {e}")

    # Step 1: Complete CS101
    print("\nSimulating completion of CS101...")
    student_alan.add_grade("CS101", 3.8) # Grade in A- range
    
    # Attempt 2: Enroll in CS201 (should succeed)
    try:
        student_alan.enroll_course(cs201, student_alan.completed_courses)
    except Exception as e:
        print(f"Enrollment failed unexpectedly: {e}")
        
    print("\n--- 4. Academic Status Tracking ---")
    print(student_alan.get_academic_summary())
    
    # Step 2: Complete CS201 with a high grade
    print("\nSimulating completion of CS201...")
    student_alan.add_grade("CS201", 4.0) # Perfect grade
    
    print("\nUpdated Academic Summary:")
    print(student_alan.get_academic_summary())
    
    # Step 3: Now try to enroll in CS301 (should succeed)
    try:
        student_alan.enroll_course(cs301, student_alan.completed_courses)
    except Exception as e:
        print(f"Enrollment failed unexpectedly: {e}")
        
    print("\nFinal Academic Summary:")
    print(student_alan.get_academic_summary())
    
    # Step 4: Drop a course
    try:
        student_alan.drop_course(cs301)
    except ValueError as e:
        print(f"Error dropping course: {e}")
    
    print("\nSummary after dropping CS301:")
    print(student_alan.get_academic_summary())


if __name__ == "__main__":
    main()