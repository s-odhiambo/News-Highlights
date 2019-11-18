from flask import render_template, request



from app.requests import Request
from . import main

requests = Request()

@main.route('/')
def index():
  sources = requests.get_sources()
  if sources:
    return render_template('index.html', sources=sources)
  
  
  
  @main.route('/articles', method=["POST","GET"])
  def articles_page()
  if request.method == 'POST':
    search = request.form.get("search")
  else:
    articles = request.get_articles("tech")
  return render_template('article.html', articles=articles)
  
  @main.route('/article/<id>')
  def source_article(id)
  source = id
  return render_template('display.html', source_article = source_articles, source = source )

  
from flask import render_template, request

from app.requests import Request
from . import main

requests = Request()


@main.route('/')
def index():
    sources = requests.get_sources()
    if sources:
        return render_template('index.html', sources=sources)


@main.route('/articles', methods=["POST", "GET"])
def articles_page():
    if request.method == 'POST':
        search = request.form.get("search")
        articles = requests.get_articles(search)
    else:
        articles = requests.get_articles("tech")
    return render_template('articles.html', articles=articles)


@main.route('/article/<id>')
def source_article(id):
    source_articles = requests.get_article_by_source(id)
    source = id
    return render_template('display.html', source_articles=source_articles, source=source)
