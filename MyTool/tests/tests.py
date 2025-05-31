import unittest
import string
from my_mini import MinimakeUser
from my_mini import MinimakePassword
from my_mini import MinimakeEmail


class TesMinimakeUser(unittest.TestCase):
    def test_usernamer_returns_str(self):
        str_length = 12
        usr = MinimakeUser(str_length)
        usrname = usr.usernamer()
        self.assertIsInstance(usrname, str)

    def test_usrname_length(self):
        usr = MinimakeUser(str_length=12)
        usrname = usr.usernamer()
        self.assertEqual(len(usrname), 12)

    def test_usernamer_alphabet(self):
        usr = MinimakeUser(str_length=12)
        usrname = usr.usernamer()
        for i in usrname:
            self.assertIn(i, string.ascii_letters + string.digits)


class TestMinimakePassword(unittest.TestCase):
    def test_pass_length(self):
        pswd = MinimakePassword()
        pass_output = pswd.randomiser()
        self.assertEqual(len(pass_output), 12)

    def test_pass_signs(self):
        passw = MinimakePassword()
        pass_output = passw.randomiser()
        for i in pass_output:
            self.assertIn(i, string.ascii_letters + string.digits + string.punctuation)


class TestMinimakeEmail(unittest.TestCase):
    def test_email_returns_str(self):
        mail = MinimakeEmail(rand_email=12, str_length=10, picker="", domain="")
        rander = mail.rand_email()
        self.assertIsInstance(rander, str)

    def test_email_length(self):
        email = MinimakeEmail(rand_email=12, str_length=12, picker="", domain="")
        mailer = email.rand_email()
        self.assertEqual(len(mailer), 12)

    def test_usernamer_alphabet(self):
        email = MinimakeEmail(rand_email=12, str_length=12, picker="", domain="")
        mailer = email.rand_email()
        for i in mailer:
            self.assertIn(i, string.ascii_letters + string.digits)

    def test_final_email(self):
        email = MinimakeEmail(rand_email=12, str_length=12, picker="", domain="")
        finalise = email.final_email()
        comparitor = email.rand_email()
        self.assertNotEqual(finalise, comparitor)
