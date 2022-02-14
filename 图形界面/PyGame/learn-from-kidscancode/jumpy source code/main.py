# -*- coding:utf-8 -*-
#!/usr/bin/env python
#Jumpy!(a platform game)original author:http://patreon.com/kidscancode
#Art from Kenny.nl
#Happy Tune by http://opengameart.org/users/syncopika
#Yippee by http://opengameart.org/users/snabisch

import pygame as pg
import random,sys
from settings import *
from sprites import *
from os import path

class Game:
    def __init__(self):
        global pg
        pg.init()
        pg.mixer.init()
        self.screen = pg.display.set_mode(SIZE)
        pg.display.set_caption(TITLE)
        icon=pg.image.load(path.join('img','icon.png'))
        icon.set_colorkey(BLACK)
        pg.display.set_icon(icon)
        self.clock = pg.time.Clock()
        self.running=True
        self.font_name=pg.font.match_font(FONT_NAME)
        self.load_data()

    def load_data(self):
        #load high score
        self.dir=path.dirname(__file__)
        #img_dir=path.join(self.dir,'img')#this step is rebundent
        with open(path.join(self.dir,HS_FILE),'w') as f:
            try:
                self.highscore=int(f.read())
            except:
                self.highscore=0
        #load spritesheet image
        self.spritesheet=Spritesheet(path.join('img',SPRITESHEET))#sys compensate the front msg
        #cloud images
        self.cloud_images=[]
        for i in range(1,4):
            self.cloud_images.append(pg.image.load(path.join('img','cloud%d.png'%i)).convert())
        #load sounds
        self.jump_sound=pg.mixer.Sound(path.join('snd','Jump.wav'))
        self.boost_sound = pg.mixer.Sound(path.join('snd', 'Boost.wav'))
        self.hurt_sound = pg.mixer.Sound(path.join('snd', 'Hurt.wav'))

    def new(self):
        #restart the game
        self.score=0
        self.all_sprites = pg.sprite.LayeredUpdates()
        self.platforms=pg.sprite.Group()
        self.powerups=pg.sprite.Group()
        self.mobs=pg.sprite.Group()
        self.clouds = pg.sprite.Group()
        self.player=Player(self)
        for plat in PLATFORM_LIST:
            Platform(self,*plat)#explode the conponents
        self.mob_timer=0
        pg.mixer.music.load(path.join('snd','Happy Tune.ogg'))
        for i in range(10):
            c=Cloud(self)
            c.rect.y+=500
        self.run()

    def run(self):
        #game loop
        pg.mixer.music.play(loops=-1)
        self.playing=True
        while self.playing:
            self.clock.tick(FPS)
            self.events()
            self.update()
            self.draw()
        pg.mixer.music.fadeout(500)

    def update(self):
        #game loop update
        self.all_sprites.update()
        #spawn a mob
        now=pg.time.get_ticks()
        if now-self.mob_timer>5000+random.choice([-1000,-500,0,500,1000]):
            self.mob_timer=now
            Mob(self)

        #hit a mob
        mob_hits=pg.sprite.spritecollide(self.player,self.mobs,False,pg.sprite.collide_mask)
        if mob_hits:
            self.playing=False
            self.hurt_sound.play()

        #check if player hits a platform only if falling
        if self.player.vel.y>0:
            hits=pg.sprite.spritecollide(self.player,self.platforms,False)
            if hits:
                lowest=hits[0]
                for hit in hits:
                    if hit.rect.bottom>lowest.rect.bottom:
                        lowest=hit
                if lowest.rect.left-10<self.player.pos.x<lowest.rect.right+10:
                    if self.player.pos.y<lowest.rect.centery:
                        self.player.pos.y=lowest.rect.top
                        self.player.vel.y=0#这个时候虽然也在加速，但只要一加速就会碰撞，速度又降为0
                        self.player.jumping=False

        #if player reach 1/4 of screen
        if self.player.rect.top<=HEIGHT//4:
            if random.randrange(100)<8:
                Cloud(self)
            self.player.pos.y+=max(abs(self.player.vel.y),2)#窗口是无限的，取正值，下移,相对于窗口相机(视角)就上移了
            for cloud in self.clouds:
                rand=random.randrange(2,5)
                cloud.rect.y+=max(abs(self.player.vel.y)//rand,2)
            for mob in self.mobs:
                mob.rect.y+=max(abs(self.player.vel.y),2)
            for plat in self.platforms:
                plat.rect.y+=max(abs(self.player.vel.y),2)
                if plat.rect.top>=HEIGHT:
                    plat.kill()
                    self.score+=10

        #hits a powerup
        pow_hits = pg.sprite.spritecollide(self.player, self.powerups, False)
        for pow in pow_hits:
            if pow.type=='boost':
                self.boost_sound.play()
                self.player.vel.y=-BOOST_POWER
                self.player.jumping=False
        #die
        if self.player.rect.bottom>HEIGHT:
            for sprite in self.all_sprites:
                sprite.rect.y-=max(self.player.vel.y,10)
                if sprite.rect.bottom<0:
                    sprite.kill()
        if len(self.platforms)==0:
            self.playing=False

        #spawn new platforms to keep some average number
        while len(self.platforms)<6:
            width=random.randrange(50,100)
            Platform(self,random.randrange(0,WIDTH-width),
                       random.randrange(-60,-30))

    def events(self):
        #game loop events
        for event in pg.event.get():
            if event.type==pg.QUIT:
                if self.playing:
                    self.playing=False
                self.running=False
            if event.type==pg.KEYDOWN:
                if event.key==pg.K_SPACE:
                    self.player.jump()
            if event.type==pg.KEYUP:
                if event.key==pg.K_SPACE:
                    self.player.jump_cut()

    def draw(self):
        #game loop draw
        self.screen.fill(BGCOLOR)
        self.all_sprites.draw(self.screen)#plat can overlap player now
        self.draw_text(str(self.score),22,WHITE,WIDTH//2,15)
        # after drawing everything,flip the display
        pg.display.flip()

    def show_start_screen(self):
        #start screen
        pg.mixer.music.load(path.join('snd','Yippee.ogg'))
        pg.mixer.music.play(loops=-1)
        self.screen.fill(BGCOLOR)
        self.draw_text(TITLE,48,WHITE,WIDTH//2,HEIGHT//4)
        self.draw_text('Arrows to move,Space to jump',22,WHITE,WIDTH//2,HEIGHT//2)
        self.draw_text('Press a key to play',22,WHITE,WIDTH//2,HEIGHT*3//4)
        self.draw_text('High Score:%d'%self.highscore, 22, WHITE, WIDTH // 2, 15)
        self.draw_text('@Original Author:Patreon Practice:Hue' , 14, WHITE, WIDTH // 2, HEIGHT-20)
        pg.display.flip()
        self.wait_for_key()
        pg.mixer.music.fadeout(500)

    def show_go_screen(self):
        #game over
        if not self.running:
            return
        pg.mixer.music.load(path.join('snd', 'Yippee.ogg'))
        pg.mixer.music.play(loops=-1)
        self.screen.fill(BGCOLOR)
        self.draw_text('GAME OVER', 48, WHITE, WIDTH // 2, HEIGHT // 4)
        self.draw_text('Score:%d'%self.score, 22, WHITE, WIDTH // 2, HEIGHT // 2)
        self.draw_text('Press a key to play again', 22, WHITE, WIDTH // 2, HEIGHT * 3 // 4)
        self.draw_text('@Original Author:Patreon Practice:Hue', 14, WHITE, WIDTH // 2, HEIGHT - 20)
        if self.score>self.highscore:
            self.highscore=self.score
            self.draw_text('NEW HIGH SCORE!',22,WHITE,WIDTH//2,HEIGHT//2+40)
            with open(path.join(self.dir,HS_FILE),'w') as f:
                f.write(str(self.highscore))
        else:
            self.draw_text('High Score:%d' % self.highscore, 22, WHITE, WIDTH // 2, HEIGHT//2+40)
        pg.display.flip()
        self.wait_for_key()
        pg.mixer.music.fadeout(500)

    def wait_for_key(self):
        waiting=True
        while waiting:
            self.clock.tick(FPS)
            for event in pg.event.get():
                if event.type==pg.QUIT:
                    Waiting=False
                    self.running=False
                if event.type==pg.KEYUP:
                    waiting=False

    def draw_text(self,text,size,color,x,y):
        font=pg.font.Font(self.font_name,size)
        text_surface=font.render(text,True,color)
        text_rect=text_surface.get_rect()
        text_rect.midtop=(x,y)
        self.screen.blit(text_surface,text_rect)


g=Game()
g.show_start_screen()
while g.running:
    g.new()
    g.show_go_screen()

pg.quit()