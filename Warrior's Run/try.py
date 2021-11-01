import pygame
import sys
from pygame import mixer

pygame.init()
mixer.init()
clock = pygame.time.Clock()

gravity = 0.25
font=pygame.font.Font("freesansbold.ttf", 30)
font2=pygame.font.Font("freesansbold.ttf", 35)

window = pygame.display.set_mode((939,562))

background=pygame.image.load("materials_data/bg.jpg")
background=pygame.transform.scale(background, (939,562))

star=pygame.image.load("materials_data/star-vector-png-transparent-image-pngpix-21.png")
star=pygame.transform.scale(star, (35,35))
star_x=2
x_cor=5000
y_cor=400

background_glow=pygame.image.load("materials_data/bg_glow.jpg")
background_glow=pygame.transform.scale(background_glow, (939,562))

floor=pygame.image.load("materials_data/bottom_floor.jpg")
floor=pygame.transform.scale(floor, (939,171))
floor_x=0

cha=pygame.image.load("character_data/Warrior_Jump_2.png")
cha=pygame.transform.scale(cha, (90,75))
cha_y_change=0
cha_rect=cha.get_rect(center=(50, 250))

coin=pygame.image.load("materials_data/coins_hud.png")
coin = pygame.transform.scale(coin, (15,15))
coin_x_change=2
coin_x=600
coin_y=400
coin_list=[]
bomb_x_change=2
bomb_list=[]
bomb_x=500
bomb_y=400
score=0
score_list=[]
rocket_x_change = 3
rocket_list=[]


#********** karakterin run durumunun oluşumu ve ölçeklendirilmesi **********
cha_run_1=pygame.image.load("character_data/Warrior_Run_1.png").convert_alpha()
cha_run_2=pygame.image.load("character_data/Warrior_Run_2.png").convert_alpha()
cha_run_3=pygame.image.load("character_data/Warrior_Run_3.png").convert_alpha()
cha_run_4=pygame.image.load("character_data/Warrior_Run_4.png").convert_alpha()
cha_run_5=pygame.image.load("character_data/Warrior_Run_5.png").convert_alpha()
cha_run_6=pygame.image.load("character_data/Warrior_Run_6.png").convert_alpha()
cha_run_7=pygame.image.load("character_data/Warrior_Run_7.png").convert_alpha()
cha_run_8=pygame.image.load("character_data/Warrior_Run_8.png").convert_alpha()

cha_run_1=pygame.transform.scale(cha_run_1, (90,75))
cha_run_2=pygame.transform.scale(cha_run_2, (90,75))
cha_run_3=pygame.transform.scale(cha_run_3, (90,75))
cha_run_4=pygame.transform.scale(cha_run_4, (90,75))
cha_run_5=pygame.transform.scale(cha_run_5, (90,75))
cha_run_6=pygame.transform.scale(cha_run_6, (90,75))
cha_run_7=pygame.transform.scale(cha_run_7, (90,75))
cha_run_8=pygame.transform.scale(cha_run_8, (90,75))

cha_list=[cha_run_1,cha_run_2,cha_run_3,cha_run_4,cha_run_5,cha_run_6,cha_run_7,cha_run_8]

#*************************************************************************


anim_num=0
character_time=pygame.time.get_ticks()
#cha_delay=150
cha_delay=1000

game_over=pygame.image.load("text_data/gameover.png").convert_alpha()
game_over=pygame.transform.scale(game_over, (480, 200))
game_over_rect=game_over.get_rect(center= (460,200))

score_img=pygame.image.load("text_data/score.png").convert_alpha()
score_img=pygame.transform.scale(score_img, (105,45))

high_score_img=pygame.image.load("text_data/HIGH-SCORE.png")
high_score_img=pygame.transform.scale(high_score_img,(140,60))

areyouready=pygame.image.load("text_data/are_you_ready.png")
areyouready=pygame.transform.scale(areyouready,(490,210))

press_space=pygame.image.load("text_data/press_space.png")
press_space=pygame.transform.scale(press_space,(630,270))

resume=pygame.image.load("text_data/resume.png")
resume=pygame.transform.scale(resume, (75,75))

pause=pygame.image.load("text_data/stop.png")
pause=pygame.transform.scale(pause, (55,55))

cong=pygame.image.load("text_data/finish.png")
cong=pygame.transform.scale(cong, (350,96))

lvl1=pygame.image.load("text_data/lvl1.png")
lvl1=pygame.transform.scale(lvl1,(100,60))

lvl2=pygame.image.load("text_data/lvl2.png")
lvl2=pygame.transform.scale(lvl2,(120,85))


def floor_loop(floor_x):
    window.blit(floor, (floor_x, 439))
    window.blit(floor, (floor_x + 939, 439))

def animation(delay, anim_num, limit, character_time):
    if pygame.time.get_ticks() - character_time > delay:
        anim_num += 1
        if anim_num == limit:
            anim_num = 0
        character_time = pygame.time.get_ticks()
    return anim_num

def rect():
    return pygame.Rect(cha_rect.centerx - 10 , cha_rect.centery - 24, 20, 55)

def get_coin(x,y):
    coin = pygame.image.load("materials_data/coins_hud.png")
    coin = pygame.transform.scale(coin, (15,15))
    return [coin, x, y, (x+4, y+3, 11, 10)]
coin_list.append(get_coin(400,400))

def get_bomb(x,y):
    bomb = pygame.image.load("materials_data/bomb.png")
    bomb = pygame.transform.scale(bomb, (25,30))
    return [bomb, x, y, (x+4, y+3, 11, 10)]
bomb_list.append(get_bomb(440,400))


def get_rocket(x,y):
    rocket = pygame.image.load("materials_data/red-rocket-png-5.png")
    rocket = pygame.transform.scale(rocket, (50,60))
    return [rocket, x, y, ((x+4, y+3, 11, 10))]
rocket_list.append(get_rocket(1000,335))

def gameover(score):
    maks=max(score_list)
    window.blit(game_over, game_over_rect)
    window.blit(press_space,(182,180))
    window.blit(high_score_img, (385,240))
    text2=font.render(f"{maks}", True, (209, 0, 13))
    window.blit(text2, (535, 255))
    window.blit(score_img, (405,295))
    text3 = font.render(f"{score}", True, (209, 0, 13))
    window.blit(text3, (515, 303))

def start():
    window.blit(press_space,(182,150))
    window.blit(areyouready, (232,170))


collision=False
sit = False

go=False
st=True
running=True
stop=False
done=False
lvl1_done=False
mixer.music.load("sound_data/fireboy-and-watergirl-theme-song-garageband-remix.mp3")
mixer.music.set_volume(0.1)
mixer.music.play(-1)
while True:
    score_list.append(score)
    window.blit(background_glow, (0, 0))
    window.blit(pause, (882, 4))
    while stop:
        maks = max(score_list)
        window.blit(high_score_img, (372, 200))
        text2 = font.render(f"{maks}", True, (255,255,255))
        window.blit(text2, (520, 218))
        window.blit(score_img, (390, 270))
        text3 = font.render(f"{score}", True, (0,0,0))
        window.blit(text3, (500, 280))
        window.blit(press_space, (182, 150))
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    stop = False
    window.blit(background, (0, 0))
    while running:
        if go:
            x_cor=5000
            for bomb in bomb_list:
                bomb_list.remove(bomb)
            for coin in coin_list:
                coin_list.remove(coin)
            for rocket in rocket_list:
                rocket_list.remove(rocket)
            gameover(score)
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        score=0
                        cha_rect.center = (50, 360)
                        bird_y_change = 0
                        bird_y_change -= 6
                        running=False
                        coin_list.append(get_coin(400, 400))
                        bomb_list.append(get_bomb(500, 400))
                        rocket_list.append(get_rocket(1000, 335))
        if st:
            start()
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        score = 0
                        cha_rect.center = (50, 360)
                        bird_y_change = 0
                        bird_y_change -= 6
                        running = False
                        st=False



    x_cor-=star_x
    window.blit(star,(x_cor,y_cor))
    #pygame.draw.rect(window, (255, 0, 255), (x_cor, y_cor, 35,35), 1)
    if x_cor <= 0:
        x_cor=5000

    window.blit(resume, (880, -2))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and sit == True:
                jump_sound=mixer.Sound("sound_data/whoosh-sound-effect.mp3")
                jump_sound.set_volume(1)
                jump_sound.play()
                cha_rect.center=(50, 360)
                cha_y_change = 0
                cha_y_change -= 6
            if event.key == pygame.K_ESCAPE:
                stop=True

    if cha_rect.centery <= 400:
        sit = False
        cha_y_change += gravity
        cha_rect.centery += cha_y_change
    else:
        sit = True

    if sit:
        anim_num=animation(cha_delay, anim_num, 8, character_time)
        window.blit(cha_list[anim_num], cha_rect)
    else:
        window.blit(cha, cha_rect)
    #pygame.draw.rect(window, (255,0,255), (cha_rect.centerx - 10 , cha_rect.centery - 24, 20, 55),2)

    if lvl1_done == False:
        window.blit(lvl1, (415,0))
        for coin in coin_list:
            window.blit(coin[0], (coin[1], coin[2]))
            coin[1]-=coin_x_change
            #pygame.draw.rect(window, (255,0,0), (coin[1]+4, coin[2]+3, 11, 10), 1)
            if score <= 2:
                if coin[1] == 250:
                    coin_list.append(get_coin(1000, 400))
            elif score >= 3 and score < 6:
                if coin[1] == 250:
                    coin_list.append(get_coin(1000, 400))
                    coin_list.append(get_coin(1400, 400))
            elif score >= 6 and score < 10:
                if coin[1] == 250:
                    coin_list.append(get_coin(1000, 400))
                    coin_list.append(get_coin(1500, 400))
                    coin_list.append(get_coin(1900, 400))



        for coin in coin_list:
            if rect().colliderect(coin[1]+4, coin[2]+3, 11, 10):
                coin_sound=mixer.Sound("sound_data/coin-collect-variant-sound-effect.mp3")
                coin_sound.set_volume(1)
                coin_sound.play()
                score += 1
                coin_list.remove(coin)

        for bomb in bomb_list:
            window.blit(bomb[0], (bomb[1], bomb[2]))
            bomb[1] -= bomb_x_change
            #pygame.draw.rect(window, (0, 0, 0), (bomb[1] + 3, bomb[2] + 5, 15, 23), 1)
            if score <= 2:
                if bomb[1] == 300:
                    bomb_list.append(get_bomb(1070, 400))
            elif score >= 3 and score < 6:
                if bomb[1] == 300:
                    bomb_list.append(get_bomb(1000, 400))
                    bomb_list.append(get_bomb(1420, 400))
            elif score >= 6 and score < 10:
                if bomb[1] == 300:
                    bomb_list.append(get_bomb(1350, 400))
                    bomb_list.append(get_bomb(1800, 400))
                    '''bomb_list.append(get_bomb(2100, 400))
                    bomb_list.append(get_bomb(2400, 400))'''
            elif score >= 10:
                if bomb[1] == 300:
                    bomb_list.append(get_bomb(1300, 400))
                    bomb_list.append(get_bomb(1700, 400))
                    bomb_list.append(get_bomb(2100, 400))


        for bomb in bomb_list:
            if rect().colliderect(bomb[1] + 3, bomb[2] + 5, 15, 23):
                collision_sound=mixer.Sound("sound_data/xp-critical-error-sound-effect.mp3")
                collision_sound.set_volume(1)
                collision_sound.play()
                score_list.append(score)
                running=True
                go=True

        for rocket in rocket_list:
            window.blit(rocket[0], (rocket[1], rocket[2]))
            rocket[1] -= rocket_x_change
            #pygame.draw.rect(window, (0, 0, 0), (rocket[1] + 3, rocket[2] + 22, 40, 18), 1)
            if score <= 2:
                if rocket[1] == 310:
                    rocket_list.append(get_rocket(1000, 335))
            elif score >= 3 and score < 6:
                if rocket[1] == 310:
                    rocket_list.append(get_rocket(1000, 335))
            elif score >=6 and score < 10:
                if rocket[1] == 310:
                    rocket_list.append(get_rocket(1000, 335))
            elif score >= 10:
                if rocket[1] == 310:
                    rocket_list.append(get_rocket(1000, 335))

        for rocket in rocket_list:
            if rect().colliderect(rocket[1] + 3, rocket[2] + 22, 40, 18):
                collision_sound = mixer.Sound("sound_data/xp-critical-error-sound-effect.mp3")
                collision_sound.set_volume(1)
                collision_sound.play()
                rocket_list.remove(rocket)
                score_list.append(score)
                running=True
                go=True
    elif lvl1_done == True:
        window.blit(lvl2, (405, -10))
        for coin in coin_list:
            window.blit(coin[0], (coin[1], coin[2]))
            coin[1]-=coin_x_change
            #pygame.draw.rect(window, (255,0,0), (coin[1]+4, coin[2]+3, 11, 10), 1)
            if score <= 2:
                if coin[1] == 250:
                    coin_list.append(get_coin(1000, 400))
            elif score >= 3 and score < 6:
                if coin[1] == 250:
                    coin_list.append(get_coin(1000, 400))
                    coin_list.append(get_coin(1400, 400))
            elif score >= 6 and score < 10:
                if coin[1] == 250:
                    coin_list.append(get_coin(1000, 400))
                    coin_list.append(get_coin(1350, 400))
            elif score >= 10:
                if coin[1] == 250:
                    coin_list.append(get_coin(1000, 400))
                    coin_list.append(get_coin(1250, 400))
                    coin_list.append(get_coin(1440, 400))



        for coin in coin_list:
            if rect().colliderect(coin[1]+4, coin[2]+3, 11, 10):
                coin_sound=mixer.Sound("sound_data/coin-collect-variant-sound-effect.mp3")
                coin_sound.set_volume(1)
                coin_sound.play()
                score += 1
                coin_list.remove(coin)




        for bomb in bomb_list:
            window.blit(bomb[0], (bomb[1], bomb[2]))
            bomb[1] -= bomb_x_change
            #pygame.draw.rect(window, (0, 0, 0), (bomb[1] + 3, bomb[2] + 5, 15, 23), 1)
            if score <= 2:
                if bomb[1] == 300:
                    bomb_list.append(get_bomb(1070, 400))
            elif score >= 3 and score < 6:
                if bomb[1] == 300:
                    bomb_list.append(get_bomb(1000, 400))
                    bomb_list.append(get_bomb(1500, 400))
            elif score >= 6 and score < 10:
                if bomb[1] == 300:
                    bomb_list.append(get_bomb(1050, 400))
                    bomb_list.append(get_bomb(1450, 400))
            elif score >= 10:
                if bomb[1] == 300:
                    bomb_list.append(get_bomb(1050, 400))
                    bomb_list.append(get_bomb(1500, 400))

        for bomb in bomb_list:
            if rect().colliderect(bomb[1] + 3, bomb[2] + 5, 15, 23):
                collision_sound=mixer.Sound("sound_data/xp-critical-error-sound-effect.mp3")
                collision_sound.set_volume(1)
                collision_sound.play()
                score_list.append(score)
                running=True
                go=True

        for rocket in rocket_list:
            window.blit(rocket[0], (rocket[1], rocket[2]))
            rocket[1] -= rocket_x_change
            #pygame.draw.rect(window, (0, 0, 0), (rocket[1] + 3, rocket[2] + 22, 40, 18), 1)
            if score <= 2:
                if rocket[1] == 310:
                    rocket_list.append(get_rocket(1000, 335))
            elif score >= 3 and score < 6:
                if rocket[1] == 310:
                    rocket_list.append(get_rocket(1000, 335))
            elif score >=6 and score < 10:
                if rocket[1] == 310:
                    rocket_list.append(get_rocket(1000, 335))
            elif score >= 10:
                if rocket[1] == 310:
                    rocket_list.append(get_rocket(1000, 335))

        for rocket in rocket_list:
            if rect().colliderect(rocket[1] + 3, rocket[2] + 22, 40, 18):
                collision_sound = mixer.Sound("sound_data/xp-critical-error-sound-effect.mp3")
                collision_sound.set_volume(1)
                collision_sound.play()
                rocket_list.remove(rocket)
                score_list.append(score)
                running=True
                go=True


    window.blit(score_img, (0, 0))
    text2 = font2.render(f"{score}", True, (0, 0, 0))
    window.blit(text2, (110, 8))

    if rect().colliderect(x_cor, y_cor, 35,35):
        done = True
        while done:
            for bomb in bomb_list:
                bomb_list.remove(bomb)
            for coin in coin_list:
                coin_list.remove(coin)
            for rocket in rocket_list:
                rocket_list.remove(rocket)
            maks = max(score_list)
            window.blit(high_score_img, (380, 200))
            text2 = font.render(f"{maks}", True, (255, 255, 255))
            window.blit(text2, (525, 218))
            window.blit(score_img, (398, 270))
            text3 = font.render(f"{score}", True, (0, 0, 0))
            window.blit(text3, (505, 280))
            window.blit(press_space, (120, 150))
            window.blit(cong, (290, 100))
            window.blit(lvl2, (620, 318))
            pygame.display.update()
            lvl1_done=True
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_SPACE:
                        score=0
                        coin_list.append(get_coin(400, 400))
                        bomb_list.append(get_bomb(440, 400))
                        rocket_list.append(get_rocket(1000, 335))
                        background=pygame.image.load("materials_data/hell.jpg")
                        background=pygame.transform.scale(background, (939,562))
                        background_glow = pygame.image.load("materials_data/hell_glow.jpg")
                        background_glow = pygame.transform.scale(background_glow, (939, 562))
                        cha_rect.center = (50, 360)
                        cha_y_change = 0
                        cha_y_change -= 6
                        done=False
                    if event.key == pygame.K_ESCAPE:
                        stop = True

    floor_x -= 2
    floor_loop(floor_x)
    if floor_x <= -939:
        floor_x = 0



    clock.tick(60)
    pygame.display.update()
