from app import app
import urllib.request,json
from .models import news

# Getting api key
api_key = app.config['NEWS_API_KEY']

base_url = app.config["NEWS_API_BASE_URL"]

News = news.News


def get_news(category):
  '''
  Function that gets the json response to our url request
  '''
  get_news_url = base_url.format(category,api_key)
  
  with urllib.request.urlopen(get_news_url) as url:
    get_news_data = url.read()
    get_news_response = json.loads(get_news_data)
    
    news_results = None
    
    if get_news_response['results']:
      news_results_list = get_news_response['results']
      news_results= process_results(news_results_list)
      
      
      return news_results
    
    
def process_results(news_list):
  '''
  Function that process the movie results and transform them to a list of objects
  
  Args:
  news_list: A list of dictionaries that contains news details
  
  Return :
  news_results: A list of news objects
  '''
  news_results = []
  
  for news_item in news_list:
    
    id = news_item.get('id')
    name = news_item.get('original_name')
    description = news_item.get('description')
    url = news_item.get('url')
    category = news_item.get('category_path')
    country = news_item.get('country')
    language = news_item.get('language')
    
    if urlToImage:
      news_object = News(id,name,description,url,country,language)
      news_results.append(news_object)
      
      return news_results
    
         