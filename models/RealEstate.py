"""
RealEstate is an abstract base class
It encapsulates each property data and uses private attributes with public properties
Uses all OOP principles: encapsulation, inherirance, polymorphism, abstraction

__init__: 
Initializes new RealEstate object

display_info:
Abstract method which returns formatted data about property and should be overriden by  its children
to specify residential type
I implemented method overriding in child classes. By calling super().display_info(), I reused the base formatting
logic while specifing class identifiers (residential types). This ensures data consistency when writing it to files

to_database:
Converts the object attributes into a tuple format
It is specifically created to match SQLite database schema
"""

from abc import ABCMeta, abstractmethod

class RealEstate(metaclass=ABCMeta):
    def __init__(self, serial_number, list_year, date_recorded, town, address, assessed_value, sale_amount, sales_ratio,  residential_type):
        self.__serial_number = serial_number
        self.__list_year = list_year
        self.__date_recorded = date_recorded
        self.__town = town
        self.__address = address
        self.__assessed_value = assessed_value
        self.__sale_amount = sale_amount
        self.__sales_ratio = sales_ratio
        self.__residential_type = residential_type

    @abstractmethod
    def display_info(self):
        return (f"Serial Number: {self.serial_number}, List Year: {self.list_year}, "
                f"Date Recorded: {self.date_recorded}, Town: {self.town}, Address: {self.address}, "
                f"Assessed Value: {self.assessed_value}, Sale Amount: {self.sale_amount}, Sale Ratio: {self.sales_ratio}")

    @property
    def serial_number(self):
        return self.__serial_number

    @property
    def list_year(self):
        return self.__list_year

    @property
    def date_recorded(self):
        return self.__date_recorded

    @property
    def town(self):
        return self.__town

    @property
    def address(self):
        return self.__address

    @property
    def assessed_value(self):
        return self.__assessed_value

    @property
    def sale_amount(self):
        return self.__sale_amount

    @property
    def sales_ratio(self):
        return self.__sales_ratio

    @property
    def residential_type(self):
        return self.__residential_type

    def to_database(self):
        return (
            self.serial_number,
            self.list_year,
            self.date_recorded,
            self.town,
            self.address,
            self.assessed_value,
            self.sale_amount,
            self.sales_ratio,
            self.residential_type
        )
