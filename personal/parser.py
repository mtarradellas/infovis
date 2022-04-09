import sys
import json

with open('./dataset/watch-history.json', 'r') as f:
    config = json.load(f)

full_history_list: list = config

music_history_list: list = [item for item in full_history_list if item['header'] == "YouTube Music"]

stdout = sys.stdout
with open('parsed-history.csv', 'w') as output:
    sys.stdout = output
    for i in music_history_list:
        month = int(i["time"][5:7]);
        if (month > 2):
            artist = i["subtitles"][0]["name"][:-8] if i["subtitles"][0]["name"][-8:] == " - Topic" else i["subtitles"][0]["name"]
            print(f'{i["title"][8:]};{artist};{i["time"]}');
sys.stdout = stdout
