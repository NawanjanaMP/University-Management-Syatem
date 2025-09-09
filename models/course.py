# models/course.py

from typing import List, Set

# Forward declaration to avoid circular import with student
class SecureStudentRecord:
    pass

class Course:
    """Represents a university course."""
    def __init__(self, course_code: str, title: str, credits: int, max_capacity: int, prerequisites: List[str] = None):
        """Initializes a Course."""
        self.course_code = course_code
        self.title = title
        self.credits = credits
        self.max_capacity = max_capacity
        self.prerequisites = set(prerequisites) if prerequisites else set()
        self._enrolled_students: List['SecureStudentRecord'] = []

    @property
    def current_enrollment(self) -> int:
        """Returns the number of students currently enrolled."""
        return len(self._enrolled_students)

    def is_full(self) -> bool:
        """Checks if the course has reached its maximum capacity."""
        return self.current_enrollment >= self.max_capacity

    def add_student(self, student: 'SecureStudentRecord') -> None:
        """Adds a student to the course's roster."""
        if not self.is_full():
            self._enrolled_students.append(student)
        else:
            raise OverflowError("Course is already full.")

    def remove_student(self, student: 'SecureStudentRecord') -> None:
        """Removes a student from the course's roster."""
        if student in self._enrolled_students:
            self._enrolled_students.remove(student)

    def check_prerequisites(self, completed_courses: Set[str]) -> bool:
        """
        Checks if a student's completed courses satisfy the prerequisites.
        Returns True if prerequisites are met, False otherwise.
        """
        return self.prerequisites.issubset(completed_courses)
    
    def __str__(self):
        return f"{self.course_code}: {self.title}"