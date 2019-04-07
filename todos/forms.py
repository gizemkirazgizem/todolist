from django import forms

from todos.models import Todo

class TodoForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(TodoForm, self).__init__(*args, **kwargs)
        for field in iter(self.fields):
            self.fields[field].widget.attrs.update({
                'class': 'form-control',
            })
    class Meta:
        model = Todo
        #fields = "__all__"
        fields = ['todo', 'status']

