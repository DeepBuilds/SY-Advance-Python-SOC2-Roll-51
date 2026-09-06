'''4. Mobile Store Management System

Develop a Python application to maintain mobile phone details.

Requirements
Create a Mobile class with:
Brand
Model
Price
Categorize mobiles as:
Premium
Mid-range
Budget
Create a Store class.
Add mobiles.
Display all mobiles.'''
def decorator(func):
  def wrapper(*args,**kwargs):
    print("="*40)
    print("GB Mobile store")
    print("="*40)
    func(*args,**kwargs)
    print("="*40)
  return wrapper

class Mobile:
  def __init__(self,brand,model,price):
    self.brand=brand
    self.model=model
    self.price=price
  def cate(self):
    if self.price >=100000:
      return "Premium"
    elif self.price >=50000:
      return "Mid-range"
    else:
      return "budget"
  def display(self):
    print("Brand:",self.brand)
    print("Model:",self.model)
    print("Price:",self.price)
    print("Grade",self.cate())
    print()
class Store:
  def __init__(self):
    self.mobiles=[]
  def add_mob(self,mobile):
    self.mobiles.append(mobile)
  @decorator
  def display(self):
    for mobile in self.mobiles:
      mobile.display()
store= Store()
m1=Mobile("Apple","17",120000)
m2=Mobile("Samsung","A25",55000)
m3=Mobile("oppo","A7",12000)
store.add_mob(m1)
store.add_mob(m2)
store.add_mob(m3)
store.display()
    
   