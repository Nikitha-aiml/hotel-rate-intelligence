import csv

rows = [
["name","date","rate"],
["hotel AM","14-11-26",1500],
["hotel AR","15-11-26",1600],
["hotel AS","14-11-26",1550],
["hotel BB","14-11-26",1660],
["hotel BMS","14-11-26",1700],
["hotel CR","15-11-26",1570],
["hotel CB","15-11-26",1630],
["hotel DP","15-11-26",1720],
["hotel HN","15-11-26",1530]
]
with open("rates.csv","w",newline="") as f:
    csv.writer(f).writerows(rows)
try:
    with open("rates.csv","r",newline="") as f:
        for row in csv.reader(f):
            print(row)
except FileNotFoundError:
    print("rates.csv not found")
