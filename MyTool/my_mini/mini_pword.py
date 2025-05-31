import string
import secrets


class MinimakePassword:
    """Generates pseudo-random string"""

    def __init__(self):
        self._punctuation_no_semic = string.punctuation.replace(";", "")
        self._alphabet = (
            string.ascii_letters + string.digits + self._punctuation_no_semic
        )

    @property
    def punctuation_no_semic(self):
        return self._punctuation_no_semic

    @property
    def alphabet(self):
        return self._alphabet

    @punctuation_no_semic.setter
    def punctuation_no_semic_maker(self, new_value):
        self.punctuation_no_semic = new_value

    @alphabet.setter
    def alphabet_maker(self, new_value):
        self.alphabet = new_value

    def randomiser(self):
        while True:
            password = "".join(secrets.choice(self._alphabet) for i in range(12))
            if (
                any(c.islower() for c in password)
                and any(c.isupper() for c in password)
                and sum(c.isdigit() for c in password) >= 3
            ):
                break
        return password
