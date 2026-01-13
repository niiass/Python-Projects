"""
FourFamily is child class of RealEstate

__init__:
It calls __init__ method of RealEstate class and specifies residential type: "Four Family"
This method is used to create FourFamily type objects

display_info:
It returns string representation of residential type and display_info method of parent class
This method is used specifically for saving data to text file
"""

from Project.models.RealEstate import RealEstate

class FourFamily(RealEstate):
    def __init__(self, serial_number, list_year, date_recorded, town, address, assessed_value, sale_amount,
                 sales_ratio):
        super().__init__(serial_number, list_year, date_recorded, town, address, assessed_value, sale_amount, sales_ratio,
                       "Four Family")
    def display_info(self):
        return f"Four Family - {super().display_info()}"