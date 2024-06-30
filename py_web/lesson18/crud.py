from db_orm import Session, Word, Skill, WordSkill


def add_words(cur, new):
    res = cur.query(Word).filter_by(word=new['keywords']).first()
    if res:
        if res.count < new['count']:
            res.count = new['count']
            res.up = new['up']
            res.down = new['down']
            print('Edit')
        else:
            print('Not edit')
    else:
        cur.add(Word(word=new['keywords'], count=new['count'], up=new['up'], down=new['down']))
        print('Done')
    return cur


def add_skills(cur, new):
    for item in new['requirements']:
        res = cur.query(Skill).filter_by(name=item['name']).one_or_none()
        if not res:
            print(item['name'])
            cur.add(Skill(name=item['name']))
        else:
            print('skill not added')
    return cur


def add_ws(cur, new):
    res = cur.query(Word).filter_by(word=new['keywords']).first()
    word_id, word_count = res.id, res.count
    for item in new['requirements']:
        skill_id = cur.query(Skill).filter_by(name=item['name']).first().id
        print(word_id, skill_id)
        res = cur.query(WordSkill).filter_by(id_word=word_id, id_skill=skill_id).one_or_none()
        if not res:
            cur.add(WordSkill(id_word=word_id, id_skill=skill_id, count=item['count'], percent=item['percent']))
            print('ws done')
        elif word_count < new['count']:
            res.count = item['count']
            res.percent = item['percent']
            print('ws edit')
        else:
            print('ws not edit')
    return cur


def add_row(new):
    cur = Session()
    cur = add_words(cur, new)
    cur = add_skills(cur, new)
    cur = add_ws(cur, new)
    cur.commit()
    cur.close()


if __name__ == '__main__':
    add_row({'keywords': 'python1', 'count': 225, 'up': 234567.32, 'down': 654321.34,
             'requirements': [{'name': 'first', 'count': 25, 'percent': 34},
                              {'name': 'second', 'count': 24, 'percent': 33}]})
