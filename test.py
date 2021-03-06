from CGame import *

#  ***********************************************************************


class ITest:

    def do_test(self):
        return True

    def print_ok(self, i):
        print('test ', i, ' - Ok')

    def print_error(self, i):
        print('Wrong test ', i)


class TestSize11(ITest):

    def do_test(self):
        my_world = Game(1, 1)
        lst = ['f']
        my_world.set_world(lst)
        for l in range(12):
            my_world.update_world()
        return my_world.world[0][0] == Nothing()


class TestSize12(ITest):

    def do_test(self):
        my_world = Game(1, 1)
        lst = ['r']
        my_world.set_world(lst)
        for l in range(7):
            my_world.update_world()
        return my_world.world[0][0].char_type == 'r'


class TestSize21(ITest):

    def do_test(self):
        my_world = Game(2, 2)
        my_world.set_world([['f', 'f'], ['f', 'f']])
        for l in range(8):
            my_world.update_world()
        return my_world.world == [[Fish(), Fish()],
                                  [Fish(), Fish()]]


class TestSize22(ITest):

    def do_test(self):
        my_world = Game(2, 2)
        my_world.set_world([['n', 'f'], ['f', 'f']])
        for l in range(2):
            my_world.update_world()
        return my_world.world == [[Fish(), Fish()],
                                  [Fish(), Fish()]]


class TestSize23(ITest):

    def do_test(self):
        my_world = Game(2, 2)
        my_world.set_world([['n', 'f'], ['f', 's']])
        for l in range(3):
            my_world.update_world()
        return my_world.world == [[Nothing(), Nothing()],
                                  [Nothing(), Nothing()]]


class TestSize31(ITest):

    def do_test(self):
        my_world = Game(3, 3)
        my_world.set_world([['s', 'f', 's'], ['f', 's', 'f'], ['s', 'f', 's']])
        for l in range(3):
            my_world.update_world()
        return my_world.world == [[Nothing(), Fish(),
                                   Nothing()],
                                  [Fish(),
                                   Nothing(), Fish()],
                                  [Nothing(), Fish(),
                                   Nothing()]]


class TestSize32(ITest):

    def do_test(self):
        my_world = Game(2, 3)
        my_world.set_world([['f', 'f', 'f'], ['f', 'f', 'f']])
        for l in range(3):
            my_world.update_world()
        return my_world.world == [[Nothing(), Nothing(),
                                   Nothing()],
                                  [Nothing(), Nothing(),
                                   Nothing()]]


class TestSizeN(ITest):

    def do_test(self):
        my_world = Game(50, 50)
        my_list = [['n'] * 50 for _ in range(50)]
        for l in range(50):
            for l_ in range(50):
                my_list[l][l_] = 'f'

        my_world.set_world(my_list)
        my_world.update_world()
        my_world.update_world()

        for l in range(50):
            for l_ in range(50):
                if not my_world.world[l][l_].char_type == 'n':
                    return False
        return True


class TestMakeSteps(ITest):
    def do_test(self):
        my_world = Game(2, 3)
        my_world.set_world([['f', 'f', 'f'], ['f', 'f', 'f']])
        my_world.make_steps(3)
        return my_world.world == [[Nothing(), Nothing(),
                                   Nothing()],
                                  [Nothing(), Nothing(),
                                   Nothing()]]


class TestSetWorld(ITest):
    def do_test(self):
        my_world = Game(2, 3)
        my_world.set_world([['f', 'f', 'f'], ['f', 'f', 'f']])
        return my_world.world == [[Fish(), Fish(),
                                   Fish()],
                                  [Fish(), Fish(),
                                   Fish()]]


class TestInit(ITest):
    def do_test(self):
        my_world = Game(1, 1)
        return (my_world.weight == 1) and\
               (my_world.height == 1) and\
               (my_world.world[0][0] == Nothing())


class TestGetNeighbors(ITest):
    def do_test(self):
        my_world = Game(2, 2)
        my_world.set_world([['n', 'f'], ['f', 's']])
        d_f_t = my_world.get_neighbors(0, 0)
        return (d_f_t['n'] == 0) and\
               (d_f_t['f'] == 2) and\
               (d_f_t['s'] == 1) and\
               (d_f_t['r'] == 0)


class TestUpdateRock(ITest):
    def do_test(self):
        my_world = Game(2, 2)
        my_world.set_world([['r', 'f'], ['f', 'f']])
        my_world.world[0][0] = my_world.world[0][0].update({'n': 0, 's': 0,
                                                            'f': 3, 'r': 0})
        return my_world.world[0][0].char_type == 'r'


class TestUpdateNothingFish(ITest):
    def do_test(self):
        my_world = Game(2, 2)
        my_world.set_world([['n', 'f'], ['f', 'f']])
        my_world.world[0][0] = my_world.world[0][0].update({'n': 0, 's': 0,
                                                            'f': 3, 'r': 0})
        return my_world.world[0][0].char_type == 'f'


class TestUpdateNothingShirm(ITest):
    def do_test(self):
        my_world = Game(2, 2)
        my_world.set_world([['n', 's'], ['s', 's']])
        my_world.world[0][0] = my_world.world[0][0].update({'n': 0, 's': 3,
                                                            'f': 0, 'r': 0})
        return my_world.world[0][0].char_type == 's'


class TestUpdateFishDie(ITest):
    def do_test(self):
        my_world = Game(2, 2)
        my_world.set_world([['f', 'f'], ['r', 'r']])
        my_world.world[0][0] = my_world.world[0][0].update({'n': 0, 's': 0,
                                                            'f': 1, 'r': 2})
        return my_world.world[0][0].char_type == 'n'


class TestUpdateFishLive(ITest):
    def do_test(self):
        my_world = Game(2, 2)
        my_world.set_world([['f', 'f'], ['f', 'f']])
        my_world.world[0][0] = my_world.world[0][0].update({'n': 0, 's': 0,
                                                            'f': 3, 'r': 0})
        return my_world.world[0][0].char_type == 'f'


class TestUpdateShirmDie(ITest):
    def do_test(self):
        my_world = Game(2, 2)
        my_world.set_world([['s', 'f'], ['f', 'f']])
        my_world.world[0][0] = my_world.world[0][0].update({'n': 0, 's': 0,
                                                            'f': 3, 'r': 0})
        return my_world.world[0][0].char_type == 'n'


class TestUpdateShirmLive(ITest):
    def do_test(self):
        my_world = Game(2, 2)
        my_world.set_world([['s', 's'], ['s', 's']])
        my_world.world[0][0] = my_world.world[0][0].update({'n': 0, 's': 3,
                                                            'f': 0, 'r': 0})
        return my_world.world[0][0].char_type == 's'

#  ***********************************************************************


def custom_tests():
    test_list = [TestSize11(), TestSize12(),
                 TestSize21(), TestSize22(), TestSize23(),
                 TestSize31(), TestSize32(), TestSizeN(),
                 TestMakeSteps(), TestSetWorld(),
                 TestInit(), TestGetNeighbors(),
                 TestUpdateRock(), TestUpdateNothingFish(),
                 TestUpdateFishDie(), TestUpdateShirmDie(),
                 TestUpdateFishLive(), TestUpdateShirmLive(),
                 TestUpdateNothingShirm()]
    for i in range(len(test_list)):
        if test_list[i].do_test():
            test_list[i].print_ok(i+1)
        else:
            test_list[i].print_error(i+1)

    print("That is all")


