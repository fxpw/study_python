from sqlite3 import connect

# Создание баз данных в файле. Если таблицы уже созданы, то его исполнять не нужно

cur = connect('base.db').cursor()

cur.executescript('''
    create table words (
    id integer primary key,
    word varchar(50) not null,
    count real,
    up real,
    down real);
    
    create table skills (
    id integer primary key,
    name varchar(255)
    );
    
    create table wordskills (
    id integer primary key,
    id_word integer,
    id_skill integer,
    count real,
    percent real,
    foreign key (id_word) references words (id)
    foreign key (id_skill) references skills (id)
    );
    
    create table area (
    id integer primary key,
    name varchar(50) unique,
    ind integer
    );
''')

cur.close()
