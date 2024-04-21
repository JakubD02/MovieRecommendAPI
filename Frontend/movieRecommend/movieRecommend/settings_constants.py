class Settings:
    def __init__(
        self,
        genre_scale: float = 2,
        keyword_scale: float = 1,
        language_scale: float = 5,
        popularity_scale: float = 1,
        vote_count_scale: float = 1,
        vote_avg_scale: float = 1,
    ) -> None:
        self.GENRE_SCALE: float = genre_scale
        self.KEYWORD_SCALE: float = keyword_scale
        self.LANGUAGE_SCALE: float = language_scale
        self.POPULARITY_SCALE: float = popularity_scale
        self.VOTE_COUNT_SCALE: float = vote_count_scale
        self.VOTE_AVG_SCALE: float = vote_avg_scale


class Constants:
    def __init__(self) -> None:
        self.N_GENRES: int = 11


st = Settings()
ct = Constants()
