from django.db import models

class AddressBookList(models.Model):
    """docstring for AddressBookList."""
    fname = models.CharField(max_length=100)
    lname = models.CharField(max_length=100)
    cnumber = models.CharField(max_length=12)
    address = models.CharField(max_length=250)

    def __str__(self):
        return f'{self.fname} {self.lname} {self.cnumber} {self.address}'
