from .__init__ import csv_er
import time
import csv

class Looper:
    """Unfinished"""
    def __init__(self, quant):
        pass

    @property
    def amount(self):
        return self.amount
    @amount.setter
    def amount_maker(self, new_value):
        self.amount = new_value


    def quant(self):
        timestamp = time.time()
        with open(f'snap-{timestamp}.csv', 'w', newline='', encoding='utf-8') as csvfile:
            fieldnames = ['username', 'password', 'email']
            writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
            writer.writeheader()
            for user in csv_er:
                writer.writerow(user)