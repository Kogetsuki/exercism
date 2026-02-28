class SpaceAge:
  ORBITAL_PERIODS = {
    "mercury": 0.2408467,
    "venus": 0.61519726,
    "earth": 1.0,
    "mars": 1.8808158,
    "jupiter": 11.862615,
    "saturn": 29.447498,
    "uranus": 84.016846,
    "neptune": 164.79132
  }
  
  def __init__(self, seconds):
    self.age = seconds / 31_557_600
    
  def on_planet(self, planet):
    period = self.ORBITAL_PERIODS[planet.lower()]
    return round(self.age / period, 2)
    
  def on_mercury(self): return self.on_planet("mercury")
  def on_venus(self): return self.on_planet("venus")
  def on_earth(self): return self.on_planet("earth")
  def on_mars(self): return self.on_planet("mars")
  def on_jupiter(self): return self.on_planet("jupiter")
  def on_saturn(self): return self.on_planet("saturn")
  def on_uranus(self): return self.on_planet("uranus")
  def on_neptune(self): return self.on_planet("neptune")
