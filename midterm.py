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


def main():

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
  main()

