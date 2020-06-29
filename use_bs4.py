import requests
from bs4 import BeautifulSoup

url = 'https://detik.com'
try:
    response = requests.get('%s' % url)
    print(f'success! Request Code = {response.status_code}')
#    print(f'Content {response.text}')
    soup = BeautifulSoup(response.text, features="html.parser")
    print(f'Hasil Pemanggilan {url}')
    print(f'Title: {soup.title.string}')
except Exception as e:
    print('There is an error', e)
print('Program Ended')