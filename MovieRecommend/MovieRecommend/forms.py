from django import forms

class LanguageGenreForm(forms.Form):
    language = forms.ChoiceField(choices=[('1', 'ES - Spanish'), ('2', 'EN - English')], widget=forms.Select(attrs={'class': 'form-select', 'style': 'width: 100%; padding: 10px; font-size: 16px; border-radius: 5px;'}))
    genre = forms.ChoiceField(choices=[
        ('Fantasy Horror', 'Fantasy Horror'),
        ('Action', 'Action'),
        ('Romance', 'Romance'),
        ('Science Fiction', 'Science Fiction'),
        ('Comedy', 'Comedy'),
        ('Western', 'Western'),
        ('Documentary', 'Documentary'),
        ('Thriller', 'Thriller'),
        ('Music', 'Music'),
        ('History', 'History'),
        ('Crime', 'Crime'),
    ], widget=forms.Select(attrs={'class': 'form-control', 'style': 'width: 100%;'}))
    description = forms.CharField(widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 3, 'style': 'width: 100%;', 'placeholder': 'Enter movie description...'}))
