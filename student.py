from datetime import date, timedelta

class Student:
    """ a Student class as base of method testing """

    def __init__(self, first_name, last_name):
        self._first_name = first_name
        self._last_name = last_name
        # '._' for read only fields
        self._start_date = date.today()
        self.end_date = date.today() + timedelta(days=365)
        self.naughty_list = False
    

# method to return a student’s full name
    @property
    def full_name(self):
        return f"{self._first_name} {self._last_name}"