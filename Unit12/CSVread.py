import csv

csv_file = open('cochise.csv')
csv_reader = csv.reader(csv_file)
csv_contents = list(csv_reader)

print(csv_contents)
