import os
import csv

budget_data = os.path.join("Resources", "budget_data.csv")
print('Financial Analysis')
print('---------------------------------------')

with open(budget_data, 'r') as csv_file:
    reader = csv.reader(csv_file, delimiter=',')
    next(reader)
    data = list(reader)
    months = len(data)
    print(f'Total Months: {months}')
 
net = []
for row in data:
    net.append(int(row[1]))
print(f'Total: ${sum(net)}')

Changes = 0
for i in range(1,len(data)):
    # print(int(data[i][1]))
    dif = int(data[i][1]) - int(data[i-1][1])
    Changes += dif
Average_change = Changes/(len(data)-1)
Average_change_format= "${:,.2f}".format(Average_change)
print(f'Average Change: {Average_change_format}')

