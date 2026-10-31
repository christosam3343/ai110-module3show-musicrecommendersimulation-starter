from copy import deepcopy
from dataclasses import replace

import pytest

from src.recommender import Song, UserProfile, Recommender

def make_small_recommender() -> Recommender:
    songs = [
        Song(
            id=1,
            title="Test Pop Track",
            artist="Test Artist",
            genre="pop",
            mood="happy",
            energy=0.8,
            tempo_bpm=120,
            valence=0.9,
            danceability=0.8,
            acousticness=0.2,
        ),
        Song(
            id=2,
            title="Chill Lofi Loop",
            artist="Test Artist",
            genre="lofi",
            mood="chill",
            energy=0.4,
            tempo_bpm=80,
            valence=0.6,
            danceability=0.5,
            acousticness=0.9,
        ),
    ]
    return Recommender(songs)


def test_recommend_returns_songs_sorted_by_score():
    user = UserProfile(
        favorite_genre="pop",
        favorite_mood="happy",
        target_energy=0.8,
        likes_acoustic=False,
    )
    rec = make_small_recommender()
    results = rec.recommend(user, k=2)

    assert len(results) == 2
    assert [song.id for song in results] == [1, 2]
    assert all(isinstance(song, Song) for song in results)
    assert results[0] is rec.songs[0]


def test_explain_recommendation_returns_non_empty_string():
    user = UserProfile(
        favorite_genre="pop",
        favorite_mood="happy",
        target_energy=0.8,
        likes_acoustic=False,
    )
    rec = make_small_recommender()
    song = rec.songs[0]

    explanation = rec.explain_recommendation(user, song)
    assert isinstance(explanation, str)
    assert "Genre matches pop: +40 points." in explanation
    assert "Mood matches happy: +30 points." in explanation
    assert "Energy 0.80 compared with target 0.80: +20.00 points." in explanation
    assert "Valence 0.90 compared with target 0.60: +7.00 points." in explanation


def make_pop_user() -> UserProfile:
    return UserProfile(
        favorite_genre="pop",
        favorite_mood="happy",
        target_energy=0.8,
        likes_acoustic=False,
    )


def test_recommend_ranks_reversed_input_without_changing_songs():
    pop_song, lofi_song = make_small_recommender().songs
    songs = [lofi_song, pop_song]
    original_values = deepcopy(songs)
    rec = Recommender(songs)

    results = rec.recommend(make_pop_user(), k=2)

    assert results[0] is pop_song
    assert results[1] is lofi_song
    assert songs == original_values
    assert rec.songs is songs
    assert songs[0] is lofi_song
    assert songs[1] is pop_song


def test_recommend_changes_ranking_for_a_lofi_user():
    rec = make_small_recommender()
    user = UserProfile(
        favorite_genre="lofi",
        favorite_mood="chill",
        target_energy=0.4,
        likes_acoustic=True,
    )

    results = rec.recommend(user, k=2)

    assert [song.id for song in results] == [2, 1]


@pytest.mark.parametrize("k, expected_count", [(0, 0), (1, 1), (5, 2)])
def test_recommend_respects_k(k, expected_count):
    results = make_small_recommender().recommend(make_pop_user(), k=k)

    assert len(results) == expected_count


def test_recommend_handles_an_empty_catalog():
    assert Recommender([]).recommend(make_pop_user(), k=5) == []


def test_recommend_preserves_input_order_for_equal_scores():
    pop_song = make_small_recommender().songs[0]
    first = replace(pop_song, id=3, title="First Tied Song")
    second = replace(pop_song, id=2, title="Second Tied Song")
    rec = Recommender([first, second])

    results = rec.recommend(make_pop_user(), k=2)

    assert results[0] is first
    assert results[1] is second


def test_recommend_uses_energy_similarity_with_matching_genre_and_mood():
    pop_song = make_small_recommender().songs[0]
    higher_energy = replace(pop_song, id=3, energy=1.0)
    rec = Recommender([higher_energy, pop_song])

    results = rec.recommend(make_pop_user(), k=2)

    assert results[0] is pop_song
    assert results[1] is higher_energy


def test_recommend_uses_the_users_target_valence():
    pop_song = make_small_recommender().songs[0]
    low_valence = replace(pop_song, id=3, valence=0.2)
    rec = Recommender([pop_song, low_valence])
    user = UserProfile(
        favorite_genre="pop",
        favorite_mood="happy",
        target_energy=0.8,
        likes_acoustic=False,
        target_valence=0.2,
    )

    results = rec.recommend(user, k=2)

    assert results[0] is low_valence
    assert results[1] is pop_song
    explanation = rec.explain_recommendation(user, low_valence)
    assert "Valence 0.20 compared with target 0.20: +10.00 points." in explanation


def test_explanation_reports_mismatches_and_partial_similarity_points():
    rec = make_small_recommender()
    lofi_song = rec.songs[1]

    explanation = rec.explain_recommendation(make_pop_user(), lofi_song)

    assert "Genre does not match pop: +0 points." in explanation
    assert "Mood does not match happy: +0 points." in explanation
    assert "Energy 0.40 compared with target 0.80: +12.00 points." in explanation
    assert "Valence 0.60 compared with target 0.60: +10.00 points." in explanation
