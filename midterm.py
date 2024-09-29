import json

class ProcessedOrders:
    def __init__(self, file):
        with open(file) as file_name:
            self.data = json.load(file_name)
