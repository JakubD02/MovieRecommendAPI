### Movie recommender API based on database containing over 9000 movies.


## Movie Genres
 - Fantasy Horror
 - Action
 - Romance
 - Science Fiction
 - Comedy
 - Western
 - Documentary
 - Thriller
 - Music
 - History
 - Crime
## Languages
 - en (English)
 - es (Spanish)

# Usage
Function returns list of objects of type 'Entry'. Every parameter is optional.
### Syntax
```python
list_of_movies: list[Entry] = get_movies(
    gens: [ Genres as strings in list ],
    lang: es | en,
    keywords: [ Keywords as strings in list ]
)
```
### Example
```python
list_of_movies = get_movies(["thriller"], "en", ["breathtaking"])
```
### Entry variables
Entry contains public variables such as 
```python
release_date: str,
title: str,
overview: str,
popularity: float,
vote_count: int,
vote_average: float,
original_language: str,
genres: list[str],
poster_url: str,
points: float,
```

### Example 
```python
from movies_recommender import get_movies

movies: list[Entry] = get_movies(["Action", "crime"])
# notice that genres are case-insensitive

first_title: str = movies[0].title
# etc
```

### No params
```python
movies = get_movies()
# returns whole db
```

# Settings
Every column has own scale which is being used to calculate points, every scale can beeasly changed. **Change scales before get_movies(...)**.

### List of scales
```python
genre_scale: float = 2,
keyword_scale: float = 1,
language_scale: float = 5,
popularity_scale: float = 1,
vote_count_scale: float = 1,
vote_avg_scale: float = 1,
```
### Example 
```python
from movies_recommender import st

st.keyword_scale = 10
# scale for every keyword changed from 1 to 10 -> every keyword gives even more points
```

# Database 
[link to database](https://www.kaggle.com/datasets/disham993/9000-movies-dataset)
