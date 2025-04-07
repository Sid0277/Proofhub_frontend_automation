import csv
# This utility can read data from CSV/Excel for data-driven testing.


def read_csv(file_path):
    with open(file_path, mode="r") as file:
        reader = csv.DictReader(file)
        return [row for row in reader]
