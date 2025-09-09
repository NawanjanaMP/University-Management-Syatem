# models/faculty.py

from .person import Person
from abc import abstractmethod

class Faculty(Person):
    """Base class for all faculty members."""
    def __init__(self, name: str, person_id: int, email: str, department: str):
        super().__init__(name, person_id, email)
        self.department = department

    @abstractmethod
    def calculate_workload(self) -> str:
        """Abstract method to calculate the faculty member's workload."""
        pass

class Professor(Faculty):
    """Represents a professor."""
    def get_responsibilities(self) -> str:
        return "Teach advanced courses, conduct research, and mentor graduate students."

    def calculate_workload(self) -> str:
        return "High (Teaching + Research + Service)"

class Lecturer(Faculty):
    """Represents a lecturer."""
    def get_responsibilities(self) -> str:
        return "Deliver lectures and grade undergraduate assignments."

    def calculate_workload(self) -> str:
        return "Medium (Primarily Teaching)"

class TA(Faculty):
    """Represents a Teaching Assistant."""
    def get_responsibilities(self) -> str:
        return "Assist professors, lead tutorials, and grade papers."

    def calculate_workload(self) -> str:
        return "Variable (Based on assigned course)"