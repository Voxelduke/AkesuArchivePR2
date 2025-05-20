from .models import Subject, Topic, Note
from django.forms import ModelForm

class SubjectForm(ModelForm):
    class Meta:
        model = Subject
        fields = '__all__'

class TopicForm(ModelForm):
    class Meta:
        model = Topic
        fields = '__all__'

class NoteForm(ModelForm):
    class Meta:
        model = Note
        fields = '__all__'