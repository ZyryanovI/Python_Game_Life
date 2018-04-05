from CGame import Game
from abc import abstractmethod

#  ***********************************************************************


class ITest:

    @abstractmethod
    def do_test(self):
        ''' func '''


class TestSize11(ITest):

    def do_test(self):
        my_world = Game(1, 1)
        my_world.world[0][0] = 'f'
        for l in range(12):
            my_world.update_world()
        if my_world.world[0][0] == 'n':
            print('test_1_1 - OK')
        else:
            print('Wrong')
            my_world.print_world()


class TestSize12(ITest):

    def do_test(self):
        my_world = Game(1, 1)
        my_world.world[0][0] = 'r'
        for l in range(7):
            my_world.update_world()
        if my_world.world[0][0] == 'r':
            print('test_1_2 - OK')
        else:
            print('Wrong')
            my_world.print_world()


class TestSize21(ITest):

    def do_test(self):
        my_world = Game(2, 2)
        my_world.set_world([['f', 'f'], ['f', 'f']])
        for l in range(8):
            my_world.update_world()
        if my_world.world == [['f', 'f'], ['f', 'f']]:
            print('test_2_1 - OK')
        else:
            print('Wrong')
            my_world.print_world()


class TestSize22(ITest):

    def do_test(self):
        my_world = Game(2, 2)
        my_world.set_world([['n', 'f'], ['f', 'f']])
        for l in range(2):
            my_world.update_world()
        if my_world.world == [['f', 'f'], ['f', 'f']]:
            print('test_2_2 - OK')
        else:
            print('Wrong')
            my_world.print_world()


class TestSize23(ITest):

    def do_test(self):
        my_world = Game(2, 2)
        my_world.set_world([['n', 'f'], ['f', 's']])
        for l in range(3):
            my_world.update_world()
        if my_world.world == [['n', 'n'], ['n', 'n']]:
            print('test_2_3 - OK')
        else:
            print('Wrong')
            my_world.print_world()


class TestSize31(ITest):

    def do_test(self):
        my_world = Game(3, 3)
        my_world.set_world([['s', 'f', 's'], ['f', 's', 'f'], ['s', 'f', 's']])
        for l in range(3):
            my_world.update_world()
        if my_world.world == [['n', 'f', 'n'], ['f', 'n', 'f'], ['n', 'f', 'n']]:
            print('test_3_1 - OK')
        else:
            print('Wrong')
            my_world.print_world()


class TestSize32(ITest):

    def do_test(self):
        my_world = Game(2, 3)
        my_world.set_world([['f', 'f', 'f'], ['f', 'f', 'f']])
        for l in range(3):
            my_world.update_world()
        if my_world.world == [['n', 'n', 'n'], ['n', 'n', 'n']]:
            print('test_3_2 - OK')
        else:
            print('Wrong')
            my_world.print_world()


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
                if not my_world.world[l][l_] == 'n':
                    return False
                    print('Wrong')
                    my_world.print_world()
                    break

        print('test_n - OK')

#  ***********************************************************************


def custom_tests():
    test_list = [TestSize11(), TestSize12(), TestSize21(), TestSize22(), TestSize23(),
                 TestSize31(), TestSize32(), TestSizeN()]
    for i in range(len(test_list)):
        test_list[i].do_test()
    print("That is all")


custom_tests()
