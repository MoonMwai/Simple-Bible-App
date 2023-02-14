from django import forms

class BibleVerseForm(forms.Form):
    book = forms.CharField(label='Book', max_length=100)
    chapter = forms.IntegerField(label='Chapter')
    verse = forms.CharField(label='Verse')