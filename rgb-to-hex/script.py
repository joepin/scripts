from ast import literal_eval
import csv

tups = []
lines = []
with open('test.csv', 'r') as file:
    for row in file.readlines():
         lines.append(row.strip().replace(',', ';'))
         tups.append(literal_eval(row))

assert len(tups) == len(lines)

with open('output.csv', 'w') as file:
    writer = csv.writer(file, delimiter=',')
    for i in range(len(tups)):
        writer.writerow([lines[i], '#%02x%02x%02x' % tups[i]])
