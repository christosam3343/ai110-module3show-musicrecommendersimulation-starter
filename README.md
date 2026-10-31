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

## Phase 4: Stress Test Results

I loaded the 18 songs once with `load_songs()` and ran all six profiles through `recommend_songs()` with `k=5`. The output below was captured from that run using the existing 40/30/20/10 scoring rule. Each profile returned five songs in descending score order.

### High-Energy Pop

```text
=== High-Energy Pop ===
Preferences: genre=pop, mood=happy, energy=0.85, valence=0.80
1. Sunrise City | Score: 99.00/100
   Genre matches pop: +40 points. Mood matches happy: +30 points. Energy 0.82 compared with target
   0.85: +19.40 points. Valence 0.84 compared with target 0.80: +9.60 points.
2. Gym Hero | Score: 68.10/100
   Genre matches pop: +40 points. Mood does not match happy: +0 points. Energy 0.93 compared with
   target 0.85: +18.40 points. Valence 0.77 compared with target 0.80: +9.70 points.
3. Rooftop Lights | Score: 58.10/100
   Genre does not match pop: +0 points. Mood matches happy: +30 points. Energy 0.76 compared with
   target 0.85: +18.20 points. Valence 0.81 compared with target 0.80: +9.90 points.
4. Electric Horizon | Score: 28.40/100
   Genre does not match pop: +0 points. Mood does not match happy: +0 points. Energy 0.90 compared
   with target 0.85: +19.00 points. Valence 0.86 compared with target 0.80: +9.40 points.
5. Plaza in Bloom | Score: 27.80/100
   Genre does not match pop: +0 points. Mood does not match happy: +0 points. Energy 0.81 compared
   with target 0.85: +19.20 points. Valence 0.94 compared with target 0.80: +8.60 points.
Confirmed: 5 recommendations; scores in descending order.
```

### Chill Lofi

```text
=== Chill Lofi ===
Preferences: genre=lofi, mood=chill, energy=0.40, valence=0.60
1. Midnight Coding | Score: 99.20/100
   Genre matches lofi: +40 points. Mood matches chill: +30 points. Energy 0.42 compared with target
   0.40: +19.60 points. Valence 0.56 compared with target 0.60: +9.60 points.
2. Library Rain | Score: 99.00/100
   Genre matches lofi: +40 points. Mood matches chill: +30 points. Energy 0.35 compared with target
   0.40: +19.00 points. Valence 0.60 compared with target 0.60: +10.00 points.
3. Focus Flow | Score: 69.90/100
   Genre matches lofi: +40 points. Mood does not match chill: +0 points. Energy 0.40 compared with
   target 0.40: +20.00 points. Valence 0.59 compared with target 0.60: +9.90 points.
4. Spacewalk Thoughts | Score: 57.10/100
   Genre does not match lofi: +0 points. Mood matches chill: +30 points. Energy 0.28 compared with
   target 0.40: +17.60 points. Valence 0.65 compared with target 0.60: +9.50 points.
5. Velvet Letters | Score: 29.00/100
   Genre does not match lofi: +0 points. Mood does not match chill: +0 points. Energy 0.43 compared
   with target 0.40: +19.40 points. Valence 0.64 compared with target 0.60: +9.60 points.
Confirmed: 5 recommendations; scores in descending order.
```

### Intense Rock

```text
=== Intense Rock ===
Preferences: genre=rock, mood=intense, energy=0.90, valence=0.45
1. Storm Runner | Score: 99.50/100
   Genre matches rock: +40 points. Mood matches intense: +30 points. Energy 0.91 compared with
   target 0.90: +19.80 points. Valence 0.48 compared with target 0.45: +9.70 points.
2. Gym Hero | Score: 56.20/100
   Genre does not match rock: +0 points. Mood matches intense: +30 points. Energy 0.93 compared with
   target 0.90: +19.40 points. Valence 0.77 compared with target 0.45: +6.80 points.
3. Iron Resolve | Score: 27.60/100
   Genre does not match rock: +0 points. Mood does not match intense: +0 points. Energy 0.97
   compared with target 0.90: +18.60 points. Valence 0.35 compared with target 0.45: +9.00 points.
4. Night Drive Loop | Score: 26.60/100
   Genre does not match rock: +0 points. Mood does not match intense: +0 points. Energy 0.75
   compared with target 0.90: +17.00 points. Valence 0.49 compared with target 0.45: +9.60 points.
5. Electric Horizon | Score: 25.90/100
   Genre does not match rock: +0 points. Mood does not match intense: +0 points. Energy 0.90
   compared with target 0.90: +20.00 points. Valence 0.86 compared with target 0.45: +5.90 points.
Confirmed: 5 recommendations; scores in descending order.
```

### High-Energy Melancholic

```text
=== High-Energy Melancholic ===
Preferences: genre=rock, mood=melancholic, energy=0.90, valence=0.20
1. Storm Runner | Score: 67.00/100
   Genre matches rock: +40 points. Mood does not match melancholic: +0 points. Energy 0.91 compared
   with target 0.90: +19.80 points. Valence 0.48 compared with target 0.20: +7.20 points.
2. Empty Platform | Score: 47.50/100
   Genre does not match rock: +0 points. Mood matches melancholic: +30 points. Energy 0.29 compared
   with target 0.90: +7.80 points. Valence 0.23 compared with target 0.20: +9.70 points.
3. Iron Resolve | Score: 27.10/100
   Genre does not match rock: +0 points. Mood does not match melancholic: +0 points. Energy 0.97
   compared with target 0.90: +18.60 points. Valence 0.35 compared with target 0.20: +8.50 points.
4. Night Drive Loop | Score: 24.10/100
   Genre does not match rock: +0 points. Mood does not match melancholic: +0 points. Energy 0.75
   compared with target 0.90: +17.00 points. Valence 0.49 compared with target 0.20: +7.10 points.
5. Gym Hero | Score: 23.70/100
   Genre does not match rock: +0 points. Mood does not match melancholic: +0 points. Energy 0.93
   compared with target 0.90: +19.40 points. Valence 0.77 compared with target 0.20: +4.30 points.
Confirmed: 5 recommendations; scores in descending order.
```

### Missing Genre

```text
=== Missing Genre ===
Preferences: genre=bluegrass, mood=chill, energy=0.40, valence=0.60
1. Midnight Coding | Score: 59.20/100
   Genre does not match bluegrass: +0 points. Mood matches chill: +30 points. Energy 0.42 compared
   with target 0.40: +19.60 points. Valence 0.56 compared with target 0.60: +9.60 points.
2. Library Rain | Score: 59.00/100
   Genre does not match bluegrass: +0 points. Mood matches chill: +30 points. Energy 0.35 compared
   with target 0.40: +19.00 points. Valence 0.60 compared with target 0.60: +10.00 points.
3. Spacewalk Thoughts | Score: 57.10/100
   Genre does not match bluegrass: +0 points. Mood matches chill: +30 points. Energy 0.28 compared
   with target 0.40: +17.60 points. Valence 0.65 compared with target 0.60: +9.50 points.
4. Focus Flow | Score: 29.90/100
   Genre does not match bluegrass: +0 points. Mood does not match chill: +0 points. Energy 0.40
   compared with target 0.40: +20.00 points. Valence 0.59 compared with target 0.60: +9.90 points.
5. Velvet Letters | Score: 29.00/100
   Genre does not match bluegrass: +0 points. Mood does not match chill: +0 points. Energy 0.43
   compared with target 0.40: +19.40 points. Valence 0.64 compared with target 0.60: +9.60 points.
Confirmed: 5 recommendations; scores in descending order.
```

### Intense Classical

```text
=== Intense Classical ===
Preferences: genre=classical, mood=intense, energy=0.95, valence=0.20
1. Storm Runner | Score: 56.40/100
   Genre does not match classical: +0 points. Mood matches intense: +30 points. Energy 0.91 compared
   with target 0.95: +19.20 points. Valence 0.48 compared with target 0.20: +7.20 points.
2. Gym Hero | Score: 53.90/100
   Genre does not match classical: +0 points. Mood matches intense: +30 points. Energy 0.93 compared
   with target 0.95: +19.60 points. Valence 0.77 compared with target 0.20: +4.30 points.
3. Quiet Observatory | Score: 50.40/100
   Genre matches classical: +40 points. Mood does not match intense: +0 points. Energy 0.18 compared
   with target 0.95: +4.60 points. Valence 0.62 compared with target 0.20: +5.80 points.
4. Iron Resolve | Score: 28.10/100
   Genre does not match classical: +0 points. Mood does not match intense: +0 points. Energy 0.97
   compared with target 0.95: +19.60 points. Valence 0.35 compared with target 0.20: +8.50 points.
5. Night Drive Loop | Score: 23.10/100
   Genre does not match classical: +0 points. Mood does not match intense: +0 points. Energy 0.75
   compared with target 0.95: +16.00 points. Valence 0.49 compared with target 0.20: +7.10 points.
Confirmed: 5 recommendations; scores in descending order.
```

These results show how much exact genre and mood labels affect the rankings. Gym Hero beats Rooftop Lights for High-Energy Pop because genre earns more points than mood. For Intense Rock, Gym Hero also beats metal song Iron Resolve because its intense mood matches, while defiant receives no mood points. Storm Runner beats Empty Platform for High-Energy Melancholic because its genre and energy matches outweigh the melancholic mood match. For Intense Classical, rock and pop songs rank above Quiet Observatory because they better match the requested mood and energy. Bluegrass is absent from the catalog, so Missing Genre returns other genres and no song can earn more than 60 points. The recommender still returns five results even when none match the requested genre.

### Weight Shift Experiment

I temporarily changed the genre/mood/energy/valence weights from **40/30/20/10** to **20/30/40/10**. Both versions have a maximum score of 100. I kept the default CLI profile unchanged: pop, happy, energy 0.80, and target valence 0.60. The actual before/after results were:

| Song | Original rank | Original score | Experimental rank | Experimental score |
| --- | ---: | ---: | ---: | ---: |
| Sunrise City | 1 | 97.20 | 1 | 96.80 |
| Gym Hero | 2 | 65.70 | 3 | 63.10 |
| Rooftop Lights | 3 | 57.10 | 2 | 76.30 |
| Sidewalk Crown | 4 | 28.40 | 4 | 48.00 |
| Night Drive Loop | 5 | 27.90 | 5 | 46.90 |

Rooftop Lights overtook Gym Hero because energy similarity became more important and genre matching became less important. The top-five membership did not change. This shows different rankings, not proven improved accuracy; listener feedback would be needed to judge which recommendations are more useful.

After recording the experiment, I restored the original **40/30/20/10** weights and their scoring explanations.

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



