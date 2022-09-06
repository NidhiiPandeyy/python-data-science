
import pgzrun 
import random


WIDTH = 600
HEIGHT = 800
MAX_BULLETS = 3

level = 1
lives = 3
score = 0

game_over = False
game_started = False 

bg = Actor('bg',center =(400,450))
background = Actor("bgimg",center = (0,0))
player = Actor("ironman", (200, 580))
enemies = []
bullets = []
bombs = []

center = (WIDTH//2, HEIGHT//2) #points to center coordinates of screen

def show_screen_1():
    bg.draw()
    screen.draw.text('Our Game', center = center, fontsize = 100, color = 'black')
    screen.draw.text('Press Space to start', center =(center[0],center[1]+100), fontsize = 50, color='white')
    #show_screen_1

def draw1():
    screen.clear()
    if not game_started:
        show_screen_1()
    elif game_started and not game_over:
        draw() 
    else:
        show_game_over()

def draw():
    
    background.draw()
    player.draw()
    for enemy in enemies:
        enemy.draw()
    for bullet in bullets:
        bullet.draw()
    for bomb in bombs:
        bomb.draw()
    draw_text()

def show_game_over():
    bg.draw()
    screen.draw.text('Game Over', center = center, fontsize=100, color='white')

def update(delta):
    
    move_player()
    move_bullets()
    move_enemies()
    create_bombs()
    move_bombs()
    check_for_end_of_level()
'''
def move_player():
    pass

def move_enemies():
    pass

def move_bullets():
    pass

def create_bombs():
    pass

def move_bombs():
    pass

def check_for_end_of_level():
    pass

def draw_text():
    pass
'''

def create_enemies():
    for x in range(0, 600, 60):
        for y in range(0, 200, 60):
            enemy = Actor("enemy", (x, y))
            enemy.vx = level * 2
            enemies.append(enemy)
create_enemies()

def move_player():
    if keyboard.right:
        player.x = player.x + 5
    if keyboard.left:
        player.x = player.x - 5
    if player.x > WIDTH:
        player.x = WIDTH
    if player.x < 0:
        player.x = 0

def move_enemies():
    global score
    for enemy in enemies:
        enemy.x = enemy.x + enemy.vx
        if enemy.x > WIDTH or enemy.x < 0:
            enemy.vx = -enemy.vx
            animate(enemy, duration=0.1, y=enemy.y + 60)
        for bullet in bullets:
            if bullet.colliderect(enemy):
                enemies.remove(enemy)
                bullets.remove(bullet)
                score = score + 1
        if enemy.colliderect(player):
            exit()

def draw_text():
    screen.draw.text("Level " + str(level), (0, 0), color="red")
    screen.draw.text("Score " + str(score), (100, 0), color="red")
    screen.draw.text("Lives " + str(lives), (200, 0), color="red")

def on_key_down(key):
    if key == keys.SPACE and len(bullets) < MAX_BULLETS:
        bullet = Actor("bullet", pos=(player.x, player.y))
        bullets.append(bullet)

def move_bullets():
    for bullet in bullets:
        bullet.y = bullet.y - 6
        if bullet.y < 0:
            bullets.remove(bullet)

def create_bombs():
    if random.randint(0, 100 - level * 6) == 0:
        enemy = random.choice(enemies)
        bomb = Actor("bomb", enemy.pos)
        bombs.append(bomb)

def move_bombs():
    global lives
    for bomb in bombs:
        bomb.y = bomb.y + 10
        if bomb.colliderect(player):
            bombs.remove(bomb)
            lives = lives - 1
            if lives == 0:
                exit()

def check_for_end_of_level():
    global level
    if len(enemies) == 0:
        level = level + 1
        create_enemies()

pgzrun.go()