from cs1robots import *
create_world()
hubo = Robot(beepers=1)
hubo.set_trace('blue')
hubo.set_pause(.25)

hubo.move()
hubo.move()
hubo.drop_beeper()
hubo.move()
hubo.move()