import sys
import json

with open('./dataset/watch-history.json', 'r') as f:
    config = json.load(f)

with open('./dataset/song-data.json', 'r') as f:
    song_data = json.load(f)

full_history_list: list = config
music_history_list: list = [item for item in full_history_list if item['header'] == "YouTube Music"]

songs_missing = list()
stdout = sys.stdout
with open('parsed-history.csv', 'w') as output:
    sys.stdout = output
    print("Title;Artist;Date;Genre;Duration")
    for i in music_history_list:
        month = int(i["time"][5:7]);
        if (month > 2):
            title = i["title"][8:]
            artist = i["subtitles"][0]["name"][:-8] if i["subtitles"][0]["name"][-8:] == " - Topic" else i["subtitles"][0]["name"]
            date = f'{i["time"][5:7]}/{i["time"][8:10]}/{i["time"][0:4]}'
            if (artist in song_data and title in song_data[artist]):
                try:
                    data = song_data[artist][title]
                    genre = data["Genre"]
                    duration = data["Duration"]
                    print(f'{title};{artist};{date};{genre};{duration}');
                except:
                    sys.stdout = stdout
                    print('Data Exception:')
                    print(f'{artist} | {title}')
                    sys.stdout = output
            else:
                songs_missing.append((artist, title));
sys.stdout = stdout

if len(songs_missing) > 0:
    print("Missing:")
    for missing in songs_missing:
        print(f'{missing[0]} | {missing[1]}')