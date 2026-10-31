# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

**Music Recommender Simulation**

---

## 2. Intended Use  

This project is a content-based music recommender for classroom exploration. It compares song attributes with a user's preferences and suggests the closest matches. It assumes the user's chosen genre, mood, energy, and valence describe what they want to hear for that listening session.

This is a classroom simulation, not a production-ready recommendation service. Its scores describe matches under the chosen rules and should not be used as a measure of real listener satisfaction.

---

## 3. How the Model Works  

The current command-line recommender uses rules and weights that I chose by hand. It reads the songs from the CSV file and calculates a matching score for each song:

- **Genre:** 40 points for an exact match with the preferred genre; otherwise 0.
- **Mood:** 30 points for an exact match with the preferred mood; otherwise 0.
- **Energy:** Up to 20 points based on how close the song's intensity is to the user's target.
- **Valence:** Up to 10 points based on how close the song's positivity is to the user's target.

For energy and valence, similarity is calculated as **1 - abs(song value - user preference)**. Absolute difference means the distance between the two values, regardless of which is larger. A smaller distance gives a higher similarity. Energy points equal 20 times this similarity, and valence points equal 10 times this similarity. For example, energy 0.42 compared with a target of 0.40 gives a similarity of 0.98 and earns 19.6 energy points.

Energy and valence inputs are expected to be between 0 and 1. The four contributions add up to a score between 0 and 100. If the user does not provide a target valence, the program uses 0.60. The current terminal example prefers pop, happy, and energy 0.80. The README also describes a lofi/chill profile with energy 0.40 and valence 0.60.

Every song receives a score. The program sorts all songs from highest to lowest score and returns the top k recommendations, where k is the number requested. The terminal currently requests five. Songs with equal scores keep their original order. Each result includes human-readable reasons showing genre and mood matches or mismatches and the energy and valence points awarded.

The CSV loading, scoring, and ranking functions are implemented. The class-based recommendation and explanation methods also use the same scoring function. They return ranked Song objects and readable scoring reasons while preserving the original song collection.

---

## 4. Data  

The catalog currently contains **18 fictional songs** in data/songs.csv. I kept the original 10 songs and added eight to include more styles, such as classical, hip-hop, reggae, electronic, R&B, folk, latin, and metal. The dataset also includes pop, lofi, rock, ambient, jazz, synthwave, and indie pop.

Each song stores an ID, title, artist, genre, mood, energy, tempo, valence, danceability, and acousticness. The current score uses only genre, mood, energy, and valence. These made-up examples help demonstrate the algorithm, but they do not represent the full range of music or listener tastes. Moods include happy, chill, intense, relaxed, peaceful, and melancholic. Coverage is uneven: there are three lofi songs and two pop songs, while each other genre has only one song.

---

## 5. Strengths  

The score is easy to follow because each feature contributes a known number of points. Matching energy to a target also supports calm preferences instead of always rewarding high-energy songs. The explanations let a user see why a song ranked highly and check whether that reasoning fits their taste.

---

## 6. Limitations and Bias 

During testing, I found that exact genre matching sometimes outweighed a match with the requested mood. For example, Storm Runner scored 67.00 points for the High-Energy Melancholic profile, while Empty Platform scored only 47.50 despite matching the user's preferred mood. This happened because Storm Runner received 40 points for its genre and nearly full points for energy similarity. The system may therefore overlook songs that better match a user's emotional preferences. A possible improvement would be to let users adjust the scoring weights based on whether genre or mood matters more to them.

- The catalog has only 18 fictional songs, so most genres have very few examples and many musical styles are missing.
- Exact genre and mood matches control **70% of the score**. Related labels such as chill and relaxed receive no partial credit, which can push otherwise similar songs down the list.
- This limits cross-genre discovery. A jazz song with suitable energy and valence can lose to a lofi song because its genre label does not match.
- Repeatedly showing the same preferred styles could create a filter bubble, where the user sees little outside their existing tastes. The current rules do not intentionally add variety.
- The user profile stores likes_acoustic, but the scoring formula does not currently use it. Tempo, danceability, and acousticness are also stored song attributes that do not affect scores.
- The rules do not consider lyrics, language, listening history, or feedback from the user. A high score means a strong match under these rules; it does not guarantee the user will enjoy the song.

---

## 7. Evaluation  

I evaluated the recommender with **18 fictional songs** and six profiles using the original **40/30/20/10** weights. Each profile returned five recommendations in descending score order. I checked the scores, ranking order, and explanations recorded in the README.

Separately, **12 automated test cases pass** with `python -m pytest -q`. They cover class-based ranking, reversed input, different preferences, energy and valence matching, empty catalogs, result limits, stable ties, unchanged inputs, and specific scoring explanations. The six profiles below were manually evaluated from their generated recommendations; they are separate from the automated test suite.

- **High-Energy Pop:** Pop, happy, energy 0.85, valence 0.80; tests upbeat preferences.
- **Chill Lofi:** Lofi, chill, energy 0.40, valence 0.60; tests calmer preferences.
- **Intense Rock:** Rock, intense, energy 0.90, valence 0.45; tests high energy without requiring a happy sound.
- **High-Energy Melancholic:** Rock, melancholic, energy 0.90, valence 0.20; tests a combination that the catalog does not fully cover.
- **Missing Genre (Bluegrass):** Bluegrass, chill, energy 0.40, valence 0.60; tests an unavailable genre.
- **Intense Classical:** Classical, intense, energy 0.95, valence 0.20; tests a preferred genre whose only song has a very different mood and energy.

The normal profiles ranked Sunrise City first for High-Energy Pop (99.00), Midnight Coding first for Chill Lofi (99.20), and Storm Runner first for Intense Rock (99.50). The edge cases showed the limits of the rules. For High-Energy Melancholic, Storm Runner ranked first with 67.00, ahead of Empty Platform at 47.50, because genre and energy outweighed the melancholic mood match. With bluegrass missing, the first two results were lofi songs Midnight Coding (59.20) and Library Rain (59.00); every song received zero genre points. For Intense Classical, Storm Runner (56.40) and Gym Hero (53.90) ranked above third-place Quiet Observatory (50.40) because their mood and energy matched better.

In a separate weight experiment, I kept the default pop/happy CLI profile at energy 0.80 and valence 0.60 and temporarily changed the weights to **20/30/40/10**. Rooftop Lights moved from third (57.10) to second (76.30), while Gym Hero moved from second (65.70) to third (63.10). Increasing the energy weight and reducing the genre weight changed their order, but the top-five membership stayed the same. I then restored **40/30/20/10**.

### Comparing User Profiles

**High-Energy Pop vs. Chill Lofi:** High-Energy Pop ranked Sunrise City first (99.00), while Chill Lofi ranked Midnight Coding first (99.20) and Library Rain second (99.00). The preferences changed from pop and happy with energy 0.85 to lofi and chill with energy 0.40; target valence also changed from 0.80 to 0.60. Each leading song earns 40 genre points and 30 mood points for its own profile, with the remaining points based on closeness to the energy and valence targets. Different preferences therefore favor different songs.

**Intense Rock vs. High-Energy Melancholic:** Both profiles prefer rock and energy 0.90, so Storm Runner keeps 40 genre points and 19.80 energy points. Changing the mood from intense to melancholic removes its 30 mood points, and lowering target valence from 0.45 to 0.20 reduces its valence points from 9.70 to 7.20. Its score falls from 99.50 to 67.00, but it stays first. Empty Platform comes second at 47.50 because its melancholic mood match cannot make up for missing the rock genre and having much lower energy.

**Missing Genre (Bluegrass) vs. Intense Classical:** Bluegrass is absent, so no song earns genre points. Midnight Coding still ranks first (59.20) through its chill mood match and close energy and valence values. Classical is available, but its only song, Quiet Observatory, has a peaceful mood and low energy. It ranks third (50.40), behind Storm Runner first (56.40) and Gym Hero second (53.90), whose intense mood and high energy contribute more points overall. Missing genres and limited coverage mean the highest-scoring result may be outside the requested genre.

These numerical results show how the rules behave. Listener satisfaction was not measured, so the changed rankings do not prove better recommendation accuracy.

---

## 8. Future Work  

These are possible future improvements; they are not part of the current scoring system:

- Expand the catalog with more songs and more examples within each genre and mood.
- Allow several preferred genres and moods, and give partial credit for related mood labels.
- Let users adjust the scoring weights, then compare the results to see whether less emphasis on exact genre matches improves cross-genre discovery.
- Add an acousticness preference so likes_acoustic can affect recommendations. If it receives points, adjust the other weights to keep the total at 100.
- Consider tempo or danceability preferences and add a simple way to include varied genres among the top results.
- Collect listener feedback to check whether the recommendations feel useful.

---

## 9. Personal Reflection  

My biggest learning moment was seeing how the 40/30/20/10 weights shape rankings. Storm Runner outranked Empty Platform for a melancholic profile because its genre and energy points outweighed the mood match. I was surprised that the same song could stay first even after the requested mood changed.

Codex helped me implement the code, create test profiles, troubleshoot the CLI, and document the findings. I still needed to check its suggestions against the files and actual terminal output. Codex initially counted the CSV's 10 columns as 11. Checking the actual CSV header caught the mistake and reminded me to verify AI-generated details, including column counts and score calculations.

The temporary 20/30/40/10 experiment moved Rooftop Lights above Gym Hero, showing that different weights change rankings without proving better listener satisfaction. Next, I would add more diverse songs, give partial credit for related moods, and let users adjust the weights. I would also collect listener feedback to check whether those changes make the recommendations more useful.
