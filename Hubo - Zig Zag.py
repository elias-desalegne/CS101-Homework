# My first program
from cs1robots import *
create_world()
hubo = Robot()
hubo.set_trace("purple")
hubo.set_pause(1)

def turn_right() :
    hubo.turn_left()
    hubo.turn_left()
    hubo.turn_left()

def turn_back() : 
    hubo.turn_left()
    hubo.turn_left()

def step_back() :
    hubo.turn_left()
    hubo.turn_left()
    hubo.move()
    hubo.turn_left()
    hubo.turn_left()

def move_across() :
    hubo.move()
    hubo.move()
    hubo.move()
    hubo.move()
    hubo.move()
    hubo.move()
    hubo.move()
    hubo.move()
    hubo.move()


def one_zig() :
    hubo.turn_left()
    move_across()
    turn_right()
    hubo.move()
    turn_right()
    move_across()

one_zig()
hubo.turn_left()
hubo.move()
one_zig()
hubo.turn_left()
hubo.move()
one_zig()
hubo.turn_left()
hubo.move()
one_zig()
hubo.turn_left()
hubo.move()
one_zig()