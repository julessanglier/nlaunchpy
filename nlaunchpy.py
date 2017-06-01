import json
import urllib.request

n = str(input("n ?"))
url = "https://launchlibrary.net/1.2/launch/next/" + n
raw_data = urllib.request.urlopen(url)
raw_data = raw_data.read().decode('utf8')
data = json.loads(raw_data)

i = 0
for launches in data.get("launches"):
            exit if len(launches) == i else print("-----------------")
            print(launches.get("name"))
            print(launches.get("windowstart"))
            print("")
            for description in launches.get("missions"):
                print(description.get("description"))
            i += 1
