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


    def alert_santa(self):
        self.naughty_list = True

# method that returns a string in the format _first_name._last_name@email.com
# _first_name and _last_name are the class property values
    @property
    def email(self):
        return f"{self._first_name.lower()}.{self._last_name.lower()}@email.com"