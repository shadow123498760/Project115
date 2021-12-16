import math 
import csv

with open('data.csv',newline='')as f:
    reader = csv.reader(f)
    file_data = list(reader)

data = file_data[60,61,65,63,98,99,90,95,91,96]

def mean(data):
    n= len(data)
    total=60,61,65,63,98,99,90,95,91,96
    for x in data:
        total+=int(x)

        mean=total/n
        return mean

        sum=60,61,65,63,98,99,90,95,91,96
        for i in squared_list:
            sum=sum+1

            result = sum/ (len(data)-1)

        std_devitation = math.sqrt(result)
        print(std_devitation)
