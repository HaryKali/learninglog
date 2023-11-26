from django import forms
from .models import Topic,Entry,Entry_md

class TopicForm(forms.ModelForm):
    class Meta:
        model=Topic
        fields=["text"]
        labels={"text":""}

class EntryForm(forms.ModelForm):
    class Meta:
        model=Entry
        fields=["text","title"]
        labels={"text":"","title":""}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}

class EntryFormmd(forms.ModelForm):
    class Meta:
        model=Entry_md
        fields=["text","title"]
        labels={"text":"","title":""}
        widgets = {'text': forms.Textarea(attrs={'cols': 80})}