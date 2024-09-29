import json

class ProcessedOrders():
  def __init__(self, file):
    with open(file) as filename:
      self.data = json.load(filename)
  
  def customerInfo(self):

    customer = {}

    for information in self.data:
      name = information["name"]
      phoneNumber = information["phone"]

      if phoneNumber not in customer:
        customer[phoneNumber] = name

    with open('customer.json', 'w') as customerFile:
      json.dump(customer, customerFile, indent=4)
  
  def itemCount(self):

    item = {}

    for order in self.data:

      for items in order["items"]:      
        foodName = items["name"]
        price = items["price"]

        if foodName not in item:
          item[foodName] = {"price": price, "orders": 1}
        else:
          item[foodName]["orders"] += 1
      with open('items.json', 'w') as itemsFile:
        json.dump(item, itemsFile, indent=4)


process = ProcessedOrders('example_orders.json')
process.customerInfo()
process.itemCount()
