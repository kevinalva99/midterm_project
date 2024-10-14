import json
import argparse

class ProcessedOrders():
  def __init__(self, file):
    with open(file) as filename:
      self.data = json.load(filename)
  
  def customerInfo(self):

    customer = {}

    for information in self.data:
      name = information["name"]
      phone_number = information["phone"]

      if phone_number not in customer:
        customer[phone_number] = name

    with open('customer.json', 'w') as customer_file:
      json.dump(customer, customer_file, indent=4)
  
  def itemCount(self):

    item = {}

    for order in self.data:

      for items in order["items"]:      
        food_name = items["name"]
        price = items["price"]

        if food_name not in item:
          item[food_name] = {"price": price, "orders": 1}
        else:
          item[food_name]["orders"] += 1
      with open('items.json', 'w') as items_file:
        json.dump(item, items_file, indent=4)


def Main():

  parser = argparse.ArgumentParser(
    description="Process oders from example_orders.json to generate customer and item data"
  )

  parser.add_argument(
    "input_file",
    type=str,
    help="is the JSON file containing the order data. Type: python midterm.py input_file"
  )

  args = parser.parse_args()
  orders = ProcessedOrders(args.input_file)

  orders.customerInfo()
  orders.itemCount()

if __name__== "__main__":
  Main()

