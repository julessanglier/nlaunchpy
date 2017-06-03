import json
import urllib.request
import datetime
import time
from datetime import datetime
import gmplot

def timecode_modif(distant_str):
    model = "%B %d, %Y %H:%M:%S %Z" 
    distant = datetime.strptime(distant_str, model)
    distant = distant.replace(hour= +2)
    return distant

def tminus_second(distant):
    now = datetime.now()
    if distant.day != now.day and distant.hour != now.hour:
        return distant

    return (now-distant).total_seconds()

auto_n5 = 0
n = 5 if auto_n5 == 1 else str(input("n ?"))
url = "https://launchlibrary.net/1.2/launch/next/" + str(n)
raw_data = urllib.request.urlopen(url)
raw_data = raw_data.read().decode('utf8')
data = json.loads(raw_data)

gmap = gmplot.GoogleMapPlotter(0, 0, 3)

i = 0
for launches in data.get("launches"):
            exit if len(launches) == i else print("-----------------")
            print(launches.get("name"))
            print("")
            modif = timecode_modif(launches.get("windowstart"))
            tminus = tminus_second(modif)
            if type(tminus) is float:
                print(str(tminus) + " sec / " + str((tminus/3600)) + " h")
            else:
                print (tminus)
            for pads_data in data['launches'][i]['location']['pads']:
                print(pads_data.get("name"))
                gmap.marker(float(pads_data.get("latitude")), float(pads_data.get("longitude")), "red")
            
            print("")
            for description in launches.get("missions"):
                print(description.get("description"))
            
            i += 1

gmap.draw('./nlaunchpymap.html')

    
