import random

class Apple:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.location = [random.randint(0, width - 1), random.randint(0, height - 1)]
    
    def recreate(self, body, head):
        location = [random.randint(0, self.width - 1), random.randint(0, self.height - 1)]
        if location in body or location == head:
            self.recreate(body, head)
        else:
            self.location = location
