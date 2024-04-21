# Release Date
# Title
# Overview
# Popularity
# Vote Count
# Vote Average
# Original Language
# Genre
# Poster Url


class Entry:
    def __init__(
        self,
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
    ) -> None:
        self.release_date: str = release_date
        self.title: str = title
        self.overview: str = overview
        self.popularity: float = popularity
        self.vote_count: int = vote_count
        self.vote_average: float = vote_average
        self.original_language: str = original_language
        self.genres: list[str] = genres
        self.poster_url: str = poster_url
        self.points: float = points

    def __repr__(self) -> str:
        return f"{self.title}: {self.points} points"

    def __lt__(self, other) -> bool:
        return self.points < other.points


def build_from_df_row(row, points: float = 0) -> Entry:
    entry_gens = str(row["Genre"]).split(", ")
    entry = Entry(
        row["Release_Date"],
        row["Title"],
        row["Overview"],
        row["Popularity"],
        row["Vote_Count"],
        row["Vote_Average"],
        row["Original_Language"],
        entry_gens,
        row["Poster_Url"],
        points,
    )
    return entry
