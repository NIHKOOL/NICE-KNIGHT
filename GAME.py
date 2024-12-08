import pygame as pg
import random


#setup
pg.init() 
pg.mixer.init()
pg.display.set_caption("NICE KNIGHT FIGHT MIGHT LIKE MIKE")
screen_w = 1200
screen_h = 675
screen = pg.display.set_mode((screen_w,screen_h))

#music_sound
pg.mixer.music.load("music/Now-We-Ride(chosic.com).mp3")
pg.mixer.music.set_volume(0.4)
pg.mixer.music.play()
Blink_eff = pg.mixer.Sound("music/shining-anime-sound-effect-240582.mp3")
Blink_eff.set_volume(0.2)
fin_cd = pg.mixer.Sound("music/key-get-39925.mp3")
fin_cd.set_volume(0.5)
death_g = pg.mixer.Sound('music/male-death-sound-128357.mp3')
death_g.set_volume(0.2)
dg = pg.mixer.Sound('music/dragon-growl-37570.mp3')
dg.set_volume(0.4)


#color-RGB
white = (255,255,255)
green = (0,255,0)

#speed
speed = 3
blink = 200
cooldown = 0

#time
t = 45

#back gound - font
bg_img = pg.image.load('img/bg3.jpg')
font = pg.font.Font(None,35)
cd_text = font.render("Blink Cooldown : " + str(cooldown), True, white)
tutorial = font.render("Press O or P to Blink", True , white)

#Protagonist and other 
char = pg.image.load('img/pngegg.png')
char = pg.transform.scale(char,(91,100))
char_rect = char.get_rect()
char_rect.centerx = screen_w//2-55
char_rect.centery = screen_h//2+165
clock = pg.time.Clock() ; FPS = 120
cd = False

gob = pg.image.load('img/Gob.png')
gob = pg.transform.scale(gob,(91,100))
gob_rect = gob.get_rect()
gob_rect.center = (screen_w//2-200, screen_h//2+165)

dragon = pg.image.load('img/Dragon.png')
dragon = pg.transform.scale(dragon,(500,500))
dragon_rect = dragon.get_rect()
dragon_rect.center = (screen_w + 1600,screen_h//2)

score = 0
play_once = True

#jump
is_jumping = False
jump_speed = 12
gravity = 0.5
velocity_y = 0  
ground_y = screen_h//2 + 113




#run game 
running = True 
while running :
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False 

    if char_rect.colliderect(gob_rect):
        death_g.play()
        score += 1
        gob_rect.left = random.randint(0,screen_w - 50)

    if char_rect.colliderect(dragon_rect):
        running = False


    keys = pg.key.get_pressed()
    if (keys[pg.K_SPACE] or keys[pg.K_w]) and not is_jumping:
        is_jumping = True
        velocity_y = -jump_speed
    if keys[pg.K_a] and char_rect.left > 0: 
        char_rect.x -= speed
    if keys[pg.K_d] and char_rect.right < screen_w+1: 
        char_rect.x += speed
    if not char_rect.right + blink > screen_w :
        if keys[pg.K_p] and cooldown == 0:
            char_rect.x += blink
            Blink_eff.play()
            cooldown = 3.5
            cd = False
    else:
        if keys[pg.K_p] and cooldown == 0:
            char_rect.x = 1110
            Blink_eff.play()
            cooldown = 3.5
            cd = False

    if not char_rect.left - blink < 0 :
        if keys[pg.K_o] and cooldown == 0:
            char_rect.x -= blink
            Blink_eff.play()
            cooldown = 3.5
            cd = False
    else:
        if keys[pg.K_o] and cooldown == 0:
            char_rect.x = 0
            Blink_eff.play()
            cooldown = 3.5
            cd = False

    if is_jumping:
        char_rect.y += velocity_y
        velocity_y += gravity  
        if char_rect.y >= ground_y:  
            char_rect.y = ground_y
            is_jumping = False
            velocity_y = 0

    cooldown -= 0.01
    if cooldown < 0 :
        cooldown = 0
        if cd == False:
            fin_cd.play()
            cd = True 

    if t < 0:
        t = 0
        if play_once == True: 
            dg.play()
            play_once = False
        dragon_rect.x -= 6
    t -= 0.0085

    cd_text = font.render("Blink Cooldown : " + str(round(cooldown,1)), True, white)
    score_text = font.render("Score : " + str(score), True, green)
    Time = font.render("Time : " + str(round(t)), True, white)

    screen.blit(bg_img,(0,0))
    screen.blit(gob,gob_rect)
    screen.blit(dragon,dragon_rect)
    screen.blit(char,char_rect)
    screen.blit(cd_text,(50,620))
    screen.blit(score_text,(50,50))
    screen.blit(Time, (50,100))
    screen.blit(tutorial,(925,620))

    #้hitbox
    #pg.draw.rect(screen,white,char_rect,2)
    #pg.draw.rect(screen,white,gob_rect,2)

    pg.display.update()
    clock.tick(FPS)
pg.quit()

print("\nnGood job your score is : " + str(score))
print("  / \\  ")
print("  | |   ")
print("  |.|   ")
print("  |:|   ")
print(",_|:|_,  ")
print("  [|]   ")
print("   |    ")
print("  ''' ")
print("")