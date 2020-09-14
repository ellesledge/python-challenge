import os
import csv

budget_data = os.path.join("Resources", "budget_data.csv")
print('Financial Analysis')
print('---------------------------------------')

with open(budget_data, 'r') as csv_file:
    reader = csv.reader(csv_file, delimiter=',')
    next(csv_file)
    months = len(list(csv_file))
    print(f'Total Months: {months}')

with open(budget_data, 'r') as csv_file:
    reader = csv.reader(csv_file, delimiter=',')
    next(csv_file)
    net = []
    for row in reader:
        net.append(int(row[1]))

    print(f'Total: ${sum(net)}')

with open(budget_data, 'r') as csv_file:
    reader = csv.reader(csv_file, delimiter=',')
    next(csv_file)
    net = []
    for row in reader:
        net. append(int(row[1]))
    Average = len(net) / sum(net)
    # print(Average)
    print(f'Average Change: ${Average(net)}')

   
    
    