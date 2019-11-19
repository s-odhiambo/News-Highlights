import os

class Config:
   	NEWS_SOURCES_BASE_URL ='https://newsapi.org/v2/sources?apiKey=371b70b2e2e748929d82d77bb7e60612'
   	ARTICLES_BASE_URL = 'https://newsapi.org/v2/everything?q=bitcoin&apiKey=371b70b2e2e748929d82d77bb7e60612'
   	NEWS_API_KEY = os.environ.get('NEWS_API_KEY')
   	@staticmethod
   	def init_app(app):
   		pass


class ProdConfig(Config):
    pass


class DevConfig(Config):
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig}