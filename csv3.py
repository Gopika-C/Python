import csv
with open('data.csv','r') as csvfile:
 data = csv.DictReader(csvfile)
 print("Appeared  Designed By")
 print("---------------------------------")
 for row in data:
   print(row['Appeared'] ,row['Designed by'])
