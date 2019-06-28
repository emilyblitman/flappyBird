import pygame, random, sys, pandas
from pygame.locals import *
from Bird import Bird
from platforms import Platform
from scorecounter import ScoreCounter
from coin import Coin

pygame.init()
screen_info = pygame.display.Info()

# set the width and height to the size of the screen
size = (width, height) = (int(screen_info.current_w), int(screen_info.current_h))

screen = pygame.display.set_mode(size)
clock = pygame.time.Clock()
color = (30, 0, 30)
background = pygame.image.load('background.png')
background = pygame.transform.scale(background, (width, height))


# Setup Game Variables
platforms = pygame.sprite.Group()
scorecounters = pygame.sprite.Group()
coins = pygame.sprite.Group()

startPos = (width/8, height/2)
Player = Bird(startPos)
GapSize = 200
Ticks = 0
loopCount = 0
score = 0

def lose():
    global score
    score = 0
    font = pygame.font.SysFont(None, 70)
    text = font.render("You Died!", True, (255, 0, 0))
    text_rect = text.get_rect()
    text_rect.center = (width/2, height/2)
    while True:
        clock.tick(60)
        screen.fill(color)
        screen.blit(text, text_rect)
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    scorecounters.empty()
                    platforms.empty()
                    coins.empty()
                    Player.reset(startPos)
                    return


def displayScore(score):
    font = pygame.font.SysFont(None, 70)
    text = font.render("Score: " + str(score), True, (255, 0, 0))
    text_rect = text.get_rect()
    text_rect.center = (width/2, height/2)
    screen.blit(text, text_rect)


def main():
    global loopCount, score
    while True:
        clock.tick(45)
        if loopCount % 70 == 0:
            toppos = random.randint(0, height/2) - 400
            platforms.add(Platform((width + 100, toppos + GapSize + 800)))
            platforms.add(Platform((width + 100, toppos), True))
            scorecounters.add(ScoreCounter((width + 100, 0)))
        elif loopCount % 35 == 0 and random.randint(0, 2) == 1:
            coins.add(Coin((width + 100, random.randint(height/4, height - (height/4)))))

        for event in pygame.event.get():
            if event.type == QUIT:
                 sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    Player.speed[1] = -10
            # if event.type == pygame.KEYUP:
            #     Player.speed[1] = 10
        screen.fill(color)
        Player.update()
        platforms.update()
        coins.update()
        scorecounters.update()

        gets_hit = pygame.sprite.spritecollide(Player, platforms, False) \
                   or Player.rect.center[1] > height

        score_counters_hit = pygame.sprite.spritecollide(Player, scorecounters, False)

        if score_counters_hit.__len__() > 0:
            score += 1
            scorecounters.remove(score_counters_hit)

        coins_collected = pygame.sprite.spritecollide(Player, coins, False)

        if coins_collected.__len__() > 0:
            score += 5
            coins.remove(coins_collected)

        screen.blit(background, [0, 0])
        platforms.draw(screen)
        scorecounters.draw(screen)
        coins.draw(screen)
        displayScore(score)
        screen.blit(Player.image, Player.rect)
        pygame.display.flip()
        loopCount += 1

        if gets_hit:
            lose()


if __name__ == '__main__':
    main()