# models/person.py

from abc import ABC, abstractmethod

class Person(ABC):
    """
    A base class to represent a person in the university system.
    This is an Abstract Base Class (ABC) as a person must be a more specific type.
    """
    def __init__(self, name: str, person_id: int, email: str):
        """Initializes a Person object."""
        self.name = name
        self.person_id = person_id
        self.email = email

    def display_info(self) -> None:
        """Displays the person's basic information."""
        print(f"Name: {self.name}, ID: {self.person_id}, Email: {self.email}")

    @abstractmethod
    def get_responsibilities(self) -> str:
        """
        Abstract method to get the responsibilities of the person.
        Must be implemented by subclasses.
        """
        pass

class Staff(Person):
    """Represents a staff member."""
    def __init__(self, name: str, person_id: int, email: str, job_title: str):
        super().__init__(name, person_id, email)
        self.job_title = job_title

    def get_responsibilities(self) -> str:
        """Returns the responsibilities of a staff member."""
        return f"Perform administrative duties related to {self.job_title}."