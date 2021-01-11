import math

class Cylinder:
  def __init__(self, radius, height):
    self.radius = radius
    self.height = height

  def get_radius(self):
    return self.radius

  def set_radius(self):
    if radius > 0:
      self.radius = radius

  def get_height(self):
    return self.height

  def set_height(self):
    if height > 0:
      self.height = height

  def base_area(self):
    return (self.radius**2) * math.pi

  def surface_area(self):
    return math.pi * 2 * self.radius * self.height

  def calc_area(self):
    return 2* base_area(self) + surface_area(self)

  def calc_volume(self):
    return base_area(self) * surface_area(self)


a = Cylinder(3,5)

print(a.calc_area())
print(a.calc_volume())