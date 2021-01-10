import pygame
import time
import math
import random
import os

fps = 20
pygame.init()

# Current Directory
BASE_DIR = os.getcwd()
SurviveImages = os.path.join(BASE_DIR,"SurviveImages")
SurviveAudio = os.path.join(BASE_DIR,"SurviveAudio")

# Window
WIDTH = 1440
HEIGHT = 900
gamewindow = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Survive')

#Title Screen
title_screen = pygame.image.load(os.path.join(SurviveImages, "titlescreen.png"))

# Main Character Movement Images
# Down
standstilldown = pygame.image.load(os.path.join(SurviveImages, "standstilldown.png"))
down1 = pygame.image.load(os.path.join(SurviveImages, "downwalk1.png"))
down2 = pygame.image.load(os.path.join(SurviveImages, "downwalk2.png"))
# Up
standstillup = pygame.image.load(os.path.join(SurviveImages, "standstillup.png"))
upwalk1 = pygame.image.load(os.path.join(SurviveImages, "upwalk1.png"))
upwalk2 = pygame.image.load(os.path.join(SurviveImages, "upwalk2.png"))
# Right
standstill_right = pygame.image.load(os.path.join(SurviveImages, "standstill_right.png"))
rightwalk1 = pygame.image.load(os.path.join(SurviveImages, "rightwalk1.png"))
rightwalk2 = pygame.image.load(os.path.join(SurviveImages, "rightwalk2.png"))
# Left
standstill_left = pygame.image.load(os.path.join(SurviveImages, "standstill_left.png"))
leftwalk1 = pygame.image.load(os.path.join(SurviveImages, "leftwalk1.png"))
leftwalk2 = pygame.image.load(os.path.join(SurviveImages, "leftwalk2.png"))
leftwalk3 = pygame.image.load(os.path.join(SurviveImages, "leftwalk3.png"))

# Movement Image Patterns
walk_down = [down1, down2, down1, down2, down1, down2, down1, down2, down1, down2]
walk_up = [upwalk1, upwalk2, upwalk1, upwalk2, upwalk1, upwalk2, upwalk1, upwalk2, upwalk1]
walk_left = [leftwalk1, leftwalk2, leftwalk3, leftwalk1, leftwalk2, leftwalk3, leftwalk1, leftwalk2, leftwalk3]
walk_right = [rightwalk1, rightwalk2, rightwalk1, rightwalk2, rightwalk1, rightwalk2, rightwalk1, rightwalk2]

# Punching
left_punch = pygame.image.load(os.path.join(SurviveImages, "punchleft.png"))
right_punch = pygame.image.load(os.path.join(SurviveImages, "punchright.png"))
down_punch = pygame.image.load(os.path.join(SurviveImages, "punchdown.png"))
up_punch = pygame.image.load(os.path.join(SurviveImages, "punchup.png"))

#Shooting
left_shoot = pygame.image.load(os.path.join(SurviveImages, "leftshoot.png"))
right_shoot = pygame.image.load(os.path.join(SurviveImages, "rightshoot.png"))
down_shoot = pygame.image.load(os.path.join(SurviveImages, "downshoot.png"))
up_shoot = pygame.image.load(os.path.join(SurviveImages, "upshoot.png"))

# Swing Sword
sword_left = pygame.image.load(os.path.join(SurviveImages, "sword_left.png"))
sword_right = pygame.image.load(os.path.join(SurviveImages, "sword_right.png"))
sword_up = pygame.image.load(os.path.join(SurviveImages, "sword_up.png"))
sword_down = pygame.image.load(os.path.join(SurviveImages, "sword_down.png"))

# Death
death1 = pygame.image.load(os.path.join(SurviveImages, "death1.png"))

# Car Images
car_right = pygame.image.load(os.path.join(SurviveImages, "car_right.png"))
car_left = pygame.image.load(os.path.join(SurviveImages, "car_left.png"))
car_up = pygame.image.load(os.path.join(SurviveImages, "car_up.png"))
car_down = pygame.image.load(os.path.join(SurviveImages, "car_down.png"))

# Enemy Images
# Wolf
smallwolf = pygame.image.load(os.path.join(SurviveImages, "smallwolf.png"))
smallwolf_death = pygame.image.load(os.path.join(SurviveImages, "smallwolf_death.png"))
bigwolf = pygame.image.load(os.path.join(SurviveImages, "bigwolf.png"))
bigwolf_death = pygame.image.load(os.path.join(SurviveImages, "bigwolf_death.png"))

# Spider
small_spider = pygame.image.load(os.path.join(SurviveImages, "small_spider.png"))
smallspider_death = pygame.image.load(os.path.join(SurviveImages, "smallspider_death.png"))
big_spider = pygame.image.load(os.path.join(SurviveImages, "big_spider.png"))
bigspider_death = pygame.image.load(os.path.join(SurviveImages, "bigspider_death.png"))

# Rats
rat_left = pygame.image.load(os.path.join(SurviveImages, "rat_left.png"))
rat_right = pygame.image.load(os.path.join(SurviveImages, "rat_right.png"))
rat_death = pygame.image.load(os.path.join(SurviveImages, "rat_death.png"))

#Boss
boss1 = pygame.image.load(os.path.join(SurviveImages, "boss1.png"))

# Bats
bat_right = pygame.image.load(os.path.join(SurviveImages, "bat_right.png"))
bat_left = pygame.image.load(os.path.join(SurviveImages, "bat_left.png"))
bat_death = pygame.image.load(os.path.join(SurviveImages, "bat_death.png"))

# Wizards
wizard_left = pygame.image.load(os.path.join(SurviveImages, "wizard_left.png"))
wizard_right = pygame.image.load(os.path.join(SurviveImages, "wizard_right.png"))
wizard_death = pygame.image.load(os.path.join(SurviveImages, "wizard_death.png"))

# Goblin
goblin_img = pygame.image.load(os.path.join(SurviveImages, "goblin.png"))
goblin_death = pygame.image.load(os.path.join(SurviveImages, "goblin_death.png"))

# Croc
right_croc = pygame.image.load(os.path.join(SurviveImages, "right_croc.png"))

# Knight
knight_right = pygame.image.load(os.path.join(SurviveImages, "knight_right.png"))
knight_left = pygame.image.load(os.path.join(SurviveImages, "knight_left.png"))
knight_death = pygame.image.load(os.path.join(SurviveImages, "knight_death.png"))

# Deer
deer_small = pygame.image.load(os.path.join(SurviveImages, "deer_small.png"))
deer_small_death = pygame.image.load(os.path.join(SurviveImages, "deer_small_death.png"))
deer_big_left = pygame.image.load(os.path.join(SurviveImages, "deer_big_left.png"))
deer_big_right = pygame.image.load(os.path.join(SurviveImages, "deer_big_right.png"))
deer_big_death = pygame.image.load(os.path.join(SurviveImages, "deer_big_death.png"))

# Dog Man
dog_man = pygame.image.load(os.path.join(SurviveImages, "dog_man.png"))
dog_man_death = pygame.image.load(os.path.join(SurviveImages, "dog_man_death.png"))

# Police
police_gun = pygame.image.load(os.path.join(SurviveImages, "police_gun.png"))
police_stick = pygame.image.load(os.path.join(SurviveImages, "police_stick.png"))

# Bear
bear = pygame.image.load(os.path.join(SurviveImages, "bear.png"))
bear_death = pygame.image.load(os.path.join(SurviveImages, "bear_death.png"))

# Chicken
chicken = pygame.image.load(os.path.join(SurviveImages, "chicken.png"))
chicken_death_left = pygame.image.load(os.path.join(SurviveImages, "chicken_death_left.png"))
chicken_death_right = pygame.image.load(os.path.join(SurviveImages, "chicken_death_right.png"))

# Rock
rock = pygame.image.load(os.path.join(SurviveImages, "rock.png"))

# Lazer
lazer_img = pygame.image.load(os.path.join(SurviveImages, "lazer.png"))

# Son
son_down = pygame.image.load(os.path.join(SurviveImages, "sondown.png"))
son_left = pygame.image.load(os.path.join(SurviveImages, "sonleft.png"))
son_right = pygame.image.load(os.path.join(SurviveImages, "sonright.png"))
son_up = pygame.image.load(os.path.join(SurviveImages, "sonup.png"))

# Weapons On Ground
sword_ground = pygame.image.load(os.path.join(SurviveImages, "sword_ground.png"))
gun_ground = pygame.image.load(os.path.join(SurviveImages, "gun_ground.png"))


# Sounds
punch_sound = pygame.mixer.Sound(os.path.join(SurviveAudio, "Smack.wav"))
punch_sound.set_volume(0.2)

main_hit = pygame.mixer.Sound(os.path.join(SurviveAudio, "main_hit.wav"))
main_hit.set_volume(0.04)

gun_sound = pygame.mixer.Sound(os.path.join(SurviveAudio, "gun.wav"))
gun_sound.set_volume(0.1)

background_music = pygame.mixer.music.load(os.path.join(SurviveAudio, "gamemusic.wav"))
pygame.mixer.music.set_volume(0.075)

# Enemy Sounds
death_sound = pygame.mixer.Sound(os.path.join(SurviveAudio, "deathsound.wav"))
death_sound.set_volume(0.15)
clock = pygame.time.Clock()
rock_list = []
chicken_list = []
son_list = []
time_list = []
punch_list = []
sword_list = []


# Main Character
class MainCharacter():
    def __init__(self, x, y, direction, width, height, left=False, right=False,
                 up=False, down=True, standing=True, walk_count=0):
        self.x = x
        self.y = y
        self.direction = direction
        self.width = width
        self.height = height
        self.left = left
        self.right = right
        self.up = up
        self.down = down
        self.standing = standing
        self.walk_count = walk_count
        self.can_move = True
        self.has_punch = True
        self.has_sword = False
        self.swing_sword = True
        self.has_gun = True
        self.current_room = "room1"
        self.alive = True
        self.hitbox = (self.x + 40, self.y + 15, 50, 95)
        self.current_hp = 100
        self.full_hp = 100
        self.xp = 0
        self.xp_needed = 30
        self.level = 1
        self.cooldown = 0
        self.objective2 = False
        self.objective3 = False
        self.objective4 = False
        self.objective5 = False
        self.objective6 = False
        self.objective7 = False
        self.objective8 = False
        self.objective9 = False
        self.objective10 = False
        self.objective11 = False
        self.bridge = 0
        self.question = 0
        self.wrong = 0
        self.son_location = (self.x + self.width//2 - 15, self.y + 60)
        self.has_son = False
        self.found_son = False
        self.in_car = False
        self.speed = 10
        self.has_key = False
        self.has_banana = False
        self.hog = 'hanging'
        self.damaged_door = 0
        self.banana_tree = 0
        self.punch_dmg = 3
        self.sword_dmg = 3
        self.gun_dmg = 60
        self.cave = 'closed'
        self.has_chicken = False
        self.found_chicken = False
        self.chicken_room = 'room33'
        self.chicken_location = (self.x + self.width//2 - 15, self.y + 60)
        self.has_rock = False
        self.found_rock = False
        self.rock_location = (self.x + self.width//2 - 15, self.y + 60)


    # Enter New room
    def enter_new_room(self): # 1440, 900
        if self.current_room == 'room1':
            if self.x < 435:
                self.x = 435
            elif self.x > 840:
                self.x = 835
            elif self.y < 0:
                self.y = 0
            elif self.y > 775:
                self.current_room = 'room2'
                self.x = 210
                self.y = 465
        
        elif self.current_room == 'room2':
            if self.y < 440:
                self.y = 440
                
            elif self.x < -39:
                self.x = -39
                
            elif self.x > 1350:
                self.x = 1350
                
            elif self.y > 775 and self.objective2 == True:
                self.y -= 800
                self.current_room = 'room3'
                
            elif self.y > 775 and self.objective2 == False:
                self.y = 775
              
        elif self.current_room == 'room3':
            if self.y < -15:
                self.y = -15
                
            elif self.x < 230 and self.y < 586:
                self.x = 230
                
            elif self.x > 229 and self.x < 400 and self.y > 585:
                self.y = 585
                
            elif self.y > 585 and self.x < 415:
                self.x = 415

            elif self.x > 1100 and self.y > 300:
                self.x = 1100
                
            elif self.x < 1101 and self.y < 390 and self.x > 990:
                self.y = 390

            elif self.x > 980 and self.y < 390:
                self.x = 980

            elif self.y > 775 and self.objective3 == False:
                self.y = 775
            elif self.y > 775 and self.objective3 == True:
                self.current_room = 'room4'
                self.y -= 800

        elif self.current_room == 'room4':
            if self.y < -15:
                self.y = -15
                
            elif self.y > 775:
                self.y = 775
                
            elif self.x < -49:
                self.current_room = 'room5'
                self.x += 1400
            
            elif self.x > 1360:
                self.current_room = 'room6'
                self.x -= 1400
                
        elif self.current_room == 'room5':
            if self.y < -15:
                self.y = -15
                
            elif self.x > 1360:
                self.x -= 1400
                self.current_room = 'room4'
                
            elif self.x < -49:
                self.x += 1400
                self.current_room = 'room8'
                
        elif self.current_room == 'room6':
            if self.y < -15:
                self.y = -15
                
            if self.x < -49:
                self.current_room = 'room4'
                self.x += 1400

            if self.x > 1360:
                self.current_room = 'room7'
                self.x -= 1400

        elif self.current_room == 'room7':
            if self.x < -15:
                self.x = -15
                
            elif self.y < 310:
                self.y = 310

            elif self.x > 1350:
                self.x = 1350

        elif self.current_room == 'room8':
            if self.y < -15 and self.x > 660:
                self.y = -15

            elif self.y < -15 and self.x < 490:
                self.y = -15

            elif self.x < -35:
                self.x = -35
                
            elif self.x > 1345:
                self.x = 1345

            elif self.y < - 40:
                self.y += 830
                self.current_room = 'room9'
                
        elif self.current_room == 'room9':
            if self.y > 780: 
                self.y = 780

            elif self.x < -30:
                self.x = -30

            elif self.x > 1350:
                self.x = 1350

            elif self.y < -30 and self.x < 490 or self.y < -30 and self.x > 665:
                self.y = -30

            elif self.y < -30 and self.objective4 == False:
                self.y = -30

            elif self.y < -30 and self.objective4 == True:
                self.y += 820
                self.current_room = 'room10'
                

        elif self.current_room == 'room10':
                    
            if self.y > 780:
                self.y = 780

            elif self.y < -20:
                self.y = -20

            elif self.x < -45:
                self.x = -45

            elif self.x > 1345 and self.objective5 == True and \
                 self.y < 223 and self.y > 69:
                self.x -= 1375
                self.current_room = 'room11'
                
            elif self.x > 1350 and self.objective5 == False and \
                 self.y < 223 and self.y > 69:
                self.x = 1350

            elif self.x > 1350:
                self.x = 1350
                
        elif self.current_room == 'room11':
 
            if self.x < -45:
                self.x = -45

            elif self.y < -20:
                self.y = -20

            elif self.y >= 469 and self.bridge != 4:
                self.y = 465

            elif self.y > 780:
                self.y = 780

            elif self.x > 1356 and self.y < 708:
                self.x = 1356

            elif self.x > 1360:
                self.x -= 1415
                self.current_room = 'room12'
                
        elif self.current_room == 'room12':
            if self.x < -35:
                self.x = -35
            
            elif self.y < - 40:
                self.y += 835
                self.current_room = 'room15'
                
            elif self.x > 1360:
                self.x -= 1400
                self.current_room = 'room13'
                
            elif self.y >= 763:
                self.y = 763

        elif self.current_room == 'room13':
            if self.x < -49:
                self.x += 1400
                self.current_room = 'room12'
                
            elif self.y < - 40:
                self.y += 835
                self.current_room = 'room14'
                
            elif self.x > 1323:
                self.x = 1323
                
            elif self.y >= 763:
                self.y = 763

                
        elif self.current_room == 'room14':
            if self.x > 1323:
                self.x = 1323
                
            elif self.x < -49:
                self.x += 1400
                self.current_room = 'room15'
                
            elif self.y < 415:
                self.y = 415

            elif self.y >= 800:
                self.current_room = 'room13'
                self.y -= 820

            elif self.x >= 222 and self.y <= 429 and self.x <= 393:
                self.current_room = 'room16'
                self.y = 775
                

        elif self.current_room == 'room15':
            if self.y >= 800 and self.has_key == False:
                self.current_room = 'room12'
                self.y -= 820
                
            if self.y >= 780 and self.has_key == True:
                self.y = 780
                
            if self.x < -35:
                self.x = -35

            if self.x > 1360 and self.has_key == False:
                self.current_room = 'room14'
                self.x -= 1400
                
            if self.x > 1360 and self.has_key == True:
                self.x = 1360

            if self.y < 420:
                self.y = 420

            if self.x >= 1030 and self.x <= 1050 and self.y <= 429 and self.has_key == True:
                self.current_room = 'room17'
                self.has_key = False
                self.x = 663
                self.y = 748
                
        elif self.current_room == 'room16':
            if self.x < -35:
                self.x = -35

            if self.y <= 400:
                self.y = 400

            if self.y >= 835:
                self.current_room = 'room14'
                self.x = 310
                self.y = 475

            if self.x > 1360 and self.objective6 == False:
                self.x = 1360

            if self.x > 1360 and self.objective6 == True:
                self.current_room = 'room7'
                self.x -= 1400
                self.y = 600

        elif self.current_room == 'room17':
            if self.x < -35:
                self.x = -35
                
            elif self.y < -20:
                self.y = -20

            elif self.y > 784:
                self.y = 784

            elif self.x > 1360:
                self.x = 1360

            elif self.x <= -20 and self.y <= 586 and self.y >= 514 and\
               self.has_key == True:
                self.current_room = 'room18'
                self.x = 1343

        elif self.current_room == 'room18':
            if self.x > 1360:
                self.x = 1360
                
            elif self.y < 442:
                self.y = 442

            elif self.y > 784:
                self.y = 784

            elif self.x < -35:
                self.x = -35

            elif self.x >= 6 and self.x <= 42 and self.y <= 442 and self.up == True and\
                 enemy63.visible == False and enemy64.visible == False:
                self.current_room = 'room19'
                self.x = 604
                self.y = 748
                self.current_hp = self.full_hp
                self.can_move = False
                self.standing = True

        
        elif self.current_room == 'room19':
            if self.x < -35:
                self.x = -35
                
            elif self.y > 784:
                self.y = 784

            elif self.x > 1360:
                self.x = 1360
                
            elif self.y < -20:
                self.y = -20

            elif self.x >= 1257 and self.x <= 1320 and self.y <= 20 and\
                 self.has_son == True and self.up == True:
                self.current_room = 'room20'
                self.has_key = False
                self.has_gun = False
                self.x = 1
                self.y = 757
                
        elif self.current_room == 'room20':
            if self.x < -35:
                self.x = -35
                
            if self.y > 784:
                self.y = 784
                
            if self.x > 1360:
                self.x = 1360

            if self.y < 352:
                self.y = 352

            if self.x >= 667 and self.x <= 712 and self.y <= 352 and\
               self.has_key == True and self.up == True and self.damaged_door == 5 and\
               self.has_son == True and self.has_gun == True and enemy65.visible == False:
                self.current_room = 'room21'
                self.x = 1
                self.y = 757

        elif self.current_room == 'room21':
            if self.y > 739:
                self.y = 739
                
            elif self.x > 1200:
                self.x = 1200

            elif self.x < -35:
                self.x = -35

            elif self.y < -15 and self.objective7 == False:
                self.y = -15

            elif self.y < -15 and self.objective7 == True and self.has_son == False:
                self.y = -15

            elif self.y < -15 and self.objective7 == True and self.has_son == True:
                self.y += 830
                self.current_room = 'room22'


        elif self.current_room == 'room22':
            if self.x < 0:
                self.x = 0

            elif self.y < 0:
                self.y = 0

            elif self.y > 800:
                self.y = 800

            elif self.x > 1230 and self.in_car == False:
                self.x = 1230

            elif self.x > 1409 and self.in_car == True:
                self.x -= 1575
                self.current_room = 'room23'

            
        elif self.current_room == 'room23':
            if self.x < -71:
                self.x = -71

            elif self.y < 0:
                self.y = 0

            elif self.y > 800:
                self.y = 800

            elif self.x > 1409:
                self.x -= 1575
                self.current_room = 'room24'


        elif self.current_room == 'room24':
            if self.x < -71:
                self.x = -71
                
            elif self.y < 0:
                self.y = 0
                
            elif self.y > 800:
                self.y = 800

            elif self.x > 1409:
                self.x -= 1575
                self.current_room = 'room25'
                

        elif self.current_room == 'room25':
            if self.x < -71:
                self.x = -71

            elif self.y < 0:
                self.y = 0

            elif self.y > 800:
                self.y = 800

            elif self.x > 1409:
                self.x -= 1575
                self.current_room = 'room26'


        elif self.current_room == 'room26':
            if self.x < -71:
                self.x = -71

            elif self.y < 0:
                self.y = 0

            elif self.x > 1349:
                self.x = 1349

            elif self.y > 800 and self.objective8 == False:
                self.y = 800

            elif self.y > 800 and self.objective8 == True:
                self.y -= 850
                self.current_room = 'room27'


        elif self.current_room == 'room27':
            if self.y < -45:
                self.y = -45

            elif self.x < -71:
                self.x = -71
                
            elif self.x > 1349:
                self.x = 1349
                
            elif self.y > 800:
                self.y -= 850
                self.current_room = 'room28'

        elif self.current_room == 'room28':
            if self.y < -45:
                self.y = -45

            elif self.x < -71:
                self.x = -71

            elif self.x > 1349:
                self.x = 1349

            elif self.y > 800:
                self.y -= 850
                self.current_room = 'room29'


        elif self.current_room == 'room29':
            
            if self.y < -45:
                self.y = -45

            elif self.x < -71:
                self.x = -71

            elif self.y > 800:
                self.y = 800

            elif self.x > 1349 and self.y < 510:
                self.x = 1349

            elif self.x > 1349 and self.y > 695:
                self.x = 1349

            elif self.x > 1409:
                self.x -= 1575
                self.current_room = 'room30'
                
        elif self.current_room == 'room30':
            if self.y < 514:
                self.y = 514

            elif self.y > 685:
                self.y = 685

            elif self.x < -71:
                self.x = -71

            elif self.x > 1409:
                self.current_room = 'room31'

        elif self.current_room == 'room31':

            if self.x < -39:
                self.x = -39

            elif self.x > 1350:
                self.x = 1350

            elif self.y < 0:
                self.y = 0

            elif self.y > 780 and enemy121.hp <= 0: 
                self.y = 780

            elif self.y > 780 and enemy121.hp > 0 and self.has_son == False:
                self.y = 780

            elif self.y > 780 and enemy121.hp > 0 and self.has_son == True:
                self.y -= 800
                self.current_room = 'room32'

        elif self.current_room == 'room32':
            if self.x < 250:
                self.x = 250
                
            elif self.y < -15:
                self.y = -15

            elif self.x > 1030:
                self.x = 1030

            elif self.y > 780 and self.objective9 == False:
                self.y = 780
                
            elif self.y > 780 and self.objective9 == True and self.has_son == False:
                self.y = 780
  
            elif self.y > 780 and self.objective9 == True and self.has_son == True:
                self.y -= 800
                self.current_room = 'room33'

        elif self.current_room == 'room33':
            if self.y > 487:
                self.y = 487

            if self.y < - 10:
                self.y = -10

            elif self.x > 865:
                self.x = 865

            elif self.x < -49 and self.has_son == False:
                self.x = -49
    
            elif self.x < -49 and self.has_son == True:
                self.x += 1400
                self.current_room = 'room34'

                
        elif self.current_room == 'room34':

            if self.x > 1360 and self.has_son == False:
                self.x = 1360

            elif self.x > 1360 and self.has_rock == True:
                self.x = 1360

            elif self.x > 1360 and self.has_son == True:
                self.x -= 1400
                self.current_room = 'room33'
                
            elif self.y > 487:
                self.y = 487

            elif self.x < -44:
                self.x = -44

            elif self.cave == 'open' and self.x <= 676 and self.x >= 492 and self.y < 110 and\
                 self.up == True and self.has_son == True and enemy135.visible == False and\
                 enemy136.visible == False and self.has_rock == False and self.has_chicken == True:
                self.x = 591
                self.y = 775
                self.current_room = 'room35'
                self.chicken_room = 'room35'

            elif self.y < 108:
                self.y = 108


        elif self.current_room == 'room35':

            if self.y > 780:
                self.y = 780

            elif self.x > 1360:
                self.x = 1360

            elif self.y < 325:
                self.y = 325

            elif self.x < -49 and self.has_son == False:
                self.x = -49

            elif self.x < -49 and self.objective10 == False:
                self.x = -49

            elif self.x < -49 and self.objective10 == True and self.has_son == True:
                self.x += 1400
                self.current_room = 'room36'


        elif self.current_room == 'room36':
            if self.x > 1350:
                self.x = 1350

            elif self.y < 325:
                self.y = 325


             
    def load_room(self):
        # Room 1
        if self.current_room == 'room1':
            gamewindow.blit( pygame.image.load( os.path.join(SurviveImages, "room1.png")), (0,0))
            font20 = pygame.font.Font(None, 20)
            text1 = font20.render('How did I get here?', 1, (255,255,255))
            text2 = font.render("Objective: Find A Way Out", 1, (255,255,255))
            gamewindow.blit(text1, (self.x, self.y-10))
            gamewindow.blit(text2, (1100, 10))
            
        # Room 2    
        elif self.current_room == 'room2':
            gamewindow.blit( pygame.image.load(os.path.join(SurviveImages, "room2.png")), (0,0))
            font20 = pygame.font.Font(None, 20)
            font30 = pygame.font.Font(None, 30)
            text1 = font30.render('Its a baby wolf! Wheres his parents?', 1, (255,255,255))
            text4 = font30.render('Objective: Kill the baby wolf', 1, (255,255,255))
            text2 = font30.render('They saw me kill him!', 1, (255,255,255))
            text6 = font30.render('Objective: Defend Yourself', 1, (255,255,255))
            text3 = font30.render('That was close. I need to be more careful out here.', 1, (255,255,255))
            text7 = font20.render("Press 'D' to PUNCH", 1, (255,255,255))

            if enemy2.hp <= 0:
                enemy2.visible = False
                gamewindow.blit(bigwolf_death, (enemy2.x-32 , enemy2.y+32))    

            if enemy3.hp <= 0:
                enemy3.visible = False
                gamewindow.blit(bigwolf_death, (enemy3.x-32 , enemy3.y+32)) 

            if enemy4.hp <= 0:
                enemy4.visible = False
                gamewindow.blit(bigwolf_death, (enemy4.x-32 , enemy4.y+32))
                
            if enemy5.hp <= 0:
                enemy5.visible = False
                gamewindow.blit(bigwolf_death, (enemy5.x-32 , enemy5.y+32))
     
            if enemy1.hp > 0:
                enemy1.visible = True
                enemy1.draw(gamewindow)
                gamewindow.blit(text1, (1050, 20))
                gamewindow.blit(text4, (1100, 50))
                gamewindow.blit(text7, (self.x, self.y))
                
            if enemy1.hp <= 0:
                enemy1.visible = False
                gamewindow.blit(smallwolf_death, (enemy1.x-32 , enemy1.y+32))
             
                if enemy2.hp > 0:
                    enemy2.visible = True
                    enemy2.draw(gamewindow, self)
                if enemy3.hp > 0:
                    enemy3.visible = True
                    enemy3.draw(gamewindow, self)
                if enemy4.hp > 0:
                    enemy4.visible = True
                    enemy4.draw(gamewindow, self)
                if enemy5.hp > 0:
                    enemy5.visible = True
                    enemy5.draw(gamewindow, self)
                       

      
            if enemy2.visible == True or enemy3.visible == True or enemy4.visible == True or enemy5.visible == True:
                gamewindow.blit(text2, (1100, 20))
                gamewindow.blit(text6, (1050, 50))          
                
            if enemy1.visible == False and enemy2.visible == False and \
                enemy3.visible == False and enemy4.visible == False and \
                enemy5.visible == False:
                gamewindow.blit(text3, (800, 20))
                self.objective2 = True

                
        # Room 3
        elif self.current_room == 'room3':
            text7 = font.render('Why SPIDERS! Just WHY!', 1, (255,255,255))
            text8 = font.render('Objective: Kill all the spiders.', 1, (255,255,255))
            text9 = font.render('There is no way I am going survive. I cant fight like this forever.', 1, (255,255,255))
            gamewindow.blit( pygame.image.load(os.path.join(SurviveImages, "room3.png")), (0,0))

            if enemy6.hp <= 0:
                enemy6.visible = False
                gamewindow.blit(smallspider_death, (enemy6.x-0 , enemy6.y+20))
            if enemy7.hp <= 0:
                enemy7.visible = False
                gamewindow.blit(smallspider_death, (enemy7.x-0 , enemy7.y+20))
            if enemy8.hp <= 0:
                enemy8.visible = False
                gamewindow.blit(smallspider_death, (enemy8.x-0 , enemy8.y+20))            
            if enemy9.hp <= 0:
                enemy9.visible = False
                gamewindow.blit(smallspider_death, (enemy9.x-0 , enemy9.y+20))        
            if enemy10.hp <= 0:
                enemy10.visible = False
                gamewindow.blit(smallspider_death, (enemy10.x-0 , enemy10.y+20))
            if enemy11.hp <= 0:
                enemy11.visible = False
                gamewindow.blit(smallspider_death, (enemy11.x-0 , enemy11.y+20))
            if enemy12.hp <= 0:
                enemy12.visible = False
                gamewindow.blit(smallspider_death, (enemy12.x-0 , enemy12.y+20))
            if enemy13.hp <= 0:
                enemy13.visible = False
                gamewindow.blit(smallspider_death, (enemy13.x-0 , enemy13.y+20))
            if enemy14.hp <= 0:
                enemy14.visible = False
                gamewindow.blit(bigspider_death, (enemy14.x-0 , enemy14.y+20))
            if enemy15.hp <= 0:
                enemy15.visible = False
                gamewindow.blit(smallspider_death, (enemy15.x-0 , enemy15.y+20))            
            if enemy16.hp <= 0:
                enemy16.visible = False
                gamewindow.blit(smallspider_death, (enemy16.x-0 , enemy16.y+20))
            if enemy17.hp <= 0:
                enemy17.visible = False
                gamewindow.blit(smallspider_death, (enemy17.x-0 , enemy17.y+20))
            if enemy18.hp <= 0:
                enemy18.visible = False
                gamewindow.blit(smallspider_death, (enemy18.x-0 , enemy18.y+20))
            if enemy19.hp <= 0:
                enemy19.visible = False
                gamewindow.blit(smallspider_death, (enemy19.x-0 , enemy19.y+20))
            if enemy20.hp <= 0:
                enemy20.visible = False
                gamewindow.blit(smallspider_death, (enemy20.x-0 , enemy20.y+20))

            if enemy6.hp > 0:
                enemy6.visible = True
                enemy6.draw(gamewindow, self)
       
            if enemy7.hp > 0:
                enemy7.visible = True
                enemy7.draw(gamewindow)
                  
            if enemy8.hp > 0:
                enemy8.visible = True
                enemy8.draw(gamewindow, self)
               
            if enemy9.hp > 0:
                enemy9.visible = True
                enemy9.draw(gamewindow, self)

            if enemy10.hp > 0:
                enemy10.visible = True
                enemy10.draw(gamewindow, self)
                
            if enemy11.hp > 0:
                enemy11.visible = True
                enemy11.draw(gamewindow, self)
              
            if enemy12.hp > 0:
                enemy12.visible = True
                enemy12.draw(gamewindow, self)
              
            if enemy13.hp > 0:
                enemy13.visible = True
                enemy13.draw(gamewindow, self)

            if enemy14.hp > 0:
                enemy14.visible = True
                enemy14.draw(gamewindow, self)

            if enemy15.hp > 0:
                enemy15.visible = True
                enemy15.draw(gamewindow, self)
                
            if enemy16.hp > 0:
                enemy16.visible = True
                enemy16.draw(gamewindow, self)
               
            if enemy17.hp > 0:
                enemy17.visible = True
                enemy17.draw(gamewindow, self)
                
            if enemy18.hp > 0:
                enemy18.visible = True
                enemy18.draw(gamewindow, self)

            if enemy19.hp > 0:
                enemy19.visible = True
                enemy19.draw(gamewindow)

            if enemy20.hp > 0:
                enemy20.visible = True
                enemy20.draw(gamewindow)
              
            if enemy6.visible == True or enemy7.visible == True or \
                enemy8.visible == True or enemy9.visible == True or \
                enemy10.visible == True or enemy11.visible == True or \
                enemy12.visible == True or enemy13.visible == True or \
                enemy14.visible == True or enemy15.visible == True or \
                enemy16.visible == True or enemy17.visible == True or \
                enemy18.visible == True or enemy19.visible == True or \
                enemy20.visible == True:
                gamewindow.blit(text7, (1050, 20))
                gamewindow.blit(text8, (1050, 50))                

            if enemy6.visible == False and enemy7.visible == False and \
                enemy8.visible == False and enemy9.visible == False and \
                enemy10.visible == False and enemy11.visible == False and \
                enemy12.visible == False and enemy13.visible == False and \
                enemy14.visible == False and enemy15.visible == False and \
                enemy16.visible == False and enemy17.visible == False and \
                enemy18.visible == False and enemy19.visible == False and \
                enemy20.visible == False:
                gamewindow.blit(text9, (650, 20))
                self.objective3 = True
                
        # Room 4                
        elif self.current_room == 'room4':
            gamewindow.blit( pygame.image.load(os.path.join(SurviveImages, "room4.png")), (0,0))
            text1 = font.render('Objective: Follow the river bank.', 1, (255,255,255))
            text2 = font.render('Should I go left or right?', 1, (255,255,255))
            text3 = font.render('OUCH! The Water Hurts!', 1, (255,255,255))

            enemy22.visible = False

            if self.y < 605:
                gamewindow.blit(text1, (1040, 20))
                gamewindow.blit(text2, (1100, 50)) 

            if self.y > 560:       
                self.current_hp -= 1
                if self.alive == True:
                    main_hit.play()
                gamewindow.blit(text3, (600, 750))
                
        # Room 5
        elif self.current_room == 'room5':
            gamewindow.blit( pygame.image.load(os.path.join(SurviveImages, "room5.png")), (0,0))
            text1 = font.render('Objective: Follow the river bank.', 1, (255,255,255))
            text3 = font.render('OUCH! The Water Hurts!', 1, (255,255,255))
            
            if self.y < 605:
                gamewindow.blit(text1, (1040, 20))            

            if self.y > 560:       
                self.current_hp -= 1
                if self.alive == True:
                    main_hit.play()
                gamewindow.blit(text3, (600, 750))

            if enemy22.hp <= 0:
                enemy22.visible = False
                gamewindow.blit(rat_death, (enemy22.x-32 , enemy22.y+32))  

            if enemy58a.hp <= 0:
                enemy58a.visible = False
                gamewindow.blit(rat_death, (enemy58a.x-32 , enemy58a.y+32))        

            if enemy59a.hp <= 0:
                enemy59a.visible = False
                gamewindow.blit(rat_death, (enemy59a.x-32 , enemy59a.y+32))       

            if enemy60a.hp <= 0:
                enemy60a.visible = False
                gamewindow.blit(rat_death, (enemy60a.x-32 , enemy60a.y+32))       

            if enemy61a.hp <= 0:
                enemy61a.visible = False
                gamewindow.blit(rat_death, (enemy61a.x-32 , enemy61a.y+32))

            if enemy22.hp > 0:
                enemy22.visible = True
                enemy22.draw(gamewindow, self) 

            if enemy58a.hp > 0:
                enemy58a.visible = True
                enemy58a.draw(gamewindow, self)

            if enemy59a.hp > 0:
                enemy59a.visible = True
                enemy59a.draw(gamewindow, self)

            if enemy60a.hp > 0:
                enemy60a.visible = True
                enemy60a.draw(gamewindow, self)

            if enemy61a.hp > 0:
                enemy61a.visible = True
                enemy61a.draw(gamewindow, self)

        # Room 6            
        elif self.current_room == 'room6':
            text1 = font.render('Objective: Follow the river bank.', 1, (255,255,255))
            text3 = font.render('OUCH! The Water Hurts!', 1, (255,255,255))
            gamewindow.blit( pygame.image.load(os.path.join(SurviveImages, "room6.png")), (0,0))

            if enemy21.hp <= 0:
                enemy21.visible = False
                gamewindow.blit(rat_death, (enemy21.x-32 , enemy21.y+32))   

            if enemy21.hp > 0:
                enemy21.visible = True
                enemy21.draw(gamewindow, self) 

            if self.y < 605:
                gamewindow.blit(text1, (1040, 20))            

            if self.y > 560:       
                self.current_hp -= 1
                if self.alive == True:
                    main_hit.play()
                gamewindow.blit(text3, (600, 750))
                
        # Room 7 (Boss)            
        elif self.current_room == 'room7':

            text1 = font.render('You went the wrong way.', 1, (255,255,255))
            text2 = font.render('Objective: Die.', 1, (255,255,255))
            text3 = font.render('OUCH! Its Lava!', 1, (255,255,255))
            text4 = font.render('Your Not Going Anywhere', 1, (255,255,255))
            text5 = font.render('YOU FOOL! Hes IMMORTAL', 1, (255,255,255))
            text6 = font.render('The Lava Rises', 1, (255,255,255))
            text7 = font.render('Heres your treasure.', 1, (255,255,255))
            
            if boss1.hp <= 300 and boss1.hp >= 280:
                gamewindow.blit( pygame.image.load(os.path.join(SurviveImages, "room7.png")), (0,0))
                if self.y > 645:       
                    self.current_hp -= 5
                    if self.alive == True:
                        main_hit.play()
                    gamewindow.blit(text3, (600, 775))

            if boss1.hp < 280 and boss1.hp >= 260:
                gamewindow.blit( pygame.image.load(os.path.join(SurviveImages, "room7-1.png")), (0,0))
                gamewindow.blit(text5, (550, 20))
                gamewindow.blit(text6, (600, 50))
                if self.y > 505:       
                    self.current_hp -= 3
                    if self.alive == True:
                        main_hit.play()
                    gamewindow.blit(text3, (600, 775))

            if boss1.hp < 260 and boss1.hp >= 240:
                gamewindow.blit( pygame.image.load(os.path.join(SurviveImages, "room7-2.png")), (0,0))
                gamewindow.blit(text5, (550, 20))
                gamewindow.blit(text6, (600, 50))
                if self.y > 399:       
                    self.current_hp -= 2
                    if self.alive == True:
                        main_hit.play()
                    gamewindow.blit(text3, (600, 775))

            if boss1.hp < 240 and boss1.hp > 0:
                gamewindow.blit( pygame.image.load(os.path.join(SurviveImages, "room7-3.png")), (0,0))
                self.current_hp -= 1
                if self.alive == True:
                    main_hit.play()
                gamewindow.blit(text3, (600, 775))
                
            if boss1.hp > 0:
                boss1.visible = True
                boss1.draw(gamewindow, self)
        
            if self.y < 800 and self.x > -13 and self.x < 1350:
                gamewindow.blit(text2, (1100, 50))

                if self.objective6 == True:
                    gamewindow.blit(text7, (1100, 20))
                else:
                    gamewindow.blit(text1, (1100, 20))
                
            if self.x < -16 or self.x > 1350:
                gamewindow.blit(text4, (550, 80))

        # Room 8
        elif self.current_room == 'room8':
            gamewindow.blit( pygame.image.load(os.path.join(SurviveImages, "room8.png")), (0,0))
            text2 = font.render('Objective: Follow path', 1, (255,255,255))
            text3 = font.render('OUCH! The Water Hurts!', 1, (255,255,255))
            text4 = font.render('Stand on cross to completely heal health', 1, (255,255,255))
            
            gamewindow.blit(text2, (1160, 20))

            enemy22.visible = False
            enemy58a.visible = False
            enemy59a.visible = False
            enemy60a.visible = False
            enemy61a.visible = False
   
            if self.y > 560 and self.alive == True:       
                self.current_hp -= 1
                main_hit.play()
                gamewindow.blit(text3, (600, 750))

            elif self.x > 539 and self.x < 611 and self.y > -13 and self.y < 36:
                gamewindow.blit(text4, (450, 200))
                self.current_hp = self.full_hp

            if enemy62a.hp <= 0:
                enemy62a.visible = False
                gamewindow.blit(rat_death, (enemy62a.x-32 , enemy62a.y+32))    
                
            if enemy63a.hp <= 0:
                enemy63a.visible = False
                gamewindow.blit(bigspider_death, (enemy63a.x-32 , enemy63a.y+32)) 

            if enemy64a.hp <= 0:
                enemy64a.visible = False
                gamewindow.blit(bigwolf_death, (enemy64a.x-32 , enemy64a.y+32)) 

            if enemy62a.hp > 0:
                enemy62a.visible = True
                enemy62a.draw(gamewindow, self)

            if enemy63a.hp > 0:
                enemy63a.visible = True
                enemy63a.draw(gamewindow, self)

            if enemy64a.hp > 0:
                enemy64a.visible = True
                enemy64a.draw(gamewindow, self)


        # Room 9
        elif self.current_room == 'room9':
            gamewindow.blit( pygame.image.load(os.path.join(SurviveImages, "room9.png")), (0,0))
            son_list.append(time.time())
            text1 = font.render('Johnny! Is that you?', 1, (255,255,255))
            text2 = font.render('Objective: Get your son', 1, (255,255,255))
            text3 = font.render('OUCH! The Water Hurts!', 1, (255,255,255))
            gamewindow.blit(text1, (950, 20))
            gamewindow.blit(text2, (950, 50))
        
            if self.y < 466 and self.x < 490 or self.y < 466 and self.x > 665 and self.alive == True:       
                self.current_hp -= 2
                main_hit.play()
                gamewindow.blit(text3, (1050, 450))

            if son_list[0] + 3.5 > time.time():
                gamewindow.blit(son_down, (625,0))

            if son_list[0] + 3.5 < time.time():
                if enemy27.hp > 0:
                    enemy27.visible = True
                    enemy27.draw(gamewindow)

            if enemy23.hp <= 0:
                enemy23.visible = False
                gamewindow.blit(bat_death, (enemy23.x-32 , enemy23.y+32))

            if enemy24.hp <= 0:
                enemy24.visible = False
                gamewindow.blit(bat_death, (enemy24.x-32 , enemy24.y+32))               
                
            if enemy25.hp <= 0:
                enemy25.visible = False
                gamewindow.blit(wizard_death, (enemy25.x-32 , enemy25.y+32))                     

            if enemy26.hp <= 0:
                enemy26.visible = False
                gamewindow.blit(wizard_death, (enemy26.x-32 , enemy26.y+32))

            if enemy27.hp <= 0:
                enemy27.visible = False
                gamewindow.blit(goblin_death, (enemy27.x-32 , enemy27.y+32))

            if enemy23.hp > 0:
                enemy23.visible = True
                enemy23.draw(gamewindow, self)

            if enemy24.hp > 0:
                enemy24.visible = True
                enemy24.draw(gamewindow, self)

            if enemy25.hp > 0:
                enemy25.visible = True
                enemy25.draw(gamewindow, self)

            if enemy26.hp > 0:
                enemy26.visible = True
                enemy26.draw(gamewindow, self)
                
            if enemy23.visible == False and enemy24.visible == False and \
                enemy27.visible == False:
                self.objective4 = True

        # Room 10
        elif self.current_room == 'room10':
            font20 = pygame.font.Font(None, 20)
            text1 = font.render('Dad! Help!', 1, (255,255,255))
            text2 = font.render('Sword Acquired', 1, (255,255,255))
            text3 = font.render('OUCH! The Water Hurts!', 1, (255,255,255))
            text4 = font20.render("Press 'S' to use SWORD", 1, (255,255,255))
            enemy25.visible = False
            enemy26.visible = False
            gamewindow.blit( pygame.image.load(os.path.join(SurviveImages, "room10.png")), (0,0))

            if son_list[-1] + 6 > time.time():
                gamewindow.blit(son_left, (1410,225))
                gamewindow.blit(text1, (1315, 200))
                
            if son_list[-1] + 7 < time.time():
                pass

            if self.x > 1215 and self.y > 590 and \
               self.x < 1262 and self.y < 673:
                self.has_sword = True

            if self.has_sword == False:
                gamewindow.blit(sword_ground, (1275,690))

            if self.has_sword == True:
                if enemy30.visible == True or enemy31.visible == True:
                    gamewindow.blit(text4, (self.x - 10, self.y))

            if main_character.x < 487 and main_character.y > 518 and self.alive == True:
                gamewindow.blit(text3, (950, 50))
                self.current_hp -= 2
                main_hit.play()             
                
            if main_character.x < -25 and self.alive == True:
                gamewindow.blit(text3, (950, 50))
                self.current_hp -= 2
                main_hit.play()
                
            if main_character.y < 61 and self.alive == True:
                gamewindow.blit(text3, (950, 50))
                self.current_hp -= 2
                main_hit.play()
             
            if main_character.x > 144 and main_character.y < 349 and \
               main_character.y > 230 and self.alive == True:
                gamewindow.blit(text3, (950, 50))
                self.current_hp -= 2
                main_hit.play()

            if self.x > 675 and self.y >= 349 and \
               self.y < 573 and self.x < 1163 and \
                self.alive == True:
                gamewindow.blit(text3, (950, 50))
                self.current_hp -= 2
                main_hit.play()

            if self.x > 1163 and self.y < 537 and self.y > 222 and self.alive == True:
                gamewindow.blit(text3, (950, 50))
                self.current_hp -= 2
                main_hit.play()

            if self.x > 1287 and self.y >= 537  and self.alive == True:
                gamewindow.blit(text3, (950, 50))
                self.current_hp -= 2
                main_hit.play()
                
            if self.x <= 1287 and self.y > 680 and self.x > 675  and self.alive == True:
                gamewindow.blit(text3, (950, 50))
                self.current_hp -= 2
                main_hit.play()
                
            if self.y <= 680 and self.x > 675 and \
               self.y > 626 and self.x < 1171 and \
                self.alive == True:
                gamewindow.blit(text3, (950, 50))
                self.current_hp -= 2
                main_hit.play()                
                
            if enemy28.hp > 0:
                enemy28.visible = True
                enemy28.draw(gamewindow, self)

            if enemy29.hp > 0:
                enemy29.visible = True
                enemy29.draw(gamewindow)

            if enemy28.hp <= 0:
                enemy28.visible = False
                gamewindow.blit(goblin_death, (enemy28.x-32 , enemy28.y+32))
                if enemy39.hp > 0:
                    enemy39.visible = True
                    enemy39.draw(gamewindow, self)             
                if enemy40.hp > 0:
                    enemy40.visible = True
                    enemy40.draw(gamewindow, self)
                if enemy41.hp > 0:
                    enemy41.visible = True
                    enemy41.draw(gamewindow, self)

            if enemy29.hp <= 0:
                enemy29.visible = False
                gamewindow.blit(wizard_death, (enemy29.x-32 , enemy29.y+32))

                if enemy30.hp > 0:
                    enemy30.visible = True
                    enemy30.draw(gamewindow, self)

                if enemy31.hp > 0:
                    enemy31.visible = True
                    enemy31.draw(gamewindow)

                if enemy32.hp > 0:
                    enemy32.visible = True
                    enemy32.draw(gamewindow)

                if enemy33.hp > 0:
                    enemy33.visible = True
                    enemy33.draw(gamewindow)
                          
            if enemy30.hp <= 0:
                enemy30.visible = False
                gamewindow.blit(bat_death, (enemy30.x-32 , enemy30.y+32))

            if enemy31.hp <= 0:
                enemy31.visible = False
                gamewindow.blit(bat_death, (enemy31.x-32 , enemy31.y+32))

            if enemy32.hp <= 0:
                enemy32.visible = False
                gamewindow.blit(bat_death, (enemy32.x-32 , enemy32.y+32))

            if enemy33.hp <= 0:
                enemy33.visible = False
                gamewindow.blit(bat_death, (enemy33.x-32 , enemy33.y+32))
                if enemy34.hp > 0:
                    enemy34.visible = True
                    enemy34.draw(gamewindow, self)

                if enemy35.hp > 0:
                    enemy35.visible = True
                    enemy35.draw(gamewindow, self)

                if enemy36.hp > 0:
                    enemy36.visible = True
                    enemy36.draw(gamewindow, self)

                if enemy37.hp > 0:
                    enemy37.visible = True
                    enemy37.draw(gamewindow, self)

                if enemy38.hp > 0:
                    enemy38.visible = True
                    enemy38.draw(gamewindow, self)


            if enemy34.hp <= 0:
                enemy34.visible = False
                gamewindow.blit(bat_death, (enemy34.x-32 , enemy34.y+32))

            if enemy35.hp <= 0:
                enemy35.visible = False
                gamewindow.blit(bat_death, (enemy35.x-32 , enemy35.y+32))

            if enemy36.hp <= 0:
                enemy36.visible = False
                gamewindow.blit(bat_death, (enemy36.x-32 , enemy36.y+32))

            if enemy37.hp <= 0:
                enemy37.visible = False
                gamewindow.blit(bat_death, (enemy37.x-32 , enemy37.y+32))

            if enemy38.hp <= 0:
                enemy38.visible = False
                gamewindow.blit(wizard_death, (enemy38.x-32 , enemy38.y+32))
                
            if enemy39.hp <= 0:
                enemy39.visible = False
                gamewindow.blit(bat_death, (enemy39.x-32 , enemy39.y+32))             

            if enemy40.hp <= 0:
                enemy40.visible = False
                gamewindow.blit(bat_death, (enemy40.x-32 , enemy40.y+32))

            if enemy41.hp <= 0:
                enemy41.visible = False
                gamewindow.blit(bat_death, (enemy41.x-32 , enemy41.y+32))

            if enemy28.visible == False and enemy29.visible == False and \
               enemy30.visible == False and enemy31.visible == False and \
               enemy32.visible == False and enemy33.visible == False and \
               enemy34.visible == False and enemy35.visible == False and \
               enemy36.visible == False and enemy37.visible == False and \
               enemy38.visible == False and enemy39.visible == False and \
               enemy40.visible == False and enemy41.visible == False and \
               self.has_sword == True:
                self.objective5 = True

        # Room 11
        elif self.current_room == 'room11' :
            enemy42.hp = 100
            
            text1 = font.render('WHERE IS MY SON!', 1, (255,255,255))
            text3 = font.render('OUCH! The Water Hurts!', 1, (255,255,255))
            text4 = font.render('NO I CANT MOVE', 1, (255,255,255))
            son_list.clear()

            if self.bridge == 0:
                gamewindow.blit( pygame.image.load(os.path.join(SurviveImages, "room11.png")), (0,0))

                if self.x < 834 and self.x > 609 and self.y > 402 and self.y < 636:
                    gamewindow.blit(text4, (600, 385))
                    enemy42.visible = True
                    enemy42.draw(gamewindow, self)
                    self.has_gun = False
                    self.has_sword = False
                    self.has_punch = False
                    self.can_move = False
                    
                # Button 4
                if self.up == True and self.y < 150 and self.y >= 114 and keys[pygame.K_s] and \
                   self.has_sword == True and self.swing_sword == True and \
                   self.x <= 717 and self.x >= 699:
                    self.bridge = 1

            elif self.bridge == 1:
                gamewindow.blit( pygame.image.load(os.path.join(SurviveImages, "room11-1.png")), (0,0))

                if self.x < 780 and self.x > 609 and self.y > 402 and self.y < 636:
                    gamewindow.blit(text4, (600, 385))
                    enemy42.visible = True
                    enemy42.draw(gamewindow, self)
                    self.has_gun = False
                    self.has_sword = False
                    self.has_punch = False
                    self.can_move = False

                # Button 2
                if self.up == True and self.y < 150 and self.y >= 114 and keys[pygame.K_s] and \
                   self.has_sword == True and self.swing_sword == True and \
                   self.x <= 528 and self.x >= 510:
                    self.bridge = 2
                
                # Button 1                    
                if self.up == True and self.y < 150 and self.y >= 114 and keys[pygame.K_s] and \
                   self.has_sword == True and self.swing_sword == True and \
                   self.x <= 438 and self.x >= 420:
                    self.bridge = 0

                # Button 8                    
                if self.up == True and self.y < 150 and self.y >= 114 and keys[pygame.K_s] and \
                   self.has_sword == True and self.swing_sword == True and \
                   self.x <= 1086 and self.x >= 1068:
                    self.bridge = 0

            elif self.bridge == 2:
                gamewindow.blit( pygame.image.load(os.path.join(SurviveImages, "room11-2.png")), (0,0))
                
                if self.x < 717 and self.x > 609 and self.y > 402 and self.y < 636:
                    gamewindow.blit(text4, (600, 385))
                    enemy42.visible = True
                    enemy42.draw(gamewindow, self)
                    self.has_gun = False
                    self.has_sword = False
                    self.has_punch = False
                    self.can_move = False
                    
                # Button 8                    
                if self.up == True and self.y < 150 and self.y >= 114 and keys[pygame.K_s] and \
                   self.has_sword == True and self.swing_sword == True and \
                   self.x <= 1086 and self.x >= 1068:
                    self.bridge = 3
                # Button 1                    
                if self.up == True and self.y < 150 and self.y >= 114 and keys[pygame.K_s] and \
                   self.has_sword == True and self.swing_sword == True and \
                   self.x <= 429 and self.x >= 420:
                    self.bridge = 0

            elif self.bridge == 3:
                gamewindow.blit( pygame.image.load(os.path.join(SurviveImages, "room11-3.png")), (0,0))
                if self.x < 654 and self.x > 609 and self.y > 402 and self.y < 636:
                    gamewindow.blit(text4, (600, 385))
                    enemy42.visible = True
                    enemy42.draw(gamewindow, self)
                    self.has_gun = False
                    self.has_sword = False
                    self.has_punch = False
                    self.can_move = False                    

                # Button 1                    
                if self.up == True and self.y < 150 and self.y >= 114 and keys[pygame.K_s] and \
                   self.has_sword == True and self.swing_sword == True and \
                   self.x <= 438 and self.x >= 420:
                    self.bridge = 4

            elif self.bridge == 4:
                gamewindow.blit( pygame.image.load(os.path.join(SurviveImages, "room11-4.png")), (0,0))

                if enemy44.hp > 0:
                    enemy44.visible = True
                    enemy44.draw(gamewindow)
                    
                if enemy45.hp > 0:
                    enemy45.visible = True
                    enemy45.draw(gamewindow)

                if enemy46.hp > 0:
                    enemy46.visible = True
                    enemy46.draw(gamewindow)

                if enemy47.hp > 0:
                    enemy47.visible = True
                    enemy47.draw(gamewindow)

                if enemy48.hp > 0:
                    enemy48.visible = True
                    enemy48.draw(gamewindow)

                if enemy49.hp > 0:
                    enemy49.visible = True
                    enemy49.draw(gamewindow, self)
                    
                if enemy50.hp > 0:
                    enemy50.visible = True
                    enemy50.draw(gamewindow, self)
                    
                if enemy51.hp > 0:
                    enemy51.visible = True
                    enemy51.draw(gamewindow, self)

                if enemy52.hp > 0:
                    enemy52.visible = True
                    enemy52.draw(gamewindow, self)
                
                if enemy44.hp <= 0:
                    enemy44.visible = False
                    gamewindow.blit(bat_death, (enemy44.x-32 , enemy44.y+32))

                if enemy45.hp <= 0:
                    enemy45.visible = False
                    gamewindow.blit(bat_death, (enemy45.x-32 , enemy45.y+32))

                if enemy46.hp <= 0:
                    enemy46.visible = False
                    gamewindow.blit(bat_death, (enemy46.x-32 , enemy46.y+32))

                if enemy47.hp <= 0:
                    enemy47.visible = False
                    gamewindow.blit(bat_death, (enemy47.x-32 , enemy47.y+32))

                if enemy48.hp <= 0:
                    enemy48.visible = False
                    gamewindow.blit(bat_death, (enemy48.x-32 , enemy48.y+32))

                if enemy49.hp <= 0:
                    enemy49.visible = False
                    gamewindow.blit(bat_death, (enemy49.x-32 , enemy49.y+32))

                if enemy50.hp <= 0:
                    enemy50.visible = False
                    gamewindow.blit(bat_death, (enemy50.x-32 , enemy50.y+32))

                if enemy51.hp <= 0:
                    enemy51.visible = False
                    gamewindow.blit(bat_death, (enemy51.x-32 , enemy51.y+32))

                if enemy52.hp <= 0:
                    enemy52.visible = False
                    gamewindow.blit(bat_death, (enemy52.x-32 , enemy52.y+32))

            gamewindow.blit(text1, (1200, 20))


            # Button 3       
            if self.up == True and self.y < 150 and self.y >= 114 and keys[pygame.K_s] and \
               self.has_sword == True and self.swing_sword == True and \
               self.x <= 627 and self.x >= 609:
                if self.bridge != 4:
                    self.bridge = 0          
            # Button 5
            if self.up == True and self.y < 150 and self.y >= 114 and keys[pygame.K_s] and \
               self.has_sword == True and self.swing_sword == True and \
               self.x <= 798 and self.x >= 780:
                if self.bridge != 4:
                    self.bridge = 0
            # Button 6
            if self.up == True and self.y < 150 and self.y >= 114 and keys[pygame.K_s] and \
               self.has_sword == True and self.swing_sword == True and \
               self.x <= 888 and self.x >= 870:
                if self.bridge != 4:
                    self.bridge = 0

            # Button 7
            if self.up == True and self.y < 150 and self.y >= 114 and keys[pygame.K_s] and \
               self.has_sword == True and self.swing_sword == True and \
               self.x <= 996 and self.x >= 978:
                if self.bridge != 4:
                    self.bridge = 0

            if self.y < 60 or self.x > 101 and self.y < 114 or self.x > 1270 and self.y < 708 or \
               self.y > 177 and self.x > 100 and self.x < 1216 and self.y < 294 or \
               self.y >= 690 and self.y < 708 and self.x > 249 or self.y > 474 and self.y < 689 and \
                self.x > 249 and self.x <= 496 or self.x <= 1270 and self.x >= 995 and self.y > 474 and \
                self.y < 690 or self.y < 411 and self.y >= 294 and self.x < 1212 and self.x >= 955 or \
                self.x > 100 and self.x <= 496 and self.y >= 294 and self.y < 411 or \
                self.y > 222 and self.x <= 100 or self.x < 222 and self.y >= 411:            
                gamewindow.blit(text3, (600, 385))
                self.current_hp -= 5
                if self.alive == True:
                    main_hit.play()

            if self.x > 496 and self.x < 995 and self.y > 474 and self.y < 690 or \
               self.x > 609 and self.x < 834 and self.y > 457 and self.y <= 474 or \
               self.y >= 294 and self.y < 411 and self.x > 496 and self.x < 955 or \
               self.y >= 411 and self.y < 420 and self.x > 609 and self.x < 834:
                gamewindow.blit(text4, (600, 385))
                self.can_move = False
                self.has_gun = False
                self.has_sword = False
                self.has_punch = False
                enemy42.visible = True
                enemy42.draw(gamewindow, self)


            if self.x >= 1269 and self.y >= 715 and self.x <= 1350 and self.y <= 780:
                self.current_hp = self.full_hp

        # Room 12        
        elif self.current_room == 'room12':
            enemy44.visible = False
            enemy49.visible = False
            gamewindow.blit( pygame.image.load(os.path.join(SurviveImages, "room12.png")), (0,0))
            font25 = pygame.font.Font(None, 25)
            font20 = pygame.font.Font(None, 20)
            text1 = font25.render('Market', 1, (255,255,255))
            gamewindow.blit(text1, (1350, 222))
            text2 = font20.render('"Please Help!"', 1, (0, 0, 0))
            text3 = font20.render('"Hi there sir"', 1, (0, 0, 0))
            text4 = font20.render('"I am really hungry"', 1, (0, 0, 0))
            text5 = font20.render('"Have any food?"', 1, (0, 0, 0))
            text6 = font20.render('"Thank you so much!"', 1, (0, 0, 0))           
            text7 = font20.render('"Here, take this key"', 1, (0, 0, 0))
            text8 = font20.render('"This will help you get your son"', 1, (0, 0, 0))
            text9 = font20.render("Press 'E' to give banana", 1, (0, 0, 0))

            if self.has_banana == False: 
                if self.x > 942 and self.y < 253 and self.y > -17:
                    gamewindow.blit(text3, (1150, 140))
                    gamewindow.blit(text4, (1150, 155))
                    gamewindow.blit(text5, (1150, 170))
                    
                else:
                    gamewindow.blit(text2, (1085, 130))
                

            if self.has_banana == True:
                if self.has_key == False:
                    if self.x >= 969 and self.y <= 253 and \
                       self.y >= 28 and self.x <= 1179:
                        gamewindow.blit(text9, (self.x, self.y))
                        if keys[pygame.K_e]:
                            self.has_key = True
                            
                if self.has_key == True:
                    gamewindow.blit(text6, (1150, 140))
                    gamewindow.blit(text7, (1150, 155))
                    gamewindow.blit(text8, (1150, 170))
     
        # Room 13        
        elif self.current_room == 'room13':
            gamewindow.blit(pygame.image.load(os.path.join(SurviveImages, "room13.png")), (0,0))
            font20 = pygame.font.Font(None, 20)
            text1 = font20.render('"Fresh Bananas For Sale!"', True, (0, 0, 0))
            text2 = font20.render('"Come back when you have money"', True, (0,0,0))
            text3 = font20.render('"Need some money?"', True, (0, 0, 0))
            text4 = font20.render('"Theres a cave up North"', True, (0, 0, 0))
            text5 = font20.render('"At the end is a large chest"', True, (0, 0, 0))          
            text6 = font20.render('"Good Luck."', True, (0, 0, 0))   

            if self.y <= 175 and self.x >= 414 and self.x <= 789:
                gamewindow.blit(text3, (620, 55))
                gamewindow.blit(text4, (615, 70))
                gamewindow.blit(text5, (615, 85))
                gamewindow.blit(text6, (640, 110))

            if self.x >= 984 and self.x <= 1209 and self.y >= 205 and self.y <= 490:
                gamewindow.blit(text2, (1050, 365))

            else:
                gamewindow.blit(text1, (1100, 365))
                
                    
        # Room 14       
        elif self.current_room == 'room14':
            enemy53.visible = False
            enemy54.visible = False
            enemy55.visible = False
            
            if self.banana_tree == 0:
                gamewindow.blit(pygame.image.load(os.path.join(SurviveImages, "room14.png")), (0,0))

                if self.x >= 780 and self.has_sword == True and \
                   self.direction == 'Right' and keys[pygame.K_s] and \
                   self.y <= 505 and self.x <= 870:
                    self.banana_tree = 1

                if self.x >= 816 and self.direction == 'Right' and \
                   keys[pygame.K_d] and self.y <= 505 and self.x <= 870:
                    self.banana_tree = 1

                if self.x >= 879 and self.has_sword == True and \
                   self.direction == 'Left' and keys[pygame.K_s] and \
                   self.y <= 505 and self.x <= 960:
                    self.banana_tree = 1

                if self.x >= 870 and self.direction == 'Left' and \
                   keys[pygame.K_d] and self.y <= 505 and self.x <= 933:
                    self.banana_tree = 1

                if self.x >= 843 and self.has_sword == True and \
                   self.direction == 'Up' and keys[pygame.K_s] and \
                   self.y <= 559 and self.x <= 906:
                    self.banana_tree = 1

                if self.x >= 825 and self.direction == 'Up' and \
                   keys[pygame.K_d] and self.y <= 541 and self.x <= 924:
                    self.banana_tree = 1

            elif self.banana_tree == 1:
                gamewindow.blit(pygame.image.load(os.path.join(SurviveImages, "room14-1.png")), (0,0))
                if self.y >= 604 and self.x >= 942 and self.x <= 987 and self.y <= 703:
                    self.has_banana = True
                    self.banana_tree = 2

            elif self.banana_tree == 2 and self.has_banana == True:
                gamewindow.blit(pygame.image.load(os.path.join(SurviveImages, "room14-2.png")), (0,0))


        # Room 15   
        elif self.current_room == 'room15' :
            gamewindow.blit(pygame.image.load(os.path.join(SurviveImages, "room15.png")), (0,0))
            font25 = pygame.font.Font(None, 25)
            font30 = pygame.font.Font(None, 30)
            
            text1 = font25.render('Door is Locked. Find a Key.', 1, (255,100,100))
            text2 = font30.render('Objective: Enter House', 1, (255,255,255))
            text3 = font30.render('Your son was last seen taken into this house', 1, (255,255,255))

            gamewindow.blit(text2, (1150, 35))
            gamewindow.blit(text3, (1000, 5))

            if self.x >= 1030 and self.x <= 1050 and self.y <= 429 and self.has_key == False:
                gamewindow.blit(text1, (1000, 150))
                

        # Room 16   
        elif self.current_room == 'room16':
            gamewindow.blit(pygame.image.load(os.path.join(SurviveImages, "room16.png")), (0,0))
            font30 = pygame.font.Font(None, 30)
            text1 = font30.render('Treasure', True, (255, 255, 255))
            gamewindow.blit(text1, (1265, 335))

            if enemy53.hp > 0:
                enemy53.visible = True
                enemy53.draw(gamewindow, self)

            if enemy54.hp > 0:
                enemy54.visible = True
                enemy54.draw(gamewindow, self)

            if enemy55.hp > 0:
                enemy55.visible = True
                enemy55.draw(gamewindow, self)

            if enemy53.hp <= 0:
                gamewindow.blit(bat_death, (enemy53.x-32 , enemy53.y+32))

            if enemy54.hp <= 0:
                gamewindow.blit(smallspider_death, (enemy54.x-32 , enemy54.y+32))

            if enemy55.hp <= 0:
                gamewindow.blit(rat_death, (enemy55.x-32 , enemy55.y+32))

            if enemy53.visible == False and enemy54.visible == False and \
                enemy55.visible == False:
                self.objective6 = True    


        # Room 17   
        elif self.current_room == 'room17':
            gamewindow.blit(pygame.image.load(os.path.join(SurviveImages, "room17.png")), (0,0))    
            font20 = pygame.font.Font(None, 20)
            font25 = pygame.font.Font(None, 25)
            font30 = pygame.font.Font(None, 30)
            text1 = font30.render('Objective: Find Your Son', True, (255, 255, 255))
            text2 = font20.render("'E' to Search Body", True, (255, 255, 255))
            text3 = font25.render('Door is Locked.', True, (255,100,100))
            text4 = font20.render('Key Acquired', True, (255, 255, 255)) 

            gamewindow.blit(text1, (1190, 10))
            
            if enemy56.hp > 0:
                enemy56.visible = True
                enemy56.draw(gamewindow, self)

            if enemy57.hp > 0:
                enemy57.visible = True
                enemy57.draw(gamewindow, self)
                
            if enemy56.hp <= 0:
                enemy56.visible = False
                gamewindow.blit(knight_death, (enemy56.x-32 , enemy56.y+32))
                if enemy58.hp > 0:
                    enemy58.visible = True
                    enemy58.draw(gamewindow, self)
                    
            if enemy57.hp <= 0:
                enemy57.visible = False
                gamewindow.blit(knight_death, (enemy57.x-32 , enemy57.y+32))
                if enemy59.hp > 0:
                    enemy59.visible = True
                    enemy59.draw(gamewindow, self)

            if enemy58.hp <= 0:
                gamewindow.blit(knight_death, (enemy58.x-32 , enemy58.y+32))
                if enemy60.hp > 0:
                    enemy60.visible = True
                    enemy60.draw(gamewindow, self)
                if enemy61.hp > 0:
                    enemy61.visible = True
                    enemy61.draw(gamewindow, self)
                if enemy62.hp > 0:
                    enemy62.visible = True
                    enemy62.draw(gamewindow, self)

            if enemy59.hp <= 0:
                enemy59.visible = False
                gamewindow.blit(knight_death, (enemy59.x-32 , enemy59.y+32))

            if enemy60.hp <= 0:
                enemy60.visible = False
                gamewindow.blit(knight_death, (enemy60.x-32 , enemy60.y+32))

            if enemy61.hp <= 0:
                enemy61.visible = False
                gamewindow.blit(knight_death, (enemy61.x-32 , enemy61.y+32))

            if enemy62.hp <= 0:
                enemy62.visible = False
                gamewindow.blit(knight_death, (enemy62.x-32 , enemy62.y+32))
                if self.x >= enemy62.x - 105 and self.x <= enemy62.x + 15 and\
                   self.y >= enemy62.y - 72 and self.y <= enemy62.y + 70 and\
                   self.has_key == False:
                    gamewindow.blit(text2, (self.x, self.y))
                    if keys[pygame.K_e]:
                        self.has_key = True

            if self.x <= -35 and self.y <= 343 and self.y >= 262:
                gamewindow.blit(text3, (650, 150))

            if self.x <= -35 and self.y <= 586 and self.y >= 514 and\
               self.has_key == False:
                gamewindow.blit(text3, (650, 150))

            if self.x >= 1360 and self.y <= 253 and self.y >= 172:
                gamewindow.blit(text3, (650, 150))

            if self.x >= 1360 and self.y <= 496 and self.y >= 415:
                gamewindow.blit(text3, (650, 150))

            if self.has_key == True:
                gamewindow.blit(text4, (self.x+20, self.y))
            

        # Room 18
        elif self.current_room == 'room18':
            gamewindow.blit(pygame.image.load(os.path.join(SurviveImages, "room18.png")), (0,0))
            enemy57.visible = False
            enemy59.visible = False
            enemy60.visible = False
            enemy61.visible = False
            self.has_key = False
            son_list.clear()
            time_list.clear()

            if enemy63.hp > 0:
                enemy63.visible = True
                enemy63.draw(gamewindow, self)
                
            if enemy64.hp > 0:
                enemy64.visible = True
                enemy64.draw(gamewindow, self)      

            if enemy63.hp <= 0:
                enemy63.visible = False
                gamewindow.blit(knight_death, (enemy63.x-32 , enemy63.y+32))

            if enemy64.hp <= 0:
                enemy64.visible = False
                gamewindow.blit(knight_death, (enemy64.x-32 , enemy64.y+32))


        # Room 19
        elif self.current_room == 'room19':

            font20 = pygame.font.Font(None, 20)
            font25 = pygame.font.Font(None, 25)
            font30 = pygame.font.Font(None, 30)

            text1 = font30.render("'E' to Continue", True, (255, 255, 255))
            text2 = font30.render("'R' to Continue", True, (255, 255, 255))

            text98 = font30.render('"WRONG!"', True, (255, 255, 255))
            text99 = font30.render('"Correct"', True, (255, 255, 255))
            text100 = font30.render('"YOU LOST! DIE!"', True, (255, 255, 255))
            text102 = font20.render('"E" to Pick Up', True, (255, 255, 255))

            if self.wrong == 0:
                gamewindow.blit(pygame.image.load(os.path.join(SurviveImages, "room19.png")), (0,0))
            elif self.wrong == 1:
                gamewindow.blit(pygame.image.load(os.path.join(SurviveImages, "room19-1.png")), (0,0))
            elif self.wrong == 2:
                gamewindow.blit(pygame.image.load(os.path.join(SurviveImages, "room19-2.png")), (0,0))                
            elif self.wrong == 3:
                if self.current_hp > -5:
                    self.current_hp -= 2

                if self.alive == True:
                    main_hit.play()

                if self.current_hp < 75:
                    self.alive = False

                if self.current_hp >= 75:
                    gamewindow.blit(pygame.image.load(os.path.join(SurviveImages, "room19-3.png")), (0,0))

                elif self.current_hp < 75 and self.current_hp >= 45:
                    gamewindow.blit(pygame.image.load(os.path.join(SurviveImages, "room19-3-1.png")), (0,0))
                    gamewindow.blit(death1, (565,748))

                elif self.current_hp < 45 and self.current_hp >= 1:
                    gamewindow.blit(pygame.image.load(os.path.join(SurviveImages, "room19-3-2.png")), (0,0))
                    
                gamewindow.blit(text100, (810, 145))

                                    
            elif self.question == 100 and self.wrong == 100 and self.found_son == False:
                gamewindow.blit(pygame.image.load(os.path.join(SurviveImages, "room19-4.png")), (0,0))
                
                if self.x >= 469 and self.x <= 523 and self.y <= 55:
                    gamewindow.blit(text102, (self.x + 20, self.y))
                    if keys[pygame.K_e]:
                        self.found_son = True
                        self.has_son = True
                               
            elif self.question == 100 and self.wrong == 100 and self.found_son == True:
                gamewindow.blit(pygame.image.load(os.path.join(SurviveImages, "room19-4-1.png")), (0,0))                          
                
            # 0
            text3 = font20.render('"Hello there Mr. Callaway."', True, (255, 255, 255))
            text4 = font20.render('"I have been expecting you."', True, (255, 255, 255))
            # 0.25
            text5 = font20.render('"You have impressed me thus far."', True, (255, 255, 255))
            text6 = font20.render('"But your journey is not over."', True, (255, 255, 255))
            text7 = font20.render('"I will give you your son."', True, (255, 255, 255))
            text8 = font20.render('"But first, lets play a game."', True, (255, 255, 255))
            # 0.50
            text9 = font20.render('"If you want your son back,', True, (255, 255, 255))
            text10 = font20.render('you are going to have to', True, (255, 255, 255))
            text11 = font20.render('answer some questions."', True, (255, 255, 255))
            text12 = font20.render('"Every quesiton you get wrong,', True, (255, 255, 255))
            text13 = font20.render('the closer those spikes get."', True, (255, 255, 255))
            
            # 0.75
            text14 = font20.render('"There will be 7 questions"', True, (255, 255, 255))
            text15 = font20.render('"Get 3 wrong, and those', True, (255, 255, 255))
            text16 = font20.render('spikes will kill you."', True, (255, 255, 255))
            text17 = font25.render('"Lets get started!"', True, (255, 255, 255))
        
            if self.question == 0:
                gamewindow.blit(text1, (1250, 10))
                gamewindow.blit(text3, (815, 90))
                gamewindow.blit(text4, (810, 110))
                if keys[pygame.K_e]:
                    self.question = 0.25

            elif self.question == 0.25:
                gamewindow.blit(text2, (1250, 10))
                gamewindow.blit(text5, (790, 90))
                gamewindow.blit(text6, (800, 110))
                gamewindow.blit(text7, (815, 130))
                gamewindow.blit(text8, (810, 150))
                if keys[pygame.K_r]:
                    self.question = 0.50
               
            elif self.question == 0.50:
                gamewindow.blit(text1, (1250, 10))
                gamewindow.blit(text9, (805, 90))
                gamewindow.blit(text10, (815, 110))
                gamewindow.blit(text11, (815, 130))
                gamewindow.blit(text12, (795, 170))
                gamewindow.blit(text13, (805, 190))
                if keys[pygame.K_e]:
                    self.question = 0.75

            elif self.question == 0.75:
                gamewindow.blit(text2, (1250, 10))
                gamewindow.blit(text14, (810, 90))
                gamewindow.blit(text15, (815, 110))
                gamewindow.blit(text16, (830, 130))
                gamewindow.blit(text17, (820, 170))
                if keys[pygame.K_r]:
                    self.question = 1

            
            elif self.question == 1:
                text18 = font20.render('"Question 1"', True, (255, 255, 255))
                text19 = font20.render('"What food did you give', True, (255, 255, 255))
                text20 = font20.render('to the homeless man?"', True, (255, 255, 255))
                text21 = font20.render('A: Apple', True, (255, 255, 255))
                text22 = font20.render('B: Banana', True, (255, 255, 255))
                text23 = font20.render('C: Ice Cream', True, (255, 255, 255))

                gamewindow.blit(text18, (850, 90))
                gamewindow.blit(text19, (810, 125))
                gamewindow.blit(text20, (815, 145))
                gamewindow.blit(text21, (820, 170))
                gamewindow.blit(text22, (820, 190))
                gamewindow.blit(text23, (820, 210))

                if keys[pygame.K_a]:
                    self.wrong += 1
                    self.question = 1.50

                if keys[pygame.K_b]:
                    self.question = 1.75

                if keys[pygame.K_c]:
                    self.wrong += 1
                    self.question = 1.50

            elif self.question == 1.50:
                gamewindow.blit(text1, (1250, 10))
                gamewindow.blit(text98, (850, 125)) # Wrong
                if keys[pygame.K_e]:
                    self.question = 2
                
            elif self.question == 1.75:
                gamewindow.blit(text1, (1250, 10)) 
                gamewindow.blit(text99, (850, 125)) # Correct
                if keys[pygame.K_e]:
                    self.question = 2

            elif self.question == 2:
                text24 = font20.render('"Question 2"', True, (255, 255, 255))
                text25 = font20.render('"What direction did you choose', True, (255, 255, 255))
                text26 = font20.render('when following the stream?"', True, (255, 255, 255))
                text27 = font20.render('A: Left', True, (255, 255, 255))
                text28 = font20.render('B: Right', True, (255, 255, 255))
                text29 = font20.render('C: Up', True, (255, 255, 255))
                
                gamewindow.blit(text24, (850, 90))
                gamewindow.blit(text25, (795, 125))
                gamewindow.blit(text26, (810, 145))
                gamewindow.blit(text27, (810, 170))
                gamewindow.blit(text28, (810, 190))
                gamewindow.blit(text29, (810, 210))
                
                if keys[pygame.K_a]:
                    self.question = 2.75

                if keys[pygame.K_b]:
                    self.wrong += 1
                    self.question = 2.50

                if keys[pygame.K_c]:
                    self.wrong += 1
                    self.question = 2.50

            elif self.question == 2.50:
                gamewindow.blit(text1, (1250, 10))
                gamewindow.blit(text98, (850, 125))
                if keys[pygame.K_e]:
                    self.question = 3
                
            elif self.question == 2.75:
                gamewindow.blit(text1, (1250, 10))
                gamewindow.blit(text99, (850, 125))
                if keys[pygame.K_e]:
                    self.question = 3

            elif self.question == 3:
                text30 = font20.render('"Question 3"', True, (255, 255, 255))
                text31 = font20.render('"What is your sons name?"', True, (255, 255, 255))
                text32 = font20.render('A: Jimmy', True, (255, 255, 255))
                text33 = font20.render('B: Joey', True, (255, 255, 255))
                text34 = font20.render('C: Johnny', True, (255, 255, 255))

                gamewindow.blit(text30, (850, 90))
                gamewindow.blit(text31, (800, 125))
                gamewindow.blit(text32, (820, 150))
                gamewindow.blit(text33, (820, 170))
                gamewindow.blit(text34, (820, 190))
                
                if keys[pygame.K_a]:
                    self.wrong += 1
                    self.question = 3.50

                if keys[pygame.K_b]:
                    self.wrong += 1
                    self.question = 3.50

                if keys[pygame.K_c]:
                    self.question = 3.75       

            elif self.question == 3.50 and self.wrong < 3:
                gamewindow.blit(text1, (1250, 10))
                gamewindow.blit(text98, (850, 125))
                if keys[pygame.K_e]:
                    self.question = 4
                
            elif self.question == 3.75 and self.wrong < 3:
                gamewindow.blit(text1, (1250, 10))
                gamewindow.blit(text99, (850, 125))
                if keys[pygame.K_e]:
                    self.question = 4


            elif self.question == 4 and self.wrong < 3:
                text35 = font20.render('"Question 4"', True, (255, 255, 255))
                text36 = font20.render('"What is the order of the', True, (255, 255, 255))
                text37 = font20.render('first animals you killed?"', True, (255, 255, 255))
                text38 = font20.render('A: Wolf, Spider, Rat', True, (255, 255, 255))
                text39 = font20.render('B: Spider, Wolf, Rat', True, (255, 255, 255))
                text40 = font20.render('C: Wolf, Rat, Spider', True, (255, 255, 255))

                gamewindow.blit(text35, (850, 90))
                gamewindow.blit(text36, (810, 120))
                gamewindow.blit(text37, (820, 140))
                gamewindow.blit(text38, (810, 170))
                gamewindow.blit(text39, (810, 190))
                gamewindow.blit(text40, (810, 210))
                
                if keys[pygame.K_a]:
                    self.question = 4.75

                if keys[pygame.K_b]:
                    self.wrong += 1
                    self.question = 4.50

                if keys[pygame.K_c]:
                    self.wrong += 1
                    self.question = 4.50


            elif self.question == 4.50 and self.wrong < 3:
                gamewindow.blit(text1, (1250, 10))
                gamewindow.blit(text98, (850, 125))
                if keys[pygame.K_e]:
                    self.question = 5
                
            elif self.question == 4.75 and self.wrong < 3:
                gamewindow.blit(text1, (1250, 10))
                gamewindow.blit(text99, (850, 125))
                if keys[pygame.K_e]:
                    self.question = 5


            elif self.question == 5 and self.wrong < 3:
                text41 = font20.render('"Question 5"', True, (255, 255, 255))
                text42 = font20.render('"What letter was missing', True, (255, 255, 255))
                text43 = font20.render('on the "Rest In Peace"', True, (255, 255, 255))
                text44 = font20.render('from the previous room?"', True, (255, 255, 255))
                text45 = font20.render('A: "R"', True, (255, 255, 255))
                text46 = font20.render('B: "I"', True, (255, 255, 255))
                text47 = font20.render('C: "E"', True, (255, 255, 255))

                gamewindow.blit(text41, (850, 90))
                gamewindow.blit(text42, (810, 110))
                gamewindow.blit(text43, (820, 125))
                gamewindow.blit(text44, (815, 140))
                gamewindow.blit(text45, (810, 160))
                gamewindow.blit(text46, (810, 175))
                gamewindow.blit(text47, (810, 190))

                if keys[pygame.K_a]:
                    self.wrong += 1
                    self.question = 5.50

                if keys[pygame.K_b]:
                    self.wrong += 1
                    self.question = 5.50

                if keys[pygame.K_c]:
                    self.question = 5.75         

            elif self.question == 5.50 and self.wrong < 3:
                gamewindow.blit(text1, (1250, 10))
                gamewindow.blit(text98, (850, 125))
                if keys[pygame.K_e]:
                    self.question = 6
                
            elif self.question == 5.75 and self.wrong < 3:
                gamewindow.blit(text1, (1250, 10))
                gamewindow.blit(text99, (850, 125))
                if keys[pygame.K_e]:
                    self.question = 6

            elif self.question == 6 and self.wrong < 3:
                text48 = font20.render('"Question 6"', True, (255, 255, 255))
                text49 = font20.render('"What was the sequence', True, (255, 255, 255))
                text50 = font20.render('to complete the bridge?"', True, (255, 255, 255))
                text51 = font20.render('A: 2 - 4 - 1 - 8', True, (255, 255, 255))
                text52 = font20.render('B: 4 - 2 - 8 - 1', True, (255, 255, 255))
                text53 = font20.render('C: 1 - 4 - 8 - 2', True, (255, 255, 255))

                gamewindow.blit(text48, (850, 90))
                gamewindow.blit(text49, (810, 110))
                gamewindow.blit(text50, (820, 125))
                gamewindow.blit(text51, (810, 145))
                gamewindow.blit(text52, (810, 165))
                gamewindow.blit(text53, (810, 185))

                if keys[pygame.K_a]:
                    self.wrong += 1
                    self.question = 6.50

                if keys[pygame.K_b]:
                    self.question = 6.75

                if keys[pygame.K_c]:
                    self.wrong += 1
                    self.question = 6.50
                    
            elif self.question == 6.50 and self.wrong < 3:
                gamewindow.blit(text1, (1250, 10))
                gamewindow.blit(text98, (850, 125))
                if keys[pygame.K_e]:
                    self.question = 7
                
            elif self.question == 6.75 and self.wrong < 3:
                gamewindow.blit(text1, (1250, 10))
                gamewindow.blit(text99, (850, 125))
                if keys[pygame.K_e]:
                    self.question = 7

            elif self.question == 7 and self.wrong < 3:
                text54 = font20.render('"Last Question"', True, (255, 255, 255))
                text55 = font20.render('"What is your last name?', True, (255, 255, 255))
                text56 = font20.render('A: Callaway', True, (255, 255, 255))
                text57 = font20.render('B: Calloway', True, (255, 255, 255))
                text58 = font20.render('C: Caleway', True, (255, 255, 255))

                gamewindow.blit(text54, (850, 90))
                gamewindow.blit(text55, (820, 120))
                gamewindow.blit(text56, (820, 150))
                gamewindow.blit(text57, (820, 170))
                gamewindow.blit(text58, (820, 190))

                if keys[pygame.K_a]:
                    self.question = 7.75

                if keys[pygame.K_b]:
                    self.wrong += 1
                    self.question = 7.50

                if keys[pygame.K_c]:
                    self.wrong += 1
                    self.question = 7.50

            elif self.question == 7.50 and self.wrong < 3:
                gamewindow.blit(text1, (1250, 10))
                gamewindow.blit(text98, (850, 125))
                if keys[pygame.K_e]:
                    self.question = 8
                
            elif self.question == 7.75 and self.wrong < 3:
                gamewindow.blit(text1, (1250, 10))
                gamewindow.blit(text99, (850, 125))
                if keys[pygame.K_e]:
                    self.question = 8

            elif self.question == 8 and self.wrong < 3:
                text59 = font25.render('"A deal is a deal"', True, (255, 255, 255))
                text60 = font25.render('"You may have your son"', True, (255, 255, 255))

                gamewindow.blit(text2, (1250, 10))
                gamewindow.blit(text59, (820, 120))
                gamewindow.blit(text60, (800, 150))
                
                if keys[pygame.K_r]:
                    self.question = 100
                    self.wrong = 100
                    self.can_move = True
                
                    
        # Room 20
        elif self.current_room == 'room20':

            font30 = pygame.font.Font(None, 30)
            
            text1 = font30.render('Door Is Locked', True, (160, 0, 0 ))
            text2 = font30.render('"Space" to Shoot Gun', True, (255, 255, 255))

            if self.hog == 'hanging' and self.damaged_door == 0:
                gamewindow.blit(pygame.image.load(os.path.join(SurviveImages, "room20.png")), (0,0))

                if self.x >= 1009 and self.x <= 1036 and self.y == 352 and\
                   keys[pygame.K_s] and self.has_sword == True and self.swing_sword == True and\
                   self.up == True:
                    self.hog = 'cut'
                

            if self.hog == 'cut' and self.damaged_door == 0:
                gamewindow.blit(pygame.image.load(os.path.join(SurviveImages, "room20-1.png")), (0,0))
                if self.has_gun == False:
                    gamewindow.blit(gun_ground, (1050,640))

                if self.x >= 973 and self.x <= 1072 and self.y >= 532 and self.y <= 613:
                    self.has_gun = True

            if self.hog == 'cut' and self.damaged_door == 1:
                gamewindow.blit(pygame.image.load(os.path.join(SurviveImages, "room20-2.png")), (0,0))
                
            if self.hog == 'cut' and self.damaged_door == 2:
                gamewindow.blit(pygame.image.load(os.path.join(SurviveImages, "room20-2-1.png")), (0,0))

            if self.hog == 'cut' and self.damaged_door == 3:
                gamewindow.blit(pygame.image.load(os.path.join(SurviveImages, "room20-2-2.png")), (0,0))

            if self.hog == 'cut' and self.damaged_door == 4:
                gamewindow.blit(pygame.image.load(os.path.join(SurviveImages, "room20-2-3.png")), (0,0))

            if self.hog == 'cut' and self.damaged_door == 5:
                gamewindow.blit(pygame.image.load(os.path.join(SurviveImages, "room20-2-4.png")), (0,0))
                self.has_key = True

            if self.x >= 667 and self.x <= 712 and self.y <= 352 and\
               self.has_key == False and self.up == True:
                gamewindow.blit(text1, (600, 100))

            if self.hog == 'cut' and self.has_gun == True:
                if enemy65.hp > 0:
                    gamewindow.blit(text2, (600, 100))
                    enemy65.visible = True
                    enemy65.draw(gamewindow, self)
                    
            if enemy65.hp <= 0:
                enemy65.visible = False
                gamewindow.blit(knight_death, (enemy65.x-32 , enemy65.y+32))

        # Room 21
        elif self.current_room == 'room21':
            gamewindow.blit(pygame.image.load(os.path.join(SurviveImages, "room21.png")), (0,0))
            font20 = pygame.font.Font(None, 20)
            font25 = pygame.font.Font(None, 25)
            font30 = pygame.font.Font(None, 30)

            text1 = font30.render('Objective: Guard Your Son', True, (255, 255, 255))

            gamewindow.blit(text1, (1160, 10))

            if enemy66.hp <= 0:
                enemy66.visible = False
                gamewindow.blit(wizard_death, (enemy66.x-32 , enemy66.y+32))

            if enemy67.hp <= 0:
                enemy67.visible = False
                gamewindow.blit(wizard_death, (enemy67.x-32 , enemy67.y+32))

            if enemy68.hp <= 0:
                enemy68.visible = False
                gamewindow.blit(wizard_death, (enemy68.x-32 , enemy68.y+32))

            if enemy69.hp <= 0:
                enemy69.visible = False
                gamewindow.blit(wizard_death, (enemy69.x-32 , enemy69.y+32))

            if enemy70.hp <= 0:
                enemy70.visible = False
                gamewindow.blit(wizard_death, (enemy70.x-32 , enemy70.y+32))

            if enemy71.hp <= 0:
                enemy71.visible = False
                gamewindow.blit(smallspider_death, (enemy71.x-32 , enemy71.y+32))

            if enemy72.hp <= 0:
                enemy72.visible = False
                gamewindow.blit(smallspider_death, (enemy72.x-32 , enemy72.y+32))

            if enemy73.hp <= 0:
                enemy73.visible = False
                gamewindow.blit(smallspider_death, (enemy73.x-32 , enemy73.y+32))

            if enemy74.hp <= 0:
                enemy74.visible = False
                gamewindow.blit(bat_death, (enemy74.x-32 , enemy74.y+32))

            if enemy75.hp <= 0:
                enemy75.visible = False
                gamewindow.blit(bat_death, (enemy75.x-32 , enemy75.y+32))

            if enemy76.hp <= 0:
                enemy76.visible = False
                gamewindow.blit(goblin_death, (enemy76.x-32 , enemy76.y+32))

            if enemy77.hp <= 0:
                enemy77.visible = False
                gamewindow.blit(smallwolf_death, (enemy77.x-32 , enemy77.y+32))

            if enemy78.hp <= 0:
                enemy78.visible = False
                gamewindow.blit(bigwolf_death, (enemy78.x-32 , enemy78.y+32))

            if enemy79.hp <= 0:
                enemy79.visible = False
                gamewindow.blit(bigwolf_death, (enemy79.x-32 , enemy79.y+32))

            if enemy80.hp <= 0:
                enemy80.visible = False
                gamewindow.blit(bigwolf_death, (enemy80.x-32 , enemy80.y+32))

            if enemy66.hp > 0:
                enemy66.visible = True
                enemy66.draw(gamewindow, self)
                
            if enemy67.hp > 0:
                enemy67.visible = True
                enemy67.draw(gamewindow, self)
                
            if enemy68.hp > 0:
                enemy68.visible = True
                enemy68.draw(gamewindow, self)

            if enemy69.hp > 0:
                enemy69.visible = True
                enemy69.draw(gamewindow, self)

            if enemy70.hp > 0:
                enemy70.visible = True
                enemy70.draw(gamewindow, self)

            if enemy71.hp > 0:
                enemy71.visible = True
                enemy71.draw(gamewindow, self)

            if enemy72.hp > 0:
                enemy72.visible = True
                enemy72.draw(gamewindow, self)

            if enemy73.hp > 0:
                enemy73.visible = True
                enemy73.draw(gamewindow, self)
                
            if enemy74.hp > 0:
                enemy74.visible = True
                enemy74.draw(gamewindow, self)

            if enemy75.hp > 0:
                enemy75.visible = True
                enemy75.draw(gamewindow, self)

            if enemy76.hp > 0:
                enemy76.visible = True
                enemy76.draw(gamewindow)

            if enemy77.hp > 0:
                enemy77.visible = True
                enemy77.draw(gamewindow, self)

            if enemy78.hp > 0:
                enemy78.visible = True
                enemy78.draw(gamewindow, self)

            if enemy79.hp > 0:
                enemy79.visible = True
                enemy79.draw(gamewindow, self)

            if enemy80.hp > 0:
                enemy80.visible = True
                enemy80.draw(gamewindow, self)


            if enemy66.visible == False and enemy67.visible == False and\
               enemy68.visible == False and enemy69.visible == False and\
               enemy70.visible == False and enemy71.visible == False and\
               enemy72.visible == False and enemy73.visible == False and\
               enemy74.visible == False and enemy75.visible == False and\
               enemy76.visible == False and enemy77.visible == False and\
               enemy78.visible == False and enemy79.visible == False and\
               enemy80.visible == False:
                self.objective7 = True
                

        # Room 22
        elif self.current_room == 'room22':

            font20 = pygame.font.Font(None, 20)
            font25 = pygame.font.Font(None, 25)
            font30 = pygame.font.Font(None, 30)

            text1 = font30.render('Objective: Get In Car and Escape', True, (255, 255, 255))

            if self.in_car == False:
                gamewindow.blit(pygame.image.load(os.path.join(SurviveImages, "room22.png")), (0,0))                
                text2 = font20.render("Press 'Q' to Enter Car", True, (255, 255, 255))
                
                if self.x <= 415 and self.x >= 199 and self.y <= 451 and self.y >= 298 and\
                   self.has_son == True:
                    gamewindow.blit(text2, (self.x, self.y - 20))
                    if keys[pygame.K_q] and self.has_son and self.in_car == False:
                        self.in_car = True
                        self.has_son = False
                        self.found_son = False
                        self.speed = 20
                        self.has_gun = False
                        self.has_punch = False
                        self.has_sword = False

            if self.in_car == True:
                gamewindow.blit(pygame.image.load(os.path.join(SurviveImages, "room22-1.png")), (0,0))
            gamewindow.blit(text1, (1100, 10))
            
        # Room 23
        elif self.current_room == 'room23':
            gamewindow.blit(pygame.image.load(os.path.join(SurviveImages, "room23.png")), (0,0))

            if enemy81.hp <= 0:
                enemy81.visible = False
                gamewindow.blit(knight_death, (enemy81.x-32 , enemy81.y+32))
                
            if enemy82.hp <= 0:
                enemy82.visible = False
                gamewindow.blit(knight_death, (enemy82.x-32 , enemy82.y+32))

            if enemy81.hp > 0:
                enemy81.visible = True
                enemy81.draw(gamewindow, self)
                
            if enemy82.hp > 0:
                enemy82.visible = True
                enemy82.draw(gamewindow, self)

        # Room 24
        elif self.current_room == 'room24':
            gamewindow.blit(pygame.image.load(os.path.join(SurviveImages, "room24.png")), (0,0))
            font20 = pygame.font.Font(None, 20)
            font40 = pygame.font.Font(None, 40)
            enemy81.visible = False
            enemy82.visible = False
            text1 = font40.render('WATCH OUT FOR THE DEER!', True, (255, 255, 255))
            text2 = font40.render('Or Not...', True, (255, 255, 255))
            text3 = font40.render('Absolute Savage', True, (255, 255, 255))         

            if enemy83.visible == True and enemy84.visible == True and enemy85.visible == True and\
               enemy86.visible == True and enemy87.visible == True and enemy88.visible == True and\
               enemy89.visible == True and enemy90.visible == True:
                gamewindow.blit(text1, (500, 475))
            
            elif enemy83.visible == True or enemy84.visible == True or enemy85.visible == True or\
               enemy86.visible == True or enemy87.visible == True or enemy88.visible == True or\
               enemy89.visible == True or enemy90.visible == True:
                gamewindow.blit(text2, (600, 475))

            else:
                gamewindow.blit(text3, (600, 475))
                
            if enemy83.hp <= 0:
                enemy83.visible = False
                gamewindow.blit(deer_big_death, (enemy83.x-32 , enemy83.y+32))

            if enemy84.hp <= 0:
                enemy84.visible = False
                gamewindow.blit(deer_big_death, (enemy84.x-32 , enemy84.y+32))  

            if enemy85.hp <= 0:
                enemy85.visible = False
                gamewindow.blit(deer_big_death, (enemy85.x-32 , enemy85.y+32))

            if enemy86.hp <= 0:
                enemy86.visible = False
                gamewindow.blit(deer_big_death, (enemy86.x-32 , enemy86.y+32))

            if enemy87.hp <= 0:
                enemy87.visible = False
                gamewindow.blit(deer_big_death, (enemy87.x-32 , enemy87.y+32))

            if enemy88.hp <= 0:
                enemy88.visible = False
                gamewindow.blit(deer_big_death, (enemy88.x-32 , enemy88.y+32))

            if enemy89.hp <= 0:
                enemy89.visible = False
                gamewindow.blit(deer_small_death, (enemy89.x-32 , enemy89.y+32))

            if enemy90.hp <= 0:
                enemy90.visible = False
                gamewindow.blit(deer_small_death, (enemy90.x-32 , enemy90.y+32))

            if enemy83.hp > 0:
                enemy83.visible = True
                enemy83.draw(gamewindow)

            if enemy84.hp > 0:
                enemy84.visible = True
                enemy84.draw(gamewindow)

            if enemy85.hp > 0:
                enemy85.visible = True
                enemy85.draw(gamewindow)

            if enemy86.hp > 0:
                enemy86.visible = True
                enemy86.draw(gamewindow)

            if enemy87.hp > 0:
                enemy87.visible = True
                enemy87.draw(gamewindow)

            if enemy88.hp > 0:
                enemy88.visible = True
                enemy88.draw(gamewindow)

            if enemy89.hp > 0:
                enemy89.visible = True
                enemy89.draw(gamewindow)

            if enemy90.hp > 0:
                enemy90.visible = True
                enemy90.draw(gamewindow)

            
        # Room 25
        elif self.current_room == 'room25':
            gamewindow.blit(pygame.image.load(os.path.join(SurviveImages, "room25.png")), (0,0))

            enemy83.visible = False
            enemy84.visible = False
            enemy85.visible = False
            enemy86.visible = False
            enemy87.visible = False
            enemy88.visible = False
            enemy89.visible = False
            enemy90.visible = False

            if enemy91.hp <= 0:
                enemy91.visible = False
                gamewindow.blit(wizard_death, (enemy91.x-32 , enemy91.y+32))
                
            if enemy92.hp <= 0:
                enemy92.visible = False
                gamewindow.blit(deer_big_death, (enemy92.x-32 , enemy92.y+32))
     
            if enemy91.hp > 0:
                enemy91.visible = True
                enemy91.draw(gamewindow, self)

            if enemy92.hp > 0:
                enemy92.visible = True
                enemy92.draw(gamewindow)


        # Room 26
        elif self.current_room == 'room26':
            gamewindow.blit(pygame.image.load(os.path.join(SurviveImages, "room26.png")), (0,0))
            enemy91.visible = False
            enemy92.visible = False
            font40 = pygame.font.Font(None, 40)
            text1 = font40.render('Killing Spree!', True, (255, 255, 255))

            if enemy93.hp <= 0:
                enemy93.visible = False
                gamewindow.blit(wizard_death, (enemy93.x-32 , enemy93.y+32))

            if enemy94.hp <= 0:
                enemy94.visible = False
                gamewindow.blit(bigwolf_death, (enemy94.x-32 , enemy94.y+32))

            if enemy95.hp <= 0:
                enemy95.visible = False
                gamewindow.blit(bigwolf_death, (enemy95.x-32 , enemy95.y+32))

            if enemy96.hp <= 0:
                enemy96.visible = False
                gamewindow.blit(rat_death, (enemy96.x-32 , enemy96.y+32))

            if enemy97.hp <= 0:
                enemy97.visible = False
                gamewindow.blit(rat_death, (enemy97.x-32 , enemy97.y+32))

            if enemy98.hp <= 0:
                enemy98.visible = False
                gamewindow.blit(smallwolf_death, (enemy98.x-32 , enemy98.y+32))

            if enemy99.hp <= 0:
                enemy99.visible = False
                gamewindow.blit(smallwolf_death, (enemy99.x-32 , enemy99.y+32))

            if enemy100.hp <= 0:
                enemy100.visible = False
                gamewindow.blit(bigspider_death, (enemy100.x-32 , enemy100.y+32))

            if enemy101.hp <= 0:
                enemy101.visible = False
                gamewindow.blit(bigspider_death, (enemy101.x-32 , enemy101.y+32))

            if enemy102.hp <= 0:
                enemy102.visible = False
                gamewindow.blit(goblin_death, (enemy102.x-32 , enemy102.y+32))

            if enemy103.hp <= 0:
                enemy103.visible = False
                gamewindow.blit(goblin_death, (enemy103.x-32 , enemy103.y+32))

            if enemy104.hp <= 0:
                enemy104.visible = False
                gamewindow.blit(smallspider_death, (enemy104.x-32 , enemy104.y+32))

            if enemy105.hp <= 0:
                enemy105.visible = False
                gamewindow.blit(smallspider_death, (enemy105.x-32 , enemy105.y+32))

            if enemy106.hp <= 0:
                enemy106.visible = False
                gamewindow.blit(bat_death, (enemy106.x-32 , enemy106.y+32))

            if enemy107.hp <= 0:
                enemy107.visible = False
                gamewindow.blit(bat_death, (enemy107.x-32 , enemy107.y+32))

            if enemy93.hp > 0:
                enemy93.visible = True
                enemy93.draw(gamewindow, self)

            if enemy94.hp > 0:
                enemy94.visible = True
                enemy94.draw(gamewindow, self)

            if enemy95.hp > 0:
                enemy95.visible = True
                enemy95.draw(gamewindow, self)

            if enemy96.hp > 0:
                enemy96.visible = True
                enemy96.draw(gamewindow, self)

            if enemy97.hp > 0:
                enemy97.visible = True
                enemy97.draw(gamewindow, self)

            if enemy98.hp > 0:
                enemy98.visible = True
                enemy98.draw(gamewindow, self)

            if enemy99.hp > 0:
                enemy99.visible = True
                enemy99.draw(gamewindow, self)

            if enemy100.hp > 0:
                enemy100.visible = True
                enemy100.draw(gamewindow, self)

            if enemy101.hp > 0:
                enemy101.visible = True
                enemy101.draw(gamewindow, self)

            if enemy102.hp > 0:
                enemy102.visible = True
                enemy102.draw(gamewindow)

            if enemy103.hp > 0:
                enemy103.visible = True
                enemy103.draw(gamewindow)

            if enemy104.hp > 0:
                enemy104.visible = True
                enemy104.draw(gamewindow, self)

            if enemy105.hp > 0:
                enemy105.visible = True
                enemy105.draw(gamewindow, self)

            if enemy106.hp > 0:
                enemy106.visible = True
                enemy106.draw(gamewindow, self)

            if enemy107.hp > 0:
                enemy107.visible = True
                enemy107.draw(gamewindow, self)

            if enemy93.visible == False and enemy94.visible == False and\
               enemy95.visible == False and enemy96.visible == False and\
               enemy97.visible == False and enemy98.visible == False and\
               enemy99.visible == False and enemy101.visible == False and\
               enemy101.visible == False and enemy102.visible == False and\
               enemy103.visible == False and enemy104.visible == False and\
               enemy105.visible == False and enemy106.visible == False and\
               enemy107.visible == False:
                gamewindow.blit(text1, (1225, 10))
                self.objective8 = True

        # Room 27
        elif self.current_room == 'room27':
            gamewindow.blit(pygame.image.load(os.path.join(SurviveImages, "room27.png")), (0,0))

        # Room 28
        elif self.current_room == 'room28':
            gamewindow.blit(pygame.image.load(os.path.join(SurviveImages, "room28.png")), (0,0))

        # Room 29
        elif self.current_room == 'room29':
            gamewindow.blit(pygame.image.load(os.path.join(SurviveImages, "room29.png")), (0,0))
            font40 = pygame.font.Font(None, 40)                       
            text1 = font40.render('DONT KILL THE DEER!', True, (255, 255, 255))
            text2 = font40.render('You Are Terrible', True, (255, 255, 255))

            if enemy108.hp <= 0:
                enemy108.visible = False
                gamewindow.blit(deer_big_death, (enemy108.x-16 , enemy108.y+16))

            if enemy109.hp <= 0:
                enemy109.visible = False
                gamewindow.blit(deer_big_death, (enemy109.x-16 , enemy109.y+16))

            if enemy110.hp <= 0:
                enemy110.visible = False
                gamewindow.blit(deer_small_death, (enemy110.x-16 , enemy110.y+16))

            if enemy111.hp <= 0:
                enemy111.visible = False
                gamewindow.blit(deer_small_death, (enemy111.x-16 , enemy111.y+16))

            if enemy108.hp > 0:
                enemy108.visible = True
                enemy108.draw(gamewindow)

            if enemy109.hp > 0:
                enemy109.visible = True
                enemy109.draw(gamewindow)

            if enemy110.hp > 0:
                enemy110.visible = True
                enemy110.draw(gamewindow)

            if enemy111.hp > 0:
                enemy111.visible = True
                enemy111.draw(gamewindow)

            if enemy108.visible == True or enemy109.visible == True or\
               enemy110.visible == True or enemy111.visible == True:
                gamewindow.blit(text1, (950, 475))
            else:
                gamewindow.blit(text2, (975, 475))
                
                
        # Room 30
        elif self.current_room == 'room30':
            gamewindow.blit(pygame.image.load(os.path.join(SurviveImages, "room30.png")), (0,0))
            font50 = pygame.font.Font(None, 50)
            text1 = font50.render('KILLTACULAR!', True, (255, 255, 255))
            enemy108.visible = False
            enemy109.visible = False
            enemy110.visible = False
            enemy111.visible = False

            if enemy112.hp <= 0:
                enemy112.visible = False
                gamewindow.blit(knight_death, (enemy112.x-32 , enemy112.y+32))

            if enemy113.hp <= 0:
                enemy113.visible = False
                gamewindow.blit(knight_death, (enemy113.x-32 , enemy113.y+32))

            if enemy114.hp <= 0:
                enemy114.visible = False
                gamewindow.blit(knight_death, (enemy114.x-32 , enemy114.y+32))

            if enemy115.hp <= 0:
                enemy115.visible = False
                gamewindow.blit(knight_death, (enemy115.x-32 , enemy115.y+32))

            if enemy116.hp <= 0:
                enemy116.visible = False
                gamewindow.blit(knight_death, (enemy116.x-32 , enemy116.y+32))

            if enemy117.hp <= 0:
                enemy117.visible = False
                gamewindow.blit(knight_death, (enemy117.x-32 , enemy117.y+32))

            if enemy118.hp <= 0:
                enemy118.visible = False
                gamewindow.blit(knight_death, (enemy118.x-32 , enemy118.y+32))

            if enemy119.hp <= 0:
                enemy119.visible = False
                gamewindow.blit(knight_death, (enemy119.x-32 , enemy119.y+32))

            if enemy120.hp <= 0:
                enemy120.visible = False
                gamewindow.blit(knight_death, (enemy120.x-32 , enemy120.y+32))

            if enemy112.hp > 0:
                enemy112.visible = True
                enemy112.draw(gamewindow)

            if enemy113.hp > 0:
                enemy113.visible = True
                enemy113.draw(gamewindow)

            if enemy114.hp > 0:
                enemy114.visible = True
                enemy114.draw(gamewindow)

            if enemy115.hp > 0:
                enemy115.visible = True
                enemy115.draw(gamewindow)

            if enemy116.hp > 0:
                enemy116.visible = True
                enemy116.draw(gamewindow)

            if enemy117.hp > 0:
                enemy117.visible = True
                enemy117.draw(gamewindow)

            if enemy118.hp > 0:
                enemy118.visible = True
                enemy118.draw(gamewindow)

            if enemy119.hp > 0:
                enemy119.visible = True
                enemy119.draw(gamewindow)

            if enemy120.hp > 0:
                enemy120.visible = True
                enemy120.draw(gamewindow)

            if enemy112.visible == False and enemy113.visible == False and\
               enemy114.visible == False and enemy115.visible == False and\
               enemy116.visible == False and enemy117.visible == False and\
               enemy118.visible == False and enemy119.visible == False and\
               enemy120.visible == False:
                gamewindow.blit(text1, (975, 475))
                
        # Room 31
        elif self.current_room == 'room31':
            font20 = pygame.font.Font(None, 20)
            font25 = pygame.font.Font(None, 25)
            font30 = pygame.font.Font(None, 30)

            text1 = font20.render("Press 'Q' to Exit Car", True, (255, 255, 255))
            text2 = font30.render('Objective: Get Revenge', True, (255,255,255))
            text3 = font30.render('Leave the Man and Dog Alone', True, (255,255,255))
            text4 = font30.render('Police Saw That!', True, (255,255, 255))
            text5 = font25.render('Die You Murderer!', True, (255, 255, 255))

            if self.in_car == True:
                gamewindow.blit(pygame.image.load(os.path.join(SurviveImages, "room31.png")), (0,0))
                gamewindow.blit(text1, (self.x + 20, self.y - 20))
                self.x = 0
                self.y = 611
                self.can_move = False

                if keys[pygame.K_q]:
                    self.can_move = True
                    self.in_car = False
                    self.has_son = True
                    self.found_son = True
                    self.speed = 10
                    self.has_gun = True
                    self.has_punch = True
                    self.has_sword = True
                    self.x = 41
                    self.y = 501

            if self.in_car == False:
                gamewindow.blit(pygame.image.load(os.path.join(SurviveImages, "room31-1.png")), (0,0))

            gamewindow.blit(text2, (1175, 10))
            
            enemy122.hp = 50
            enemy123.hp = 50
            enemy124.hp = 50
            enemy125.hp = 50
            
            if enemy121.hp <= 0:
                enemy121.visible = False
                gamewindow.blit(dog_man_death, (enemy121.x , enemy121.y+32))
                gamewindow.blit(text4, (1220, 40))
                gamewindow.blit(text5, (enemy125.x - 15, enemy125.y - 17))
                
                if enemy122.hp > 0:
                    enemy122.visible = True
                    enemy122.draw(gamewindow, self)
                if enemy123.hp > 0:
                    enemy123.visible = True
                    enemy123.draw(gamewindow, self)             
                if enemy124.hp > 0:
                    enemy124.visible = True
                    enemy124.draw(gamewindow, self)
                if enemy125.hp > 0:
                    enemy125.visible = True
                    enemy125.draw(gamewindow, self)
       
            if enemy121.hp > 0:
                gamewindow.blit(text3, (1145, 40))
                enemy121.visible = True
                enemy121.draw(gamewindow)


        # Room 32
        elif self.current_room == 'room32':
            gamewindow.blit(pygame.image.load(os.path.join(SurviveImages, "room32.png")), (0,0))
            enemy121.visible = False
            self.has_key = False

            if enemy126.hp <= 0:
                enemy126.visible = False
                gamewindow.blit(bear_death, (enemy126.x-32 , enemy126.y+32))
            if enemy127.hp <= 0:
                enemy127.visible = False
                gamewindow.blit(bear_death, (enemy127.x-32 , enemy127.y+32))
            if enemy128.hp <= 0:
                enemy128.visible = False
                gamewindow.blit(bear_death, (enemy128.x-32 , enemy128.y+32))
            if enemy129.hp <= 0:
                enemy129.visible = False
                gamewindow.blit(bear_death, (enemy129.x-32 , enemy129.y+32))
            if enemy130.hp <= 0:
                enemy130.visible = False
                gamewindow.blit(bear_death, (enemy130.x-32 , enemy130.y+32))

            if enemy126.hp > 0:
                enemy126.visible = True
                enemy126.draw(gamewindow, self)
            if enemy127.hp > 0:
                enemy127.visible = True
                enemy127.draw(gamewindow, self)             
            if enemy128.hp > 0:
                enemy128.visible = True
                enemy128.draw(gamewindow, self)
            if enemy129.hp > 0:
                enemy129.visible = True
                enemy129.draw(gamewindow, self)
            if enemy130.hp > 0:
                enemy130.visible = True
                enemy130.draw(gamewindow, self)

            if enemy126.visible == False and enemy127.visible == False and\
               enemy128.visible == False and enemy129.visible == False and\
               enemy130.visible == False:
                self.objective9 = True
                

        # Room 33
        elif self.current_room == 'room33':
            gamewindow.blit(pygame.image.load(os.path.join(SurviveImages, "room33.png")), (0,0))
            font20 = pygame.font.Font(None, 20)
            font25 = pygame.font.Font(None, 25)
            font30 = pygame.font.Font(None, 30)

            text1 = font30.render("Your Son Is Scared! You Can't Leave Him!", True, (255, 255, 255))
            text2 = font20.render('"G" to Pick Up Chicken', True, (255, 255, 255))
            text3 = font20.render('"H" to Drop Chicken', True, (255, 255, 255))
            
            if self.x < -48 and self.has_son == False:
                gamewindow.blit(text1, (1000, 10))
                
            if enemy131.hp > 0:
                enemy131.visible = True
                enemy131.draw(gamewindow)
            if enemy132.hp > 0:
                enemy132.visible = True
                enemy132.draw(gamewindow)             
            if enemy133.hp > 0:
                enemy133.visible = True
                enemy133.draw(gamewindow)
            if enemy134.hp > 0:
                enemy134.visible = True
                enemy134.draw(gamewindow)

            if enemy131.hp <= 0:
                enemy131.visible = False
                if self.has_chicken == False and self.found_chicken == False:
                    gamewindow.blit(chicken_death_right, (enemy131.x , enemy131.y+16))
                    
            if enemy131.visible == False and self.found_chicken == False:
                if self.x > 271 and self.x < 343 and self.y >= 100 and self.y < 200:
                    gamewindow.blit(text2, (self.x - 5, self.y - 25))
                    if keys[pygame.K_g]:
                        self.found_chicken = True
                        self.has_chicken = True

            if enemy132.hp <= 0:
                enemy132.visible = False
                gamewindow.blit(chicken_death_left, (enemy132.x , enemy132.y+16))
                
            if enemy133.hp <= 0:
                enemy133.visible = False
                gamewindow.blit(chicken_death_left, (enemy133.x , enemy133.y+16))
                
            if enemy134.hp <= 0:
                enemy134.visible = False
                gamewindow.blit(chicken_death_right, (enemy134.x , enemy134.y+16))

            if self.has_chicken == True:
                self.has_gun = False
                self.has_punch = False
                self.has_sword = False

                gamewindow.blit(text3, (self.x, self.y - 25))              

                if self.left == True and self.standing == False:
                    gamewindow.blit(chicken_death_left, (self.x + 30 , self.y + 70))

                if self.left == True and self.standing == True:
                    gamewindow.blit(chicken_death_left, (self.x + 47 , self.y + 75))

                if self.right == True and self.standing == False:
                    gamewindow.blit(chicken_death_right, (self.x + 60 , self.y + 70))

                if self.right == True and self.standing == True:
                    gamewindow.blit(chicken_death_right, (self.x + 40 , self.y + 75))

                if self.up == True and self.standing == True:
                    gamewindow.blit(chicken_death_left, (self.x + 45 , self.y + 60))

                if self.up == True and self.standing == False:
                    gamewindow.blit(chicken_death_left, (self.x + 45 , self.y + 60))

            if self.has_chicken == True and keys[pygame.K_h]:
                chicken_list.append((self.x + self.width//2 - 15, self.y + 80))
                self.chicken_location = chicken_list[0]
                chicken_list.clear()
                self.has_chicken = False
                self.chicken_room = 'room33'
                self.has_gun = True
                self.has_punch = True
                self.has_sword = True
            
            if self.has_chicken == False and self.found_chicken == True:
                if self.chicken_room == 'room33':
                    gamewindow.blit(chicken_death_left, (self.chicken_location))

            if self.has_chicken == False and self.found_chicken == True:
                if self.x >= self.chicken_location[0] - 76 and\
                   self.x <= self.chicken_location[0] - 22 and\
                   self.y <= self.chicken_location[1] and\
                   self.y >= self.chicken_location[1] - 96:
                    if self.chicken_room == 'room33':
                        gamewindow.blit(text2, (self.x + 20, self.y))
                        if keys[pygame.K_g]:
                            self.has_chicken = True

        # Room 34
        elif self.current_room == 'room34':

            enemy131.visible = False
            enemy132.visible = False
            enemy133.visible = False
            enemy134.visible = False

            font20 = pygame.font.Font(None, 20)
            font25 = pygame.font.Font(None, 25)
            font30 = pygame.font.Font(None, 30)

            text1 = font30.render("Your Son Is Scared! You Can't Leave Him!", True, (255, 255, 255))
            text4 = font30.render("Bring The Chicken... Trust Me", True, (255, 255, 255))

            if self.cave == 'closed' and self.found_rock == False:
                gamewindow.blit(pygame.image.load(os.path.join(SurviveImages, "room34.png")), (0,0))

            if self.cave == 'closed' and self.found_rock == True:
                gamewindow.blit(pygame.image.load(os.path.join(SurviveImages, "room34-1.png")), (0,0))          

            if self.cave == 'open':
                gamewindow.blit(pygame.image.load(os.path.join(SurviveImages, "room34-2.png")), (0,0))

                if enemy135.hp <= 0:
                    enemy135.visible = False
                    gamewindow.blit(bat_death, (enemy135.x-32 , enemy135.y+32))

                if enemy136.hp <= 0:
                    enemy136.visible = False
                    gamewindow.blit(smallspider_death, (enemy136.x-32 , enemy136.y+32))
                    
                if enemy135.hp > 0:
                    enemy135.visible = True
                    enemy135.draw(gamewindow, self)

                if enemy136.hp > 0:
                    enemy136.visible = True
                    enemy136.draw(gamewindow, self)
   
                if self.y < 110 and self.x <= 676 and self.x >= 492 and\
                   self.has_son == False:
                    gamewindow.blit(text1, (1000, 10)) 
                
                if self.y < 110 and self.x <= 676 and self.x >= 492 and\
                   self.has_chicken == False:
                    gamewindow.blit(text4, (1050, 40))


            # Chicken
            text2 = font20.render('"G" to Pick Up Chicken', True, (255, 255, 255))
            text3 = font20.render('"H" to Drop Chicken', True, (255, 255, 255))
            
            if self.has_chicken == True:
                self.has_gun = False
                self.has_punch = False
                self.has_sword = False

                gamewindow.blit(text3, (self.x, self.y - 25))              

                if self.left == True and self.standing == False:
                    gamewindow.blit(chicken_death_left, (self.x + 30 , self.y + 70))

                if self.left == True and self.standing == True:
                    gamewindow.blit(chicken_death_left, (self.x + 47 , self.y + 75))

                if self.right == True and self.standing == False:
                    gamewindow.blit(chicken_death_right, (self.x + 60 , self.y + 70))

                if self.right == True and self.standing == True:
                    gamewindow.blit(chicken_death_right, (self.x + 40 , self.y + 75))

                if self.up == True and self.standing == True:
                    gamewindow.blit(chicken_death_left, (self.x + 45 , self.y + 60))

                if self.up == True and self.standing == False:
                    gamewindow.blit(chicken_death_left, (self.x + 45 , self.y + 60))

            if self.has_chicken == True and keys[pygame.K_h]:
                chicken_list.append((self.x + self.width//2 - 15, self.y + 80))
                self.chicken_location = chicken_list[0]
                chicken_list.clear()
                self.has_chicken = False
                self.chicken_room = 'room34'
                self.has_gun = True
                self.has_punch = True
                self.has_sword = True
            
            if self.has_chicken == False and self.found_chicken == True:
                if self.chicken_room == 'room34':
                    gamewindow.blit(chicken_death_left, (self.chicken_location))

            if self.has_chicken == False and self.found_chicken == True and self.has_rock == False:
                if self.x >= self.chicken_location[0] - 76 and\
                   self.x <= self.chicken_location[0] - 22 and\
                   self.y <= self.chicken_location[1] and\
                   self.y >= self.chicken_location[1] - 96:
                    gamewindow.blit(text2, (self.x + 20, self.y))
                    if self.chicken_room == 'room34':
                        if keys[pygame.K_g]:
                            self.has_chicken = True


            # Rock
            text4 = font20.render('"G" to Pick Up Rock', True, (255, 255, 255))
            text5 = font20.render('"H" to Drop Rock', True, (255, 255, 255))

            if self.y >= 118 and self.x >= 802 and self.y <= 235 and self.x <= 892 and\
               self.has_chicken == False and self.found_rock == False:
                gamewindow.blit(text4, (self.x, self.y - 25))
                if keys[pygame.K_g]:
                    self.found_rock = True
                    self.has_rock = True
                    
            if self.has_rock == True:
                self.has_gun = False
                self.has_punch = False
                self.has_sword = False

                gamewindow.blit(text5, (self.x + 5, self.y - 25))              

                if self.left == True and self.standing == False:
                    gamewindow.blit(rock, (self.x + 30 , self.y + 70))

                if self.left == True and self.standing == True:
                    gamewindow.blit(rock, (self.x + 47 , self.y + 75))

                if self.right == True and self.standing == False:
                    gamewindow.blit(rock, (self.x + 60 , self.y + 70))

                if self.right == True and self.standing == True:
                    gamewindow.blit(rock, (self.x + 40 , self.y + 75))

                if self.up == True and self.standing == True:
                    gamewindow.blit(rock, (self.x + 45 , self.y + 60))

                if self.up == True and self.standing == False:
                    gamewindow.blit(rock, (self.x + 45 , self.y + 60))

            if self.has_rock == True and keys[pygame.K_h]:
                rock_list.append((self.x + self.width//2 - 20, self.y + 80))
                self.rock_location = rock_list[0]
                rock_list.clear()
                self.has_rock = False
                self.has_gun = True
                self.has_punch = True
                self.has_sword = True
            
            if self.has_rock == False and self.found_rock == True:
                gamewindow.blit(rock, (self.rock_location))

            if self.has_rock == False and self.found_rock == True and self.has_chicken == False:
                if self.x >= self.rock_location[0] - 86 and\
                   self.x <= self.rock_location[0] - 22 and\
                   self.y <= self.rock_location[1] and\
                   self.y >= self.rock_location[1] - 96:
                    gamewindow.blit(text4, (self.x, self.y - 25))
                    if keys[pygame.K_g]:
                        self.has_rock = True


            # Locations
            if self.rock_location[1] >= 459 and self.rock_location[1] <= 531 and\
               self.rock_location[0] >= 1107 and self.rock_location[0] <= 1197 and\
               self.has_rock == False and\
               self.chicken_location[0] >= 131 and self.chicken_location[0] <= 231 and\
               self.chicken_location[1] >= 449 and self.chicken_location[1] <= 540 and\
               self.has_chicken == False and\
               self.son_location[1] >= 412 and self.son_location[1] <= 529 and\
               self.son_location[0] >= 437 and self.son_location[0] <= 545 and\
               self.has_son == False and\
               self.y >= 352 and self.x >= 703 and self.x <= 811 and self.y <= 460:
                self.cave = 'open'
                

        # Room 35
        elif self.current_room == 'room35':
            font20 = pygame.font.Font(None, 20)
            font25 = pygame.font.Font(None, 25)
            font30 = pygame.font.Font(None, 30)

            text1 = font20.render('"H" to Drop Chicken', True, (255, 255, 255))
            text2 = font20.render('That Chicken Got Devoured', True, (255, 255, 255))
            gamewindow.blit(pygame.image.load(os.path.join(SurviveImages, "room35.png")), (0,0))
                
            # Chicken
            if self.has_chicken == True:
                self.chicken_location = (self.x + self.width//2 - 15, self.y + 60)
                self.has_gun = False
                self.has_punch = False
                self.has_sword = False

                gamewindow.blit(text1, (self.x, self.y - 25))              

                if self.left == True and self.standing == False:
                    gamewindow.blit(chicken_death_left, (self.x + 30 , self.y + 70))

                if self.left == True and self.standing == True:
                    gamewindow.blit(chicken_death_left, (self.x + 47 , self.y + 75))

                if self.right == True and self.standing == False:
                    gamewindow.blit(chicken_death_right, (self.x + 60 , self.y + 70))

                if self.right == True and self.standing == True:
                    gamewindow.blit(chicken_death_right, (self.x + 40 , self.y + 75))

                if self.up == True and self.standing == True:
                    gamewindow.blit(chicken_death_left, (self.x + 45 , self.y + 60))

                if self.up == True and self.standing == False:
                    gamewindow.blit(chicken_death_left, (self.x + 45 , self.y + 60))

            if self.has_chicken == True and keys[pygame.K_h]:
                chicken_list.append((self.x + self.width//2 - 15, self.y + 80))
                self.chicken_location = chicken_list[0]
                chicken_list.clear()
                self.has_chicken = False
                self.chicken_room = 'room35'
                self.has_gun = True
                self.has_punch = True
                self.has_sword = True
            
            if self.has_chicken == False and self.found_chicken == True:
                if self.chicken_room == 'room35' and self.objective10 == False:
                    gamewindow.blit(chicken_death_left, (self.chicken_location))

            if enemy147.hp <= 0:
                enemy147.visible = False
                gamewindow.blit(smallspider_death, (enemy147.x-0 , enemy147.y+10))

            if enemy137.hp <= 0:
                enemy137.visible = False
                gamewindow.blit(bat_death, (enemy137.x-0 , enemy137.y+14))

            if enemy138.hp <= 0:
                enemy138.visible = False
                gamewindow.blit(bat_death, (enemy138.x-30 , enemy138.y+24))

            if enemy139.hp <= 0:
                enemy139.visible = False
                gamewindow.blit(bat_death, (enemy139.x-20 , enemy139.y+34))

            if enemy140.hp <= 0:
                enemy140.visible = False
                gamewindow.blit(bat_death, (enemy140.x-10 , enemy140.y+44))

            if enemy141.hp <= 0:
                enemy141.visible = False
                gamewindow.blit(bat_death, (enemy141.x+10 , enemy141.y+54))                    

            if enemy142.hp <= 0:
                enemy142.visible = False
                gamewindow.blit(bat_death, (enemy142.x+20 , enemy142.y+64))

            if enemy143.hp <= 0:
                enemy143.visible = False
                gamewindow.blit(bat_death, (enemy143.x+30 , enemy143.y+74))

            if enemy144.hp <= 0:
                enemy144.visible = False
                gamewindow.blit(bat_death, (enemy144.x-35 , enemy144.y+84))

            if enemy145.hp <= 0:
                enemy145.visible = False
                gamewindow.blit(bat_death, (enemy145.x+35 , enemy145.y+94))

            if enemy146.hp <= 0:
                enemy146.visible = False
                gamewindow.blit(bat_death, (enemy146.x-32 , enemy146.y+104))

            if enemy146.hp <= 0:
                enemy146.visible = False
                gamewindow.blit(bat_death, (enemy146.x-32 , enemy146.y+114))

            if enemy147.hp > 0:
                enemy147.visible = True
                enemy147.draw(gamewindow, self)

            if enemy137.hp > 0:
                enemy137.visible = True
                enemy137.draw(gamewindow, self)

            if enemy138.hp > 0:
                enemy138.visible = True
                enemy138.draw(gamewindow, self)

            if enemy139.hp > 0:
                enemy139.visible = True
                enemy139.draw(gamewindow, self)

            if enemy140.hp > 0:
                enemy140.visible = True
                enemy140.draw(gamewindow, self)

            if enemy141.hp > 0:
                enemy141.visible = True
                enemy141.draw(gamewindow, self)

            if enemy142.hp > 0:
                enemy142.visible = True
                enemy142.draw(gamewindow, self)

            if enemy143.hp > 0:
                enemy143.visible = True
                enemy143.draw(gamewindow, self)

            if enemy144.hp > 0:
                enemy144.visible = True
                enemy144.draw(gamewindow, self)

            if enemy145.hp > 0:
                enemy145.visible = True
                enemy145.draw(gamewindow, self)

            if enemy146.hp > 0:
                enemy146.visible = True
                enemy146.draw(gamewindow, self)

            if enemy137.visible == False and enemy138.visible == False and\
               enemy139.visible == False and enemy140.visible == False and\
               enemy141.visible == False and enemy142.visible == False and\
               enemy143.visible == False and enemy144.visible == False and\
               enemy145.visible == False and enemy146.visible == False and\
               enemy147.visible == False:
                self.objective10 = True
               
            if self.objective10 == True:
                gamewindow.blit(text2, (self.x - 10, self.y - 25)) 


        # Room 36
        elif self.current_room == 'room36':
            font20 = pygame.font.Font(None, 20)
            font25 = pygame.font.Font(None, 25)
            font30 = pygame.font.Font(None, 30)
            text1 = font30.render("Your Son Is Scared! You Can't Leave Him!", True, (255, 255, 255))
            gamewindow.blit(pygame.image.load(os.path.join(SurviveImages, "room36.png")), (0,0))

            if enemy148.hp <= 0:
                enemy148.visible = False
                gamewindow.blit(smallspider_death, (enemy148.x-0 , enemy148.y+20))
                
            if enemy149.hp <= 0:
                enemy149.visible = False
                gamewindow.blit(smallspider_death, (enemy149.x-0 , enemy149.y+20))
                
            if enemy150.hp <= 0:
                enemy150.visible = False
                gamewindow.blit(smallspider_death, (enemy150.x-0 , enemy150.y+20))
                
            if enemy151.hp <= 0:
                enemy151.visible = False
                gamewindow.blit(smallspider_death, (enemy151.x-0 , enemy151.y+20))

            if enemy152.hp <= 0:
                enemy152.visible = False
                gamewindow.blit(smallspider_death, (enemy152.x-0 , enemy152.y+20))
                
            if enemy153.hp <= 0:
                enemy153.visible = False
                gamewindow.blit(smallspider_death, (enemy153.x-0 , enemy153.y+20))
                
            if enemy154.hp <= 0:
                enemy154.visible = False
                gamewindow.blit(smallspider_death, (enemy154.x-0 , enemy154.y+20))
                
            if enemy155.hp <= 0:
                enemy155.visible = False
                gamewindow.blit(smallspider_death, (enemy155.x-0 , enemy154.y+20))
                
            if enemy156.hp <= 0:
                enemy156.visible = False
                gamewindow.blit(smallspider_death, (enemy156.x-0 , enemy156.y+20))
                
            if enemy157.hp <= 0:
                enemy157.visible = False
                gamewindow.blit(smallspider_death, (enemy157.x-0 , enemy157.y+20))
               
            if enemy158.hp <= 0:
                enemy158.visible = False
                gamewindow.blit(smallspider_death, (enemy158.x-0 , enemy158.y+20))
                
            if enemy159.hp <= 0:
                enemy159.visible = False
                gamewindow.blit(smallspider_death, (enemy159.x-0 , enemy159.y+20))
                
            if enemy160.hp <= 0:
                enemy160.visible = False
                gamewindow.blit(smallspider_death, (enemy160.x-0 , enemy160.y+20))


            if enemy148.hp > 0:
                enemy148.visible = True
                enemy148.draw(gamewindow, self)
       
            if enemy149.hp > 0:
                enemy149.visible = True
                enemy149.draw(gamewindow, self)
                  
            if enemy150.hp > 0:
                enemy150.visible = True
                enemy150.draw(gamewindow, self)
               
            if enemy151.hp > 0:
                enemy151.visible = True
                enemy151.draw(gamewindow, self)

            if enemy152.hp > 0:
                enemy152.visible = True
                enemy152.draw(gamewindow, self)
                
            if enemy153.hp > 0:
                enemy153.visible = True
                enemy153.draw(gamewindow, self)
              
            if enemy154.hp > 0:
                enemy154.visible = True
                enemy154.draw(gamewindow, self)
              
            if enemy155.hp > 0:
                enemy155.visible = True
                enemy155.draw(gamewindow, self)

            if enemy156.hp > 0:
                enemy156.visible = True
                enemy156.draw(gamewindow, self)

            if enemy157.hp > 0:
                enemy157.visible = True
                enemy157.draw(gamewindow, self)
                
            if enemy158.hp > 0:
                enemy158.visible = True
                enemy158.draw(gamewindow, self)
               
            if enemy159.hp > 0:
                enemy159.visible = True
                enemy159.draw(gamewindow, self)
                
            if enemy160.hp > 0:
                enemy160.visible = True
                enemy160.draw(gamewindow, self)

            if enemy148.visible == False and enemy149.visible == False and \
                enemy150.visible == False and enemy151.visible == False and \
                enemy152.visible == False and enemy153.visible == False and \
                enemy154.visible == False and enemy155.visible == False and \
                enemy156.visible == False and enemy157.visible == False and \
                enemy158.visible == False and enemy159.visible == False and \
                enemy160.visible == False:
                self.objective11 = True



    def son(self):
        text101 = font20.render('"W" to Drop', True, (255, 255, 255))
        text102 = font20.render('"E" to Pick Up', True, (255, 255, 255))
        if self.has_son == True and keys[pygame.K_w]:
            son_list.append((self.x + self.width//2 - 15, self.y + 60))
            self.son_location = son_list[0]
            son_list.clear()
            self.has_son = False
        if self.has_son == False and self.found_son == True:
            gamewindow.blit(son_down, (self.son_location))
        if self.has_son == False and self.found_son == True:
            if self.x >= self.son_location[0] - 76 and\
               self.x <= self.son_location[0] - 22 and\
               self.y <= self.son_location[1] and\
               self.y >= self.son_location[1] - 96:
                if self.current_room == 'room19':
                    gamewindow.blit(text102, (self.x + 20, self.y))
                if keys[pygame.K_e]:
                    self.has_son = True
        if self.has_son == True:
            if self.current_room == 'room19':
                gamewindow.blit(text101, (self.x + 20, self.y - 20))
            if self.down == True:
                gamewindow.blit(son_down, (self.x + 49, self.y))
            elif self.left == True:
                gamewindow.blit(son_left, (self.x + 70, self.y + 15))
            elif self.right == True:
                gamewindow.blit(son_right, (self.x + 30, self.y + 15))


    def stats(self):
        level_up = font.render('LEVEL UP!', 1, (175,0,0))
        hp_text = font.render('HP + 10', 1, (175,0,0))
        speed_text0 = font.render('Speed + 0', 1, (175,0,0))
        speed_text1 = font.render('Speed + 1', 1, (175,0,0))
        punch_dmg0 = font.render('Punch Damage + 0', 1, (175,0,0))
        punch_dmg1 = font.render('Punch Damage + 1', 1, (175,0,0))
        sword_dmg0 = font.render('Sword Damage + 0', 1, (175,0,0))       
        sword_dmg1 = font.render('Sword Damage + 1', 1, (175,0,0))
        gun_dmg0 = font.render('Gun Damage + 0', 1, (175,0,0))
        gun_dmg2 = font.render('Gun Damage + 2', 1, (175,0,0))

        if self.xp >= 0 and self.xp < 20 and self.level > 1:
            time_list.append(time.time())
            if time.time() - time_list[0] < 5:
                gamewindow.blit(level_up, (325, 20))
                gamewindow.blit(hp_text, (325, 40))

                if self.level == 5 or self.level == 10 or self.level == 14 or self.level == 18:
                    gamewindow.blit(speed_text1, (325, 60))
                else:
                    gamewindow.blit(speed_text0, (325, 60))

                if self.level < 10:
                    gamewindow.blit(punch_dmg1, (325, 80))
                    gamewindow.blit(sword_dmg1, (325, 100))
                    gamewindow.blit(gun_dmg0, (325, 120))

                if self.level >= 10:
                    gamewindow.blit(gun_dmg2, (325, 120))
                      
        if self.xp > 20:
            time_list.clear()
             

    def level_up(self):             
        if self.xp >= self.xp_needed and self.level < 20:
            self.level += 1         
            self.xp_needed = int(self.xp_needed * 1.25)
            self.xp = 0
            self.full_hp += 10
            self.current_hp = self.full_hp
            
            if self.level < 10:
                self.punch_dmg += 1
                self.sword_dmg += 1
                
            if self.level >= 10 and self.level < 20:
                self.gun_dmg += 2

            if self.level == 5:
                self.speed = 10
            if self.level == 11:
                self.speed = 11
            if self.level == 18:
                self.speed = 12
         
        if self.level == 20:
            self.xp = self.xp_needed

          
    def hit(self):
        for enemy in enemies:
            if enemy.visible == True:
                if self.hitbox[1] < enemy.hitbox[1] + enemy.hitbox[3] and self.hitbox[1] + self.hitbox[3] > enemy.hitbox[1]:
                    if self.hitbox[0] + self.hitbox[2] > enemy.hitbox[0] and self.hitbox[0] < enemy.hitbox[0] + enemy.hitbox[2]:
                        if self.in_car == False:
                            self.current_hp -= enemy.damage
                            if enemy.damage > 0 and self.alive == True:
                                main_hit.play()
                            self.walk_count = 0
                            pygame.display.update()

                        if self.in_car == True and self.standing == True:
                            self.current_hp -= enemy.damage
                            if enemy.damage > 0 and self.alive == True:
                                main_hit.play()
                            pygame.display.update()

                        if self.in_car == True and self.standing == False:
                            enemy.hp = 0
                            self.xp += 2
                            pygame.display.update()
                            

    def draw(self, gamewindow):
        if self.alive == True:
            if self.in_car == False:
                if self.walk_count + 1 >= 17:
                    self.walk_count = 0

                if not(self.standing):
                    if self.up == True:
                        gamewindow.blit(walk_up[self.walk_count//3], (self.x, self.y))
                        self.walk_count +=1
                        
                    elif self.down == True:
                        gamewindow.blit(walk_down[self.walk_count//3], (self.x, self.y))
                        self.walk_count +=1
                    elif self.left == True:
                        gamewindow.blit(walk_left[self.walk_count//3], (self.x, self.y))
                        self.walk_count +=1
                    elif self.right == True:
                        gamewindow.blit(walk_right[self.walk_count//3], (self.x, self.y))
                        self.walk_count +=1

                else:
                    # Right                
                    if self.right and keys[pygame.K_d] and self.has_punch == True:
                        punch_list.append(loop)
         
                        if len(punch_list) < 4:
                            self.has_punch = True
                            gamewindow.blit(right_punch, (self.x, self.y))
                        if len(punch_list) == 1:
                            punch_sound.play()
                        if len(punch_list) == 2:
                            punch_sound.play()
                        if len(punch_list) == 3:
                            punch_sound.play()
                        if len(punch_list) == 4:
                            self.has_punch = True
                            gamewindow.blit(standstill_right, (self.x, self.y))
                            punch_list.clear()
        
                    elif self.right and keys[pygame.K_s] and self.has_sword == True:
                        sword_list.append(loop)
                        if len(sword_list) < 5:
                            self.swing_sword = True
                            gamewindow.blit(sword_right, (self.x, self.y))
                        if len(sword_list) >= 5 and len(sword_list) < 9:
                            self.swing_sword = False
                            gamewindow.blit(standstill_right, (self.x, self.y))
                        if len(sword_list) >= 9 and len(sword_list) < 13:
                            self.swing_sword = True
                            gamewindow.blit(sword_right, (self.x, self.y))
                            
                        if len(sword_list) >= 13 and len(sword_list) < 17:
                            self.swing_sword = False
                            gamewindow.blit(standstill_right, (self.x, self.y))
                            
                        if len(sword_list) >= 17:
                            self.swing_sword = True
                            gamewindow.blit(sword_right, (self.x, self.y))
                            sword_list.clear()

                    elif self.right and keys[pygame.K_SPACE] and self.has_gun == True:
                        gamewindow.blit(right_shoot, (self.x, self.y))

                    elif self.right:
                        gamewindow.blit(standstill_right, (self.x, self.y))

                    # Up
                    elif self.up and keys[pygame.K_d] and self.has_punch == True:
                        punch_list.append(loop)
         
                        if len(punch_list) < 4:
                            self.has_punch = True
                            gamewindow.blit(up_punch, (self.x, self.y))
                        if len(punch_list) == 1:
                            punch_sound.play()
                        if len(punch_list) == 2:
                            punch_sound.play()
                        if len(punch_list) == 3:
                            punch_sound.play()
                        if len(punch_list) == 4:
                            self.has_punch = True
                            gamewindow.blit(standstillup, (self.x, self.y))
                            punch_list.clear()

                    elif self.up and keys[pygame.K_s] and self.has_sword == True:
                        sword_list.append(loop)
                        if len(sword_list) < 5:
                            self.swing_sword = True
                            gamewindow.blit(sword_up, (self.x, self.y))
                        if len(sword_list) >= 5 and len(sword_list) < 9:
                            self.swing_sword = False
                            gamewindow.blit(standstillup, (self.x, self.y))
                        if len(sword_list) >= 9 and len(sword_list) < 13:
                            self.swing_sword = True
                            gamewindow.blit(sword_up, (self.x, self.y))
                        if len(sword_list) >= 13 and len(sword_list) < 17:
                            self.swing_sword = False
                            gamewindow.blit(standstillup, (self.x, self.y))
                        if len(sword_list) >= 17:
                            self.swing_sword = True
                            gamewindow.blit(sword_up, (self.x, self.y))
                            sword_list.clear()


                    elif self.up and keys[pygame.K_SPACE] and self.has_gun == True:
                        gamewindow.blit(up_shoot, (self.x, self.y))

                    elif self.up:
                        gamewindow.blit(standstillup, (self.x, self.y))

                    # Left
                    elif self.left and keys[pygame.K_d] and self.has_punch == True:
                        punch_list.append(loop)
         
                        if len(punch_list) < 4:
                            self.has_punch = True
                            gamewindow.blit(left_punch, (self.x, self.y))
                        if len(punch_list) == 1:
                            punch_sound.play()
                        if len(punch_list) == 2:
                            punch_sound.play()
                        if len(punch_list) == 3:
                            punch_sound.play()
                        if len(punch_list) == 4:
                            self.has_punch = True
                            gamewindow.blit(standstill_left, (self.x, self.y))
                            punch_list.clear()

                    elif self.left and keys[pygame.K_s] and self.has_sword == True:
                        sword_list.append(loop)
                        if len(sword_list) < 5:
                            self.swing_sword = True
                            gamewindow.blit(sword_left, (self.x, self.y))
                        if len(sword_list) >= 5 and len(sword_list) < 9:
                            self.swing_sword = False
                            gamewindow.blit(standstill_left, (self.x, self.y))
                        if len(sword_list) >= 9 and len(sword_list) < 13:
                            self.swing_sword = True
                            gamewindow.blit(sword_left, (self.x, self.y))
                        if len(sword_list) >= 13 and len(sword_list) < 17:
                            self.swing_sword = False
                            gamewindow.blit(standstill_left, (self.x, self.y))
                        if len(sword_list) >= 17:
                            self.swing_sword = True
                            gamewindow.blit(sword_left, (self.x, self.y))
                            sword_list.clear()


                    elif self.left and keys[pygame.K_SPACE] and self.has_gun == True:
                        gamewindow.blit(left_shoot, (self.x, self.y))

                    elif self.left:
                        gamewindow.blit(standstill_left, (self.x, self.y))

                    # Down
                    elif self.down and keys[pygame.K_d] and self.has_punch == True:
                        punch_list.append(loop)
         
                        if len(punch_list) < 4:
                            gamewindow.blit(down_punch, (self.x, self.y))
                        if len(punch_list) == 1:
                            punch_sound.play()
                        if len(punch_list) == 2:
                            punch_sound.play()
                        if len(punch_list) == 3:
                            punch_sound.play()
                        if len(punch_list) == 4:
                            self.has_punch = True
                            gamewindow.blit(standstilldown, (self.x, self.y))
                            punch_list.clear()

                    elif self.down and keys[pygame.K_s] and self.has_sword == True:
                        sword_list.append(loop)
                        if len(sword_list) < 5:
                            self.swing_sword = True
                            gamewindow.blit(sword_down, (self.x, self.y))
                        if len(sword_list) >= 5 and len(sword_list) < 9:
                            self.swing_sword = False
                            gamewindow.blit(standstilldown, (self.x, self.y))
                        if len(sword_list) >= 9 and len(sword_list) < 13:
                            self.swing_sword = True
                            gamewindow.blit(sword_down, (self.x, self.y))
                        if len(sword_list) >= 13 and len(sword_list) < 17:
                            self.swing_sword = False
                            gamewindow.blit(standstilldown, (self.x, self.y))
                        if len(sword_list) >= 17:
                            self.swing_sword = True
                            gamewindow.blit(sword_down, (self.x, self.y))
                            sword_list.clear()

                    elif self.down and keys[pygame.K_SPACE] and self.has_gun == True:
                        gamewindow.blit(down_shoot, (self.x, self.y))

                    elif self.down:
                        gamewindow.blit(standstilldown, (self.x, self.y))


                self.hitbox = (self.x + 50, self.y + 25, 25, 85)
                #pygame.draw.rect(gamewindow, (0,0,0), self.hitbox, 1)

            if self.in_car == True:

                if not(self.standing):
                    if self.up == True:
                        gamewindow.blit(car_up, (self.x, self.y))
                        self.hitbox = (self.x, self.y, 100, 200)
                        
                    elif self.down == True:
                        gamewindow.blit(car_down, (self.x, self.y))
                        self.hitbox = (self.x, self.y, 100, 200)
                        
                    elif self.left == True:
                        gamewindow.blit(car_left, (self.x, self.y))
                        self.hitbox = (self.x, self.y, 200, 100)
     
                    elif self.right == True:
                        gamewindow.blit(car_right, (self.x, self.y))
                        self.hitbox = (self.x, self.y, 200, 100)


                else:
                    if self.right:
                        gamewindow.blit(car_right, (self.x, self.y))
                        self.hitbox = (self.x, self.y, 200, 100)

                    elif self.down:
                        gamewindow.blit(car_down, (self.x, self.y))
                        self.hitbox = (self.x, self.y, 100, 200)

                    elif self.up:
                        gamewindow.blit(car_up, (self.x, self.y))
                        self.hitbox = (self.x, self.y, 100, 200)
                        
                    elif self.left:
                        gamewindow.blit(car_left, (self.x, self.y))
                        self.hitbox = (self.x, self.y, 200, 100)

                #pygame.draw.rect(gamewindow, (0,0,0), self.hitbox, 1)

   
              
    def main_character_movement(self):
        if self.can_move == True:
            if keys[pygame.K_LEFT]:
                self.x -= self.speed
                self.direction = "Left"
                self.left = True
                self.right = False
                self.up = False
                self.down = False
                self.standing = False
            elif keys[pygame.K_RIGHT]:
                self.x += self.speed
                self.direction = "Right"
                self.right = True
                self.left = False
                self.up = False
                self.down = False
                self.standing = False
            elif keys[pygame.K_UP]:
                self.y -= self.speed
                self.direction = "Up"
                self.up = True
                self.down = False
                self.left = False
                self.right = False
                self.standing = False
            elif keys[pygame.K_DOWN]:
               self.y += self.speed
               self.direction = "Down"
               self.down = True
               self.up = False
               self.left = False
               self.right = False
               self.standing = False
            else:
                self.standing = True
                self.walk_count = 0


main_character = MainCharacter(604, 748, 'down', 128, 128)


# Sword
swords = []
sword_timer = []

class Sword():
    def __init__(self, x, y, radius, color, facing_x, facing_y):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing_x = facing_x
        self.facing_y = facing_y
        self.vel_x = 25 * facing_x # Speed of bullets
        self.vel_y = 25 * facing_y

    def draw(self, window):
        pygame.draw.circle(gamewindow, self.color, (self.x,self.y), self.radius)


    def sword_distance():
        for enemy in enemies:
            if enemy.visible == True:
                for sword in swords:
                    if sword.y - sword.radius < enemy.hitbox[1] + enemy.hitbox[3] and sword.y + sword.radius > enemy.hitbox[1]:
                        if sword.x + sword.radius > enemy.hitbox[0] and sword.x - sword.radius < enemy.hitbox[0] + enemy.hitbox[2]:
                            enemy.weapon_hit_by = 'sword'
                            enemy.hit()
                            swords.pop(swords.index(sword))

        for sword in swords:
            if sword.x < main_character.x + 114 and sword.x > main_character.x + 14:  # 1440, 900
                sword.x += sword.vel_x
            else:
                swords.pop(swords.index(sword))
                
        for sword in swords:
            if sword.y < main_character.y + 120 and sword.y > main_character.y + 5:
                sword.y += sword.vel_y
            else:
                swords.pop(swords.index(sword))


    def swing_sword():
        if keys[pygame.K_s] and main_character.standing == True:
                if main_character.left:
                    facing_x = -1
                    facing_y = 0
                elif main_character.right:
                    facing_x = 1
                    facing_y = 0
                elif main_character.up:
                    facing_y = -1
                    facing_x = 0
                else:
                    facing_y = 1
                    facing_x = 0

                if main_character.has_sword == True and main_character.swing_sword == True: 
                    swords.append(Sword(round(main_character.x + main_character.width//2 ),# where punch leave body
                                         round(main_character.y + main_character.height//2),
                                         5,(0,0,0), facing_x, facing_y)) #punch radius, color, facing_x, facing_y

  
# Punch
punches = []
class Punch():
    def __init__(self, x, y, radius, color, facing_x, facing_y):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing_x = facing_x
        self.facing_y = facing_y
        self.vel_x = 12 * facing_x # Speed of bullets
        self.vel_y = 15 * facing_y

    def draw(self, window):
        pygame.draw.circle(gamewindow, self.color, (self.x,self.y), self.radius)


    def punch_distance():
        for enemy in enemies:
            if enemy.visible == True:
                for punch in punches:
                    if punch.y - punch.radius < enemy.hitbox[1] + enemy.hitbox[3] and punch.y + punch.radius > enemy.hitbox[1]:
                        if punch.x + punch.radius > enemy.hitbox[0] and punch.x - punch.radius < enemy.hitbox[0] + enemy.hitbox[2]:
                            enemy.weapon_hit_by = 'punch'
                            enemy.hit()
                            punches.pop(punches.index(punch))

        for punch in punches:
            if punch.x < main_character.x + 85 and punch.x > main_character.x + 40:  # 1440, 900
                punch.x += punch.vel_x
            else:
                punches.pop(punches.index(punch))
        for punch in punches:
            if punch.y < main_character.y + 105 and punch.y > main_character.y + 20:
                punch.y += punch.vel_y
            else:
                punches.pop(punches.index(punch))


    def throw_punch():
        if keys[pygame.K_d] and main_character.standing == True:
            if main_character.left:
                facing_x = -1
                facing_y = 0
            elif main_character.right:
                facing_x = 1
                facing_y = 0
            elif main_character.up:
                facing_y = -1
                facing_x = 0
            else:
                facing_y = 1
                facing_x = 0

            if main_character.has_punch == True: 
                punches.append(Punch(round(main_character.x + main_character.width//2 ),# where punch leave body
                                     round(main_character.y + main_character.height//2),
                                     5,(0,0,0), facing_x, facing_y)) #punch radius, color, facing_x, facing_y



# Shoot
bullets = []
class Shoot():
    def __init__(self, x, y, radius, color, facing_x, facing_y):
        self.x = x
        self.y = y
        self.radius = radius
        self.color = color
        self.facing_x = facing_x
        self.facing_y = facing_y
        self.vel_x = 20 * facing_x # Speed of bullets
        self.vel_y = 15 * facing_y

    def draw(self, window):
        pygame.draw.circle(gamewindow, self.color, (self.x,self.y), self.radius)


    def bullet_stop():
        for enemy in enemies:
            if enemy.visible == True:
                for bullet in bullets:
                    if bullet.y - bullet.radius < enemy.hitbox[1] + enemy.hitbox[3] and bullet.y + bullet.radius > enemy.hitbox[1]:
                        if bullet.x + bullet.radius > enemy.hitbox[0] and bullet.x - bullet.radius < enemy.hitbox[0] + enemy.hitbox[2]:
                            enemy.weapon_hit_by = 'gun'
                            enemy.hit()
                            bullets.pop(bullets.index(bullet))

        for bullet in bullets:
            if bullet.x < 1440 and bullet.x > 0:  # 1440, 900
                bullet.x += bullet.vel_x
            else:
                bullets.pop(bullets.index(bullet))
        for bullet in bullets:
            if bullet.y < 900 and bullet.y > 0:
                bullet.y += bullet.vel_y
            else:
                bullets.pop(bullets.index(bullet))

        for bullet in bullets:
            if main_character.current_room == 'room20':
                if bullet.x >= 712 and bullet.x <= 794 and bullet.y < 413 and main_character.damaged_door < 5:
                    bullets.pop(bullets.index(bullet))
                    main_character.damaged_door += 1
                


    def shoot_gun():
        if keys[pygame.K_SPACE] and main_character.has_gun == True and main_character.standing == True:
            if main_character.left:
                facing_x = -1
                facing_y = 0
            elif main_character.right:
                facing_x = 1
                facing_y = 0
            elif main_character.up:
                facing_y = -1
                facing_x = 0
            else:
                facing_y = 1
                facing_x = 0
             
     
            if time.time() > main_character.cooldown: # Amount of bullets allowed on screen
                bullets.append(Shoot(round(main_character.x + main_character.width//2 ),# where bullets leave body
                                     round(main_character.y + main_character.height//2),
                                     3,(0,0,0), facing_x, facing_y)) #bullet radius, color, facing_x, facing_y
                gun_sound.play()
                main_character.cooldown = time.time() + 1.5



enemies = []
class Enemies():
    def __init__(self, x, y, start_x, start_y , width, height, speed, xp, damage,
                         image, x_hitbox, y_hitbox, hp, max_hp):
        self.x = x
        self.y = y
        self.start_x = start_x
        self.start_y = start_y
        self.width = width
        self.height = height
        self.walk_count = 0
        self.speed = speed
        self.xp = xp
        self.damage = damage
        self.image = image
        self.x_hitbox = x_hitbox
        self.y_hitbox = y_hitbox
        self.hp = hp
        self.max_hp = max_hp

# Standing Enemy
class StandingEnemy(Enemies):
    def __init__(self, x, y, start_x, start_y , width, height, speed, xp, damage,
                         image, x_hitbox, y_hitbox, hp, max_hp):
        super().__init__(x, y, start_x, start_y , width, height, speed, xp, damage,
                         image, x_hitbox, y_hitbox, hp, max_hp)
        self.hitbox = (self.x + 0, self.y + 0, 128, 128)
        self.weapon_hit_by = 'null'
        self.visible = False
        enemies.append(self)
        self.image = image


    def draw(self, gamewindow):
        if self.visible == True:
            gamewindow.blit(self.image, (self.x, self.y))
            pygame.draw.rect(gamewindow, (255,0,0), (self.hitbox[0], self.hitbox[1] - 20, self.max_hp, 5))
            pygame.draw.rect(gamewindow, (0,255,0), (self.hitbox[0], self.hitbox[1] - 20, self.hp, 5))
            self.hitbox = (self.x + self.x_hitbox,
                           self.y + self.y_hitbox,
                           self.width, self.height)
##            pygame.draw.rect(gamewindow, (0,0,0), self.hitbox, 1)


    def hit(self):
       if self.hp > 0:
           if self.weapon_hit_by == 'gun':
               self.hp -= main_character.gun_dmg
           if self.weapon_hit_by == 'sword':
               self.hp -= main_character.sword_dmg
           if self.weapon_hit_by == 'punch':
               self.hp -= main_character.punch_dmg

       if self.hp < 1:
           #death_sound.play()
           self.visible = False
           main_character.xp += self.xp

           
# XPath Enemy
class XPathEnemy(Enemies):
    def __init__(self, x, y, start_x, start_y , width, height, speed, xp, damage,
                         image, x_hitbox, y_hitbox, hp, max_hp):
        super().__init__(x, y, start_x, start_y , width, height, speed, xp, damage,
                         image, x_hitbox, y_hitbox, hp, max_hp)
        self.hitbox = (self.x + 0, self.y + 0, 128, 128)
        self.weapon_hit_by = 'null'
        self.visible = False
        self.end = self.x + random.randint(50,200)
        self.path = [self.x, self.end]
        enemies.append(self)

    def draw(self, gamewindow):
        self.move()
        if self.visible == True:
            if self.walk_count + 1 <= 18:
                self.walk_count = 0
            if self.speed > 0:
                gamewindow.blit(self.image, (self.x, self.y))
                self.walk_count += 1
            else:
                gamewindow.blit(self.image, (self.x, self.y))
                self.walk_count += 1
            pygame.draw.rect(gamewindow, (255,0,0), (self.hitbox[0], self.hitbox[1] - 20, self.max_hp, 5))
            pygame.draw.rect(gamewindow, (0,255,0), (self.hitbox[0], self.hitbox[1] - 20, self.hp, 5))
            self.hitbox = (self.x + self.x_hitbox,
                           self.y + self.y_hitbox,
                           self.width, self.height)
            #pygame.draw.rect(gamewindow, (0,0,0), self.hitbox, 1)


    def move(self):
        if self.speed > 0:
            if self.x + self.speed < self.path[1]:
                self.x += self.speed
            else:
                self.speed = self.speed * -1
                self.walk_count = 0
        else:
            if self.x - self.speed > self.path[0]:
                self.x += self.speed
            else:
                self.speed = self.speed * -1
                self.walk_count = 0

    def hit(self):
        if self.hp > 0:
            if self.weapon_hit_by == 'gun':
                self.hp -= main_character.gun_dmg
            if self.weapon_hit_by == 'sword':
               self.hp -= main_character.sword_dmg

            if self.weapon_hit_by == 'punch':
                self.hp -= main_character.punch_dmg

 
        if self.hp < 1:
            #death_sound.play()
            self.visible = False
            main_character.xp += self.xp


# YPath Enemy
class YPathEnemy(Enemies):
    def __init__(self, x, y, start_x, start_y , width, height, speed, xp, damage,
                         image, x_hitbox, y_hitbox, hp, max_hp):
        super().__init__(x, y, start_x, start_y , width, height, speed, xp, damage,
                         image, x_hitbox, y_hitbox, hp, max_hp)
        self.hitbox = (self.x + 0, self.y + 0, 128, 128)
        self.weapon_hit_by = 'null'
        self.visible = False
        self.end = self.y + random.randint(50,200)
        self.path = [self.y, self.end]
        enemies.append(self)

    def draw(self, gamewindow):
        self.move()
        if self.visible == True:
            if self.walk_count + 1 <= 18:
                self.walk_count = 0
            if self.speed > 0:
                gamewindow.blit(self.image, (self.x, self.y))
                self.walk_count += 1
            else:
                gamewindow.blit(self.image, (self.x, self.y))
                self.walk_count += 1
            pygame.draw.rect(gamewindow, (255,0,0), (self.hitbox[0], self.hitbox[1] - 20, self.max_hp, 5))
            pygame.draw.rect(gamewindow, (0,255,0), (self.hitbox[0], self.hitbox[1] - 20, self.hp, 5))
            self.hitbox = (self.x + self.x_hitbox,
                           self.y + self.y_hitbox,
                           self.width, self.height)
            #pygame.draw.rect(gamewindow, (0,0,0), self.hitbox, 1)


    def move(self):
        if self.speed > 0:
            if self.y + self.speed < self.path[1]:
                self.y += self.speed
            else:
                self.speed = self.speed * -1
                self.walk_count = 0
        else:
            if self.y - self.speed > self.path[0]:
                self.y += self.speed
            else:
                self.speed = self.speed * -1
                self.walk_count = 0

    def hit(self):
        if self.hp > 0:
            if self.weapon_hit_by == 'gun':
                self.hp -= main_character.gun_dmg
            if self.weapon_hit_by == 'sword':
               self.hp -= main_character.sword_dmg

            if self.weapon_hit_by == 'punch':
                self.hp -= main_character.punch_dmg

 
        if self.hp < 1:
            #death_sound.play()
            self.visible = False
            main_character.xp += self.xp


# Stalking Enemy
class StalkingEnemy(Enemies):
    def __init__(self, x, y, start_x, start_y , width, height, speed, xp, damage,
                         image, x_hitbox, y_hitbox, hp, max_hp):
        super().__init__(x, y, start_x, start_y , width, height, speed, xp, damage,
                         image, x_hitbox, y_hitbox, hp, max_hp)
        self.hitbox = (self.x + 0, self.y + 10, 128, 128)
        self.weapon_hit_by = 'null'
        self.visible = False
        enemies.append(self)
        self.image = image


    def draw(self, gamewindow, player):
        if self.visible == True:
            self.stalkplayer(main_character)
            gamewindow.blit(self.image, (self.x, self.y))
            pygame.draw.rect(gamewindow, (255,0,0), (self.hitbox[0], self.hitbox[1] - 20, self.max_hp, 5))
            pygame.draw.rect(gamewindow, (0,255,0), (self.hitbox[0], self.hitbox[1] - 20, self.hp, 5))
            self.hitbox = (self.x + self.x_hitbox,
                           self.y + self.y_hitbox,
                           self.width, self.height)
            #pygame.draw.rect(gamewindow, (0,0,0), self.hitbox, 1)

    def hit(self):
       if self.hp > 0:
           if self.weapon_hit_by == 'gun':
               self.hp -= main_character.gun_dmg
           if self.weapon_hit_by == 'sword':
               self.hp -= main_character.sword_dmg
           if self.weapon_hit_by == 'punch':
               self.hp -= main_character.punch_dmg


       if self.hp < 1:
           #death_sound.play()
           self.visible = False
           main_character.xp += self.xp


    def stalkplayer(self, player):
        if main_character.current_room != 'room35':
            xdiff = round(main_character.x + main_character.width//2 ) - round(self.x + self.width//2)
            ydiff = round(main_character.y + main_character.height//2) - round(self.y + self.height//2)
            magnitude = math.sqrt(float(xdiff **2 + ydiff **2))
            num_frames = int(magnitude/self.speed)

            try:
                xdiff/num_frames
                ydiff/num_frames
            except ZeroDivisionError:
                pass
            else:
                xmove = xdiff/num_frames
                ymove = ydiff/num_frames
                self.x += xmove 
                self.y += ymove

        else:
            xdiff = round(main_character.chicken_location[0] + 15) - round(self.x + self.width//2)
            ydiff = round(main_character.chicken_location[1] + 20) - round(self.y + self.height//2)
            magnitude = math.sqrt(float(xdiff **2 + ydiff **2))
            num_frames = int(magnitude/self.speed)

            try:
                xdiff/num_frames
                ydiff/num_frames
            except ZeroDivisionError:
                pass
            else:
                xmove = xdiff/num_frames
                ymove = ydiff/num_frames
                self.x += xmove 
                self.y += ymove       



xpositions = []
ypositions = []
enemybullets = []
class ShootingEnemy(Enemies):
    def __init__(self, x, y, start_x, start_y , width, height, speed, xp, damage,
                         image, x_hitbox, y_hitbox, hp, max_hp):
        super().__init__(x, y, start_x, start_y , width, height, speed, xp, damage,
                         image, x_hitbox, y_hitbox, hp, max_hp)
        self.hitbox = (self.x + 0, self.y + 10, 128, 128)
        self.weapon_hit_by = 'null'
        self.visible = False
        enemies.append(self)
        self.image = image
        self.bulletx = round(self.x + self.width//2)
        self.bullety = round(self.y + self.height//2)
        self.bulletcolor = (200,200,200)       
        self.bulletradius = 8
        self.bulletspeed = 25
        self.bulletvisible = True
        self.start = 0
        self.cooldown = self.start + 1


    def draw(self, gamewindow, player):
        if self.visible == True:
            self.shootplayer(main_character)

            if self.bulletvisible == True:
                pygame.draw.circle(gamewindow, self.bulletcolor, (round(self.bulletx),round(self.bullety)), self.bulletradius)                      
            
            gamewindow.blit(self.image, (self.x, self.y))
            pygame.draw.rect(gamewindow, (255,0,0), (self.hitbox[0], self.hitbox[1] - 20, self.max_hp, 5))
            pygame.draw.rect(gamewindow, (0,255,0), (self.hitbox[0], self.hitbox[1] - 20, self.hp, 5))
            self.hitbox = (self.x + self.x_hitbox,
                           self.y + self.y_hitbox,
                           self.width, self.height)
##            pygame.draw.rect(gamewindow, (0,0,0), self.hitbox, 1)


    def shootplayer(self, player):
        if self.visible == True:
                 
            if time.time() > self.cooldown:                
                xpositions.append(main_character.x)
                ypositions.append(main_character.y)
        
                xdiff = round(xpositions[0] + main_character.width//2) - round(self.x + self.width//2)
                ydiff = round(ypositions[0] + main_character.height//2) - round(self.y + self.height//2)
                magnitude = math.sqrt(float(xdiff **2 + ydiff **2))
                num_frames = int(magnitude/self.bulletspeed)

                xmove = xdiff/num_frames
                ymove = ydiff/num_frames

                self.bulletx += xmove 
                self.bullety += ymove
         
                if self.bulletx < 1400 and self.bulletx > 0:  
                    self.bulletvisible = True
        
                if self.bulletx > 1400 or self.bulletx < 0:
                    self.bulletvisible = False
                    self.bulletx = round(self.x + self.width//2)
                    self.bullety = round(self.y + self.height//2)
                    self.cooldown = time.time() + 3
                    xpositions.clear()
                    ypositions.clear()
             
                if self.bullety < 900 and self.bullety > 0:
                    self.bulletvisible = True

                if self.bullety > 900 or self.bullety < 0:
                    self.bulletvisible = False
                    self.bulletx = round(self.x + self.width//2)
                    self.bullety = round(self.y + self.height//2)
                    self.cooldown = time.time() + 3
                    xpositions.clear()
                    ypositions.clear()
                    
                if self.bullety - self.bulletradius < main_character.hitbox[1] + main_character.hitbox[3] and self.bullety + self.bulletradius > main_character.hitbox[1]:
                    if self.bulletx + self.bulletradius > main_character.hitbox[0] and self.bulletx - self.bulletradius < main_character.hitbox[0] + main_character.hitbox[2]:
                        if main_character.alive == True:
                            main_hit.play()
                            if main_character.current_room == 'room10':
                                main_character.current_hp -= 10
                            else:
                                main_character.current_hp -= 25
                            
                        self.bulletvisible = False
                        self.bulletx = round(self.x + self.width//2)
                        self.bullety = round(self.y + self.height//2)
                        self.cooldown = time.time() + 1
             
    def hit(self):
       if self.hp > 0:
           if self.weapon_hit_by == 'gun':
               self.hp -= main_character.gun_dmg
           if self.weapon_hit_by == 'sword':
               self.hp -= main_character.sword_dmg  
           if self.weapon_hit_by == 'punch':
               self.hp -= main_character.punch_dmg


       if self.hp < 0.00001:
           #death_sound.play()
           self.visible = False
           main_character.xp += self.xp



lazer_list = []
class Boss1Enemy(Enemies):
    def __init__(self, x, y, start_x, start_y , width, height, speed, xp, damage,
                         image, x_hitbox, y_hitbox, hp, max_hp):
        super().__init__(x, y, start_x, start_y , width, height, speed, xp, damage,
                         image, x_hitbox, y_hitbox, hp, max_hp)
        self.hitbox = (self.x + 0, self.y + 10, 128, 128)
        self.weapon_hit_by = 'null'
        self.visible = False
        enemies.append(self)
        self.image = image
        self.lazerx = round((self.x + 17) + self.width//2)
        self.lazery = round(self.y + 52 )
        self.lazercolor = (125, 0, 0)
        self.start_pos = (round(self.lazerx),round(self.lazery))
        self.end_pos = (self.lazerx, self.lazery)
        self.lazer_width = 10
        self.lazerspeed = 30
        self.lazervisible = True
        self.start = 0
        self.cooldown = self.start + 0.5


    def draw(self, gamewindow, player):
        if self.visible == True:
            gamewindow.blit(self.image, (self.x, self.y))
            
            self.shootplayer(main_character)

            if self.lazervisible == True:
                pygame.draw.line(gamewindow, self.lazercolor, self.start_pos, self.end_pos, self.lazer_width)
                

            pygame.draw.rect(gamewindow, (255,0,0), (self.hitbox[0], self.hitbox[1] - 20, self.max_hp, 5))
            pygame.draw.rect(gamewindow, (0,255,0), (self.hitbox[0], self.hitbox[1] - 20, self.hp, 5))
            self.hitbox = (self.x + self.x_hitbox,
                           self.y + self.y_hitbox,
                           self.width, self.height)
            #pygame.draw.rect(gamewindow, (0,0,0), self.hitbox, 1)


    def shootplayer(self, player):
        if self.visible == True:
                 
            if time.time() > self.cooldown:                
                xpositions.append(main_character.x)
                ypositions.append(main_character.y)
                
                xdiff = round(xpositions[0] + main_character.width//2) - round(self.x + self.width//2)
                ydiff = round(ypositions[0] + main_character.height//2) - round(self.y + self.height//2)
                magnitude = math.sqrt(float(xdiff **2 + ydiff **2))
                num_frames = int(magnitude/self.lazerspeed)

                xmove = xdiff/num_frames
                ymove = ydiff/num_frames

                self.lazerx += xmove 
                self.lazery += ymove

                self.end_pos = (self.lazerx, self.lazery)
                
                lazer_dict = {}
                lazer_dict['x'] = self.lazerx
                lazer_dict['y'] = self.lazery

                lazer_list.append(lazer_dict)

                if self.lazerx < 1400 and self.lazerx > 0 and self.lazery < 900 and self.lazery > 0:  
                    self.lazervisible = True
                    gamewindow.blit(lazer_img, (round(self.x + 2 + self.width//2) , round(self.y + 40)))

                if self.lazerx < 0 or self.lazerx > 1440 or self.lazery > 900 or self.lazery < 0:
                    self.lazervisible = False
                    self.lazerx = round(self.x + self.width//2)
                    self.lazery = round(self.y + self.height//2)
                    self.cooldown = time.time() + 0.5
                    xpositions.clear()
                    ypositions.clear()
                    lazer_list.clear()
                    
                for i in lazer_list:
                    
                    if i['y'] - self.lazer_width//2 < main_character.hitbox[1] + main_character.hitbox[3] and i['y'] + self.lazer_width//2 > main_character.hitbox[1]:
                        if i['x'] + self.lazer_width//2 > main_character.hitbox[0] and i['x'] - self.lazer_width//2 < main_character.hitbox[0] + main_character.hitbox[2]:
                            if main_character.alive == True:
                                main_hit.play()
                                main_character.current_hp -= self.damage
                            self.lazervisible = False
                            lazer_list.clear()                          
                            self.lazerx = round(self.x + self.width//2)
                            self.lazery = round(self.y + self.height//2)
                            self.cooldown = time.time() + 0.5                  

             
    def hit(self):
       if self.hp > 0:
           if self.weapon_hit_by == 'gun':
               self.hp -= main_character.gun_dmg
           if self.weapon_hit_by == 'sword':
               self.hp -= main_character.sword_dmg
           if self.weapon_hit_by == 'punch':
               self.hp -= main_character.punch_dmg


       if self.hp < 1:
           self.visible = False
           main_character.xp += self.xp



class LazerEnemy(Enemies):
    def __init__(self, x, y, start_x, start_y , width, height, speed, xp, damage,
                         image, x_hitbox, y_hitbox, hp, max_hp):
        super().__init__(x, y, start_x, start_y , width, height, speed, xp, damage,
                         image, x_hitbox, y_hitbox, hp, max_hp)
        self.hitbox = (self.x + 0, self.y + 10, 128, 128)
        self.weapon_hit_by = 'null'
        self.visible = False
        enemies.append(self)
        self.image = image
        self.lazerx = round((self.x) + self.width//2)
        self.lazery = round(self.y + self.height//2)
        self.lazercolor = (125, 0, 0)
        self.start_pos = (round(self.lazerx),round(self.lazery))
        self.end_pos = (self.lazerx, self.lazery)
        self.lazer_width = 5
        self.lazerspeed = 30
        self.lazervisible = True
        self.start = 0
        self.cooldown = self.start + 2.5

    def draw(self, gamewindow, player):
        if self.visible == True:
            gamewindow.blit(self.image, (self.x, self.y))
            
            self.shootplayer(main_character)

            if self.lazervisible == True:
                pygame.draw.line(gamewindow, self.lazercolor, self.start_pos, self.end_pos, self.lazer_width)
                
            pygame.draw.rect(gamewindow, (255,0,0), (self.hitbox[0], self.hitbox[1] - 20, self.max_hp, 5))
            pygame.draw.rect(gamewindow, (0,255,0), (self.hitbox[0], self.hitbox[1] - 20, self.hp, 5))
            self.hitbox = (self.x + self.x_hitbox,
                           self.y + self.y_hitbox,
                           self.width, self.height)
            #pygame.draw.rect(gamewindow, (0,0,0), self.hitbox, 1)


    def shootplayer(self, player):
        if self.visible == True:
                 
            if time.time() > self.cooldown:                
                xpositions.append(main_character.x)
                ypositions.append(main_character.y)
                
                xdiff = round(xpositions[0] + main_character.width//2) - round(self.x + self.width//2)
                ydiff = round(ypositions[0] + main_character.height//2) - round(self.y + self.height//2)
                magnitude = math.sqrt(float(xdiff **2 + ydiff **2))
                num_frames = int(magnitude/self.lazerspeed)

                xmove = xdiff/num_frames
                ymove = ydiff/num_frames

                self.lazerx += xmove 
                self.lazery += ymove

                self.end_pos = (self.lazerx, self.lazery)
                
                lazer_dict = {}
                lazer_dict['x'] = self.lazerx
                lazer_dict['y'] = self.lazery

                lazer_list.append(lazer_dict)

                if self.lazerx < 1400 and self.lazerx > 0 and self.lazery < 900 and self.lazery > 0:  
                    self.lazervisible = True
                    gamewindow.blit(lazer_img, (round(self.x - 13 + self.width//2) , round(self.y + self.height//2 - 14)))

                if self.lazerx < 0 or self.lazerx > 1440 or self.lazery > 900 or self.lazery < 0:
                    self.lazervisible = False
                    self.lazerx = round(self.x + self.width//2)
                    self.lazery = round(self.y + self.height//2)
                    self.cooldown = time.time() + 2.5
                    xpositions.clear()
                    ypositions.clear()
                    lazer_list.clear()
                    
                for i in lazer_list:
                    
                    if i['y'] - self.lazer_width//2 < main_character.hitbox[1] + main_character.hitbox[3] and i['y'] + self.lazer_width//2 > main_character.hitbox[1]:
                        if i['x'] + self.lazer_width//2 > main_character.hitbox[0] and i['x'] - self.lazer_width//2 < main_character.hitbox[0] + main_character.hitbox[2]:
                            if main_character.alive == True:
                                main_hit.play()
                                if main_character.current_room == 'room10':
                                    main_character.current_hp -= 10
                                else:
                                    main_character.current_hp -= 35
                            self.lazervisible = False
                            lazer_list.clear()                          
                            self.lazerx = round(self.x + self.width//2)
                            self.lazery = round(self.y + self.height//2)
                            self.cooldown = time.time() + 2.5             

             
    def hit(self):
       if self.hp > 0:
           if self.weapon_hit_by == 'gun':
               self.hp -= main_character.gun_dmg
           if self.weapon_hit_by == 'sword':
               self.hp -= main_character.sword_dmg
           if self.weapon_hit_by == 'punch':
               self.hp -= main_character.punch_dmg


       if self.hp < 1:
           self.visible = False
           main_character.xp += self.xp




# Room 2 Enemies
enemy1 = StandingEnemy(600, 625, 600, 625, 64, 30, # x, y, width, height, 
                       0, 3, 0,          # speed, xp, damage
                       smallwolf,        # image
                       -5, 0, 0.001, 0.001)    # x_hitbox, y_hitbox, hp, max_hp

enemy2 = StalkingEnemy(1100, 600, 1100, 600, 128, 60,
                       3.5, 7, 2, 
                       bigwolf,
                       -5, 0, 12, 12)

enemy3 = StalkingEnemy(1440, 550, 1440, 550, 128, 60,
                       3, 7, 2, 
                       bigwolf,
                       -5, 0, 12, 12)

enemy4 = StalkingEnemy(1400, 810, 1400, 810, 128, 60,
                       4, 7, 2, 
                       bigwolf,
                       -5, 0, 12, 12)

enemy5 = StalkingEnemy(1200, 675, 1200, 675, 128, 60,
                       4.5, 7, 2, 
                       bigwolf,
                       -5, 0, 12, 12)

# Room 3 Enemies
enemy6 = StalkingEnemy(180, 245, 180, 245, 60, 40,
                       2, 5, 1, 
                       small_spider,
                       0, -5, 15, 15)

enemy7 = XPathEnemy(700, 400, 700, 400, 60, 40,
                       4, 5, 1, 
                       small_spider,
                       0, -5, 15, 15)

enemy8 = StalkingEnemy(1100, 600, 1100, 600, 60, 40,
                       2.1, 5, 1, 
                       small_spider,
                       0, -5, 15, 15)

enemy9 = StalkingEnemy(0, 0, 0, 0, 60, 40,
                       2.2, 5, 1, 
                       small_spider,
                       0, -5, 15, 15)

enemy10 = StalkingEnemy(1400, 700, 1400, 700, 60, 40,
                       2.3, 5, 1, 
                       small_spider,
                       0, -5, 15, 15)

enemy11 = StalkingEnemy(600, 600, 600, 600, 60, 40,
                       2.4, 5, 1, 
                       small_spider,
                       0, -5, 15, 15)

enemy12 = StalkingEnemy(1300, 20, 1300, 20, 60, 40,
                       2.5, 5, 1, 
                       small_spider,
                       0, -5, 15, 15)

enemy13 = StalkingEnemy(120, 600, 120, 600, 60, 40,
                       2.6, 5, 1, 
                       small_spider,
                       0, -5, 15, 15)

enemy14 = StalkingEnemy(600, 820, 600, 820, 100, 80,
                       3.25, 15, 1, 
                       big_spider,
                       10, -5, 25, 25)

enemy15 = StalkingEnemy(950, 200, 950, 200, 60, 40,
                       2.7, 5, 1, 
                       small_spider,
                       0, -5, 15, 15)

enemy16 = StalkingEnemy(1100, 300, 1100, 300, 60, 40,
                       2.8, 5, 1, 
                       small_spider,
                       0, -5, 15, 15)

enemy17 = StalkingEnemy(250, 150, 250, 150, 60, 40,
                       2.9, 5, 1, 
                       small_spider,
                       0, -5, 15, 15)

enemy18 = StalkingEnemy(120, 450, 120, 450, 60, 40,
                       3, 5, 1, 
                       small_spider,
                       0, -5, 15, 15)

enemy19 = XPathEnemy(400, 600, 400, 600, 60, 40,
                       6, 5, 1, 
                       small_spider,
                       0, -5, 15, 15)

enemy20 = XPathEnemy(500, 500, 500, 500, 60, 40,
                       6, 5, 1, 
                       small_spider,
                       0, -5, 15, 15)

# Room 6 Enemies
enemy21 = StalkingEnemy(750, 400, 750, 400, 120, 65,
                       3.5, 10, 2, 
                       rat_left,
                       0, 25, 20, 20)

# Room 5 Enemies
enemy22 = StalkingEnemy(600, 400, 600, 400, 120, 65,
                       3, 10, 2, 
                       rat_right,
                       0, 25, 20, 20)

enemy58a = StalkingEnemy(300, 200, 300, 200, 120, 65,
                       3.5, 10, 2, 
                       rat_right,
                       0, 25, 20, 20)

enemy59a = StalkingEnemy(100, 600, 100, 600, 120, 65,
                       3.75, 10, 2, 
                       rat_right,
                       0, 25, 20, 20)

enemy60a = StalkingEnemy(800, 400, 800, 400, 120, 65,
                       3.5, 10, 2, 
                       rat_right,
                       0, 25, 20, 20)

enemy61a = StalkingEnemy(1000, 300, 1000, 300, 120, 65,
                       3.5, 10, 2, 
                       rat_right,
                       0, 25, 20, 20)

# Room 7 Boss
boss1 = Boss1Enemy(1040, 190, 1040, 190, 285, 230,
                      0, 0, 3000, 
                      boss1,
                      0, 10, 300, 300)

# Room 8 Enemies
enemy62a = StalkingEnemy(100, 500, 100, 500, 120, 65,
                       3.5, 10, 2, 
                       rat_right,
                       0, 25, 25, 25)

enemy63a = StalkingEnemy(0, 0, 0, 0, 100, 80,
                       3, 10, 2, 
                       big_spider,
                       10, -5, 25, 25)

enemy64a = StalkingEnemy(1500, -20, 1500, -20, 128, 60,
                       4, 10, 2, 
                       bigwolf,
                       -5, 0, 25, 25)

# Room 9 Enemies
enemy23 = StalkingEnemy(1400, 800, 1400, 800, 100, 80,
                       3, 10, 2, 
                       bat_left,
                       0, -5, 25, 25)

enemy24 = StalkingEnemy(0, 800, 0, 800, 100, 80,
                       3, 10, 2, 
                       bat_right,
                       0, -5, 25, 25)

enemy25 = ShootingEnemy(1325, 25, 1325, 25, 75, 85, # x, y, width, height,
                      0, 7, 2,          # speed, xp, damage
                      wizard_left,        # image
                      0, 0, 25, 25)     # x_hitbox, y_hitbox, hp, max_hp

enemy26 = ShootingEnemy(50, 260, 50, 260, 75, 85,
                       0, 7, 2,
                       wizard_right,
                       0, 0, 25, 25)

enemy27 = YPathEnemy(605, 15, 605, 15, 81, 128,
                       5, 7, 2, 
                       goblin_img,
                       0, -5, 25, 25)

# Room 10 Enemies
enemy28 = LazerEnemy(45, 125, 45, 125, 81, 128,
                     0, 20, 2,
                     goblin_img,
                     0, -5, 30, 30)
                    
enemy29 = StandingEnemy(1150, 635, 1150, 635, 75, 85,
                       0, 5, 2, 
                       wizard_left,
                       0, 0, 30, 30)

enemy30 = StalkingEnemy(1500, 550, 1500, 550, 100, 80,
                       2, 10, 2, 
                       bat_left,
                       0, -5, 30, 30)

enemy31 = YPathEnemy(950, 600, 950, 600, 100, 80,
                       3, 10, 2, 
                       bat_right,
                       0, -5, 30, 30)

enemy32 = YPathEnemy(850, 600, 850, 600, 100, 80,
                       3, 10, 2, 
                       bat_right,
                       0, -5, 30, 30)

enemy33 = YPathEnemy(750, 600, 750, 600, 100, 80,
                       3, 10, 2, 
                       bat_right,
                       0, -5, 30, 30)

enemy34 = StalkingEnemy(0, 0, 0, 0, 100, 80,
                       3, 10, 2, 
                       bat_right,
                       0, -5, 30, 30)

enemy35 = StalkingEnemy(0, 900, 0, 900, 100, 80,
                       3, 10, 2, 
                       bat_right,
                       0, -5, 30, 30)

enemy36 = StalkingEnemy(1400, 0, 1400, 0, 100, 80,
                       3, 10, 2, 
                       bat_left,
                       0, -5, 30, 30)

enemy37 = StalkingEnemy(500, 0, 500, 0, 100, 80,
                       3, 10, 2, 
                       bat_right,
                       0, -5, 30, 30)

enemy38 = ShootingEnemy(1325, 150, 1325, 150, 75, 85, # x, y, width, height,
                      0, 15, 2,          # speed, xp, damage
                      wizard_left,        # image
                      0, 0, 30, 30)     # x_hitbox, y_hitbox, hp, max_hp

enemy39 = StalkingEnemy(1150, 100, 1150, 100, 100, 80,
                       3, 10, 2, 
                       bat_left,
                       0, -5, 30, 30)

enemy40 = StalkingEnemy(1200, 175, 1200, 175, 100, 80,
                       3, 10, 2, 
                       bat_left,
                       0, -5, 30, 30)

enemy41 = StalkingEnemy(1150, 250, 1150, 250, 100, 80,
                       3, 10, 2, 
                       bat_left,
                       0, -5, 30, 30)

# Room 11 Enemies
enemy42 = StalkingEnemy(650, 500, 650, 500, 97, 99,
                       2, 0, 3, 
                       right_croc,
                       0, 0, 100, 100)

enemy44 = YPathEnemy(1275, 303, 1275, 303, 100, 80,
                       3, 10, 2, 
                       bat_left,
                       0, -5, 35, 35)

enemy45 = XPathEnemy(1050, 500, 1050, 500, 100, 80,
                       3, 10, 2, 
                       bat_right,
                       0, -5, 35, 35)

enemy46 = XPathEnemy(875, 500, 875, 500, 100, 80,
                       3, 10, 2, 
                       bat_right,
                       0, -5, 35, 35)

enemy47 = XPathEnemy(400, 500, 400, 500, 100, 80,
                       3, 10, 2, 
                       bat_right,
                       0, -5, 35, 35)

enemy48 = YPathEnemy(240, 625, 240, 625, 100, 80,
                       3, 10, 2, 
                       bat_right,
                       0, -5, 35, 35)

enemy49 = LazerEnemy(15, 825, 15, 825, 130, 80,
                       3, 5, 2, 
                       bat_right,
                       0, -5, 35, 35)

enemy50 = StalkingEnemy(1400, 1000, 1400, 1000, 100, 80,
                       3, 10, 2, 
                       bat_left,
                       0, -5, 35, 35)

enemy51 = StalkingEnemy(300, 1000, 300, 1000, 100, 80,
                       3, 10, 2, 
                       bat_right,
                       0, -5, 35, 35)

enemy52 = StalkingEnemy(800, 1000, 800, 1000, 100, 80,
                       3, 10, 2, 
                       bat_right,
                       0, -5, 35, 35)

# Room 16 Enemies (Cave)
enemy53 = StalkingEnemy(0, 0, 0, 0, 100, 80,
                       4, 5, 2, 
                       bat_right,
                       0, -5, 40, 40)

enemy54 = StalkingEnemy(0, 800, 0, 800, 60, 40,
                       4, 3, 2, 
                       small_spider,
                       0, -5, 40, 40)

enemy55 = StalkingEnemy(1300, 800, 1300, 800, 120, 65,
                       4, 5, 2, 
                       rat_left,
                       0, 25, 40, 40)

# Room 17 Enemies (House Enterance)
enemy56 = StalkingEnemy(1356, 325, 1356, 325, 79, 93,
                       3.8, 7, 3, 
                       knight_left,
                       0, 0, 50, 50)

enemy57 = StalkingEnemy(15, 325, 15, 325, 79, 93,
                       4, 7, 3, 
                       knight_right,
                       0, 0, 50, 50)

enemy58 = StalkingEnemy(1356, 25, 1356, 25, 79, 93,
                       4.2, 7, 3, 
                       knight_left,
                       0, 0, 50, 50)

enemy59 = StalkingEnemy(15, 15, 15, 15, 79, 93,
                       4.4, 7, 3, 
                       knight_right,
                       0, 0, 50, 50)

enemy60 = StalkingEnemy(1356, 760, 1356, 760, 79, 93, # x, y, width, height,
                       4.4, 7, 3,         # speed, xp, damage
                       knight_left,     # image    
                       0, 0, 50, 50)    # x_hitbox, y_hitbox, hp, max_hp

enemy61 = StalkingEnemy(0, 641, 0, 641, 79, 93,
                       4.6, 7, 3, 
                       knight_right,
                       0, 0, 50, 50)

enemy62 = StalkingEnemy(1356, 125, 1356, 125, 79, 93,
                       4.8, 7, 3, 
                       knight_left,
                       0, 0, 50, 50)


# Room 18 Enemies
enemy63 = StalkingEnemy(10, 460, 10, 460, 79, 93,
                       4, 7, 3, 
                       knight_right,
                       0, 0, 55, 55)

enemy64 = StalkingEnemy(100, 700, 100, 700, 79, 93,
                       4.3, 7, 3, 
                       knight_right,
                       0, 0, 55, 55)

# Room 20 Enemies
enemy65 = StalkingEnemy(0, 425, 0, 425, 79, 93,
                       4.8, 8, 3, 
                       knight_right,
                       0, 0, 20, 20)


# Room 21 Enemies
enemy66 = ShootingEnemy(1350, 100, 1350, 100, 75, 85, # x, y, width, height,
                      0, 20, 3,             # speed, xp, damage
                      wizard_left,          # image
                      0, 0, 20, 20)         # x_hitbox, y_hitbox, hp, max_hp

enemy67 = ShootingEnemy(1350, 250, 1350, 250, 75, 85, 
                      0, 20, 3,          
                      wizard_left,        
                      0, 0, 20, 20)     

enemy68 = LazerEnemy(1350, 400, 1350, 400, 75, 85, 
                      0, 30, 3,          
                      wizard_left,        
                      0, 0, 20, 20)   

enemy69 = ShootingEnemy(1350, 550, 1350, 550, 75, 85, 
                      0, 20, 3,          
                      wizard_left,        
                      0, 0, 20, 20)  

enemy70 = ShootingEnemy(1350, 750, 1350, 750, 75, 85, 
                      0, 20, 3,          
                      wizard_left,        
                      0, 0, 20, 20) 

enemy71 = StalkingEnemy(400, 0, 400, 0, 60, 40,
                       4, 3, 2, 
                       small_spider,
                       0, -5, 20, 20)

enemy72 = StalkingEnemy(0, 0, 0, 0, 60, 40,
                       4, 3, 2, 
                       small_spider,
                       0, -5, 20, 20)

enemy73 = StalkingEnemy(800, 100, 800, 100, 60, 40,
                       4, 3, 2, 
                       small_spider,
                       0, -5, 20, 20)

enemy74 = StalkingEnemy(0, 400, 0, 400, 100, 80,
                       3.5, 10, 2, 
                       bat_right,
                       0, -5, 20, 20)

enemy75 = StalkingEnemy(1400, 400, 1400, 400, 100, 80,
                       3.75, 10, 2, 
                       bat_left,
                       0, -5, 20, 20)

enemy76 = XPathEnemy(400, 500, 400, 500, 81, 128,
                       5, 7, 3, 
                       goblin_img,
                       0, -5, 20, 20)

enemy77 = StalkingEnemy(1500, 450, 1500, 450, 64, 30,  # x, y, width, height, 
                       2.75, 10, 2,          # speed, xp, damage
                       smallwolf,           # image
                       -5, 0, 20, 20)       # x_hitbox, y_hitbox, hp, max_hp

enemy78 = StalkingEnemy(1500, 250, 1500, 250, 128, 60,
                       3.5, 7, 3, 
                       bigwolf,
                       -5, 0, 20, 20)

enemy79 = StalkingEnemy(1500, 0, 1500, 0, 128, 60,
                       3, 7, 3, 
                       bigwolf,
                       -5, 0, 20, 20)

enemy80 = StalkingEnemy(1500, 700, 1500, 700, 128, 60,
                       4, 7, 3, 
                       bigwolf,
                       -5, 0, 20, 20)

# Room 23 Enemies
enemy81 = StalkingEnemy(1400, 400, 1400, 400, 79, 93,
                       4.8, 7, 4, 
                       knight_left,
                       0, 0, 55, 55)

enemy82 = StalkingEnemy(1400, 200, 1400, 200, 79, 93,
                       4.8, 7, 4, 
                       knight_left,
                       0, 0, 50, 50)

# Room 24 Enemies
enemy83 = StandingEnemy(1150, 625, 1150, 625, 87, 90, 
                       0, 3, 0,          
                       deer_big_left,        
                       0, 0, 10, 10)

enemy84 = StandingEnemy(1000, 325, 1000, 325, 87, 90, 
                       0, 3, 0,          
                       deer_big_left,        
                       0, 0, 10, 10)

enemy85 = StandingEnemy(1250, 720, 1250, 720, 87, 90, 
                       0, 3, 0,          
                       deer_big_left,        
                       0, 0, 10, 10)

enemy86 = StandingEnemy(1024, 720, 1024, 720, 87, 90, 
                       0, 3, 0,          
                       deer_big_right,        
                       0, 0, 10, 10)

enemy87 = StandingEnemy(1024, 568, 1024, 568, 87, 90, 
                       0, 3, 0,          
                       deer_big_right,        
                       0, 0, 10, 10)

enemy88 = StandingEnemy(920, 750, 920, 750, 87, 90, 
                       0, 3, 0,          
                       deer_big_right,        
                       0, 0, 10, 10)

enemy89 = StandingEnemy(850, 650, 850, 650, 58, 60, 
                       0, 3, 0,          
                       deer_small,        
                       0, 0, 5, 5)

enemy90 = StandingEnemy(1175, 775, 1175, 775, 58, 60, 
                       0, 3, 0,          
                       deer_small,        
                       0, 0, 5, 5)

# Room 25 Enemies
enemy91 = ShootingEnemy(1300, 50, 1300, 50, 75, 85, 
                      0, 20, 3,          
                      wizard_left,        
                      0, 0, 50, 50)

enemy92 = StandingEnemy(100, 715, 100, 715, 87, 90, 
                       0, 3, 0,          
                       deer_big_right,        
                       0, 0, 10, 10)

# Room 26 Enemies
enemy93 = ShootingEnemy(1300, 50, 1300, 50, 75, 85, 
                      0, 20, 3,          
                      wizard_left,        
                      0, 0, 50, 50)

enemy94 = StalkingEnemy(1300, 600, 1300, 600, 128, 60,
                       3.5, 7, 2, 
                       bigwolf,
                       -5, 0, 60, 60)

enemy95 = StalkingEnemy(1440, 550, 1440, 550, 128, 60,
                       3, 7, 2, 
                       bigwolf,
                       -5, 0, 60, 60)

enemy96 = StalkingEnemy(1300, 800, 1300, 800, 120, 65,
                       4, 5, 2, 
                       rat_left,
                       0, 25, 60, 60)

enemy97 = StalkingEnemy(1100, 20, 1100, 20, 120, 65,
                       3.5, 5, 3, 
                       rat_left,
                       0, 25, 60, 60)

enemy98 = StalkingEnemy(600, 600, 600, 600, 64, 30,  # x, y, width, height, 
                       2.75, 10, 2,          # speed, xp, damage
                       smallwolf,           # image
                       -5, 0, 30, 30)       # x_hitbox, y_hitbox, hp, max_hp

enemy99 = StalkingEnemy(800, 300, 800, 300, 64, 30,  
                       2.5, 10, 2,         
                       smallwolf,         
                       -5, 0, 30, 30)      

enemy100 = StalkingEnemy(300, 820, 300, 820, 100, 80,
                       3.5, 15, 2, 
                       big_spider,
                       10, -5, 60, 60)

enemy101 = StalkingEnemy(200, 20, 200, 20, 100, 80,
                       4, 15, 2, 
                       big_spider,
                       10, -5, 60, 60)

enemy102 = YPathEnemy(300, 150, 300, 150, 81, 128,
                       5, 7, 3, 
                       goblin_img,
                       0, -5, 60, 60)

enemy103 = XPathEnemy(550, 500, 550, 500, 81, 128,
                       5, 7, 2, 
                       goblin_img,
                       0, -5, 60, 60)

enemy104 = StalkingEnemy(0, 0, 0, 0, 60, 40,
                       3.5, 5, 1, 
                       small_spider,
                       0, -5, 30, 30)

enemy105 = StalkingEnemy(100, 0, 100, 0, 60, 40,
                       3, 5, 1, 
                       small_spider,
                       0, -5, 30, 30)

enemy106 = StalkingEnemy(100, 500, 100, 500, 100, 80,
                       3, 10, 3, 
                       bat_right,
                       0, -5, 50, 50)

enemy107 = StalkingEnemy(0, 800, 0, 800, 100, 80,
                       3, 10, 3, 
                       bat_right,
                       0, -5, 50, 50)

# Room 29 Enemies
enemy108 = XPathEnemy(100, 400, 100, 400, 87, 90, 
                       1, 0, 0,          
                       deer_big_right,        
                       0, 0, 10, 10)

enemy109 = XPathEnemy(400, 715, 400, 715, 87, 90, 
                       1, 3, 0,          
                       deer_big_right,        
                       0, 0, 10, 10)

enemy110 = XPathEnemy(1175, 775, 1175, 775, 58, 60, 
                       1, 0, 0,          
                       deer_small,        
                       0, 0, 5, 5)

enemy111 = XPathEnemy(1100, 400, 1100, 400, 58, 60, 
                       1, 0, 0,          
                       deer_small,        
                       0, 0, 5, 5)

# Room 30 Enemies
enemy112 = StandingEnemy(100, 600, 100, 600, 79, 93,
                       4.8, 7, 3, 
                       knight_left,
                       0, 0, 40, 40)

enemy113 = StandingEnemy(250, 600, 250, 600, 79, 93,
                       4.8, 7, 3, 
                       knight_left,
                       0, 0, 40, 40)

enemy114 = StandingEnemy(400, 600, 400, 600, 79, 93,
                       4.8, 7, 3, 
                       knight_left,
                       0, 0, 40, 40)

enemy115 = StandingEnemy(550, 600, 550, 600, 79, 93,
                       4.8, 7, 3, 
                       knight_left,
                       0, 0, 40, 40)

enemy116 = StandingEnemy(700, 600, 700, 600, 79, 93,
                       4.8, 7, 3, 
                       knight_left,
                       0, 0, 40, 40)

enemy117 = StandingEnemy(850, 600, 850, 600, 79, 93,
                       4.8, 7, 3, 
                       knight_left,
                       0, 0, 40, 40)

enemy118 = StandingEnemy(1000, 600, 1000, 600, 79, 93,
                       4.8, 7, 3, 
                       knight_left,
                       0, 0, 40, 40)

enemy119 = StandingEnemy(1150, 600, 1150, 600, 79, 93,
                       4.8, 7, 3, 
                       knight_left,
                       0, 0, 40, 40)

enemy120 = StandingEnemy(1300, 600, 1300, 600, 79, 93,
                       4.8, 7, 3, 
                       knight_left,
                       0, 0, 40, 40)

# Room 31 Enemies
enemy121 = XPathEnemy(1000, 325, 1000, 325, 80, 80, 
                       1, 0, 0,          
                       dog_man,        
                       0, 0, 5, 5)

enemy122 = ShootingEnemy(20, 150, 20, 150, 47, 111,
                       5, 0, 5, 
                       police_gun,
                       0, 0, 50, 50)

enemy123 = StalkingEnemy(20, 300, 20, 300, 47, 111,
                       6, 0, 5, 
                       police_stick,
                       0, 0, 50, 50)

enemy124 = StalkingEnemy(20, 450, 20, 450, 47, 111,
                       7, 0, 5, 
                       police_stick,
                       0, 0, 50, 50)

enemy125 = StalkingEnemy(20, 600, 20, 600, 47, 111, # x, y, width, height, 
                       8, 0, 5,         # speed, xp, damage
                       police_stick,    # image
                       0, 0, 50, 50)  # x_hitbox, y_hitbox, hp, max_hp


# Room 32 Enemies
enemy126 = StalkingEnemy(1400, 100, 1400, 100, 69, 90,
                       4, 20, 4, 
                       bear,
                       0, 0, 55, 55)

enemy127 = StalkingEnemy(800, 450, 800, 450, 69, 90,
                       4.25, 20, 4, 
                       bear,
                       0, 0, 55, 55)

enemy128 = StalkingEnemy(20, 450, 20, 450, 69, 90,
                       4.5, 20, 4, 
                       bear,
                       0, 0, 55, 55)

enemy129 = StalkingEnemy(0, 900, 0, 900, 69, 90,
                       4.75, 20, 4, 
                       bear,
                       0, 0, 55, 55)

enemy130 = StalkingEnemy(1400, 900, 1400, 900, 69, 90,
                       5, 20, 4, 
                       bear,
                       0, 0, 55, 55)


# Room 33 Enemies
enemy131 = StandingEnemy(350, 200, 350, 200, 40, 40,
                       0, 10, 0, 
                       chicken,
                       0, 0, 1, 1)

enemy132 = StandingEnemy(100, 150, 100, 150, 40, 40,
                       0, 10, 0, 
                       chicken,
                       0, 0, 1, 1)

enemy133 = StandingEnemy(450, 50, 450, 50, 40, 40,
                       0, 10, 0, 
                       chicken,
                       0, 0, 1, 1)

enemy134 = StandingEnemy(175, 300, 175, 300, 40, 40,
                       0, 10, 0, 
                       chicken,
                       0, 0, 1, 1)

# Room 34 Enemies
enemy135 = StalkingEnemy(550, 125, 550, 125, 100, 80,
                       2.5, 15, 3, 
                       bat_right,
                       0, -5, 55, 55)

enemy136 = StalkingEnemy(700, 175, 700, 175, 60, 40,
                       3, 15, 5, 
                       small_spider,
                       0, -5, 30, 30)

# Room 35 Enemies
enemy137 = StalkingEnemy(0, 50, 0, 50, 100, 80,
                       7, 15, 3, 
                       bat_right,
                       0, -5, 20, 20)

enemy138 = StalkingEnemy(150, 50, 150, 50, 100, 80,
                       6.75, 15, 3, 
                       bat_right,
                       0, -5, 21, 21)

enemy139 = StalkingEnemy(300, 50, 300, 50, 100, 80,
                       6.5, 15, 3, 
                       bat_right,
                       0, -5, 22, 22)

enemy140 = StalkingEnemy(450, 50, 450, 50, 100, 80,
                       6.25, 15, 3, 
                       bat_right,
                       0, -5, 23, 23)

enemy141 = StalkingEnemy(600, 50, 600, 50, 100, 80,
                       6, 15, 3, 
                       bat_right,
                       0, -5, 24, 24)

enemy142 = StalkingEnemy(750, 50, 750, 50, 100, 80,
                       6, 15, 3, 
                       bat_right,
                       0, -5, 25, 25)

enemy143 = StalkingEnemy(900, 50, 900, 50, 100, 80,
                       6.25, 15, 3, 
                       bat_left,
                       0, -5, 26, 26)

enemy144 = StalkingEnemy(1050, 50, 1050, 50, 100, 80,
                       6.5, 15, 3, 
                       bat_left,
                       0, -5, 27, 27)

enemy145 = StalkingEnemy(1200, 50, 1200, 50, 100, 80,
                       6.75, 15, 3, 
                       bat_left,
                       0, -5, 28, 28)

enemy146 = StalkingEnemy(1350, 50, 1350, 50, 100, 80,
                       7, 15, 3, 
                       bat_left,
                       0, -5, 29, 29)

enemy147 = StalkingEnemy(700, 425, 700, 425, 60, 40,
                       4, 15, 5, 
                       small_spider,
                       0, -5, 30, 30)

# Room 36 Enemies  
enemy148 = StalkingEnemy(0, 500, 0, 500, 60, 40, # x, y, width, height, 
                       4, 15, 3,         # speed, xp, damage
                       small_spider,    # image
                       0, -5, 30, 30)  # x_hitbox, y_hitbox, hp, max_hp

enemy149 = StalkingEnemy(0, 475, 0, 475, 60, 40,
                       4.4, 15, 3, 
                       small_spider,
                       0, -5, 30, 30)

enemy150 = StalkingEnemy(50, 475, 50, 475, 60, 40,
                       4.8, 15, 3, 
                       small_spider,
                       0, -5, 30, 30)

enemy151 = StalkingEnemy(25, 550, 25, 550, 60, 40,
                       5.2, 15, 3, 
                       small_spider,
                       0, -5, 30, 30)

enemy152 = StalkingEnemy(30, 650, 30, 650, 60, 40,
                       5.6, 15, 3, 
                       small_spider,
                       0, -5, 30, 30)

enemy153 = StalkingEnemy(100, 600, 100, 600, 60, 40,
                       6, 15, 3, 
                       small_spider,
                       0, -5, 30, 30)

enemy154 = StalkingEnemy(200, 455, 200, 455, 60, 40,
                       6.4, 15, 3, 
                       small_spider,
                       0, -5, 30, 30)

enemy155 = StalkingEnemy(0, 700, 0, 700, 60, 40,
                       6.2, 15, 3, 
                       small_spider,
                       0, -5, 30, 30)

enemy156 = StalkingEnemy(200, 750, 200, 750, 60, 40,
                       5.8, 15, 3, 
                       small_spider,
                       0, -5, 30, 30)

enemy157 = StalkingEnemy(0, 850, 0, 850, 60, 40,
                       5.4, 15, 3, 
                       small_spider,
                       0, -5, 30, 30)

enemy158 = StalkingEnemy(100, 850, 100, 850, 60, 40,
                       5, 15, 3, 
                       small_spider,
                       0, -5, 30, 30)

enemy159 = StalkingEnemy(200, 525, 200, 525, 60, 40,
                       4.6, 15, 3, 
                       small_spider,
                       0, -5, 30, 30)

enemy160 = StalkingEnemy(175, 600, 175, 600, 60, 40,
                       4.2, 15, 3, 
                       small_spider,
                       0, -5, 30, 30)



def game_over():
    if main_character.current_hp <= 0:

        main_character.alive = False
        main_character.has_son = False
        for i in enemies:
            i.visible = False
        for i in enemies:
            i.x = i.start_x
            i.y = i.start_y
            
        gamewindow.blit(pygame.image.load(os.path.join(SurviveImages, "gameover.jpg")), (0,0))
       
        if keys[pygame.K_HOME]:
            if main_character.current_room == 'room2' or main_character.current_room == 'room3' or\
               main_character.current_room == 'room4' or main_character.current_room == 'room5' or\
               main_character.current_room == 'room6' or\
               main_character.current_room == 'room8' or main_character.current_room == 'room9' or\
               main_character.current_room == 'room10' or\
               main_character.current_room == 'room7' and enemy53.hp > 0:
                main_character.objective1 = False
                main_character.objective2 = False
                main_character.objective3 = False
                main_character.objective4 = False
                main_character.objective5 = False
                main_character.x = 604
                main_character.y = 748
                main_character.level = 1
                main_character.up = False
                main_character.left = False
                main_character.right = False
                main_character.down = True
                main_character.current_hp = 0
                main_character.current_hp += 100
                main_character.full_hp = 100
                main_character.xp = 0
                main_character.xp_needed = 30
                main_character.alive = True
                main_character.has_sword = False
                main_character.sword_dmg = 1
                main_character.punch_dmg = 1
                main_character.current_room = 'room1'
                for i in enemies:
                    i.hp = i.max_hp

            elif main_character.current_room == 'room11':
                main_character.can_move = True
                main_character.bridge = 0
                main_character.x = 28
                main_character.y = 165   
                main_character.level = 7
                main_character.current_hp = 0
                main_character.current_hp += 160
                main_character.full_hp = 160
                main_character.xp = 15
                main_character.xp_needed = 110
                main_character.alive = True
                main_character.has_sword = True
                main_character.sword_dmg = 7
                main_character.punch_dmg = 7
                main_character.current_room = 'room11'
                main_character.up = False
                main_character.left = False
                main_character.down = False
                main_character.right = True
                for i in enemies:
                    i.hp = i.max_hp
                    
            elif main_character.current_room == 'room16' or\
                 main_character.current_room == 'room7' and enemy53.hp <= 0:

                main_character.can_move = True
                main_character.has_sword = True
                main_character.x = 1
                main_character.y = 745
                main_character.level = 7    
                main_character.current_hp = 0
                main_character.current_hp += 160
                main_character.full_hp = 160
                main_character.xp = 108
                main_character.xp_needed = 110
                main_character.sword_dmg = 7
                main_character.punch_dmg = 7
                main_character.alive = True
                main_character.has_son = False
                main_character.found_son = False
                main_character.in_car = False
                main_character.current_room = 'room12'
                main_character.has_key = False
                main_character.up = False
                main_character.left = False
                main_character.down = False
                main_character.right = True
                main_character.has_banana = False
                main_character.banana_tree = 0
                main_character.objective6 = False
                for i in enemies:
                    i.hp = i.max_hp

            elif main_character.current_room == 'room17' or\
                 main_character.current_room == 'room18' or\
                 main_character.current_room == 'room19':
            
                main_character.can_move = True
                main_character.has_sword = True
                main_character.x = 20
                main_character.y = 500
                main_character.level = 7
                main_character.has_key = True
                main_character.current_hp = 0
                main_character.current_hp += 160
                main_character.full_hp = 160
                main_character.xp = 108
                main_character.xp_needed = 110
                main_character.sword_dmg = 7
                main_character.punch_dmg = 7
                main_character.alive = True
                main_character.has_son = False
                main_character.found_son = False
                main_character.in_car = False
                main_character.current_room = 'room15'
                main_character.up = False
                main_character.left = False
                main_character.down = False
                main_character.right = True
                main_character.has_son = False
                main_character.found_son = False
                main_character.question = 0
                main_character.wrong = 0
                for i in enemies:
                    i.hp = i.max_hp
                    
            elif main_character.current_room == 'room20' or\
                 main_character.current_room == 'room21':
                main_character.can_move = True
                main_character.has_sword = True
                main_character.has_sword = True
                main_character.has_son = True
                main_character.found_son = True
                main_character.x = 0
                main_character.y = 700
                main_character.level = 8
                main_character.has_key = False
                main_character.current_hp = 0
                main_character.current_hp += 170
                main_character.full_hp = 170
                main_character.xp = 56
                main_character.xp_needed = 137
                main_character.sword_dmg = 8
                main_character.punch_dmg = 8
                main_character.alive = True
                main_character.in_car = False
                main_character.current_room = 'room20'
                main_character.hog = 'hanging'
                main_character.damaged_door = 0
                main_character.up = False
                main_character.left = False
                main_character.down = False
                main_character.right = True
                for i in enemies:
                    i.hp = i.max_hp

            else:
                main_character.can_move = True
                main_character.speed = 10
                main_character.has_sword = True
                main_character.has_gun = True
                main_character.has_son = True
                main_character.found_son = True
                main_character.x = 700
                main_character.y = 700
                main_character.level = 9
                main_character.current_hp = 0
                main_character.current_hp += 180
                main_character.full_hp = 180
                main_character.xp = 96
                main_character.xp_needed = 171
                main_character.sword_dmg = 9
                main_character.punch_dmg = 9
                main_character.alive = True
                main_character.in_car = False
                main_character.current_room = 'room22'
                main_character.damaged_door = 0
                main_character.up = True
                main_character.left = False
                main_character.down = False
                main_character.right = False
                main_character.chicken_room = 'room33'
                main_character.found_chicken = False
                main_character.has_chicken = False
                main_character.has_rock = False
                main_character.found_rock = False
                main_character.cave = 'closed'
                main_character.objective2 = False
                main_character.objective3 = False
                main_character.objective4 = False
                main_character.objective5 = False
                main_character.objective6 = False
                main_character.objective7 = False
                main_character.objective8 = False
                main_character.objective9 = False
                main_character.objective10 = False
                main_character.objective11 = False
                for i in enemies:
                    i.hp = i.max_hp         


               
# Pause Function
def pause():
    pause = True
    while pause:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_p:
                    pause = False

# Function Drawing for main loop
def redraw_game_window():
    main_character.load_room()
    level_text = font.render('Level: ' + str(f"{main_character.level}"), 1, (0,0,0))
    health_text = font.render('Health: ' + str(f"{main_character.current_hp} / {main_character.full_hp}"), 1, (0,0,0))
    xp_text = font.render('Exp: ' + str(f"{main_character.xp} / {main_character.xp_needed}"), 1, (0,0,0))
    gamewindow.blit(level_text, (20, 20))
    gamewindow.blit(health_text, (20, 45))
    gamewindow.blit(xp_text, (20, 70))
    main_character.enter_new_room()
    main_character.main_character_movement()
    main_character.son()
    
    main_character.stats()
    game_over()
    for bullet in bullets:
        bullet.draw(gamewindow)
    main_character.draw(gamewindow)

    if main_character.has_son == True:
        if main_character.up == True:
            gamewindow.blit(son_up, (main_character.x + 49, main_character.y + 20))
            
    if main_character.has_chicken == True:
        if main_character.down == True:
            gamewindow.blit(chicken_death_left, (main_character.x + 29, main_character.y + 75))

    if main_character.has_rock == True:
        if main_character.down == True:
            gamewindow.blit(rock, (main_character.x + 29, main_character.y + 75))

 
    pygame.display.update()


font = pygame.font.SysFont('comicsans', 30, True)
loop = 0
font20 = pygame.font.Font(None, 20)
font25 = pygame.font.Font(None, 25)
font30 = pygame.font.Font(None, 30)

# Title Loop
play = True
intro = True
while intro:
    pygame.mixer.music.play(-1)
    gamewindow.blit(title_screen, (0,0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_KP_ENTER:
                intro = False
    pygame.display.update()

# Main Loop:
while play:
    clock.tick(fps)
    pygame.mixer.music.set_volume(0.1)
    keys = pygame.key.get_pressed()
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            play = False
        if keys[pygame.K_ESCAPE]:
            play = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:
                print('Game Paused')
                pause()

    main_character.level_up()
    main_character.hit()
    Punch.throw_punch()
    Punch.punch_distance()
    Shoot.bullet_stop()
    Shoot.shoot_gun()
    Sword.sword_distance()
    Sword.swing_sword()
    redraw_game_window()
    loop += 1


pygame.quit()
