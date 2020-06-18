from flask import Flask

from cache.sqlite import SqliteCache
from sentiment import RandomSentimenter
from sentiment.caching import CachingSentimenter

CACHE_DB_PATH = 'db/cache.db'

app = Flask(__name__)

@app.route('/api/v1/sentiment_analyses/<int:tweet_id>')
def tweet_analysis(tweet_id):
    cache = SqliteCache("sentiments", CACHE_DB_PATH)
    random_sent = RandomSentimenter()
    sentimenter = CachingSentimenter(cache, random_sent)

    return sentimenter.analyze_text(str(tweet_id))
