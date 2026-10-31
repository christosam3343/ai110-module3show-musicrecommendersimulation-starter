"""
Command line runner for the Music Recommender Simulation.

This file helps you quickly run and test your recommender.

You will implement the functions in recommender.py:
- load_songs
- score_song
- recommend_songs
"""

from textwrap import fill

if __package__:
    from .recommender import load_songs, recommend_songs
else:
    from recommender import load_songs, recommend_songs


def main() -> None:
    songs = load_songs("data/songs.csv") 
    print(f"Loaded songs: {len(songs)}")

    # Starter example profile
    user_prefs = {"genre": "pop", "mood": "happy", "energy": 0.8}

    recommendations = recommend_songs(user_prefs, songs, k=5)

    print("\n" + "=" * 60)
    print("TOP 5 MUSIC RECOMMENDATIONS")
    print("=" * 60)
    for rank, rec in enumerate(recommendations, start=1):
        song, score, explanation = rec
        print()
        print(f"{rank}. {song['title']} - Score: {score:.2f}/100")
        print("   Reasons:")
        print(fill(explanation, width=80, initial_indent="   ", subsequent_indent="   "))
        print("-" * 60)


if __name__ == "__main__":
    main()
