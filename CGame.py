import collections
from abc import abstractmethod


class IType:

    def __eq__(self, other):
        return self.char_type == other.char_type

    @abstractmethod
    def update(self, neighbors):
         '''function '''


class CNothingType(IType):

    char_type = 'n'

    def update(self, neighbors):
        if neighbors['f'] == 3:
            return CFishType()
        elif neighbors['s'] == 3:
            return CShrimType()
        else:
            return CNothingType()


class CRockType(IType):

    char_type = 'r'

    def update(self, neighbors):
        return CRockType()


class CFishType(IType):

    char_type = 'f'

    def update(self, neighbors):
        if (neighbors['f'] == 2) or (neighbors['f'] == 3):
            return CFishType()
        else:
            return CNothingType()


class CShrimType(IType):

    char_type = 's'

    def update(self, neighbors):
        if (neighbors['s'] == 2) or (neighbors['s'] == 3):
            return CShrimType()
        else:
            return CNothingType()


class Game:
    cell_types = ['n', 'f', 'r', 's']

    def __init__(self, height, weight):
        self.height = height
        self.weight = weight
        self.world = [[CNothingType()]*weight for _ in range(height)]

    def set_world(self, lst):
        for i in range(self.height):
            for j in range(self.weight):
                if lst[i][j] == 'n':
                    self.world[i][j] = CNothingType()
                elif lst[i][j] == 'r':
                    self.world[i][j] = CRockType()
                elif lst[i][j] == 'f':
                    self.world[i][j] = CFishType()
                elif lst[i][j] == 's':
                    self.world[i][j] = CShrimType()

    def get_neighbors(self, x, y):
        dict_count = collections.defaultdict(int)
        for i in [1, -1, 0]:
            for j in [1, -1, 0]:
                if (x + i >= 0) and (x + i < self.height):
                    if (y + j >= 0) and (y + j < self.weight):
                        if (not i == 0) or (not j == 0):
                            dict_count[self.world[x+i][y+j].char_type] += 1
        return dict_count

    def update_world(self):
        new_world = [[CNothingType()]*self.weight for _ in range(self.height)]
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
