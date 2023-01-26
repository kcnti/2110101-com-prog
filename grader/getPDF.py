import requests
import sys
import os
import re

from dotenv import load_dotenv
load_dotenv()

COOKIE = os.getenv('COOKIE')

select = sys.argv[1]

URL = "https://2110101.nattee.net/python/main/list"

r = requests.get(URL, headers={"cookie": COOKIE})
html = r.text

output = re.findall('<option value="([^"]+)">\[([^"]+)\]\s+(?:.*?\s+)?', html)


URL = "https://2110101.nattee.net/python/tasks/download/"

for i in output:

    newURL = f"{URL}/{i[0]}/{i[1]}.pdf"

    if select == i[1][:2]: # 01 02 03 ...
        r = requests.get(newURL, headers={'Cookie': COOKIE})

        open(i[1]+'.pdf', 'wb').write(r.content)