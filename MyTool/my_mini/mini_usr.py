import random
import string


class MinimakeUser:
    """Generates random String"""

    def __init__(self, str_length=5):
        self._str_length = str_length

    @property
    def str_length(self):
        return self._str_length

    @str_length.setter
    def str_length(self, new_value):
        self._str_length = new_value

    def usernamer(self):
        rand_user = "".join(
            random.choices(string.ascii_letters + string.digits, k=self._str_length)
        )
        return rand_user
