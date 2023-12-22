import re
from datetime import datetime
from csv import DictWriter

from bs4 import BeautifulSoup
from requests import get


new = f'/feed/?q=FastAPI'
with open('base.csv', mode='w', encoding='utf8') as f:
    tt = DictWriter(f, fieldnames=['date', 'title', 'link', 'text'], delimiter=';')
    tt.writeheader()
    while new:
        row = {}
        res = get(f'https://pythondigest.ru{new}')
        soup = BeautifulSoup(res.text, 'html.parser')
        for tag in soup.find_all('div', class_='item-container'):
            title = tag.find(rel=['nofollow'])
            row['title'] = title.get_text()
            row['link'] = title.get('href')
            dat = tag.find('small')
            d1 = re.search(r'\d{2}\.\d{2}\.\d{4}', dat.get_text())[0]
            d2 = datetime.strptime(d1, '%d.%m.%Y').date()
            row['date'] = d2
            row['text'] = ''.join([x.get_text() for x in tag.find_all('p')])
            tt.writerow(row)
        ss = soup.find('ul', class_='pagination pagination-sm')
        p = ss.find_all('li')[-1]
        new = p.a.get('href')