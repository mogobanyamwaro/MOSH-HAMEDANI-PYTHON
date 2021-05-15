import csv


with open('data.csv','w') as file:
    writer = csv.writer(file)
    writer.writerow(['tran_id','prod_id','name'])
    writer.writerow([1110,1,'Douglas Mogoba'])
    writer.writerow([1000,2,'Felix Odthambo'])
    writer.writerow([1910,3,'Keuma Dolvin'])

with open('data.csv') as file:
    reader = csv.reader(file)
    print(list(reader))
   