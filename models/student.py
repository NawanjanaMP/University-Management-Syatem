# models/student.py

from .person import Person
from typing import Dict, Set

# Forward declaration for type hinting to avoid circular import
class Course:
    pass

class Student(Person):
    """Represents a student in the university."""
    def __init__(self, name: str, person_id: int, email: str, major: str):
        super().__init__(name, person_id, email)
        self.major = major
        self.enrolled_courses = {} # Using dict for quick lookups: {course_code: course}
        self.grades = {} # {course_code: grade_points}
        self.completed_courses = set() # {course_code}

    def get_responsibilities(self) -> str:
        return "Attend classes, complete assignments, and study."

class SecureStudentRecord(Student):
    """
    An enhanced Student class with private attributes, validation,
    and advanced academic management features.
    """
    def __init__(self, name: str, person_id: int, email: str, major: str):
        super().__init__(name, person_id, email, major)
        # Using name mangling for 'private' attributes
        self.__gpa = 0.0
        self.__academic_status = "Good Standing"

    @property
    def gpa(self) -> float:
        """Getter for GPA."""
        return self.__gpa

    @property
    def academic_status(self) -> str:
        """Getter for academic status."""
        return self.__academic_status

    def enroll_course(self, course: 'Course', completed_prereqs: Set[str]) -> None:
        """Enrolls a student in a course with validation."""
        if not course.check_prerequisites(completed_prereqs):
            raise PermissionError(f"Cannot enroll. Prerequisites not met for {course.course_code}.")

        if course.is_full():
            raise OverflowError(f"Cannot enroll. Course {course.course_code} is full.")

        if course.course_code in self.enrolled_courses:
            print(f"Warning: Already enrolled in {course.course_code}.")
            return
            
        self.enrolled_courses[course.course_code] = course
        course.add_student(self)
        print(f"Successfully enrolled {self.name} in {course.course_code}.")

    def drop_course(self, course: 'Course') -> None:
        """Drops a student from a course."""
        if course.course_code not in self.enrolled_courses:
            raise ValueError(f"Not enrolled in {course.course_code}.")
        
        del self.enrolled_courses[course.course_code]
        course.remove_student(self)
        print(f"Successfully dropped {course.course_code} for {self.name}.")

    def add_grade(self, course_code: str, grade_points: float) -> None:
        """Adds a grade for a course and recalculates GPA."""
        if not (0.0 <= grade_points <= 4.0):
            raise ValueError("GPA must be between 0.0 and 4.0.")
        
        self.grades[course_code] = grade_points
        self.completed_courses.add(course_code)
        self._calculate_gpa()

    def _calculate_gpa(self) -> None:
        """Private method to calculate GPA."""
        if not self.grades:
            self.__gpa = 0.0
        else:
            total_points = sum(self.grades.values())
            self.__gpa = round(total_points / len(self.grades), 2)
        self._update_academic_status()

    def _update_academic_status(self) -> None:
        """Private method to update academic status based on GPA."""
        if self.__gpa >= 3.7:
            self.__academic_status = "Dean's List"
        elif self.__gpa >= 2.0:
            self.__academic_status = "Good Standing"
        else:
            self.__academic_status = "Probation"
            
    def get_academic_summary(self) -> str:
        """Returns a summary of the student's academic standing."""
        return (f"Student: {self.name}\n"
                f"GPA: {self.gpa}\n"
                f"Status: {self.academic_status}\n"
                f"Enrolled Courses: {', '.join(self.enrolled_courses.keys())}")