# My first program
from cs1robots import *
load_world("worlds/hurdles1.wld")
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

def one_jump() :
    hubo.move()
    hubo.turn_left()
    hubo.move()
    turn_right()
    hubo.move()
    turn_right()
    hubo.move()
    hubo.turn_left()

one_jump()
one_jump()
one_jump()
one_jump()
hubo.move()
hubo.pick_beeper()