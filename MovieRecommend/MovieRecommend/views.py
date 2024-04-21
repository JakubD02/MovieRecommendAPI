from django.shortcuts import render
from .forms import LanguageGenreForm

def home(request):
    if request.method == 'POST':
        form = LanguageGenreForm(request.POST)
        if form.is_valid():
            selected_language = form.cleaned_data['language']
            selected_genre = form.cleaned_data['genre']
            description = form.cleaned_data['description']
    else:
        form = LanguageGenreForm()

    return render(request, 'home.html', {'form': form})
