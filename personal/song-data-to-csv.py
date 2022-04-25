import json

with open('./dataset/song-data.json', 'r') as f:
    data = json.load(f)

print('Title;Artist;Genre;Duration(s);Duration(m)')

for artist in data:
    for song in data[artist]:   
        time = int(data[artist][song]["Duration"])
        print(f'{song};{artist};{data[artist][song]["Genre"]};{time};{round(time/60, 2)}')

