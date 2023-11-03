from django import forms

from mailing_app.models import Blog


class BlogForm(forms.ModelForm):

    class Meta:
        model = Blog
        fields = ('name', 'text', 'preview', 'is_published')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'form-control'
