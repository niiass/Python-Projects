"""
Database Link - https://catalog.data.gov/dataset/real-estate-sales-2001-2018 (.csv)
Selected data is about Real Estate Sales from 2001 to 2023
For the project purposes, data is filtered and only Residential Real Estate Sales are left
These sales weere occurred from 2006 to 2023
Table includes Serial Number, List Year, Date Recorded, Town, Address, Assessed Value,
Sale Amount, Sales Ratio and Residential Type

- The code is written in object-oriented approach as it uses all OOP principles
- Data is processed using Pandas module
- Threads are used to write data about Condo, Single Family, Two Family, Three Family and Four Family
  in their appropriate .txt files
- SQLite3 is used to store the filtered data about all above mentioned residential type real estate properties
- Data is collected and statistics are calculated and shown through several types of graphs through matplotlib library
- Simple graphical interface app was created through tkinter library
  which helps users to search for properties by serial number
"""

import pandas as pd
from Project.models.DB_Manager import DBManager
from Project.models.StatisticsManager import StatisticsManager
from models.RealEstate import RealEstate
from models.Condo import Condo
from threading import Thread
from models.SingleFamily import SingleFamily
from models.TwoFamily import TwoFamily
from models.ThreeFamily import ThreeFamily
from models.FourFamily import FourFamily
import matplotlib.pyplot as plt
import tkinter as tk
from Project.models.SearchSystem import SearchSystem

content = pd.read_csv("data/Real_Estate_Sales_2001-2023_GL.csv").fillna('')
condo = []
single_family = []
two_family = []
three_family = []
four_family = []
for row in content.itertuples(index=False):
    if row._9 == "Condo":
        condo.append(Condo(row._0, row._1, row._2, row.Town, row.Address, row._5, row._6, row._7))
    elif row._9 == "Single Family":
        single_family.append(SingleFamily(row._0, row._1, row._2, row.Town, row.Address, row._5, row._6, row._7))
    elif row._9 == "Two Family":
        two_family.append(TwoFamily(row._0, row._1, row._2, row.Town, row.Address, row._5, row._6, row._7))
    elif row._9 == "Three Family":
        three_family.append(ThreeFamily(row._0, row._1, row._2, row.Town, row.Address, row._5, row._6, row._7))
    elif row._9 == "Four Family":
        four_family.append(FourFamily(row._0, row._1, row._2, row.Town, row.Address, row._5, row._6, row._7))


def save_to_file(data, filename):
    try:
        with open(filename, 'w') as file:
            for row in data:
                file.write(row.display_info() + "\n")
    except Exception as e:
        print(f"Error occurred: {e}")

def threads_for_files():
    condo_thread = Thread(target=save_to_file, args=(condo, "data/Condo.txt"))
    single_family_thread = Thread(target=save_to_file, args=(single_family, "data/Single_Family.txt"))
    two_family_thread = Thread(target=save_to_file, args=(two_family, "data/Two_Family.txt"))
    three_family_thread = Thread(target=save_to_file, args=(three_family, "data/Three_Family.txt"))
    four_family_thread = Thread(target=save_to_file, args=(four_family, "data/Four_Family.txt"))

    threads = [condo_thread, single_family_thread, two_family_thread, three_family_thread, four_family_thread]

    for th in threads:
        th.start()

    for th in threads:
        th.join()


def save_to_database(filename, data):
    db_manager = DBManager(filename)
    db_manager.insert_data(data)


if __name__ == "__main__":
    # Threads Testing
    threads_for_files()

    #SQLite Database Testing
    all_real_estates = condo + single_family + two_family + three_family + four_family
    save_to_database("./data/RealEstate.db", all_real_estates)

    # MATPLOTLIB Testing
    fig = plt.figure(figsize=(12, 10), facecolor="grey")
    ax_0 = fig.add_axes([0.05, 0.55, 0.4, 0.4])
    ax_1 = fig.add_axes([0.55, 0.55, 0.4, 0.4])
    ax_2 = fig.add_axes([0.15, 0.05, 0.7, 0.4])

    colors = ["r", "g", "b", "c", "m", "y", "k"]
    statistics_manager = StatisticsManager(all_real_estates)

    (years, numbers) = statistics_manager.real_estates_by_year()
    ax_0.pie(numbers, labels=years, colors=colors, shadow=True, startangle=90, autopct="%1.1f%%")
    ax_0.set_title("Saled Real Estates By Years")

    (sale_amount_range, number_of_sales) = statistics_manager.sale_amount_statistics()
    ax_1.bar(sale_amount_range, number_of_sales, color=colors)
    ax_1.set_title("Sale Amount Statistics")

    (assessed_value_range, number_of_assessed_values) = statistics_manager.assessed_value_statistics()
    ax_2.barh(assessed_value_range, number_of_assessed_values, color=colors)
    ax_2.set_xlabel("Number of Assessed Values")
    ax_2.set_ylabel("Assessed Values Range")
    ax_2.set_title("Assessed Values Statistics")

    plt.show()

    # Simple Graphical
    window = tk.Tk()
    app = SearchSystem(window, all_real_estates)
    window.mainloop()