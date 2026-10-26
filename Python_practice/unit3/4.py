import csv
sales={}
with open('sales.csv','r') as f:
  reader=csv.DictReader(f)
  for word in reader:
    product=list["Product"]
    qty=int(list["Quantity"])
    Price=float(list["Price"])
  amount = Price * qty
  if product in sales:
    sales[product]+=amount
  else:
    sales[product]=amount
for product , amount in sales.items():
  
  print(f"{product}:{amount:g}")