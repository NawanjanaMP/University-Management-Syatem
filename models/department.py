# models/department.py

from typing import Dict, List
from .course import Course
from .faculty import Faculty

class Department:
    """Represents a university department."""
    def __init__(self, name: str):
        self.name = name
        self.courses: Dict[str, Course] = {}
        self.faculty: List[Faculty] = []

    def add_course(self, course: Course):
        """Adds a course to the department."""
        self.courses[course.course_code] = course
        print(f"Course {course.course_code} added to {self.name} Department.")

    def add_faculty(self, faculty_member: Faculty):
        """Adds a faculty member to the department."""
        self.faculty.append(faculty_member)
        print(f"{faculty_member.name} joined the {self.name} Department.")