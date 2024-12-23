# -*- coding: utf-8 -*-
"""
Created on Sun Dec 22 04:17:09 2024

@author: anma
"""
from PIL import Image, ImageDraw

class Life:
    def __init__( self, figure_lst, num_of_row, num_of_char):
        self.figure_lst = figure_lst
        self.num_of_row = num_of_row
        self.num_of_char = num_of_char
    
    def draw_figure(self, number):
        koeff = max(self.num_of_row, self.num_of_char)
        lop = 600 / koeff
        im = Image.new('RGB',(600,600),(255,255,255))
        draw = ImageDraw.Draw(im)
        for ind in range(self.num_of_row):
            for jnd in range(self.num_of_char):
                if self.figure_lst[ind][jnd] == '1':
                    draw.rectangle((jnd*lop,ind*lop,
                                    jnd*lop + lop,
                                    ind*lop + lop),
                                   fill = 'black',
                                   outline = (255,255,255))
        
        im.save('figure_{0}.png'.format(number), quality=95)
    
    # def load_figure(self):
    #     with open('config.txt', 'r') as fr:
    #         # Read the lines of data into a list
    #         lines = fr.readlines()

    #         # Use method rstrip in a list comprehension to 
    #         # clean up the lines of data
    #         lines = [line.rstrip('\n') for line in lines]
    #     self.figure_lst = lines
    
    
    
    def write_figure(self, number):
        with open ('config_{0}.txt'.format(number),"w" ) as fw:
            for line in self.figure_lst:
                fw.write(line+'\n')
    
    def next_step(self):
        
        new_figure_lst=list()
        for ind in range(self.num_of_row):

            
            if ind == (self.num_of_row - 1) :
                i = -1
            else:
                i = ind
                     
            new_line = str()
            for jnd in range(self.num_of_char):

                if jnd == (self.num_of_char -1):
                    j = -1
                else:
                    j = jnd

                is_alive = int(self.figure_lst[i-1][j-1])+\
                            int(self.figure_lst[i-1][j])+\
                            int(self.figure_lst[i-1][j+1])+\
                            int(self.figure_lst[i][j-1])+\
                            int(self.figure_lst[i][j+1])+\
                            int(self.figure_lst[i+1][j-1])+\
                            int(self.figure_lst[i+1][j])+\
                            int(self.figure_lst[i+1][j+1])
                if self.figure_lst[i][j] == '1' and is_alive == 2 or is_alive == 3:
                    new_line += '1'
                # elif self.figure_lst[i][j] == '1':
                #      new_line += '0'
                elif self.figure_lst[i][j] == '0' and is_alive == 3:
                    new_line += '1'
                else:
                    new_line += '0'
                
            new_figure_lst.append (new_line)
        self.figure_lst = new_figure_lst
       
    