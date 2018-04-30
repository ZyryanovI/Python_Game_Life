import collections
from abc import abstractmethod


class Animal(object):
    char_type = ''

    def __eq__(self, other):
        return self.char_type == other.char_type

    @abstractmethod
    def update(self, neighbors):
        return Animal()


class Nothing(Animal):

    char_type = 'n'

    def update(self, neighbors):
        if neighbors['f'] == 3:
            return Fish()
        elif neighbors['s'] == 3:
            return Shrim()
        else:
            return Nothing()


class Rock(Animal):

    char_type = 'r'

    def update(self, neighbors):
        return Rock()


class Fish(Animal):

    char_type = 'f'

    def update(self, neighbors):
        if (neighbors['f'] == 2) or (neighbors['f'] == 3):
            return Fish()
        else:
            return Nothing()


class Shrim(Animal):

    char_type = 's'

    def update(self, neighbors):
        if (neighbors['s'] == 2) or (neighbors['s'] == 3):
            return Shrim()
        else:
            return Nothing()


class Game:

    def __init__(self, height, weight):
        self.height = height
        self.weight = weight
        self.world = [[Nothing()]*weight for _ in range(height)]

    def set_world(self, lst):
        cell_types_list = Animal.__subclasses__()
        cell_types_dict = {i.char_type: i() for i in cell_types_list}

        for i in range(self.height):
            for j in range(self.weight):
                self.world[i][j] = cell_types_dict[lst[i][j]]

    def get_neighbors(self, x, y):
        dict_count = collections.defaultdict(int)
        for i in [1, -1, 0]:
            for j in [1, -1, 0]:
                if (x + i >= 0) and (x + i < self.height) and\
                        (y + j >= 0) and (y + j < self.weight) and\
                        ((i != 0) or (j != 0)):
                            dict_count[self.world[x+i][y+j].char_type] += 1
        return dict_count

    def update_world(self):
        new_world = [[Nothing()]*self.weight for _ in range(self.height)]
        for i in range(self.height):
            for j in range(self.weight):
                neighbors = self.get_neighbors(i, j)
                new_world[i][j] = self.world[i][j].update(neighbors)

        self.world = new_world

    def print_world(self):
        for i in range(self.height):
            for j in range(self.weight):
                print(self.world[i][j].char_type, end='')
            print()

    def make_steps(self, steps_number):
        for i in range(steps_number):
            self.update_world()

'''    def print_world_file(self):
        for_writing = open("output.txt", "w")
        for i in range(self.height):
            for j in range(self.weight):
                for_writing.write(self.world[i][j])
            for_writing.write('\n')

        for_writing.close() '''


def read_world(cur_world, height):
    for i in range(height):
        reader = list(input())
        cur_world[i] = reader
