class Car(object):

  def __init__(self):
    self.type = "Generic"
    print("Car is starting")

  def set_type(self, carType):
    self.type = carType

  def drive(self):
    print(self.type + " car is driving")

class Tesla(Car):
  def __init__(self):
    super().__init__()
    Car.__init__(self)
    self.type = "Tesla"

class Toyota(Car):
  def __init__(self):
    self.type = "Toyota"

car = Tesla()
car.drive()

# toyota = Toyota()
# toyota.drive()