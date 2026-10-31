import csv

from typing import List, Dict, Tuple, Optional
from dataclasses import dataclass

@dataclass
class Song:
    """
    Represents a song and its attributes.
    Required by tests/test_recommender.py
    """
    id: int
    title: str
    artist: str
    genre: str
    mood: str
    energy: float
    tempo_bpm: float
    valence: float
    danceability: float
    acousticness: float

@dataclass
class UserProfile:
    """
    Represents a user's taste preferences.
    Required by tests/test_recommender.py
    """
    favorite_genre: str
    favorite_mood: str
    target_energy: float
    likes_acoustic: bool
    target_valence: float = 0.60

class Recommender:
    """
    OOP implementation of the recommendation logic.
    Required by tests/test_recommender.py
    """
    def __init__(self, songs: List[Song]):
        self.songs = songs

    def recommend(self, user: UserProfile, k: int = 5) -> List[Song]:
        # TODO: Implement recommendation logic
        return self.songs[:k]

    def explain_recommendation(self, user: UserProfile, song: Song) -> str:
        # TODO: Implement explanation logic
        return "Explanation placeholder"

def load_songs(csv_path: str) -> List[Dict]:
    """Load songs from a CSV file and convert numerical fields to numbers."""
    print(f"Loading songs from {csv_path}...")
    songs = []
    with open(csv_path, newline="", encoding="utf-8") as csv_file:
        reader = csv.DictReader(csv_file)
        for song in reader:
            song["id"] = int(song["id"])
            song["tempo_bpm"] = float(song["tempo_bpm"])
            song["energy"] = float(song["energy"])
            song["valence"] = float(song["valence"])
            song["danceability"] = float(song["danceability"])
            song["acousticness"] = float(song["acousticness"])
            songs.append(song)
    return songs

def score_song(user_prefs: Dict, song: Dict) -> Tuple[float, List[str]]:
    """Calculate a weighted matching score and return the score and reasons."""
    # Accepts genre/mood/energy or favorite_genre/favorite_mood/target_energy.
    # The longer preference names take precedence if both styles are present.
    # target_valence defaults to 0.60 when omitted.
    # Energy and valence values are expected to be between 0 and 1.
    user_genre = user_prefs.get("favorite_genre", user_prefs.get("genre"))
    user_mood = user_prefs.get("favorite_mood", user_prefs.get("mood"))
    user_energy = user_prefs.get("target_energy", user_prefs.get("energy"))
    user_valence = user_prefs.get("target_valence", 0.60)

    score = 0.0
    reasons = []

    if song["genre"] == user_genre:
        score += 40
        reasons.append(f"Genre matches {user_genre}: +40 points.")
    else:
        reasons.append(f"Genre does not match {user_genre}: +0 points.")

    if song["mood"] == user_mood:
        score += 30
        reasons.append(f"Mood matches {user_mood}: +30 points.")
    else:
        reasons.append(f"Mood does not match {user_mood}: +0 points.")

    energy_points = 20 * (1 - abs(song["energy"] - user_energy))
    score += energy_points
    reasons.append(
        f"Energy {song['energy']:.2f} compared with target {user_energy:.2f}: "
        f"+{energy_points:.2f} points."
    )

    valence_points = 10 * (1 - abs(song["valence"] - user_valence))
    score += valence_points
    reasons.append(
        f"Valence {song['valence']:.2f} compared with target {user_valence:.2f}: "
        f"+{valence_points:.2f} points."
    )

    return score, reasons

def recommend_songs(user_prefs: Dict, songs: List[Dict], k: int = 5) -> List[Tuple[Dict, float, str]]:
    """Rank songs by score and return the top k recommendations with explanations."""
    # Equally scored songs keep their original order.
    results = []
    for song in songs:
        score, reasons = score_song(user_prefs, song)
        explanation = " ".join(reasons)
        results.append((song, score, explanation))

    ranked_results = sorted(results, key=lambda result: result[1], reverse=True)
    return ranked_results[:k]
