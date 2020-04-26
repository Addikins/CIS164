import csv

csv_file = open('cochise.csv', 'w', newline='')
csv_writer = csv.writer(csv_file)

csv_writer.writerow(['Cochise', 'College', 'Online'])
csv_writer.writerow(['CIS', '164', 'Python', 'Programming'])
csv_writer.writerow(['Cochise', 'College', 'Sierra Vista', 'Campus'])
csv_writer.writerow(['Hello', 'World!'])

csv_file.close()
