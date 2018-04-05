from CGame import Game

#  ***********************************************************************


class ITest:

    def do_test(self):
        ''' func '''

    def print_ok(self, i):
        print('test ', i, ' - Ok')

    def print_error(self, i):
        print('Wrong test ', i)


class TestSize11(ITest):

    def do_test(self):
        my_world = Game(1, 1)
        my_world.world[0][0] = 'f'
        for l in range(12):
            my_world.update_world()
        if my_world.world[0][0] == 'n':
            return True
        else:
            return False


class TestSize12(ITest):

    def do_test(self):
        my_world = Game(1, 1)
        my_world.world[0][0] = 'r'
        for l in range(7):
            my_world.update_world()
        if my_world.world[0][0] == 'r':
            return True
        else:
            return False


class TestSize21(ITest):

    def do_test(self):
        my_world = Game(2, 2)
        my_world.set_world([['f', 'f'], ['f', 'f']])
        for l in range(8):
            my_world.update_world()
        if my_world.world == [['f', 'f'], ['f', 'f']]:
            return True
        else:
            return False


class TestSize22(ITest):

    def do_test(self):
        my_world = Game(2, 2)
        my_world.set_world([['n', 'f'], ['f', 'f']])
        for l in range(2):
            my_world.update_world()
        if my_world.world == [['f', 'f'], ['f', 'f']]:
            return True
        else:
            return False


class TestSize23(ITest):

    def do_test(self):
        my_world = Game(2, 2)
        my_world.set_world([['n', 'f'], ['f', 's']])
        for l in range(3):
            my_world.update_world()
        if my_world.world == [['n', 'n'], ['n', 'n']]:
            return True
        else:
            return False


class TestSize31(ITest):

    def do_test(self):
        my_world = Game(3, 3)
        my_world.set_world([['s', 'f', 's'], ['f', 's', 'f'], ['s', 'f', 's']])
        for l in range(3):
            my_world.update_world()
        if my_world.world == [['n', 'f', 'n'], ['f', 'n', 'f'], ['n', 'f', 'n']]:
            return True
        else:
            return False


class TestSize32(ITest):

    def do_test(self):
        my_world = Game(2, 3)
        my_world.set_world([['f', 'f', 'f'], ['f', 'f', 'f']])
        for l in range(3):
            my_world.update_world()
        if my_world.world == [['n', 'n', 'n'], ['n', 'n', 'n']]:
            return True
        else:
            return False


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


        return True

#  ***********************************************************************


def custom_tests():
    test_list = [TestSize11(), TestSize12(), TestSize21(), TestSize22(), TestSize23(),
                 TestSize31(), TestSize32(), TestSizeN()]
    for i in range(len(test_list)):
        if test_list[i].do_test():
            test_list[i].print_ok(i+1)
        else:
            test_list[i].print_error(i+1)


    print("That is all")


custom_tests()
