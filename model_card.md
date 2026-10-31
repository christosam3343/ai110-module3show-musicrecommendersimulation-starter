# 🎧 Model Card: Music Recommender Simulation

## 1. Model Name  

Give your model a short, descriptive name.  
Example: **VibeFinder 1.0**  

---

## 2. Intended Use  

Describe what your recommender is designed to do and who it is for. 

This project is a content-based music recommender for classroom exploration. It compares song attributes with a user's preferences and suggests the closest matches. It assumes the user's chosen genre, mood, energy, and valence describe what they want to hear for that listening session.

Prompts:  

- What kind of recommendations does it generate  
- What assumptions does it make about the user  
- Is this for real users or classroom exploration  

---

## 3. How the Model Works  

Explain your scoring approach in simple language.  

Prompts:  

- What features of each song are used (genre, energy, mood, etc.)  
- What user preferences are considered  
- How does the model turn those into a score  
- What changes did you make from the starter logic  

Avoid code here. Pretend you are explaining the idea to a friend who does not program.

The current command-line recommender uses rules and weights that I chose by hand. It reads the songs from the CSV file and calculates a matching score for each song:

- **Genre:** 40 points for an exact match with the preferred genre; otherwise 0.
- **Mood:** 30 points for an exact match with the preferred mood; otherwise 0.
- **Energy:** Up to 20 points based on how close the song's intensity is to the user's target.
- **Valence:** Up to 10 points based on how close the song's positivity is to the user's target.

For energy and valence, similarity is calculated as **1 - abs(song value - user preference)**. Absolute difference means the distance between the two values, regardless of which is larger. A smaller distance gives a higher similarity. Energy points equal 20 times this similarity, and valence points equal 10 times this similarity. For example, energy 0.42 compared with a target of 0.40 gives a similarity of 0.98 and earns 19.6 energy points.

Energy and valence inputs are expected to be between 0 and 1. The four contributions add up to a score between 0 and 100. If the user does not provide a target valence, the program uses 0.60. The current terminal example prefers pop, happy, and energy 0.80. The README also describes a lofi/chill profile with energy 0.40 and valence 0.60.

Every song receives a score. The program sorts all songs from highest to lowest score and returns the top k recommendations, where k is the number requested. The terminal currently requests five. Songs with equal scores keep their original order. Each result includes human-readable reasons showing genre and mood matches or mismatches and the energy and valence points awarded.

The CSV loading, scoring, and ranking functions now replace the starter placeholders used by the terminal program. The separate class-based recommendation and explanation methods are still placeholders.

---

## 4. Data  

Describe the dataset the model uses.  

The catalog currently contains **18 fictional songs** in data/songs.csv. I kept the original 10 songs and added eight to include more styles, such as classical, hip-hop, reggae, electronic, R&B, folk, latin, and metal. The dataset also includes pop, lofi, rock, ambient, jazz, synthwave, and indie pop.

Each song stores an ID, title, artist, genre, mood, energy, tempo, valence, danceability, and acousticness. The current score uses only genre, mood, energy, and valence. These made-up examples help demonstrate the algorithm, but they do not represent the full range of music or listener tastes.

Prompts:  

- How many songs are in the catalog  
- What genres or moods are represented  
- Did you add or remove data  
- Are there parts of musical taste missing in the dataset  

---

## 5. Strengths  

Where does your system seem to work well  

The score is easy to follow because each feature contributes a known number of points. Matching energy to a target also supports calm preferences instead of always rewarding high-energy songs. The explanations let a user see why a song ranked highly and check whether that reasoning fits their taste.

Prompts:  

- User types for which it gives reasonable results  
- Any patterns you think your scoring captures correctly  
- Cases where the recommendations matched your intuition  

---

## 6. Limitations and Bias 

Where the system struggles or behaves unfairly. 

- The catalog has only 18 fictional songs, so most genres have very few examples and many musical styles are missing.
- Exact genre and mood matches control **70% of the score**. Related labels such as chill and relaxed receive no partial credit, which can push otherwise similar songs down the list.
- This limits cross-genre discovery. A jazz song with suitable energy and valence can lose to a lofi song because its genre label does not match.
- Repeatedly showing the same preferred styles could create a filter bubble, where the user sees little outside their existing tastes. The current rules do not intentionally add variety.
- The user profile stores likes_acoustic, but the scoring formula does not currently use it. Tempo, danceability, and acousticness are also stored song attributes that do not affect scores.
- The rules do not consider lyrics, language, listening history, or feedback from the user. A high score means a strong match under these rules; it does not guarantee the user will enjoy the song.

Prompts:  

- Features it does not consider  
- Genres or moods that are underrepresented  
- Cases where the system overfits to one preference  
- Ways the scoring might unintentionally favor some users  

---

## 7. Evaluation  

How you checked whether the recommender behaved as expected. 

Prompts:  

- Which user profiles you tested  
- What you looked for in the recommendations  
- What surprised you  
- Any simple tests or comparisons you ran  

No need for numeric metrics unless you created some.

---

## 8. Future Work  

Ideas for how you would improve the model next.  

These are possible future improvements; they are not part of the current scoring system:

- Expand the catalog with more songs and more examples within each genre and mood.
- Allow several preferred genres and moods, and give partial credit for related mood labels.
- Compare different weights to see whether less emphasis on exact genre matches improves cross-genre discovery.
- Add an acousticness preference so likes_acoustic can affect recommendations. If it receives points, adjust the other weights to keep the total at 100.
- Consider tempo or danceability preferences and add a simple way to include varied genres among the top results.
- Complete the class-based recommendation methods using the same scoring rule, and collect listener feedback to check whether the recommendations feel useful.

Prompts:  

- Additional features or preferences  
- Better ways to explain recommendations  
- Improving diversity among the top results  
- Handling more complex user tastes  

---

## 9. Personal Reflection  

A few sentences about your experience.  

Prompts:  

- What you learned about recommender systems  
- Something unexpected or interesting you discovered  
- How this changed the way you think about music recommendation apps  
