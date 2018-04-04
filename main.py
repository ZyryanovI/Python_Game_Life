from CGame import Game
from CGame import read_world


ls = input()

if ls == 'f':
    for_reading = open("input.txt", "r")
    ls = for_reading.readline()
    ls = ls.split()
    HEIGHT = int(ls[0])
    WEIGHT = int(ls[1])
    k = int(ls[2])
    first_world = [['n'] * WEIGHT for _ in range(HEIGHT)]
    i = 0
    for line in for_reading:
        first_world[i] = line
        i += 1
    world = Game(HEIGHT, WEIGHT)
    world.set_world(first_world)
    world.make_steps(k)
    world.print_world_file()
    for_reading.close()
else:
    ls = ls.split()
    HEIGHT = int(ls[0])
    WEIGHT = int(ls[1])
    k = int(ls[2])
    first_world = [['n'] * WEIGHT for _ in range(HEIGHT)]
    read_world(first_world, HEIGHT)
    world = Game(HEIGHT, WEIGHT)
    world.set_world(first_world)
    world.make_steps(k)
    world.print_world()
