class Game:
    cell_types = ['n', 'f', 'r', 's']

    def __init__(self, height, weight):
        self.height = height
        self.weight = weight
        self.world = [['n']*weight for _ in range(height)]

    def set_world(self, lst):
        for i in range(self.height):
            for j in range(self.weight):
                self.world[i][j] = lst[i][j]

    def get_neighbors(self, x, y):
        dict_count = {'n': 0,
                      'f': 0,
                      'r': 0,
                      's': 0}
        for i in [1, -1, 0]:
            for j in [1, -1, 0]:
                if (x + i >= 0) and (x + i < self.height):
                    if (y + j >= 0) and (y + j < self.weight):
                        if (not i == 0) or (not j == 0):
                            if self.world[x+i][y+j] == 'n':
                                dict_count['n'] += 1
                            elif self.world[x+i][y+j] == 'f':
                                dict_count['f'] += 1
                            elif self.world[x+i][y+j] == 'r':
                                dict_count['r'] += 1
                            elif self.world[x+i][y+j] == 's':
                                dict_count['s'] += 1
        return dict_count

    def update_world(self):
        new_world = [['n']*self.weight for _ in range(self.height)]
        for i in range(self.height):
            for j in range(self.weight):
                neighbors = self.get_neighbors(i, j)
                if self.world[i][j] == 'r':
                    new_world[i][j] = self.world[i][j]
                elif self.world[i][j] == 'f':
                    if (neighbors['f'] == 2) or (neighbors['f'] == 3):
                        new_world[i][j] = 'f'
                    else:
                        new_world[i][j] = 'n'
                elif self.world[i][j] == 's':
                    if (neighbors['s'] == 2) or (neighbors['s'] == 3):
                        new_world[i][j] = 's'
                    else:
                        new_world[i][j] = 'n'
                elif self.world[i][j] == 'n':
                    if neighbors['f'] == 3:
                        new_world[i][j] = 'f'
                    elif neighbors['s'] == 3:
                        new_world[i][j] = 's'
        self.world = new_world

    def print_world(self):
        for i in range(self.height):
            for j in range(self.weight):
                print(self.world[i][j], end='')
            print()

    def make_steps(self, kol):
        for i in range(kol):
            self.update_world()

    def print_world_file(self):
        for_writing = open("output.txt", "w")
        for i in range(self.height):
            for j in range(self.weight):
                for_writing.write(self.world[i][j])
            for_writing.write('\n')

        for_writing.close()


def read_world(cur_world, height):
    for i in range(height):
        reader = list(input())
        cur_world[i] = reader
