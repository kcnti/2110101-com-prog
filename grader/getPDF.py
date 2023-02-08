import requests
import sys
import os
import re

from dotenv import load_dotenv
load_dotenv()

ID = os.getenv("ID")
PASSWD = os.getenv("PASSWD")

# COOKIE = os.getenv('COOKIE')

s = requests.Session()

auth_token = re.findall('name="authenticity_token" value="([^"]+)"', s.get("https://2110101.nattee.net/python/").text)

data = {
    'utf8': '✓',
    'authenticity_token': auth_token,
    'login': ID,
    'password': PASSWD,
    'commit': 'Login'
}

s.post("https://2110101.nattee.net/python/login/login", data=data)

select = sys.argv[1]

URL = "https://2110101.nattee.net/python/main/list"

r = s.get(URL)
html = r.text

output = re.findall('<option value="([^"]+)">\[([^"]+)\]\s+(?:.*?\s+)?', html)


URL = "https://2110101.nattee.net/python/tasks/download/"

for i in output:

    newURL = f"{URL}/{i[0]}/{i[1]}.pdf"

    if select == i[1][:2]: # 01 02 03 ...
        r = s.get(newURL)

        open(i[1]+'.pdf', 'wb').write(r.content)