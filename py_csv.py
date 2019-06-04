import csv
import random


with open('test_csv.csv', 'a') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['test', 'abc', 'gu', 'hi', f'{random.randint(0,20)}'])


with open('test_csv.csv', 'r', newline='') as f:
    reader = csv.reader(f)
    for row in reader:
        print(f'Number of columns: {len(row)}')
        print(row)
