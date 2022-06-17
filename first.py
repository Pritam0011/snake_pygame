import random
import pygame
import os

pygame.mixer.init()
x = pygame.init()

# colors
white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)
green = (0, 255, 0)

# creating window

gameWindow = pygame.display.set_mode((500, 400))
pygame.display.set_caption("My First Game")
pygame.display.update()

win = pygame.image.load("img\wel.jpg")
# win = pygame.transform.scale(win, (500, 400)).convert_alpha()
govr = pygame.image.load("img\gover.jpg")
# govr = pygame.transform.scale(win, (500, 400)).convert_alpha()
bg = pygame.image.load("img\\bgg3.jpg")
clock = pygame.time.Clock()
font = pygame.font.SysFont(None, 30)
def text_screen(text, color, x, y):
        screen_text = font.render(text, True, color)
        gameWindow.blit(screen_text, (x, y))
def plot_snk(gameWindow, color, snake_list, snake_size):
    for x, y in snake_list:
        pygame.draw.rect(gameWindow, color, [x, y, snake_size, snake_size])

def welcome():
    exit_game = False
    while not exit_game:
        gameWindow.fill(white)
        gameWindow.blit(win, (0, 0))
        
        text_screen("Welcome to PRIT snake game", white, 110, 150)
        text_screen("Enter spacebar to enter the game", (255, 255, 0), 90, 185)
        if(not os.path.exists("highScore.txt")):
            with open("highScore.txt","w") as f:
                f.write("0")
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    pygame.mixer.music.load("sounds\gsound.mp3")
                    pygame.mixer.music.play()
                    gloop()
                if event.key == pygame.K_DELETE:
                    with open("highScore.txt", "w") as f:
                        f.write("0")

        pygame.display.update()
        clock.tick(60)

def gloop():
    # Game specific variable
    game_over = False
    exit_game = False
    snake_x = 45
    snake_y = 55
    snake_size = 15
    v = 3
    v_x = 0
    v_y = 0
    f_x = random.randint(0, 500)
    f_y = random.randint(0, 400)
    score = 0
    fps = 50
    snake_len = 1
    snake_list = []
    re = red
    
    with open("highScore.txt", "r") as f:
        hi = f.read()

    

    #creating game loop
    while not exit_game:
        if game_over:
            gameWindow.fill(white)
            gameWindow.blit(govr, (0, 0))
            text_screen("Game Over! Press Enter to continue...", red, 500/2-500/4-50, 400/2-50)
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        gloop()
                    else:
                        exit_game = True

        else:
            for event in pygame.event.get():

                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type == pygame.KEYDOWN:

                    if event.key == pygame.K_RIGHT:
                        v_x = v
                        v_y = 0
                    if event.key == pygame.K_LEFT:
                        v_x = -v
                        v_y = 0
                    if event.key == pygame.K_UP:
                        v_y = -v
                        v_x = 0
                    if event.key == pygame.K_DOWN:
                        v_y = v
                        v_x = 0
            snake_x = snake_x + v_x
            snake_y = snake_y + v_y
            if abs(snake_x - f_x) < 18 and abs(snake_y - f_y) < 18:
                score += 10
                f_x = random.randint(20, 450)
                f_y = random.randint(50, 250)
                snake_len += 3
                r = random.randint(0, 255)
                g = random.randint(0, 255)
                b = random.randint(0, 255)
                re = (r, g, b)
                pygame.mixer.music.load("sounds\\beep.mp3")
                pygame.mixer.music.play()


            if score > int(hi):
                hi = score
                with open("highScore.txt", "w") as f:
                    f.write(str(hi))

            gameWindow.fill(white)
            gameWindow.blit(bg, (0, 0))
            text_screen("HighScore: " + str(hi) +"   "+ "Score: " + str(score), red, 5, 5)
            pygame.draw.circle(gameWindow, re, (f_x, f_y), snake_size-8)

            head = []
            head.append(snake_x)
            head.append(snake_y)
            snake_list.append(head)

            if len(snake_list) > snake_len:
                del snake_list[0]
            if head in snake_list[:-1]:
                game_over = True
                pygame.mixer.music.pause()
                pygame.mixer.music.load("sounds\\burst.mp3")
                pygame.mixer.music.play()
            if snake_x < 0 or snake_x > 500 or snake_y < 0 or snake_y > 400:
                game_over = True
                pygame.mixer.music.pause()
                pygame.mixer.music.load("sounds\\burst.mp3")
                pygame.mixer.music.play()


            # pygame.draw.rect(gameWindow, black, [snake_x, snake_y, snake_size, snake_size])
            plot_snk(gameWindow, black, snake_list, snake_size)

        pygame.display.update()     #to update display
        clock.tick(fps)

    pygame.quit()


    quit()

welcome()