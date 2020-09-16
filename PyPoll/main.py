import os
import csv

election_data = os.path.join("Resources", "election_data.csv")
print('Election Results')
print('---------------------------------------')

with open(election_data, 'r') as csv_file:
    reader = csv.reader(csv_file, delimiter=',')
    next(reader)
    data = list(reader)
    Votes = len()
print(f'Total Votes: {sum(list)}')  

   