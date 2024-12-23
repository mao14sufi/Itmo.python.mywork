# -*- coding: utf-8 -*-
"""
Created on Sun Dec 22 07:33:40 2024

@author: anma
"""
import life_class as lc
class Life_Control:
    
    def __init__(self, num_generation):
        self.num_generation = num_generation
    
    def load_config():
        with open('config.txt', 'r') as fr:
            lines = fr.readlines()
            lines = [line.rstrip('\n') for line in lines]
        
            
        if len(lines) > len(max(lines, key = len)):
            num_to_correct = len(lines)
        else:
            num_to_correct = len(max(lines, key = len))
                    
        for ind, line in enumerate(lines):
            
            
            
            for letter in line:
                if letter.isprintable() and not letter.isspace() and not letter == '0':
                    line = line.replace(letter,'1')
                else :
                    line = line.replace(letter,'0')
            line = line.ljust(num_to_correct,'0')
            lines[ind] =  line
        return (lines, len(lines), len(max(lines)))
        
        
       # return (lines)#, len(lines), len(max(lines)))
        
    life = lc.Life(load_config()[0],load_config()[1],load_config()[2])
    
    def game_process(self):
        
        previous_figure_lst = list()
        for ind in range(self.num_generation):
            self.life.draw_figure(ind + 1)
            self.life.write_figure(ind + 1)
            previous_figure_lst.append(self.life.figure_lst)
            self.life.next_step()
            if self.life.figure_lst in previous_figure_lst:
                break
            
        