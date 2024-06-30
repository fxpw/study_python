from pprint import pprint
from collections import Counter
import re
from datetime import datetime
import os

from django.core.management.base import BaseCommand
from django.core.exceptions import ObjectDoesNotExist
from requests import get
from pycbrf import ExchangeRates
from dotenv import load_dotenv

from hhapp.models import Word, Wordskill, Skill, Vacancy, Schedule, Employer, Area, Type

load_dotenv()


class Command(BaseCommand):
    def __init__(self, vacancy, pages, where):
        super().__init__()
        self.vac = vacancy
        self.pages = pages
        self.where = where

    def handle(self, *args, **options):
        res = start(self.vac, pages=self.pages, where=self.where)
        print(res)
        add_words(res)
        add_skills(res)
        add_ws(res)


def skills1(pp: str, skil: list, skillis: list):
    skills = set()
    pp_re = re.findall(r'\s[A-Za-z-?]+', pp)
    its = set(x.strip(' -').lower() for x in pp_re)
    for sk in skil:
        skillis.append(sk['name'].lower())
        skills.add(sk['name'].lower())
    for it in its:
        if not any(it in x for x in skills):
            skillis.append(it)
    return skillis


def parce_sup(vacancy, pages='3', where='all'):
    url = 'https://api.superjob.ru/2.0/vacancies/'
    key = os.getenv('key_super')
    head = {
        'X-Api-App-Id': key,
        'Authorization': 'Bearer r.000000010000001.example.access_token',
        'Content-Type': 'application/x-www-form-urlencoded'}

    p = {'keyword': vacancy,
         'period': 3}

    res = get(url, headers=head, params=p).json()
    count = len(res['objects'])
    pages1 = res['total'] // count
    print(pages)
    ski = []
    sal = {'from': [], 'to': [], 'cur': []}
    result = {
        'keywords': 'python',
        'count': count}
    for i in range(1, pages1):
        if i > int(pages):
            break
        p = {'keyword': 'python',
             'period': 3,
             'page': i}
        res = get(url, headers=head, params=p).json()
        result['count'] += len(res['objects'])
        for vac in res['objects']:
            # pprint(vac)
            url1 = vac['link']
            area_id = vac['town']['id']
            area_name = vac['town']['title']
            employer_id = vac['client'].get('id', 0)
            employer_name = vac['client'].get('title', '')
            employer_link = vac['client'].get('client_logo', None)
            title = vac['profession']
            published = datetime.fromtimestamp(vac['date_published'])
            schedule = vac['place_of_work']
            type = 'Открытая'
            snippet = vac['vacancyRichText']
            are = Area.objects.filter(name=area_name).first()
            if are:
                are.ind_super = area_id
                are.save()
            else:
                are = Area.objects.create(name=area_name, ind_super=area_id)
            em = Employer.objects.get_or_create(name=employer_name, ind=employer_id, link=employer_link)[0]
            sc = Schedule.objects.get_or_create(name=schedule)[0]
            t = Type.objects.get_or_create(name=type)[0]
            w = Word.objects.filter(word=vacancy).first()
            if not w:
                w = Word.objects.create(word=vacancy, count=1, up=1, down=1)
            ski = skills1(snippet, [], ski)
            if vac['payment_from'] or vac['payment_to']:
                salary_from = vac['payment_from'] if vac['payment_from'] else vac['payment_to']
                salary_to = vac['payment_to'] if vac['payment_to'] else vac['payment_from']
                sal['from'].append(salary_from)
                sal['to'].append(salary_to)
            else:
                salary_from, salary_to = 0, 0
            Vacancy.objects.create(published=published, name=title, url=url1, word_id=w, area=are, schedule=sc,
                                   snippet=snippet, salaryFrom=salary_from, salaryTo=salary_to, employer=em,
                                   type=t)
        sk2 = Counter(ski)
        up = sum(sal['from']) / len(sal['from'])
        down = sum(sal['to']) / len(sal['to'])
        result.update({'down': round(up, 2),
                       'up': round(down, 2)})
        add = []
        for name, count in sk2.most_common(5):
            add.append({'name': name,
                        'count': count,
                        'percent': round((count / result['count']) * 100, 2)})
        result['requirements'] = add
        return result


def parce(url, vacancy, pages='3', where='all'):
    # url = 'https://api.hh.ru/vacancies'
    rate = ExchangeRates()
    vacancy = vacancy if where == 'all' else f'NAME: {vacancy}' if where == 'name' else f'COMPANY_NAME: {vacancy}'
    p = {'text': vacancy}
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
            url1 = res['alternate_url']
            area_id = res['area']['id']
            area_name = res['area']['name']
            employer_id = res['employer'].get('id', 0)
            employer_name = res['employer']['name']
            employer_link = res['employer']['logo_urls']['original'] if res['employer'].get('logo_urls', 0) else None
            title = res['name']
            published = res['published_at']
            schedule = res['schedule']['name']
            type = res['type']['name']
            are = Area.objects.filter(name=area_name).first()
            if url.startswith('https://api.hh'):
                if are:
                    are.ind_hh = area_id
                    are.save()
                else:
                    are = Area.objects.create(name=area_name, ind_hh=area_id)
            else:
                if are:
                    are.ind_zarp = area_id
                    are.save()
                else:
                    are = Area.objects.create(name=area_name, ind_zarp=area_id)
            em = Employer.objects.get_or_create(name=employer_name, ind=employer_id, link=employer_link)[0]
            sc = Schedule.objects.get_or_create(name=schedule)[0]
            t = Type.objects.get_or_create(name=type)[0]
            w = Word.objects.filter(word=vacancy).first()
            if not w:
                w = Word.objects.create(word=vacancy, count=1, up=1, down=1)
            ar = res['area']
            res_full = get(res['url']).json()
            pp = res_full['description']
            pp_re = re.findall(r'\s[A-Za-z-?]+', pp)
            its = set(x.strip(' -').lower() for x in pp_re)
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
                salary_from = k * res_full['salary']['from'] if res['salary']['from'] else k * res_full['salary']['to']
                salary_to = k * res_full['salary']['to'] if res['salary']['to'] else k * res_full['salary']['from']
                sal['from'].append(salary_from)
                sal['to'].append(salary_to)
            else:
                salary_from, salary_to = 0, 0
            snippet = res_full['description']
            Vacancy.objects.create(published=published, name=title, url=url1, word_id=w, area=are, schedule=sc,
                                   snippet=snippet, salaryFrom=salary_from, salaryTo=salary_to, employer=em,
                                   type=t)
    sk2 = Counter(skillis)
    up = sum(sal['from']) / len(sal['from'])
    down = sum(sal['to']) / len(sal['to'])
    result.update({'down': round(up, 2),
                   'up': round(down, 2)})
    add = []
    for name, count in sk2.most_common(5):
        add.append({'name': name,
                    'count': count,
                    'percent': round((count / result['count']) * 100, 2)})
    result['requirements'] = add
    return result


def start(vacancy, pages='3', where='all'):
    sk1 = parce_sup(vacancy, pages=pages, where=where)
    sk2 = parce(url='https://api.hh.ru/vacancies', vacancy=vacancy, pages=pages, where=where)
    sk3 = parce(url='https://api.zarplata.ru/vacancies', vacancy=vacancy, pages=pages, where=where)
    result = {'keywords': vacancy}
    res = (it for it in (sk1, sk2, sk3) if it)
    sk = {}
    for item in res:
        result['count'] = result.get('count', 0) + item['count']
        result['down'] = item['down'] if not result.get('down', None) else (result['down'] + item['down']) / 2
        result['up'] = item['up'] if not result.get('up', None) else (result['up'] + item['up']) / 2
        for it in item['requirements']:
            if sk.get(it['name'], {}):
                sk[it['name']] = {'count': sk[it['name']]['count'] + it['count'],
                                  'percent': round((sk[it['name']]['percent'] + it['percent']) / 2, 2)}
            else:
                sk[it['name']] = {'count': it['count'],
                                  'percent': it['percent']}
    # print(sk)
    result['requirements'] = sorted([{'name': it,
                                      'count': sk[it]['count'],
                                      'percent': sk[it]['percent']} for it in sk.keys() if it],
                                    key=lambda x: x['percent'],
                                    reverse=True)
    return result


def add_words(res):
    try:
        obj = Word.objects.get(word=res['keywords'])
        print(obj)
        if obj.count < res['count']:
            obj.count = res['count']
            obj.up = res['up']
            obj.down = res['down']
            obj.save()
            print('Edit')
        else:
            print('Not edit')
    except ObjectDoesNotExist:
        Word.objects.create(word=res['keywords'], count=res['count'], up=res['up'], down=res['down'])


def add_skills(res):
    for item in res['requirements']:
        try:
            r = Skill.objects.get(name=item['name'])
            print('skill not added')
        except ObjectDoesNotExist:
            Skill.objects.create(name=item['name'])


def add_ws(res):
    word = Word.objects.get(word=res['keywords'])
    for item in res['requirements']:
        skill = Skill.objects.get(name=item['name'])
        print(word, skill)
        r = Wordskill.objects.filter(id_word=word, id_skill=skill).first()
        if not r:
            Wordskill.objects.create(id_word=word, id_skill=skill, count=item['count'], percent=item['percent'])
            print('ws done')
        elif word.count < res['count']:
            r.count = item['count']
            r.percent = item['percent']
            print('ws edit')
        else:
            print('ws not edit')


if __name__ == '__main__':
    parce('python', pages='0')
