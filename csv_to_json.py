import csv
import json
import os

CSV_KEY = "sector"
# Function to conve
# rt a CSV to JSON
# Takes the file paths as arguments
def make_json(csvFilePath, jsonFilePath):

    # create a dictionary
    data = {}

    # Open a csv reader called DictReader
    with open(csvFilePath, encoding="utf-8") as csvf:
        csvReader = csv.DictReader(csvf)

        # Convert each row into a dictionary
        # and add it to data
        for rows in csvReader:
            print(rows)
            # Assuming a column named 'No' to
            # be the primary key
            key = rows[CSV_KEY]
            data[key] = rows

    # Open a json writer, and use the json.dumps()
    # function to dump data
    with open(jsonFilePath, "w", encoding="utf-8") as jsonf:
        jsonf.write(json.dumps(data, indent=4))


ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
CSV_FILE_PATH = os.path.join(ROOT_DIR, "postcode_areas_central.csv")
JSON_FILE_PATH = os.path.join(ROOT_DIR, "postcode_areas_central.json")


make_json(CSV_FILE_PATH, JSON_FILE_PATH)
