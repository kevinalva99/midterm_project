import json

class ProcessedOrders():
  def __init__(self, file):
    with open(file) as filename:
      self.data = json.load(filename)