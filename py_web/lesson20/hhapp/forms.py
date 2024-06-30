from django import forms


class ReqForm(forms.Form):
    vacancy = forms.CharField(label='Строка поиска ')
    where = forms.ChoiceField(label='Где искать ', choices=[('all', "Везде"),
                                                            ('company', 'В названии компании'),
                                                            ('name', 'В названии вакансии')])
    pages = forms.IntegerField(label='Количество анализируемых страниц ', initial=3)
