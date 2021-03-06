import json
import sys
import requests

if len(sys.argv) != 2:
    sys.exit()

# API request - changed limit from 1 to 50 instead
response = requests.get("https://itunes.apple.com/search?entity=song&limit=50&term=" + sys.argv[1])

o = response.json()
for result in o["results"]:
    print(result["trackName"])
