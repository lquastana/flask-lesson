from flask import Flask,render_template
import feedparser
app = Flask(__name__)
RSS_FEEDS = {'bbc': 'http://feeds.bbci.co.uk/news/rss.xml',
'cnn': 'http://rss.cnn.com/rss/edition.rss',
'fox': 'http://feeds.foxnews.com/foxnews/latest',
'iol': 'http://www.iol.co.za/cmlink/1.640'}

@app.route("/")
@app.route("/<publication>")
def get_news(publication="bbc"):
 feed = feedparser.parse(RSS_FEEDS[publication])
 first_article = feed['entries']
 return render_template("home.html",articles=first_article)


if __name__ == '__main__':
    app.run(port=5000, debug=True)