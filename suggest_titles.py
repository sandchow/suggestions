import imdb
import nltk
import requests
from nltk.sentiment.vader import SentimentIntensityAnalyzer
import json

if __name__ == "__main__":
    nltk.download('vader_lexicon')

    phrases_count = {}
    with open('data/locations_3.json', 'r') as j:
        contents = json.loads(j.read())
    for k, v in contents.items():
        phrases = v['display_name'].strip().split(',')
        for phrase in phrases:
            phrase_s = phrase.strip()
            if not phrase_s.isdigit():
                if phrase_s not in phrases_count:
                    phrases_count[phrase_s] = 0
                phrases_count[phrase_s] += 1

    phrases = sorted(phrases_count, key=phrases_count.get, reverse=True)[:20]
    final = []
    sid = SentimentIntensityAnalyzer()

    with open('secrets.json', 'r') as j:
        secrets = json.loads(j.read())

    for phrase in phrases:
        r = requests.get(
            'https://ws.audioscrobbler.com/2.0/',
            params={
                'method': 'track.search',
                'track': phrase,
                'api_key': secrets['MUSIC_SEARCH_API_KEY'],
                'format': 'json'
            }
        )
        song_titles = [track['name'] for track in r.json()['results']['trackmatches']['track']]

        movies = imdb.IMDb()
        search = movies.search_movie(phrase)
        movie_titles = [movie['title'] for movie in search]

        filter_words = ['track', 'bonus', ':', 'original', 'version', '#', 'remix', '.feat']
        for title in song_titles + movie_titles:
            if phrase in title and not any([i in title.lower() for i in filter_words]):
                final.append((title.lower(), sid.polarity_scores(title)['compound']))

    final = list(set(final))
    final.sort(key=lambda x: -x[1])
    for i in final:
        print(i)
