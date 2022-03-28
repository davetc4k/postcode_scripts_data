import pandas as pd
import csv

url = (
    r"https://en.wikipedia.org/wiki/List_of_postcode_districts_in_the_United_Kingdom#PA"
)
tables = pd.read_html(url)  # Returns list of all tables on page
table = tables[1]

with open("city_postcodes.csv", "w") as file:
    writer = csv.writer(file)
    header = ["index", "area", "sector", "city", "county"]
    writer.writerow(header)
    for index, row in table.iterrows():

        writer.writerow(row)
