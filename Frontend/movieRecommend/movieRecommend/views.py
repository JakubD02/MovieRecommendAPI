
# Teraz możesz użyć funkcji z modułu movies_api, np. movies_api.get_movies()

from .movies_api import get_movies
from django.shortcuts import render
from .forms import LanguageGenreForm
# from .movies_api import get_movies
# from 'Frontend\movieRecommend\movieRecommend\Backend\movies_api.py' import get_movies
# from ..backend.movies_api import get_movies
# import sys
# sys.path.append('../movies_api')
# from movies_api import get_movies
# from Frontend. import get_movies
# from  import movies_api
# from MovieRecommendAPI3.MovieRecommend.movies_api import get_movies
# os.chdir('MovieRecommendAPI3\MovieRecommend\movies_api')

def home(request):
    recommended_movies = []
    if request.method == 'POST':
        form = LanguageGenreForm(request.POST)
        if form.is_valid():
            selected_language = form.cleaned_data['language']
            selected_genre = form.cleaned_data['genre']
            description = form.cleaned_data['description'].split()
            recommended_movies = get_movies([selected_genre], selected_language, description)[:5]
    else:
        form = LanguageGenreForm()

    return render(request, 'home.html', {'form': form, 'recommended_movies': recommended_movies})
