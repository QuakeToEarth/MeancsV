import csv
import statistics
import math
f = open('data.csv')
reader = csv.reader(f)
data = list(reader)
values = data[0]
f = 0
sum = 0
for eachdata in values:
    f = f+int(eachdata)

mean = f/len(values)

for eachdata in values:
    a = int(eachdata) - mean
    s = a**2
    sum = sum+s
d = sum / (len(values) - 1)
result = math.sqrt(d)
print(result)