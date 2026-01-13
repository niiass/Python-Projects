"""
SearchSystem is class for simple graphical interface

It creates a simple app where you enter Serial Number
If no record is found you get the proper message
Otherwise, there are shown as many properties as many there are under such Serial Number

__init__:
Used to create SearchSystem type object with arguments window and data
window is the main window - tk.Tk()
data is all real estate properties data I have

search:
Handles the searching process
Gets the Serial Number from entry, searches for such records in provided data and prints an appropriate message
"""

import tkinter as tk

class SearchSystem:
    def __init__(self, window, data):
        self.window = window
        self.data = data

        tk.Label(window, text="Search By Serial Number").pack()
        self.entry = tk.Entry(window)
        self.entry.pack()

        self.btn = tk.Button(window, text="Search", command=self.search)
        self.btn.pack()

        self.result = tk.Label(window, text="")
        self.result.pack()

    def search(self):
        serial_number = self.entry.get()
        result_list = []

        for row in self.data:
            if (str(row.serial_number) == serial_number):
                result_list.append(row.display_info())

        if result_list:
            final_output = "\n\n".join(result_list)
            self.result.config(text=final_output)
        else:
            self.result.config(text="Property not found")
