# 36. Favorite Cities

class City:
  def __init__(self, name, country, population, landmarks):
    self.name = name
    self.country = country
    self.population = population
    self.landmarks = landmarks

city = City('Granada', 'Spain', 232208, 'Alhambra')
print(vars(city))