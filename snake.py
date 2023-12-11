class Snake:
    def __init__(self):
        self.body = [[0, 2], [0, 1], [0, 0]]
        self.head = [0, 3] #x, y
        self.live = True
        self.direction = 'r' # r l d u
    
    def check_live(self):
        if self.head in self.body:
            self.live = False
            print("YOU DIE")
        else:
            self.live = True

    def move(self, width, height):
        body_copy = self.body.copy()
        for i in range(1, len(self.body[1:])+1):
                self.body[i] = body_copy[i-1]
        self.body[0] = self.head.copy()
        if self.direction == 'r':
            if self.head[1] == width - 1:
                self.head[1] = 0
            else:
                self.head[1] += 1

        elif self.direction == 'l':
            if self.head[1] == 0:
                self.head[1] = width - 1
            else:
                self.head[1] -= 1
        
        elif self.direction == 'd':
            if self.head[0] == height - 1:
                self.head[0] = 0
            else:
                self.head[0] += 1

        elif self.direction == 'u':
            if self.head[0] == 0:
                self.head[0] = height - 1
            else:
                self.head[0] -= 1

    def change_direction(self, direction):
        self.direction = direction

    def eat(self, apple):
        if self.head == apple:
            self.body.append(self.body[-1])
            return True
        else:
            return False
