from pprint import pprint
import re
from collections import Counter

from requests import get
from pycbrf import ExchangeRates

from db_orm import Session, Area


def parce(vacancy, pages='3', where='all'):
    url = 'https://api.hh.ru/vacancies'
    rate = ExchangeRates()
    p = {'text': vacancy if where == 'all' else f'NAME: {vacancy}' if where == 'name' else f'COMPANY_NAME: {vacancy}'}
    r = get(url=url, params=p).json()
    count_pages = r['pages']
    all_count = len(r['items'])
    result = {
            'keywords': vacancy,
            'count': all_count}
    sal = {'from': [], 'to': [], 'cur': []}
    skillis = []
    for page in range(count_pages):
        if page > int(pages):
            break
        else:
            print(f"Обрабатывается страница {page}")
        p = {'text': vacancy,
             'page': page}
        ress = get(url=url, params=p).json()
        all_count = len(ress['items'])
        result['count'] += all_count
        for res in ress['items']:
            pprint(res)
            skills = set()
            city_vac = res['area']['name']
            db = Session()
            rest = db.query(Area).filter_by(name=city_vac).one_or_none()
            if not rest:
                db.add(Area(name=city_vac, ind=res['area']['id']))
                db.commit()
            db.close()
            ar = res['area']
            res_full = get(res['url']).json()
            # pprint(res_full)
            pp = res_full['description']
            # print(pp)
            pp_re = re.findall(r'\s[A-Za-z-?]+', pp)
            # print(pp_re)
            its = set(x.strip(' -').lower() for x in pp_re)
            # print(its)
            for sk in res_full['key_skills']:
                skillis.append(sk['name'].lower())
                skills.add(sk['name'].lower())
            for it in its:
                if not any(it in x for x in skills):
                    skillis.append(it)
            if res_full['salary']:
                code = res_full['salary']['currency']
                if rate[code] is None:
                    code = 'RUR'
                k = 1 if code == 'RUR' else float(rate[code].value)
                sal['from'].append(k * res_full['salary']['from'] if res['salary']['from'] else k * res_full['salary']['to'])
                sal['to'].append(k * res_full['salary']['to'] if res['salary']['to'] else k*res_full['salary']['from'])
    # print(skillis)
    sk2 = Counter(skillis)
    # pprint(sk2)
    up = sum(sal['from']) / len(sal['from'])
    down = sum(sal['to']) / len(sal['to'])
    result.update({'down': round(up, 2),
                   'up': round(down, 2)})
    add = []
    for name, count in sk2.most_common(5):
        add.append({'name': name,
                    'count': count,
                    'percent': round((count / result['count'])*100, 2)})
    result['requirements'] = add
    # with open('area.pkl', mode='wb') as f:
    #     dump(area, f)
    return result


if __name__ == '__main__':
    vacancy = input('Введите интересующую вакансию: ')
    pprint(parce(vacancy))
