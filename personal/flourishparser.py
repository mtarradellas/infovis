import sys
import csv
import json

TOTAL_DATES = 55

with open('dateindex.json', 'r') as f:
    date_index_table = json.load(f)

data_list: list = [dict() for i in range (0, TOTAL_DATES)]
artist_list = list()

with open('dataset/parsed-history.csv', newline='') as csvfile:
    reader = csv.reader(csvfile, delimiter=';')
    for row in reader:
        artist: str = row[1]
        date: str = row[2]
        genre: str = row[3]
        duration: float = round(float(row[4])/60, 2)
        if artist not in artist_list:
            artist_list.append(artist)
            for data in data_list:
                data[artist] = { "date": date, "artist": artist, "genre": genre, "total": 0 }
        idx = date_index_table[date]
        for i in range(idx, TOTAL_DATES):
            data = data_list[i]
            data[artist]["total"] += duration

header = f'artist\tgenre'
for date in date_index_table:
    header += f'\t{date}'
print(header)

for artist in artist_list:
    string = f'{artist}\t{data_list[0][artist]["genre"]}'
    for data in data_list:
        string += f'\t{data[artist]["total"]}'
    print(string)