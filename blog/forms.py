from django import forms
from blog.models import Tag
from django.core.exceptions import ValidationError


class TagForm(forms.ModelForm):
    # Класс Meta позволяет не дублировать поля из  класса Tag, в соответствии с принципом DRY
    class Meta:
        model = Tag
        fields = ['title', 'slug']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'slug': forms.TextInput(attrs={'class': 'form-control'})
        }

# специальный метод дополнительной проверки поля ввода на случай конфликта
# с путем create для создания тега и перевода тегов в нижний регистр
    def clean_slug(self):
        new_slug = self.cleaned_data['slug'].lower()
        if new_slug == 'create':
            raise ValidationError('Slug may not be create')
        if Tag.objects.filter(slug__iexact=new_slug).count():
            raise ValidationError('Slug must be unique. We have "{}" slug already'.format(new_slug))
        return new_slug
