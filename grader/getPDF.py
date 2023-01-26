import requests
import sys
import os

from dotenv import load_dotenv
load_dotenv()



COOKIE = os.getenv('COOKIE')

url = sys.argv[1]

r = requests.get(url, headers={'Cookie': COOKIE})

open(url.split('/')[-1], 'wb').write(r.content)