class News:
  '''
  Movie class to define News Objects
  '''
  
  def __init__(self,title,id,name,description,url,category,country,language):
    self.title = title
    self.id = id
    self.name = name
    self.description = description
    self.url = url
    self.category = category
    self.country = country
    self.language = language