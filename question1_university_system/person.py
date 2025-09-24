# university_system/person.py
import re
from abc import ABC, abstractmethod

class Person(ABC):
    """Abstract base class representing a person in the university system."""
    
    def __init__(self, name: str, id_number: str, email: str):
        self._name = self._validate_name(name)
        self._id_number = self._validate_id(id_number)
        self._email = self._validate_email(email)

    def _validate_name(self, name: str) -> str:
        """Validate that name contains only letters and spaces."""
        if not isinstance(name, str) or not re.match(r'^[A-Za-z\s]+$', name.strip()):
            raise ValueError("Name must contain only letters and spaces")
        if len(name.strip()) < 2:
            raise ValueError("Name must be at least 2 characters long")
        return name.strip()

    def _validate_id(self, id_number: str) -> str:
        """Validate ID format (alphanumeric, 4-10 characters)."""
        if not isinstance(id_number, str) or not re.match(r'^[A-Za-z0-9]{4,10}$', id_number):
            raise ValueError("ID must be 4-10 alphanumeric characters")
        return id_number

    def _validate_email(self, email: str) -> str:
        """Validate email format."""
        pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
        if not isinstance(email, str) or not re.match(pattern, email):
            raise ValueError("Invalid email format")
        return email

    # Property decorators for Pythonic getters/setters
    @property
    def name(self) -> str:
        return self._name

    @name.setter
    def name(self, value: str):
        self._name = self._validate_name(value)

    @property
    def id_number(self) -> str:
        return self._id_number

    @property
    def email(self) -> str:
        return self._email

    @email.setter
    def email(self, value: str):
        self._email = self._validate_email(value)

    @abstractmethod
    def get_responsibilities(self) -> str:
        """Abstract method to be implemented by all subclasses."""
        pass

    def __str__(self) -> str:
        return f"{self.__class__.__name__}: {self._name} ({self._id_number})"

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}('{self._name}', '{self._id_number}', '{self._email}')"

# Student class
class Staff(Person):
    def __init__(self, name: str, id_number: str, email: str, position: str):
        super().__init__(name, id_number, email)
        self._position = self._validate_position(position)

    def _validate_position(self, position: str) -> str:
        """Validate staff position."""
        valid_positions = ["Admin", "HR", "Finance", "Technical", "Library"]
        if position not in valid_positions:
            raise ValueError(f"Position must be one of: {valid_positions}")
        return position

    def get_responsibilities(self) -> str:
        return f"Staff responsibilities: {self._position} - Manage administrative tasks"

    @property
    def position(self) -> str:
        return self._position

    @position.setter
    def position(self, value: str):
        self._position = self._validate_position(value)