"""
StatisticsManager class is used for graphical representation of some statistics

__init__:
Used to create StatisticsManager type onject with data
data is a list of all real estate properties I have

real_estates_by_year:
Counts the number of real estate properties sold each year from 2006 to 2023
Returns tuple of years and number of properties sold each year

sale_amount_statistics:
Values in the same Sale Amount range are grouped and statistics are counted
Returns ranges and number of sold properties in these sale amount ranges

assessed_value_statistics:
Values in the same Assessed Value range are grouped and statistics are counted
Returns ranges and number of sold properties in these assessed value ranges
"""

class StatisticsManager:
    def __init__(self, data):
        self.data = data

    def real_estates_by_year(self):
        dict = {}
        for item in self.data:
            if item.list_year not in dict:
                dict[item.list_year] = 0
            else:
                dict[item.list_year] += 1

        return (list(dict.keys()), list(dict.values()))

    def sale_amount_statistics(self):
        stats = {}
        stats["<100 000"] = stats["100 000 - 200 000"] = stats["200 000 - 300 000"] = stats["300 000 - 400 000"] = stats["400 000 - 500 000"] = stats[">500 000"] = 0
        for item in self.data:
            if item.sale_amount < 100000:
                stats["<100 000"] += 1
            elif item.sale_amount < 200000:
                stats["100 000 - 200 000"] += 1
            elif item.sale_amount < 300000:
                stats["200 000 - 300 000"] += 1
            elif item.sale_amount < 400000:
                stats["300 000 - 400 000"] += 1
            elif item.sale_amount < 500000:
                stats["400 000 - 500 000"] += 1
            else:
                stats[">500 000"] += 1

        return (list(stats.keys()), list(stats.values()))

    def assessed_value_statistics(self):
        stats = {}
        stats["<50 000"] = stats["50 000 - 100 000"] = stats["100 000 - 150 000"] = stats["150 000 - 200 000"] = stats["200 000 - 250 000"] = stats[">250 000"] = 0
        for item in self.data:
            if item.assessed_value < 50000:
                stats["<50 000"] += 1
            elif item.assessed_value < 100000:
                stats["50 000 - 100 000"] += 1
            elif item.assessed_value < 150000:
                stats["100 000 - 150 000"] += 1
            elif item.assessed_value < 200000:
                stats["150 000 - 200 000"] += 1
            elif item.assessed_value < 250000:
                stats["200 000 - 250 000"] += 1
            else:
                stats[">250 000"] += 1

        return (list(stats.keys()), list(stats.values()))