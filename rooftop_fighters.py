"""
Name: RoofTop Fighters
Author: Joey Burgee
Date: March 9, 2018
"""

# IMPORT MODULES
import pygame as pg

pg.font.init()
pg.mixer.init()

GREEN = (0, 255, 0)
RED = (255, 0, 0)

# ------CREATE WINDOW CLASS------
class Window (object):

    def __init__(self):
        # DEFINE WINDOW ATTRIBUTES
        self.running = False
        self.WIDTH = 800
        self.HEIGHT = 750
        self.screen = pg.display.set_mode((self.WIDTH, self.HEIGHT))
        self.clock = pg.time.Clock()
        self.FPS = 60
        self.background = pg.image.load("rooftop.png")
        self.backingtrack = pg.mixer.music.load("blues.ogg")
        pg.mixer.music.play(-1)
        
        # DEFINE FONT ATTRIBUTES
        self.font = pg.font.SysFont("Comic Sans MS", 30)
        self.font2 = pg.font.SysFont("Didot", 45)

        self.gunshot = pg.mixer.Sound("gunshot.ogg")

        self.winner = self.font.render("", False, RED)

    # ---MAKE A FUNCTION THAT OPENS START MENU AND RESETS VALUES---
    def START(self):
        # DEFINE PLAYER 1 ATTRIBUTES
        self.player1 = pg.image.load("shooter_player1.png")
        self.x1 = 25
        self.y1 = self.HEIGHT / 2
        self.x1v = 0
        self.y1v = 0
        self.health1 = 3
        self.heart1 = pg.image.load("heart.png")
        self.heart2 = pg.image.load("heart.png")
        self.heart3 = pg.image.load("heart.png")
        self.hy1 = 15
        self.hy2 = 15
        self.hy3 = 15
        # DEFINE PLAYER 1 BULLET 1 ATTRIBUTES
        self.bullet1 = pg.image.load("bullet.png")
        self.bx1 = -25
        self.by1 = self.y1 + 20
        self.bx1v = 0
        self.by1v = 0
        # DEFINE PLAYER 1 BULLET 2 ATTRIBUTES
        self.bullet2 = pg.image.load("bullet.png")
        self.bx2 = -25
        self.by2 = self.y1 + 20
        self.bx2v = 0
        self.by2v = 0
        # DEFINE PLAYER 1 BULLET 3 ATTRIBUTES
        self.bullet3 = pg.image.load("bullet.png")
        self.bx3 = -25
        self.by3 = self.y1 + 20
        self.bx3v = 0
        self.by3v = 0


        # DEFINE PLAYER 2 ATTRIBUTES
        self.player2 = pg.image.load("shooter_player2.png")
        self.x2 = 700
        self.y2 = self.HEIGHT / 2
        self.x2v = 0
        self.y2v = 0
        self.h1 = pg.image.load("heart.png")
        self.h2 = pg.image.load("heart.png")
        self.h3 = pg.image.load("heart.png")
        self.health2 = 3
        self.hearty1 = 15
        self.hearty2 = 15
        self.hearty3 = 15
        # DEFINE PLAYER 2 BULLET 1 ATTRIBUTES
        self.bul1 = pg.image.load("bullet2.png")
        self.bulx1 = self.WIDTH + 25
        self.buly1 = self.y2 + 20
        self.bulx1v = 0
        self.buly1v = 0
        # DEFINE PLAYER 2 BULLET 2 ATTRIBUTES
        self.bul2 = pg.image.load("bullet2.png")
        self.bulx2 = self.WIDTH + 25
        self.buly2 = self.y2 + 20
        self.bulx2v = 0
        self.buly2v = 0
        # DEFINE PLAYER 2 BULLET 3 ATTRIBUTES
        self.bul3 = pg.image.load("bullet2.png")
        self.bulx3 = self.WIDTH + 25
        self.buly3 = self.y2 + 20
        self.bulx3v = 0
        self.buly3v = 0

        # ------ MAKE START MENU ------
        self.screen.blit(self.background, [0, 0])

        self.screen.blit(self.winner, [self.WIDTH / 2 - 100, self.HEIGHT / 2 - 100])

        # TITLE
        self.title = self.font2.render("RoofTop Fighters", False, RED)
        self.screen.blit(self.title, [self.WIDTH / 2 - 175, self.HEIGHT / 2 - 225])

        # INSTRUCTIONS
        self.start_text = self.font.render("Press Anywhere To Start Game", False, GREEN)
        self.screen.blit(self.start_text, [self.WIDTH / 2 - 215, self.HEIGHT / 2 - 175])

        pg.display.update()

        # MAKE USER-CLICK START GAME
        button_pressed = False
        while button_pressed == False:
            for event in pg.event.get():
                if event.type == pg.MOUSEBUTTONDOWN:
                        self.running = True
                        return 0


    # ---MAKE A FUNCTION THAT INITIALIZES PYGAME WINDOW---
    def start_window(self):
        pg.init()

    # ---MAKE A FUNCTION THAT PROCESSES EVENTS---
    def event_handling(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                quit()
            if event.type == pg.KEYDOWN:
                # PLAYER 1 CONTROLS
                if event.key == pg.K_a:
                    self.x1v = -7
                if event.key == pg.K_d:
                    self.x1v = 7
                if event.key == pg.K_w:
                    self.y1v = -7
                if event.key == pg.K_s:
                    self.y1v = 7

                # PLAYER 2 CONTROLS
                if event.key == pg.K_LEFT:
                    self.x2v = -7
                if event.key == pg.K_RIGHT:
                    self.x2v = 7
                if event.key == pg.K_UP:
                    self.y2v = -7
                if event.key == pg.K_DOWN:
                    self.y2v = 7
                    
                # ---BULLET CONTROLS FOR PLAYER 1---
                # BULLET 1
                if (self.bx1 == -25):
                    if event.key == pg.K_1:
                        self.bx1 = self.x1 + 35
                        self.bx1v = 8
                        pg.mixer.Sound.play(self.gunshot)
                # BULLET 2
                if (self.bx1 > self.x1 + 35):
                    if (self.bx2 == -25):
                        if event.key == pg.K_1:
                            self.bx2 = self.x1 + 35
                            self.bx2v = 8
                            pg.mixer.Sound.play(self.gunshot)
                # BULLET 3
                if (self.bx1 > self.x1 + 40 and self.bx2 > self.x1 + 35):
                    if (self.bx3 == -25):
                        if event.key == pg.K_1:
                            self.bx3 = self.x1 + 35
                            self.bx3v = 8
                            pg.mixer.Sound.play(self.gunshot)

                # ---BULLET CONTROLS FOR PLAYER 2
                # BULLET 1
                if (self.bulx1 == self.WIDTH + 25):
                    if event.key == pg.K_SEMICOLON:
                        self.bulx1 = self.x2 - 10
                        self.bulx1v = -8
                        pg.mixer.Sound.play(self.gunshot)
                # BULLET 2
                if (self.bulx1 < self.x2 -21):
                    if (self.bulx2 == self.WIDTH + 25):
                        if event.key == pg.K_SEMICOLON:
                            self.bulx2 = self.x2 - 10
                            self.bulx2v = -8
                            pg.mixer.Sound.play(self.gunshot)
                # BULLET 3
                if (self.bulx1 < self.x2 - 26 and self.bulx2 < self.x2 - 16):
                    if (self.bulx3 == self.WIDTH + 25):
                        if event.key == pg.K_SEMICOLON:
                            self.bulx3 = self.x2 - 10
                            self.bulx3v = -8
                            pg.mixer.Sound.play(self.gunshot)

            if event.type == pg.KEYUP:
                if (event.key == pg.K_a or event.key == pg.K_d):
                    self.x1v = 0
                if (event.key == pg.K_w or event.key == pg.K_s):
                    self.y1v = 0
                if (event.key == pg.K_LEFT or event.key == pg.K_RIGHT):
                    self.x2v = 0
                if (event.key == pg.K_UP or event.key == pg.K_DOWN):
                    self.y2v = 0
                    

        # ADD VELOCITY TO PLAYER 1
        self.x1 += self.x1v
        self.y1 += self.y1v

        # ---ADD VELOCITY TO BULLETS FOR PLAYER 1---
        # BULLET 1
        if (self.bx1 == -25):
             self.by1 += self.y1v
        self.bx1 += self.bx1v

        # BULLET 2
        if (self.bx2 == -25):
            self.by2 += self.y1v
        self.bx2 += self.bx2v

        # BULLET 3
        if (self.bx3 == -25):
            self.by3 += self.y1v
        self.bx3 += self.bx3v


        # ADD VELOCITY TO PLAYER 2
        self.x2 += self.x2v
        self.y2 += self.y2v

        # ---ADD VELOCITY TO BULLETS FOR PLAYER 2---
        # BULLET 1
        if (self.bulx1 == self.WIDTH + 25):
            self.buly1 += self.y2v
        self.bulx1 += self.bulx1v

        if (self.bulx2 == self.WIDTH + 25):
            self.buly2 += self.y2v
        self.bulx2 += self.bulx2v

        if (self.bulx3 == self.WIDTH + 25):
            self.buly3 += self.y2v
        self.bulx3 += self.bulx3v

        # PLAYER 1 BOUNDARIES
        if (self.y1 < 315):
            self.y1 = 317
        elif (self.y1 > self.HEIGHT - 45):
            self.y1 = self.HEIGHT - 47
        if (self.x1 < 0):
            self.x1 = 2
        elif (self.x1 > self.WIDTH):
            self.x1 = self.WIDTH - 2

        # PLAYER 2 BOUNDARIES
        if (self.y2 < 315):
            self.y2 = 317
            self.buly1 = self.y2 + 20
            self.buly2 = self.y2 + 20
            self.buly3 = self.y2 + 20
        elif (self.y2 > self.HEIGHT - 45):
            self.y2 = self.HEIGHT - 47
        if (self.x2 < 0):
            self.x2 = 2
        elif (self.x2 > self.WIDTH - 45):
            self.x2 = self.WIDTH - 47

    # ---MAKE A FUNCTION THAT CHECKS FOR OBJECT COLLISIONS---
    def collision(self):
        # MAKE PLAYER 1 BULLETS RESET POSITION WHEN OFF-SCREEN
        if (self.bx1 > self.WIDTH):
            self.by1 = self.y1 + 20
            self.bx1v = 0
            self.bx1 = -25
        if (self.bx2 > self.WIDTH):
            self.by2 = self.y1 + 20
            self.bx2v = 0
            self.bx2 = -25
        if (self.bx3 > self.WIDTH):
            self.by3 = self.y1 + 20
            self.bx3v = 0
            self.bx3 = -25

        # ---MAKE PLAYER 1 LOSE HEALTH WHEN HIT BY BULLET---
        # BULLET 1
        if (int(self.buly1) in range(int(self.y1), int(self.y1) + 40) and int(self.bulx1) in range(int(self.x1) + 6, int(self.x1) + 12)):
            self.health1 -= 1
            self.buly1 = self.y2 + 20
            self.bulx1v = 0
            self.bulx1 = self.WIDTH + 25
            # MAKE HEARTS DECREASE AS HEALTH DECREASES
            if (self.health1 == 2):
                self.hy1 = -45
            elif (self.health1 == 1):
                self.hy2 = -45
            elif (self.health1 == 0):
                self.hy3 = -45
                self.running = False
                self.winner = self.font.render("Player 2 WINS!", False, RED)

        # BULLET 2
        if (int(self.buly2) in range(int(self.y1), int(self.y1) + 40) and int(self.bulx2) in range(int(self.x1) + 6, int(self.x1) + 12)):
            self.health1 -= 1
            self.buly2 = self.y2 + 20
            self.bulx2v = 0
            self.bulx2 = self.WIDTH + 25
            self.hy1 = -45
            # MAKE HEARTS DECREASE AS HEALTH DECREASES
            if (self.health1 == 2):
                self.hy1 = -45
            elif (self.health1 == 1):
                self.hy2 = -45
            elif (self.health1 == 0):
                self.hy3 = -45
                self.running = False
                self.winner = self.font.render("Player 2 WINS!", False, RED)
        # BULLET 3
        if (int(self.buly3) in range(int(self.y1), int(self.y1) + 40) and int(self.bulx3) in range(int(self.x1) + 6, int(self.x1) + 12)):
            self.health1 -= 1
            self.buly3 = self.y2 + 20
            self.bulx3v = 0
            self.bulx3 = self.WIDTH + 25
            self.hy1 = -45
            # MAKE HEARTS DECREASE AS HEALTH DECREASES
            if (self.health1 == 2):
                self.hy1 = -45
            elif (self.health1 == 1):
                self.hy2 = -45
            elif (self.health1 == 0):
                self.hy3 = -45
                self.running = False
                self.winner = self.font.render("Player 2 WINS!", False, RED)
            

        # MAKE PLAYER 2 BULLETS RESET POSITION WHEN OFF-SCREEN
        if (self.bulx1 < 0):
            self.buly1 = self.y2 + 20
            self.bulx1v = 0
            self.bulx1 = self.WIDTH + 25
        if (self.bulx2 < 0):
            self.buly2 = self.y2 + 20
            self.bulx2v = 0
            self.bulx2 = self.WIDTH + 25
        if (self.bulx3 < 0):
            self.buly3 = self.y2 + 20
            self.bulx3v = 0
            self.bulx3 = self.WIDTH + 25

        # ---MAKE PLAYER 2 LOSE HEALTH WHEN HIT BY BULLET---
        # BULLET 1
        if (int(self.by1) in range(int(self.y2), int(self.y2) + 40) and int(self.bx1) in range(int(self.x2) - 16, int(self.x2) - 10)):
            self.health2 -= 1
            self.by1 = self.y1 + 20
            self.bx1v = 0
            self.bx1 = -25
            # MAKE HEARTS DECREASE AS HEALTH DECREASES
            if (self.health2 == 2):
                self.hearty1 = -45
            elif (self.health2 == 1):
                self.hearty2 = -45
            elif (self.health2 == 0):
                self.hearty3 = -45
                self.running = False
                self.winner = self.font.render("Player 1 WINS!", False, RED)

        # BULLET 2
        if (int(self.by2) in range(int(self.y2), int(self.y2) + 40) and int(self.bx2) in range(int(self.x2) - 16, int(self.x2) - 10)):
            self.health2 -= 1
            self.by2 = self.y1 + 20
            self.bx2v = 0
            self.bx2 = -25
            # MAKE HEARTS DECREASE AS HEALTH DECREASES
            if (self.health2 == 2):
                self.hearty1 = -45
            elif (self.health2 == 1):
                self.hearty2 = -45
            elif (self.health2 == 0):
                self.hearty3 = -45
                self.running = False
                self.winner = self.font.render("Player 1 WINS!", False, RED)

        # BULLET 3
        if (int(self.by3) in range(int(self.y2), int(self.y2) + 40) and int(self.bx3) in range(int(self.x2) - 16, int(self.x2) - 10)):
            self.health2 -= 1
            self.by3 = self.y1 + 20
            self.bx3v = 0
            self.bx3 = -25
            # MAKE HEARTS DECREASE AS HEALTH DECREASES
            if (self.health2 == 2):
                self.hearty1 = -45
            elif (self.health2 == 1):
                self.hearty2 = -45
            elif (self.health2 == 0):
                self.hearty3 = -45
                self.running = False
                self.winner = self.font.render("Player 1 WINS!", False, RED)
        

    # ---MAKE A FUNCTION THAT DRAWS OBJECTS TO SCREEN---
    def draw(self):
        # DRAW BACKGROUND IMAGE
        self.screen.blit(self.background, [0, 0])

        
        # DRAW PLAYER 1
        self.screen.blit(self.player1, [self.x1, self.y1])       
        # DRAW PLAYER 1 BULLET 1
        self.screen.blit(self.bullet1, [self.bx1, self.by1])
        # DRAW PLAYER 1 BULLET 2
        self.screen.blit(self.bullet2, [self.bx2, self.by2])
        # DRAW PLAYER 1 BULLET 3
        self.screen.blit(self.bullet3, [self.bx3, self.by3])


        # DRAW PLAYER 2
        self.screen.blit(self.player2, [self.x2, self.y2])
        # DRAW PLAYER 2 BULLET 1
        self.screen.blit(self.bul1, [self.bulx1, self.buly1])
        # DRAW PLAYER 2 BULLET 2
        self.screen.blit(self.bul2, [self.bulx2, self.buly2])
        # DRAW PLAYER 2 BULLET 3
        self.screen.blit(self.bul3, [self.bulx3, self.buly3])

        # DRAW PLAYER 1 HEARTS
        self.screen.blit(self.heart1, [self.WIDTH / 2 - 150, self.hy1])
        self.screen.blit(self.heart2, [self.WIDTH / 2 - 195, self.hy2])
        self.screen.blit(self.heart3, [self.WIDTH / 2 - 240, self.hy3])

        # DRAW PLAYER 2 HEARTS
        self.screen.blit(self.h1, [self.WIDTH / 2 + 150, self.hearty1])
        self.screen.blit(self.h2, [self.WIDTH / 2 + 195, self.hearty2])
        self.screen.blit(self.h3, [self.WIDTH / 2 + 240, self.hearty3])
        

    # MAKE A FUNCTION THAT RENDERS DRAWN OBJECTS TO SCREEN
    def render(self):
        pg.display.update()
        self.clock.tick(self.FPS)

# ASSIGN WINDOW CLASS TO VARIABLE
Game = Window()

def START_SCREEN():
    if __name__ == '__main__':
        Game.start_window()
        Game.START()
        LOOP()

def LOOP():
    while Game.running:
        Game.start_window()
        Game.event_handling()
        Game.collision()
        Game.draw()
        Game.render()
    START_SCREEN()

START_SCREEN()
