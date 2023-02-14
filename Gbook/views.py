from django.shortcuts import render
import requests
from Gbook.form import BibleVerseForm

def get_verse(request):
    if request.method == 'POST':
        form = BibleVerseForm(request.POST)
        if form.is_valid():
            book = form.cleaned_data['book']
            chapter = form.cleaned_data['chapter']
            verse = form.cleaned_data['verse']
            url = f"https://bible-api.com/{book} {chapter}:{verse}"
            response = requests.get(url)
            verse_data = response.json()
            verse_text = verse_data['text']
            verse_text = verse_text.replace('\n', ' ')
            # Use the book, chapter, and verse to retrieve the verse text
            # and render it in the template
            return render(request, 'verse.html', {'verse_text': verse_text, 'form': form})
    else:
        form = BibleVerseForm()

    return render(request, 'verse.html', {'form': form})