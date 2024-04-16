import pandas as pd
import numpy as np
from entry import Entry, build_from_df_row
from settings_constants import st, ct


class Database:
    def __init__(self, csv_path: str) -> None:
        self.df = pd.read_csv(csv_path, lineterminator="\n")

    def normalize_column(self, column_name: str) -> None:
        x = self.df[column_name]
        mmin: float = np.min(x)
        mmax: float = np.max(x)
        if mmax - mmin == 0:
            x = np.ones(len(x))
        self.df[column_name] = (x - mmin) / (mmax - mmin)


MOVIES_DB = Database("mymoviedb.csv")
MOVIES_DB.normalize_column("Popularity")
MOVIES_DB.normalize_column("Vote_Count")
MOVIES_DB.normalize_column("Vote_Average")


def get_movies(
    target_gens: list[str] | None = None,
    target_language: str | None = None,
    keywords: list[str] | None = None,
) -> list[Entry] | None:
    if target_gens is None and target_language is None and keywords is None:
        return entry_list_all()

    potential_recommend: list[Entry] = []
    for _, row in MOVIES_DB.df.iterrows():
        score = 0
        row_gens = [x.lower() for x in str(row["Genre"]).split(", ")]
        if target_gens:
            intersected = [x.lower() for x in target_gens if x in row_gens]
            score += evaluate_genre(target_gens, intersected)
        score += evaluate_keywords(keywords, str(row["Overview"]))
        if score:
            score += evaluate_popularity(float(row["Popularity"]))
            score += evaluate_vote_count(int(row["Vote_Count"]))
            score += evaluate_vote_avg(float(row["Vote_Average"]))
            score += evaluate_language(target_language, str(row["Original_Language"]))
            potential_recommend.append(build_from_df_row(row, score))
    return sorted(potential_recommend, reverse=True)


def entry_list_all():
    result: list[Entry] = []
    for _, movie in MOVIES_DB.df.iterrows():
        result.append(build_from_df_row(movie))
    return result


def evaluate_genre(
    target_gens: list[str] | None,
    intersected: list[str] | None,
) -> float:
    if not (target_gens and intersected):
        return 0
    score: float = 0
    for i, target_gen in enumerate(target_gens):
        score += (
            (ct.N_GENRES - i) * st.GENRE_SCALE / ct.N_GENRES
            if target_gen in intersected
            else 0
        )
    return score


def evaluate_keywords(keywords: list[str] | None, overview: str) -> float:
    if not keywords:
        return 0
    score: float = 0
    ov: str = overview.lower()
    for keyword in keywords:
        score += st.KEYWORD_SCALE if keyword.lower() in ov else 0
    return score


def evaluate_language(target_language: str | None, entry_language: str) -> float:
    return st.LANGUAGE_SCALE if target_language == entry_language else 0


def evaluate_popularity(popularity: float) -> float:
    return popularity * st.POPULARITY_SCALE


def evaluate_vote_count(vote_count: int) -> float:
    return vote_count * st.VOTE_COUNT_SCALE


def evaluate_vote_avg(vote_avg: float) -> float:
    return vote_avg * st.VOTE_AVG_SCALE
