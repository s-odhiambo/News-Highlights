import unittest
from models import news
news = news.Sources

class NewsTest(unittest.TestCase):
  '''
  Test Class to test the behaviour of the News class
  '''
  
  def setUp(self):
    '''
    Set up method that will run before every Test
    '''
    self.new_news = Sources("abc-news", "ABC News", "Your trusted source for breaking news, analysis, exclusive interviews, headlines, and videos at ABCNews.com", "https://abcnews.go.com", "general", "en", "us")
    
    def test_instance(self):
      self.assertTrue(isinstance(self.new_news, Sources))
      
      
      
      if __name__== '__main__':
        unittest.main()
