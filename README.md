# 🎵 Music Recommender Simulation

## Project Summary

In this project you will build and explain a small music recommender system.

Your goal is to:

- Represent songs and a user "taste profile" as data
- Design a scoring rule that turns that data into recommendations
- Evaluate what your system gets right and wrong
- Reflect on how this mirrors real world AI recommenders

This project simulates a content-based music recommendation system using Python. It compares songs with user preferences such as genre, mood, energy, and valence. Each song will receive a weighted score out of 100 points, and the system will recommend the highest-scoring songs. The project will also explore how recommendation algorithms work and their potential limitations and biases.

---

## How The System Works

Real-world music recommendation systems use listening habits, user preferences, and song characteristics to suggest music. My project will use a simple content-based recommendation system that compares songs with a user's preferred genre, mood, energy, and valence. Each song will receive a score out of 100 points, with 40 points for genre, 30 for mood, 20 for energy similarity, and 10 for valence similarity. Energy and valence will be scored based on how close they are to the user's preferences. The system will then rank songs from highest to lowest score and recommend the best matches.


### Planned User Profile

The recommender will use this example taste profile:

```python
user_profile = {
    "favorite_genre": "lofi",
    "favorite_mood": "chill",
    "target_energy": 0.40,
    "target_valence": 0.60,
    "likes_acoustic": True
}
```


### Recommendation System Flow

Input: User Preferences
        |
        v
Load Songs from songs.csv
        |
        v
Process: Score Each Song
- Genre match (40 points)
- Mood match (30 points)
- Energy similarity (20 points)
- Valence similarity (10 points)
        |
        v
Rank Songs by Total Score
        |
        v
Output: Top K Recommended Songs


This user prefers relaxed lofi music with moderate-low energy and a slightly positive mood.

### Song and UserProfile Features

**Song:**
- `id`, `title`, and `artist`: Identify each song.
- `genre` and `mood`: Describe the song's style and feeling.
- `energy` and `valence`: Describe the song's intensity and positivity.
- `tempo_bpm`, `danceability`, and `acousticness`: Provide additional music characteristics.

**UserProfile:**
- `favorite_genre`: The user's preferred music genre.
- `favorite_mood`: The user's preferred mood.
- `target_energy`: The user's preferred energy level.
- `likes_acoustic`: Whether the user prefers acoustic music.
- `target_valence`: A planned attribute for the user's preferred positivity level.

**Recommendation Process:**

The recommender will compare each song with the user's preferences. A matching genre earns 40 points, a matching mood earns 30 points, energy similarity earns up to 20 points, and valence similarity earns up to 10 points. Songs will be ranked from highest to lowest score, and the highest-scoring songs will be recommended.

---

### Final Algorithm Recipe

The recommender uses a weighted scoring system with a maximum of 100 points:

- Genre match: 40 points
- Mood match: 30 points
- Energy similarity: 20 points
- Valence similarity: 10 points

For energy and valence, points are calculated using:

Similarity = 1 - abs(song value - user preference)

Each song receives a total score. The songs are then sorted from highest to lowest score, and the top K songs are recommended.

### Potential Biases

The system may favor certain genres and moods because 70% of the score comes from exact genre and mood matches. This could cause it to overlook songs from other genres that have similar energy or emotional characteristics. The small dataset of 18 songs also limits musical variety. In the future, the system could use partial mood matches or different scoring weights to improve recommendations.



## Getting Started

### Setup

1. Create a virtual environment (optional but recommended):

   ```bash
   python -m venv .venv
   source .venv/bin/activate      # Mac or Linux
   .venv\Scripts\activate         # Windows

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Run the app:

```bash
python -m src.main
```

### Running Tests

Run the starter tests with:

```bash
pytest
```

You can add more tests in `tests/test_recommender.py`.

---

## Sample Recommendation Output

Actual output from running `python -m src.main` from the project root:

```text
Loading songs from data/songs.csv...
Loaded songs: 18

============================================================
TOP 5 MUSIC RECOMMENDATIONS
============================================================

1. Sunrise City - Score: 97.20/100
   Reasons:
   Genre matches pop: +40 points. Mood matches happy: +30 points. Energy 0.82
   compared with target 0.80: +19.60 points. Valence 0.84 compared with target
   0.60: +7.60 points.
------------------------------------------------------------

2. Gym Hero - Score: 65.70/100
   Reasons:
   Genre matches pop: +40 points. Mood does not match happy: +0 points. Energy
   0.93 compared with target 0.80: +17.40 points. Valence 0.77 compared with
   target 0.60: +8.30 points.
------------------------------------------------------------

3. Rooftop Lights - Score: 57.10/100
   Reasons:
   Genre does not match pop: +0 points. Mood matches happy: +30 points. Energy
   0.76 compared with target 0.80: +19.20 points. Valence 0.81 compared with
   target 0.60: +7.90 points.
------------------------------------------------------------

4. Sidewalk Crown - Score: 28.40/100
   Reasons:
   Genre does not match pop: +0 points. Mood does not match happy: +0 points.
   Energy 0.78 compared with target 0.80: +19.60 points. Valence 0.72 compared
   with target 0.60: +8.80 points.
------------------------------------------------------------

5. Night Drive Loop - Score: 27.90/100
   Reasons:
   Genre does not match pop: +0 points. Mood does not match happy: +0 points.
   Energy 0.75 compared with target 0.80: +19.00 points. Valence 0.49 compared
   with target 0.60: +8.90 points.
------------------------------------------------------------
```

**Screenshot or video** *(optional)*: <!-- Insert a screenshot or demo video link here -->

---

## Experiments You Tried

Use this section to document the experiments you ran. For example:

- What happened when you changed the weight on genre from 2.0 to 0.5
- What happened when you added tempo or valence to the score
- How did your system behave for different types of users

---

## Limitations and Risks

Summarize some limitations of your recommender.

Examples:

- It only works on a tiny catalog
- It does not understand lyrics or language
- It might over favor one genre or mood

You will go deeper on this in your model card.

---

## Reflection

Read and complete `model_card.md`:

[**Model Card**](model_card.md)

Write 1 to 2 paragraphs here about what you learned:

- about how recommenders turn data into predictions
- about where bias or unfairness could show up in systems like this



