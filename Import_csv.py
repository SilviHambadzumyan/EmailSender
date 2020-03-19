#ImportTheCSV
import csv 

with open ('example.csv','r') as file:
  reader = csv.reader(file)

  next(reader)

  for line in reader:
    print(line [2])
