from CGame import Game

#  ***********************************************************************


def test_size_1_1():
    my_world = Game(1, 1)
    my_world.world[0][0] = 'f'
    for l in range(12):
        my_world.update_world()
    if my_world.world[0][0] == 'n':
        #  print('test_1_1 - OK')
        return True
    else:
        return False
        #  print('Wrong')
        #  my_world.print_world()


def test_size_1_2():
    my_world = Game(1, 1)
    my_world.world[0][0] = 'r'
    for l in range(7):
        my_world.update_world()
    if my_world.world[0][0] == 'r':
        return True
        #   print('test_1_2 - OK')
    else:
        return False
        #   print('Wrong')
        #   my_world.print_world()


def test_size_2_1():
    my_world = Game(2, 2)
    my_world.set_world([['f', 'f'], ['f', 'f']])
    for l in range(8):
        my_world.update_world()
    if my_world.world == [['f', 'f'], ['f', 'f']]:
        return True
        #  print('test_2_1 - OK')
    else:
        return False
        #  print('Wrong')
        #  my_world.print_world()


def test_size_2_2():
    my_world = Game(2, 2)
    my_world.set_world([['n', 'f'], ['f', 'f']])
    for l in range(2):
        my_world.update_world()
    if my_world.world == [['f', 'f'], ['f', 'f']]:
        return True
        #   print('test_2_2 - OK')
    else:
        return False
        #   print('Wrong')
        #   my_world.print_world()


def test_size_2_3():
    my_world = Game(2, 2)
    my_world.set_world([['n', 'f'], ['f', 's']])
    for l in range(3):
        my_world.update_world()
    if my_world.world == [['n', 'n'], ['n', 'n']]:
        return True
        #   print('test_2_3 - OK')
    else:
        return False
        #  print('Wrong')
        #  my_world.print_world()


def test_size_3_1():
    my_world = Game(3, 3)
    my_world.set_world([['s', 'f', 's'], ['f', 's', 'f'], ['s', 'f', 's']])
    for l in range(3):
        my_world.update_world()
    if my_world.world == [['n', 'f', 'n'], ['f', 'n', 'f'], ['n', 'f', 'n']]:
        return True
        #   print('test_3_1 - OK')
    else:
        return False
        #   print('Wrong')
        #   my_world.print_world()


def test_size_3_2():
    my_world = Game(2, 3)
    my_world.set_world([['f', 'f', 'f'], ['f', 'f', 'f']])
    for l in range(3):
        my_world.update_world()
    if my_world.world == [['n', 'n', 'n'], ['n', 'n', 'n']]:
        return True
        #  print('test_3_2 - OK')
    else:
        return False
        #  print('Wrong')
        #  my_world.print_world()


def test_size_n():
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
                #  print('Wrong')
                #  my_world.print_world()
                #  break

    return True
    #  print('test_n - OK')


def custom_tests():
    for i in range(8):
        test_size_1_1()
        test_size_1_2()
        test_size_2_1()
        test_size_2_2()
        test_size_2_3()
        test_size_3_1()
        test_size_3_2()
        test_size_n()
    print("That is all")
#    test_of_equal()


custom_tests()
