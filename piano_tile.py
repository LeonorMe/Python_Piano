'''
@Title: Piano Tiles
@Description: Test
@Author: Leonor Medeiros
@Date: 2023-09-21 12:00:00
@Version: V1.0.0
'''

import pygame as pg
import mido
import rtmidi

pg.init()

BLACK = [0, 0, 0]
WHITE = [255, 255, 255]
node_list = []
node_list_off = []

outport=mido.open_output()
inport=mido.open_input()

SIZE = [380, 380]
screen = pg.display.set_mode(SIZE)
pg.display.set_caption("Piano Tiles")
clock = pg.time.Clock()
done = False

while done == False:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            done = True
            
    #screen.fill(BLACK)
    for msg in inport.iter_pending():
        n = msg.note
        x = (n-47)*10
        if msg.velocity > 0: 
            msg = mido.Message('note_on', note=n)
            outport.send(msg)
            node_list.append([x, 0])
        else:
            msg = mido.Message('note_off', note=n)
            outport.send(msg)
            node_list_off.append([x, 0])
            
    for i in range(len(node_list)):
        #pg.draw.rect(screen, WHITE, [node_list[i][0], node_list[i][1], 10, 10])
        #node_list[i][1] += 10
        #if node_list[i][1] > 380:
        #    node_list_off.append(node_list[i])
        pg.draw.circle(screen, WHITE, node_list[i], 10)
        node_list[i][1] += 1
        #
    pg.display.flip()
    
    for i in range(len(node_list_off)):
        pg.draw.circle(screen, BLACK, node_list_off[i], 10)
        node_list_off[i][1] += 1
    
    clock.tick(200) # frame rate  1000/200 = 5 ms
    
pg.quit()