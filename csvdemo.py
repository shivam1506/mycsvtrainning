import csv
with open('PRODUCTS.csv','r') as csvfile:
    reader=csv.reader(csvfile)
    high=0
    c=0
    for row in reader:
        #print(row[3],row[17])
        if c != 0:
            x=int(row[6])
            if x >= high:
                high=int(row[6])
        c=c+1
    #print(high)