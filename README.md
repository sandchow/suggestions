# suggestions

## extract location data
extract_location_data.py allows us to get location data using an free api, this was pre-processed and the data now lives in data/locations_[1,2,3].json.

## suggest titles
suggest_titles.py parses the pre-processed location data and uses a few apis to suggest logical titles for the photo albums. The creative aspect involves:
1. using IMDB movie api to search for movies that have locations in them and then suggesting positive sounding movie names to the users
2. using a free music api to search for song names that have locations and processing similarly to (1)
3. using natural language processing via NLTK library to rate suggestions based on VADER ( Valence Aware Dictionary for Sentiment Reasoning). VADER is a model used for text sentiment analysis that is sensitive to both polarity (positive/negative) and intensity (strength) of emotion. We rank suggestions based on positiveness!

sample output -
```
('beautiful amalfi', 0.5994)
('campania italian special one', 0.4019)
('picturesque sorrento (italy)', 0.3818)
('escape to campania', 0.1779)
('the campania ~reflection~', 0.0)
("viva l'italia", 0.0)
...
```

this will be demoed during the interview...
