import json

class ProcessedOrders:
    def __init__(self, file):
        with open(file) as file_name:
            self.data = json.load(file_name)

    def get_phone_name(self):
        
        customers = {}

        for information in self.data:
            name = information["name"]
            phoneNumber = information["phone"]
        
            if phoneNumber not in customers:
                customers[phoneNumber] = name 

        with open('customers.json', 'w') as customer_file:
            json.dump(customers, customer_file, indent = 4)          
    
    def get_items(self):
         
        items = {}

        for order in self.data:

            for item in order["items"]:
                foodName = item["name"]
                price = item["price"]

                if foodName not in items:
                    items[foodName] = {"price": price, "orders": 1}

                else:
                    items[foodName]["orders"] += 1

        with open('items.json', 'w') as items_file:
                json.dump(items, items_file, indent=4)

process = ProcessedOrders('example_orders.json')
process.get_phone_name()
process.get_items()
