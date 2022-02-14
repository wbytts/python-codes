#!/usr/bin/env python
# -*- coding:utf-8 -*-
#Frozen Jam by tgfcoder <https://twitter.com/tgfcoder> licensed under CC-BY-3 <http://creativecommons.org/licenses/by/3.0/>
#Rumble by Michel Baradari from opengameart.org
#other sounds from bfxr.net
#art form Kenny.nl and
#original author:kidscancode practice:Hue Zhang
#shmup game
import pygame
import random
from os import path

img_dir=path.join(path.dirname(__file__),'img')
snd_dir=path.join(path.dirname(__file__),'snd')

SIZE=WIDTH,HEIGHT=480,600
FPS=60
POWERUP_TIME=3000

#colors
WHITE=(255,255,255)
BLACK=(0,0,0)
RED=(255,0,0)
GREEN=(0,255,0)
BLUE=(0,0,255)
YELLOW=(255,255,0)

#init
pygame.init()
pygame.mixer.init()
screen=pygame.display.set_mode(SIZE)
pygame.display.set_caption('Shmup!')
clock=pygame.time.Clock()

font_name=pygame.font.match_font('arial')
def draw_text(surf,text,size,x,y):
    font=pygame.font.Font(font_name,size)
    text_surface=font.render(text,True,WHITE)
    text_rect=text_surface.get_rect()
    text_rect.midtop=(x,y)
    surf.blit(text_surface,text_rect)

def draw_lives(surf,x,y,lives,img):
    for i in range(lives):
        img_rect=img.get_rect()
        img_rect.x=x+30*i
        img_rect.y=y
        surf.blit(img,img_rect)

def newmob():
    m=Mob()
    all_sprites.add(m)
    mobs.add(m)

def draw_shield_bar(surf,x,y,pct):
    if pct<0:
        pct=0
    BAR_LENGTH=100
    BAR_HEIGHT=10
    fill=(pct/100)*BAR_LENGTH#100 is the max-shield
    outline_rect=pygame.Rect(x,y,BAR_LENGTH,BAR_HEIGHT)
    fill_rect=pygame.Rect(x,y,fill,BAR_HEIGHT)
    pygame.draw.rect(surf,GREEN,fill_rect)
    pygame.draw.rect(surf,WHITE,outline_rect,2)

class Player(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image=pygame.transform.scale(player_img,(50,38))
        self.image.set_colorkey(BLACK)
        self.rect=self.image.get_rect()
        self.radius=21
        #pygame.draw.circle(self.image,RED,self.rect.center,self.radius)
        self.rect.centerx=WIDTH//2
        self.rect.bottom=HEIGHT-10
        self.speedx=0
        self.shield=100
        self.shoot_delay=250
        self.last_shot=pygame.time.get_ticks()
        self.lives=3
        self.hidden=False
        self.hide_timer=pygame.time.get_ticks()
        self.power=1
        self.power_timer=pygame.time.get_ticks()

    def update(self):

        #timeout for powerups
        if self.power>=2 and pygame.time.get_ticks()-self.power_timer>POWERUP_TIME:
            self.power-=1
            self.power_timer=pygame.time.get_ticks()
        #unhide if hidden
        if self.hidden and pygame.time.get_ticks()-self.hide_timer>1000:
            self.hidden=False
            self.rect.centerx=WIDTH//2
            self.rect.bottom=HEIGHT-10
        self.speedx=0
        keystate=pygame.key.get_pressed()
        if keystate[pygame.K_LEFT]:
            self.speedx=-5
        if keystate[pygame.K_RIGHT]:
            self.speedx=5
        if keystate[pygame.K_SPACE]:
            self.shoot()
        self.rect.x+=self.speedx
        if self.rect.right>WIDTH:
            self.rect.right=WIDTH
        if self.rect.left<0:
            self.rect.left=0

    def powerup(self):
        self.power+=1
        self.power_timer=pygame.time.get_ticks()

    def shoot(self):
        now=pygame.time.get_ticks()
        if now-self.last_shot>self.shoot_delay:
            self.last_shot=now
            if self.power==1:
                bullet=Bullet(self.rect.centerx,self.rect.top)
                all_sprites.add(bullet)
                bullets.add(bullet)
                shoot_sound.play()
            elif self.power>=2:
                bullet1 = Bullet(self.rect.left, self.rect.centery)
                bullet2 = Bullet(self.rect.right, self.rect.centery)
                all_sprites.add(bullet1)
                all_sprites.add(bullet2)
                bullets.add(bullet1)
                bullets.add(bullet2)
                shoot_sound.play()

    def hide(self):
        self.hidden=True
        self.hide_timer=pygame.time.get_ticks()
        self.rect.center=(WIDTH/2,HEIGHT+200)#move out of the screen

class Mob(pygame.sprite.Sprite):
    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image_orig=random.choice(meteor_images)
        self.image_orig.set_colorkey(BLACK)
        self.image=self.image_orig.copy()
        self.rect=self.image.get_rect()
        self.radius=int(self.rect.width*.85/2)
        #pygame.draw.circle(self.image, RED, self.rect.center, self.radius)
        self.rect.x=random.randrange(WIDTH-self.rect.width)
        self.rect.y=random.randrange(-150,-100)
        self.speedy=random.randrange(1,8)
        self.speedx=random.randrange(-3,3)
        self.rot=0#rotation
        self.rot_speed=random.randrange(-8,8)
        self.last_update=pygame.time.get_ticks()

    def update(self):
        self.rotate()
        self.rect.x += self.speedx
        self.rect.y+=self.speedy
        if self.rect.top>HEIGHT+10 or self.rect.x<-25 or self.rect.right>WIDTH+25:
            self.rect.x = random.randrange(WIDTH - self.rect.width)
            self.rect.y = random.randrange(-100, -40)
            self.speedy = random.randrange(1, 8)

    def rotate(self):
        now=pygame.time.get_ticks()
        if now-self.last_update>50:
            self.last_update=now
            self.rot=(self.rot+self.rot_speed)%360
            new_image=pygame.transform.rotate(self.image_orig,self.rot)
            old_center=self.rect.center
            self.image=new_image
            self.rect=self.image.get_rect()
            self.rect.center=old_center

class Bullet(pygame.sprite.Sprite):
    def __init__(self,x,y):
        pygame.sprite.Sprite.__init__(self)
        self.image=bullet_img
        self.image.set_colorkey(BLACK)
        self.rect=self.image.get_rect()
        self.rect.bottom=y
        self.rect.centerx=x
        self.speedy=-10

    def update(self):
        self.rect.y+=self.speedy
        #kill it if moves off the top of the screen
        if self.rect.bottom<0:
            self.kill()

class Pow(pygame.sprite.Sprite):
    def __init__(self,center):
        pygame.sprite.Sprite.__init__(self)
        self.type=random.choice(['shield','gun'])
        self.image=powerup_images[self.type]
        self.image.set_colorkey(BLACK)
        self.rect=self.image.get_rect()
        self.rect.center=center
        self.speedy=5

    def update(self):
        self.rect.y+=self.speedy
        #kill it if moves off the top of the screen
        if self.rect.top>HEIGHT:
            self.kill()

class Explosion(pygame.sprite.Sprite):
    def __init__(self,center,size):
        pygame.sprite.Sprite.__init__(self)
        self.size=size
        self.image=explosion_anim[self.size][0]
        self.rect=self.image.get_rect()
        self.rect.center=center
        self.frame=0
        self.last_update=pygame.time.get_ticks()
        self.frame_rate=50

    def update(self):
        now=pygame.time.get_ticks()
        if now-self.last_update>self.frame_rate:
            self.last_update=now
            self.frame+=1
            if self.frame==len(explosion_anim[self.size]):
                self.kill()
            else:
                center=self.rect.center
                self.image=explosion_anim[self.size][self.frame]
                self.rect=self.image.get_rect()
                self.rect.center=center

def show_go_screen():
    screen.blit(background, background_rect)
    draw_text(screen,'SHMUP!',64,WIDTH//2,HEIGHT//4)
    draw_text(screen,'Arrow keys move,Space to fire',22,WIDTH//2,HEIGHT//2)
    draw_text(screen,'Press a key to begin',18,WIDTH//2,HEIGHT*3//4)
    draw_text(screen, '@Original author:kidscancode Practice:Hue Zhang', 15, WIDTH // 2, HEIGHT -30)
    pygame.display.flip()
    waiting=True
    while waiting:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                pygame.quit()
            if event.type==pygame.KEYUP:
                waiting=False

#load all game assets
background=pygame.transform.scale(pygame.image.load(path.join(img_dir,'starfield.jpg')).convert(),(480,600))
background_rect=background.get_rect()
player_img=pygame.image.load(path.join(img_dir,'playerShip1_orange.png')).convert()
player_mini_img=pygame.transform.scale(player_img,(25,19))
player_mini_img.set_colorkey(BLACK)
bullet_img=pygame.image.load(path.join(img_dir,'laserRed16.png')).convert()
meteor_images=[]
meteor_list=['meteorBrown_big1.png','meteorBrown_big2.png',
             'meteorBrown_med1.png','meteorBrown_med2.png',
             'meteorBrown_small1.png','meteorBrown_small2.png',
             'meteorBrown_tiny1.png']
for img in meteor_list:
    meteor_images.append(pygame.image.load(path.join(img_dir,img)).convert())
explosion_anim={}
explosion_anim['lg']=[]
explosion_anim['sm']=[]
for i in range(1,17):
    filename='square_explosion%d.png'%i
    img=pygame.image.load(path.join(img_dir,filename)).convert()
    img.set_colorkey(BLACK)
    img_lg=pygame.transform.scale(img,(60,60))
    explosion_anim['lg'].append(img_lg)
    img_sm = pygame.transform.scale(img, (25, 25))
    explosion_anim['sm'].append(img_sm)

powerup_images={}
powerup_images['shield']=pygame.image.load(path.join(img_dir,'shield_gold.png')).convert()
powerup_images['gun']=pygame.image.load(path.join(img_dir,'bolt_gold.png')).convert()

#load game sounds
shoot_sound=pygame.mixer.Sound(path.join(snd_dir,'Laser.wav'))
shield_sound=pygame.mixer.Sound(path.join(snd_dir,'shield.wav'))
gun_sound=pygame.mixer.Sound(path.join(snd_dir,'gun.wav'))


expl_sounds=[]
for snd in ['Explosion1.wav','Explosion2.wav']:
    expl_sounds.append(pygame.mixer.Sound(path.join(snd_dir,snd)))
player_die_sound=pygame.mixer.Sound(path.join(snd_dir,'rumble.ogg'))
pygame.mixer.music.load(path.join(snd_dir,'tgfcoder-FrozenJam-SeamlessLoop.ogg'))
pygame.mixer.music.set_volume(0.4)



pygame.mixer.music.play(loops=-1)
#game loop
running=True
game_over=True
while running:
    if game_over:
        show_go_screen()
        game_over=False
        all_sprites = pygame.sprite.Group()
        mobs = pygame.sprite.Group()
        bullets = pygame.sprite.Group()
        powerups = pygame.sprite.Group()
        player = Player()
        all_sprites.add(player)
        for i in range(8):
            newmob()
        score = 0
        lastscore = 0

    clock.tick(FPS)
    #process input(events)
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            running=False

    #update
    all_sprites.update()

    # check if a bullet hit the mob
    hits=pygame.sprite.groupcollide(mobs,bullets,  True,True)
    for hit in hits:
        score+=50-hit.radius
        random.choice(expl_sounds).play()
        expl=Explosion(hit.rect.center,'lg')
        all_sprites.add(expl)
        if random.random()>0.9:
            pow=Pow(hit.rect.center)
            all_sprites.add(pow)
            powerups.add(pow)
        newmob()

    #check if a player hit a powerup
    hits=pygame.sprite.spritecollide(player,powerups,True)
    for hit in hits:
        if hit.type=='shield':
            shield_sound.play()
            player.shield+=random.randrange(10,30)
            if player.shield>=100:
                player.shield=100
        elif hit.type=='gun':
            player.powerup()
            gun_sound.play()


    #check if a mob hit the player
    hits=pygame.sprite.spritecollide(player,mobs,True,pygame.sprite.collide_circle)
    for hit in hits:
        player.shield-=hit.radius*2
        expl = Explosion(hit.rect.center, 'sm')
        all_sprites.add(expl)
        if player.shield<=0:
            death_expl=Explosion(player.rect.center,'lg')
            player_die_sound.play()
            all_sprites.add(death_expl)
            player.hide()
            player.lives-=1
            player.shield=100
        newmob()

    #if player died and the explosion has finished
    if player.lives==0 and not death_expl.alive():
        game_over=True

    #draw
    screen.fill(BLACK)
    screen.blit(background,background_rect)
    all_sprites.draw(screen)
    if score-lastscore>1000:
        lastscore=score
        newmob()
    draw_text(screen,'Score:%d'%score,18,WIDTH//2,10)
    draw_text(screen, 'SHD', 12, 15, 8)
    draw_shield_bar(screen,30,10,player.shield)
    draw_lives(screen,WIDTH-100,5,player.lives,player_mini_img)
    #after drawing everything,flip the display
    pygame.display.flip()
    # clock

pygame.quit()