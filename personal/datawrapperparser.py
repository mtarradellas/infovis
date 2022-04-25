import csv
import json

TOTAL_DATES = 55

with open('dateindex.json', 'r') as f:
    date_index_table = json.load(f)

data_list: list = [{"Total": 0} for i in range (0, TOTAL_DATES)]

with open('dataset/parsed-history.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=';')
    header = True
    for row in reader:
        if (header):
            header = False
        else:
            header = True
            date: str = row[2]
            duration: float = round(float(row[4])/60, 2)
            idx = date_index_table[date]
            data = data_list[idx]
            if "Date" in data:
                data["Total"] += duration
            else:
                data["Date"] = date
                data["Total"] = duration

header = 'Date,Minutes'
print(header)
for date in date_index_table:
    print(f'{date},{data_list[date_index_table[date]]["Total"]}')