class Parcel:
  def __init__(self,id,name,weight):
    self.id=id
    self.name=name
    self.weight=weight
  def cat(self):
    if self.weight>='20':
      return "Heavy"
    elif self.weight>='5':
      return "Medium"
    else:
      return "Light"
  def display(self):
    print(f"{self.id}|{self.name}|{self.weight}|{self.cat()}")
class Courierservice:
  def __init__(self):
    self.parcels=[]
  def add(self,parcel):
    self.parcels.append(parcel)
  def display(self):
    for parcel in self.parcels:
      parcel.display()
n=int(input())
cou=Courierservice()
for i in range(n):
  id,name,weight=input().split(",")
  parcel=Parcel(id,name,weight)
  cou.add(parcel)
cou.display()
      