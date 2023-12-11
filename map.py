class Map:
    def __init__(self, width:int, height:int, snake:list, head:list, apple:list):
        self.width = width
        self.height = height
        self.snake = snake
        self.apple = apple
        self.head = head
        self.map = self.create_map()
        self.game_map = self.add_elements() #карта с яблоком и с змеей
        
    def create_map(self):
        map = []
        for _ in range(self.height):
            row = ['X' for _ in range(self.width)]
            map.append(row)
        return map
    
    def add_elements(self):
        for i in self.snake:
            self.map[i[0]][i[1]] = 's'
        self.map[self.head[0]][self.head[1]] = 'O'
        self.map[self.apple[0]][self.apple[1]] = '*'

    def print_map(self):
        for i in self.map:
            print(i)
        print()
        