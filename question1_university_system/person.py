# university_system/person.py

class Person:

    # A base class to represent a person in the university system.
        
    def __init__(self, name, id_number, email):
        self._name = name  # Private attribute for encapsulation
        self._id_number = id_number
        self._email = email

    def get_name(self):
        return self._name

    def get_id(self):
        return self._id_number

    def get_email(self):
        return self._email

    def get_responsibilities(self):
        return "General university member"
# Staff class    
class Staff(Person):
    def __init__(self, name, id_number, email, position):
        super().__init__(name, id_number, email)
        self.position = position

    def get_responsibilities(self):
        return f"Staff responsibilities: {self.position}"