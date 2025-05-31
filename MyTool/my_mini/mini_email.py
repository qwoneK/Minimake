import random
import string


class MinimakeEmail:
    """Class Representing an email"""

    def __init__(self, str_length, rand_email, picker, domain):
        self._str_length = str_length
        self._picker = picker
        self._domain = domain
        self._rand_email = rand_email

    @property
    def str_length(self):
        return self._str_length

    @property
    def picker(self):
        return self._picker

    @property
    def domain(self):
        return self._domain

    @str_length.setter
    def str_length_maker(self, new_value):
        self._str_length = new_value

    @picker.setter
    def picker_maker(self, new_value):
        self._picker = new_value

    @domain.setter
    def domain_maker(self, new_value):
        self._domain = new_value


    def final_email(self):
        finalic = f"{self.rand_email()}{self.picker}{self.domain}"
        return finalic

    def rand_email(self):
        rande = "".join(
            random.choices(string.ascii_letters + string.digits, k=self._str_length)
        )
        return rande
