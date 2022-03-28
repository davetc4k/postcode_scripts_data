import csv
import re
import os


def average_latlon(list, k):
    lat = []
    long = []
    for l in list:
        if re.match("[-+]?\d+.\d+$", l[0]) and re.match("[-+]?\d+.\d+$", l[1]):
            # print(l[0], l[1])
            lat.append(float(l[0]))
            long.append(float(l[1]))
    if len(lat) > 0 and len(long) > 0:
        sumlat = sum(lat) / len(lat)
        sumlon = sum(long) / len(long)
    else:
        print("ERRRRORRRRRRR")

        sumlat = None
        sumlon = None
    return (sumlat, sumlon)


def process_postcodes(path):
    areas = {}
    centers = {}
    with open(path) as csvfile:
        spamreader = csv.reader(csvfile, delimiter=",", quotechar="|")
        for row in spamreader:
            split = row[1].split(" ")
            a = split[0]
            if areas.get(a, None) is None:
                areas[a] = []
                coordinates = (row[2], row[3])
                areas[a].append(coordinates)
            else:
                coordinates = (row[2], row[3])
                areas[a].append(coordinates)
    print("DONE PROCESS")
    for k, v in areas.items():
        rad_center = average_latlon(v, k)
        if rad_center[0] is not None and rad_center[1] is not None:
            centers[k] = rad_center
    print("AVERAGES DONE")
    return centers


ROOT_DIR = os.path.dirname(os.path.abspath(__file__))
CSV_FILE_PATH = os.path.join(ROOT_DIR, "ukpostcodes.csv")
results = process_postcodes(CSV_FILE_PATH)
count = 0
with open("postcode_areas_central.txt", "w") as file:
    writer = csv.writer(file)
    header = ["sector", "lat", "lon"]
    writer.writerow(header)
    for k, v in results.items():
        data = [k, v[0], v[1]]
        writer.writerow(data)


print("DONE")
