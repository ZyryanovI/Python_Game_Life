#  import sys
#  import random
#  sys.path.append("../Users/user/Desktop/pyton/ИграЖизнь2")
from main2 import Game
#  from dasha_main import CLifegame
#  from dasha_main import console_output


'''def generate(height, weight):
    first_world_ = [['n'] * weight for _ in range(height)]
    for i_ in range(height):
        for j in range(weight):
            element = random.choice(['n', 'f', 'r', 's'])
            first_world_[i_][j] = element
    return first_world_


def test(my_world_, dashas_world_, k):
    for _k in range(k):
        my_world_.update_world()
        dashas_world_.next()
    return check_equal(my_world_, dashas_world_)


def check_equal(my_world_, dashas_world_):
    for i in range(my_world_.height):
        for j in range(my_world_.weight):
            if not my_world_.world[i][j] == dashas_world_.arr[i][j]:
                return False
    return True


def test_of_equal():
    for i in range(1000):
        random.seed()
        height_ = random.randint(1, 100)
        weight_ = random.randint(1, 100)
        k_ = random.randint(1, 100)

        print(height_, weight_, k_, sep=' ')

        lst = generate(height_, weight_)
        my_world = Game(height_, weight_)
        dasha_world = CLifegame(height_, weight_, k_)
        for _i in range(height_):
            for j in range(weight_):
                my_world.world[_i][j] = lst[_i][j]
                dasha_world.arr[_i][j] = lst[_i][j]
        if test(my_world, dasha_world, k_):
            print('OK')
        else:
            print('Wrong')
            print('*******')
            my_world.print_world()
            print('---------')
            console_output(dasha_world)
            break;
'''
#  ***********************************************************************


def test_size_1_1():
    my_world = Game(1, 1)
    my_world.world[0][0] = 'f'
    for l in range(12):
        my_world.update_world()
    if my_world.world[0][0] == 'n':
        print('test_1_1 - OK')
    else:
        print('Wrong')
        my_world.print_world()


def test_size_1_2():
    my_world = Game(1, 1)
    my_world.world[0][0] = 'r'
    for l in range(7):
        my_world.update_world()
    if my_world.world[0][0] == 'r':
        print('test_1_2 - OK')
    else:
        print('Wrong')
        my_world.print_world()


def test_size_2_1():
    my_world = Game(2, 2)
    my_world.set_world([['f', 'f'], ['f', 'f']])
    for l in range(8):
        my_world.update_world()
    if my_world.world == [['f', 'f'], ['f', 'f']]:
        print('test_2_1 - OK')
    else:
        print('Wrong')
        my_world.print_world()


def test_size_2_2():
    my_world = Game(2, 2)
    my_world.set_world([['n', 'f'], ['f', 'f']])
    for l in range(2):
        my_world.update_world()
    if my_world.world == [['f', 'f'], ['f', 'f']]:
        print('test_2_2 - OK')
    else:
        print('Wrong')
        my_world.print_world()


def test_size_2_3():
    my_world = Game(2, 2)
    my_world.set_world([['n', 'f'], ['f', 's']])
    for l in range(3):
        my_world.update_world()
    if my_world.world == [['n', 'n'], ['n', 'n']]:
        print('test_2_3 - OK')
    else:
        print('Wrong')
        my_world.print_world()


def test_size_3_1():
    my_world = Game(3, 3)
    my_world.set_world([['s', 'f', 's'], ['f', 's', 'f'], ['s', 'f', 's']])
    for l in range(3):
        my_world.update_world()
    if my_world.world == [['n', 'f', 'n'], ['f', 'n', 'f'], ['n', 'f', 'n']]:
        print('test_3_1 - OK')
    else:
        print('Wrong')
        my_world.print_world()


def test_size_3_2():
    my_world = Game(2, 3)
    my_world.set_world([['f', 'f', 'f'], ['f', 'f', 'f']])
    for l in range(3):
        my_world.update_world()
    if my_world.world == [['n', 'n', 'n'], ['n', 'n', 'n']]:
        print('test_3_2 - OK')
    else:
        print('Wrong')
        my_world.print_world()


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
                print('Wrong')
                my_world.print_world()
                break

    print('test_n - OK')


def custom_tests():
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
