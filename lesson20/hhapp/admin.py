from django.contrib import admin
from .models import Vacancy, Area, Employer, Schedule, Skill, Word, Wordskill, Type


admin.site.register(Vacancy)
admin.site.register(Area)
admin.site.register(Employer)
admin.site.register(Schedule)
admin.site.register(Skill)
admin.site.register(Word)
admin.site.register(Wordskill)
admin.site.register(Type)

