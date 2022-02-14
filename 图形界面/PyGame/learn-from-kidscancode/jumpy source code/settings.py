# -*- coding:utf-8 -*-
#!/usr/bin/env python
#game options
TITLE='Jumpy!'
SIZE=WIDTH,HEIGHT=400,500
FPS=60
FONT_NAME='arial'
HS_FILE='highscore.txt'
SPRITESHEET='spritesheet_jumper.png'

#player property
PLAYER_ACC=0.5
PLAYER_FRICTION=-0.12
PLAYER_GRAV=0.5
PLAYER_JUMP=16

#Game properties
BOOST_POWER=60#boost speed
POW_SPAWN_PCT=10#frequence
MOB_FREQ=5000
PLAYER_LAYER=2
PLATFORM_LAYER=1
POW_LAYER=1
MOB_LAYER=2
CLOUD_LAYER=0

#starting platforms
PLATFORM_LIST=[(0,HEIGHT-60),
               (WIDTH//2-50, HEIGHT*2//3),
               (125,HEIGHT-350),
               (350,200),
               (200,220)]

#colors
WHITE=(255,255,255)
BLACK=(0,0,0)
RED=(255,0,0)
GREEN=(0,255,0)
BLUE=(0,0,255)
YELLOW=(255,255,0)
LIGHTBLUE=(0,155,155)
BGCOLOR=LIGHTBLUE