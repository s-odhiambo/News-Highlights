from flask import render_template
from app import app
# from .request import get_news

@app.route('/')
def index():
  '''
  function that returns the index page and its content
  '''
  
  message = 'News-Highlights'
  return render_template('index.html',message = message)

# @app.route('/news/<news_id>')
# def news(news_id)

# return render_template('news.html',id = news_id)

@app.route('/news/<int:news_id>')
def news(news_id):
  
  
  return render_template('news.html',id = news_id)


def index():
  '''
  View root page function that returns the index page and its data
  '''
  title = 'Home - WElcome to The best News Review Website Online'
  
  return render_template('index.html', title = title)

@app.route('/')
def index():
  
  '''
  View root page function that returns the index page and its data
  '''
  
  popular_news = get_news('popular')
  print(popular_news)
  
  title = 'Home - Welcome to The best News Reviews Website Online'
  
  return render_template('index.html', title = title,popular = popular_news, upcoming = upcoming_news, now_showing = now_showing_news )




