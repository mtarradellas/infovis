import csv
import json

TOTAL_DATES = 55

with open('dateindex.json', 'r') as f:
    date_index_table = json.load(f)

data_list: list = [dict() for i in range (0, TOTAL_DATES)]
genres_list = list()

with open('dataset/parsed-history.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=';')
    header = True
    for row in reader:
        if (header):
            header = False
        else:
            header = True
            date: str = row[2]
            genre: str = row[3]
            if "rock" in genre.lower():
                genre = "Rock"
            elif "metal" in genre.lower():
                genre = "Metal"
            elif "jazz" in genre.lower():
                genre = "Jazz"
            else:
                genre = "Other"
            duration: float = round(float(row[4])/60, 2)
            idx = date_index_table[date]
            data = data_list[idx]
            if genre not in genres_list:
                genres_list.append(genre)
            if "Date" in data:
                if genre not in data:
                    data[genre] = 0
                data[genre] += duration
            else:
                data["Date"] = date
                data[genre] = duration

header = 'Date'
for genre in genres_list:
    header += f',{genre}'
print(header)
for date in date_index_table:
    row = f'{date}'
    for genre in genres_list:
        val = 0
        if genre in data_list[date_index_table[date]]:
            val = data_list[date_index_table[date]][genre]
        row += f',{val}'
    print(row)