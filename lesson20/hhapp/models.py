from django.db import models
from django.db.models import Model, CharField, TextField, DateTimeField, ForeignKey
from django.db.models import ManyToManyField, URLField, FloatField, IntegerField


class Area(Model):
    name = CharField(max_length=30, verbose_name='Регион')
    ind_hh = IntegerField(verbose_name='Номер HH', blank=True, null=True, default=0)
    ind_zarp = IntegerField(verbose_name='Номер Zarplata', blank=True, null=True, default=0)
    ind_super = IntegerField(verbose_name='Номер SuperJob', blank=True, null=True, default=0)
    
    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name = 'Название региона'
        verbose_name_plural = 'Регионы'


class Employer(Model):
    name = CharField(max_length=30)
    ind = IntegerField(blank=True, null=True)
    link = URLField(blank=True, null=True)


class Schedule(Model):
    name = CharField(max_length=10)


class Word(Model):
    word = CharField(max_length=30, verbose_name='Запрос')
    count = IntegerField(verbose_name='Количество')
    up = FloatField(verbose_name="Верхняя граница")
    down = FloatField(verbose_name='Нижняя граница')

    def __str__(self):
        return self.word

    class Meta:
        verbose_name = 'Текст запроса'
        verbose_name_plural = 'Запросы'


class Type(Model):
    name = CharField(max_length=10, unique=True)


class Vacancy(Model):
    published = DateTimeField()
    name = CharField(max_length=50)
    url = URLField()
    word_id = ForeignKey(Word, on_delete=models.CASCADE)
    area = ForeignKey(Area, on_delete=models.CASCADE)
    schedule = ForeignKey(Schedule, on_delete=models.CASCADE)
    snippet = TextField()
    salaryFrom = FloatField(default=0)
    salaryTo = FloatField(default=0)
    employer = ForeignKey(Employer, on_delete=models.CASCADE)
    type = ForeignKey(Type, on_delete=models.CASCADE)


class Skill(Model):
    name = CharField(max_length=50, verbose_name='Навык')

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Название навыка'
        verbose_name_plural = 'Навыки'


class Wordskill(Model):
    id_word = ForeignKey(Word, on_delete=models.CASCADE)
    id_skill = ForeignKey(Skill, on_delete=models.CASCADE)
    count = FloatField()
    percent = FloatField()



