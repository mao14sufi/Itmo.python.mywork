# -*- coding: utf-8 -*-
"""
The Game of Life

number of generation in sys.argv[1]
change initial figure in config.txt


"""
import sys
import life_control_class as lcc
if len(sys.argv) > 1 :
	number_of_generation = int(sys.argv[1])
else:
	number_of_generation = 3
game_life = lcc.Life_Control(number_of_generation)
game_life.game_process()
