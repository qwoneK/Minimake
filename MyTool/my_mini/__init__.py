import argparse
from .mini_usr import MinimakeUser
from .mini_pword import MinimakePassword
from .mini_email import MinimakeEmail


usr = MinimakeUser(12)
usr_output = usr.usernamer()

pswd = MinimakePassword()
pass_output = pswd.randomiser()

mail = MinimakeEmail(rand_email=10, str_length=10, picker="", domain="")
final_email = mail.final_email()

parser = argparse.ArgumentParser()
parser.add_argument("minimake")
parser.add_argument("-e", "--email", type=str, default=None)


args = parser.parse_args()


domain = args.email
csv_er = {
    "Username:": usr_output,
    "Password": pass_output,
    "Email:": f"{usr_output}@{domain}",
}

if args.email is not None:
    print(
        f"\nUsername:   {usr_output}\nPassword:   {pass_output}\nEmail   :    {usr_output}@{domain}\n"
    )
elif args.email is None:
    print(
        f"\nUsername:   {usr_output}\nPassword:   {pass_output}\nEmail   :    {final_email}@email.com\n"
    )
