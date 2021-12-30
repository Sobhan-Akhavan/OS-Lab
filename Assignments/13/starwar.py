import math
import random
from sys import is_finalizing
import arcade
from arcade.sprite_list.spatial_hash import check_for_collision
import time
from arcade.key import E, END, F, W
import os
os.chdir("/home/sobhan/VisualStudioCode/OS-Lab/Assignments/13")
import threading

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

def Random_arrive_enemy():
    return random.randint(4,6)


class Ship(arcade.Sprite):

    def __init__(self):
       super().__init__(':resources:images/space_shooter/playerShip1_blue.png')
       self.center_x = SCREEN_WIDTH // 2
       self.center_y = 32
       self.width = 40
       self.height = 18
       self.angle = 0
       self.change_angle = 0
       self.speed = 6
       self.change_x = 0
       self.change_y = 0
       self.bullet_list = []
       self.score = 0
       self.health = 3
       
    def charkhesh(self):
        self.angle += self.change_angle * self.speed

    def move(self):
        self.center_x += self.change_x * self.speed
        self.center_y += self.change_y * self.speed

    def fire(self):
       self.bullet_list.append(Bullet(self))
       arcade.play_sound(arcade.sound.Sound(':resources:sounds/upgrade2.wav'))
    

class Enemy(arcade.Sprite):

    def __init__(self, s):
       super().__init__(':resources:images/space_shooter/playerShip1_green.png')
       self.center_x = random.randint(1, SCREEN_WIDTH - 1)
       self.center_y = SCREEN_HEIGHT + 2
       self.speed = s
       self.angle = 180
       self.width = 50
       self.height = 40
       
    def move(self):
        self.center_y -= self.speed 


class Bullet(arcade.Sprite):

     def __init__(self, host):
       super().__init__(':resources:images/space_shooter/laserRed01.png')
       self.center_x = host.center_x
       self.center_y = host.center_y
       self.speed = 7
       self.angle = host.angle
      
     def move(self):
        angle_radious = math.radians(self.angle)
        self.center_x -= self.speed * math.sin(angle_radious)
        self.center_y += self.speed * math.cos(angle_radious)

class Game(arcade.Window):

    def __init__(self):

        super().__init__(SCREEN_WIDTH , SCREEN_HEIGHT , 'Star War Game')
        arcade.set_background_color(arcade.color.BLACK)
        self.background_image=arcade.load_texture(':resources:images/backgrounds/stars.png')
        self.me=Ship()
        self.enemy_list = []
        self.num_enemy = 0
        self.thread = threading.Thread(target=self.add_enemy)
        self.thread.start()
        self.thread_disrupt = False
        self.start_time = time.time()
        self.game_over = False

    def add_enemy(self):
        speed = 2
        while True:
            for enemy in self.enemy_list:
                enemy.speed += speed
            speed += 0.1
            self.enemy_list.append(Enemy(speed))
            time.sleep(random.randint(4, 6))
            if self.thread_disrupt:
                break

    def on_draw(self):
        arcade.start_render()
        if self.me.health <= 0:
            arcade.set_background_color(arcade.color.GRANNY_SMITH_APPLE)
            arcade.draw_text('Game Over! Sorry :(', 30, SCREEN_WIDTH // 2, arcade.color.PURPLE, 30)
        else:
            arcade.draw_lrwh_rectangle_textured(0 , 0, SCREEN_WIDTH, SCREEN_WIDTH,self.background_image)
            self.me.draw()
        for tir in self.me.bullet_list:
                tir.draw()

        for doshman in self.enemy_list:
            doshman.draw()

        for health in range(self.me.health):
            health_image = arcade.load_texture('health.png')
            arcade.draw_lrwh_rectangle_textured(5 + health * 21 , 12 , 22 , 22 , health_image)
        arcade.draw_text(f'Score= {self.me.score}', 680, 18 , arcade.color.WHITE_SMOKE , 18)

    def on_update(self, delta_time):
        #self.end_time = time.time()
        #time_doshman = random.randrange(2,8,2)
        #if self.end_time - self.start_time >= time_doshman:
        #  self.num_enemy += 1
        #  self.enemy_list.append(Enemy(3 + self.num_enemy//10))
        #  self.start_time = time.time()

        self.me.move()
        self.me.charkhesh()
        
        for tir in self.me.bullet_list:
            tir.move()

        for doshman in self.enemy_list:
            doshman.move()

        for doshman in self.enemy_list:
            for tir in self.me.bullet_list:

                if check_for_collision(doshman , tir):
                    arcade.play_sound(arcade.sound.Sound(':resources:sounds/explosion2.wav'))
                    self.me.bullet_list.remove(tir)
                    self.enemy_list.remove(doshman)
                    self.me.score += 1

        for tir in self.me.bullet_list:
            if tir.center_y >= SCREEN_HEIGHT or SCREEN_WIDTH <= tir.center_x <=0 or tir.center_y <= 0:
                self.me.bullet_list.remove(tir)

        for doshman in self.enemy_list:
            if doshman.center_y <= 0:
                self.enemy_list.remove(doshman)
                self.me.health -= 1

        

    def on_key_press(self, key, modifiers: int):
        if key == arcade.key.DOWN:
            self.me.change_y = -1

        elif key == arcade.key.UP:
            self.me.change_y = 1

        elif key == arcade.key.RIGHT:
            self.me.change_x = +1

        elif key == arcade.key.LEFT:
            self.me.change_x = -1

        if key == arcade.key.D:
            self.me.change_angle = -1

        if key == arcade.key.A:
            self.me.change_angle = 1
        
        elif key == arcade.key.SPACE:
            self.me.fire()   

    def on_key_release(self, symbol: int, modifiers: int):
        return super().on_key_release(symbol, modifiers)

    def on_key_release(self, key, modifiers: int):
        self.me.change_angle = 0
        self.me.change_x = 0
        self.me.change_y = 0


game = Game()
arcade.run()