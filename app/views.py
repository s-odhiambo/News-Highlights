from flask import render_template
from app import app

@app.route('/')
def index():
  
  return render_template('index.html',message = message)

@app.route('/news/<news_id>')
def news(news_id)

return render_template('news.html',id = news_id)

@app.route('/news/<int:news_id>')
def news(news_id):
  
  
  return render_template('news.html',id = news_id)


def index():
  '''
  View root page function that returns the index page and its data
  '''
  title = 'Home - WElcome to The best News Review Website Online'
  
  return render_template('index.html', title = title)