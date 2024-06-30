from sqlite3 import connect


def add_words(cur, new):
    """
    Добавление или редактирование строки в таблице со строками поиска.
    :param cur: передача курсора доступа к базе данных.
    :param new: словарь с данными.
    :return: Курсор доступа к базе
    """
    cur.execute('select * from words where words.word = ?', (new['keywords'],))
    res = cur.fetchone()
    print(res)
    if res:
        if res[2] < new['count']:
            # обновление строки таблицы
            cur.execute('update words set count = ?, up = ?, down = ? where words.id = ?',
                        (new['count'], new['up'], new['down'], res[0]))
            print('Edit')
        else:
            print('Not edit')
    else:
        # добавление строки в таблице
        cur.execute('insert into words values (null, ?, ?, ?, ?)',
                    (new['keywords'], new['count'], new['up'], new['down']))
        print('Done')
    return cur


def add_skills(cur, new):
    """
    Добавление строки в таблицу навыков.
    :param cur: объект курсора доступа к базе данных.
    :param new: словарь данных с результатами обработки.
    :return: курсор доступа к базе данных.
    """
    for item in new['requirements']:
        res = cur.execute('select * from skills where skills.name = ?', (item['name'],))
        if not res.fetchone():
            print(item['name'])
            cur.execute('insert into skills values (null, ?)', (item['name'],))
    return cur


def add_ws(cur, new):
    """
    Добавление строки в сводную таблицу
    :param cur: курсор доступа к базе данных.
    :param new: словарь с данными обработки вакансий.
    :return: курсор доступа к базе данных.
    """
    cur.execute('select id, count from words where words.word = ?', (new['keywords'],))
    word_id, word_count = cur.fetchone()
    for item in new['requirements']:
        cur.execute('select id from skills where skills.name = ?', (item['name'],))
        skill_id = cur.fetchone()[0]
        print(word_id, skill_id)
        cur.execute('select * from wordskills as ws where ws.id_word = ? and ws.id_skill = ?',
                    (word_id, skill_id))
        res = cur.fetchone()
        if not res:
            cur.execute('insert into wordskills values (null, ?, ?, ?, ?)',
                        (word_id, skill_id, item['count'], item['percent']))
            print('ws done')
        elif word_count < new['count']:
            cur.execute('update wordskills as ws set count = ?, percent = ? where ws.id_word = ? and ws.id_skill = ?',
                        (item['count'], item['percent'], word_id, skill_id))
            print('ws edit')
        print('ws not edit')
    return cur


def add_row(new):
    """
    Добавление строк в таблицы.
    :param new: словарь с результатами обработки вакансий
    """
    con = connect('base.db')
    cur = con.cursor()
    cur = add_words(cur, new)
    cur = add_skills(cur, new)
    cur = add_ws(cur, new)
    con.commit()
    con.close()
