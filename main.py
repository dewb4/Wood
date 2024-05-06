import pygame
import sys
import random
import os
from datetime import datetime

pygame.init()

WIDTH, HEIGHT = 700, 500
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Lumberjack Simulator")

# Set up colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
YELLOW = (255, 255, 0)

# Set up fonts
font_path = "zig.ttf"
font_size = 20
font = pygame.font.Font(font_path,font_size)

# Function to display text
def draw_text(text, color, x, y):
    surface = font.render(text, True, color)
    rect = surface.get_rect()
    rect.topleft = (x, y)
    WINDOW.blit(surface, rect)

def animate_text(text, color, x, y):
    for i in range(len(text)+1):
        draw_text(text[:i], color, x, y)
        pygame.display.flip()
        pygame.time.wait(25)  # Adjust the speed of text animation here

# Function to create a button
def draw_button(x, y, width, height, color):
    pygame.draw.rect(WINDOW, color, (x, y, width, height))

def clear_text():
    draw_button(5, 350, 1000, 1000, BLACK)

def main_menu(p, car):
    if p.location == "work":
        p.time_pass(0)
    else:
        if car.drive_car() == "empty":
            map(p, car)
        else:
            p.time_pass(15)
            p.location = "work"
    p.wagetime = 0
    running = True
    wait = False
    tree_img = pygame.image.load("tree2.png")
    log_img = pygame.image.load("log.png")
    cig_img = pygame.image.load("cigpack.png")
    cig_img = pygame.transform.scale(cig_img, (50,50))
    monster_img = pygame.image.load("monster.png")
    cash_img = pygame.image.load("cash.png")
    takis_img = pygame.image.load("takis.png")
    fire_img = pygame.image.load("fire.png")
    fire_img = pygame.transform.scale(fire_img, (40,40))
    heart_img = pygame.image.load("Heart.png")
    heart_img = pygame.transform.scale(heart_img, (20,20))
    apple_img = pygame.image.load("apple.png")
    apple_img = pygame.transform.scale(apple_img, (50,50))
    beer_img = pygame.image.load("beer.png")
    beer_img = pygame.transform.scale(beer_img, (50,50))
    nrg_img = pygame.image.load("energy.png")
    nrg_img = pygame.transform.scale(nrg_img, (30,30))
    drunk_img = pygame.image.load("drunk.png")
    drunk_img = pygame.transform.scale(drunk_img, (30,30))
    car_img = pygame.image.load("car.png")
    car_img = pygame.transform.scale(car_img, (50,50))
    button_clicked = False

    while running:
        p.refresh_game_numbers()
        p.time_pass(0)
        fire_button = pygame.Rect(150, 5, 65, 65)
        WINDOW.blit(fire_img, (fire_button.x, fire_button.y))
        tree_button = pygame.Rect(200, 100, 102, 128)
        WINDOW.blit(tree_img, (tree_button.x, tree_button.y))
        log_button = pygame.Rect(550, -5, 65, 65)
        WINDOW.blit(log_img, (log_button.x, log_button.y))
        cig_button = pygame.Rect(560, 50, 50, 50)
        WINDOW.blit(cig_img, (cig_button.x, cig_button.y))
        monst_button = pygame.Rect(550, 110, 65, 65)
        WINDOW.blit(monster_img, (monst_button.x, monst_button.y))
        takis_button = pygame.Rect(550, 150, 65, 65)
        WINDOW.blit(takis_img, (takis_button.x, takis_button.y))
        apple_button = pygame.Rect(560, 210, 50, 50)
        WINDOW.blit(apple_img, (apple_button.x, apple_button.y))
        beer_button = pygame.Rect(560, 260, 65, 65)
        WINDOW.blit(beer_img, (beer_button.x, beer_button.y))
        car_button = pygame.Rect(0, 60, 65, 65)
        WINDOW.blit(car_img, (car_button.x, car_button.y))
        heart_button = pygame.Rect(15, 120, 65, 65)
        WINDOW.blit(heart_img, (heart_button.x, heart_button.y))
        WINDOW.blit(nrg_img, (10, 150))
        WINDOW.blit(drunk_img, (10, 190))

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if p.talking == True:
                    break
                else:
                    if car_button.collidepoint(event.pos):
                        pay = p.wagetime/12
                        if p.wagetime > 480:
                            pay += ((p.money - 480)/12)
                        p.money += int(pay)
                        p.wagetime = 0
                        map(p, car)
                    if tree_button.collidepoint(event.pos):
                        if p.hp == 0:
                            p.text_animation("You starve to death.")
                            running = False
                        if p.craving > 9:
                            p.text_animation("You can't function unless you have a goddamn cigarette.")
                            continue
                        if p.sleepdep > 1140:
                            p.text_animation("You need to sleep.")
                            continue

                        else:
                            if p.cut_tree() == True:
                                running = False
                            else:
                                continue
                            
                    if cig_button.collidepoint(event.pos):
                        if p.cigs > 0:
                            p.craving -= 1
                            p.cigs -= 1
                            p.heart_attack = p.heart_attack + 0.005
                            p.time_pass(15)
                            p.refresh_game_numbers()
                            continue
                        else:
                            continue
                    if monst_button.collidepoint(event.pos):
                        if p.monsters > 0:
                            p.monsters -= 1
                            p.rate += 1.5
                            p.time_pass(1)
                            p.heart_attack += 0.01
                            p.refresh_game_numbers()
                            continue
                        else:
                            p.text_animation("You don't have any Monsters.")
                            continue
                    if takis_button.collidepoint(event.pos):
                        if p.takis > 0:
                            if p.hp < 3:
                                p.hp += 1
                                p.heart_attack += 0.01
                                p.time_pass(1)
                                p.takis -= 1
                                p.refresh_game_numbers()
                                p.text_animation(f"You eat some takis.")
                                continue
                            else:
                                p.text_animation("You aren't hungry.")
                                continue
                        else:
                            p.text_animation("You don't have any takis.")
                            continue
                    if apple_button.collidepoint(event.pos):
                        if p.apples > 0:
                            if p.hp < 3:
                                p.hp += 1
                                p.time_pass(1)
                                if p.heart_attack > 0:
                                    p.heart_attack -= 0.005
                                p.apples -= 1
                                p.refresh_game_numbers()
                                p.text_animation(f"You eat an apple.")
                                p.text_animation2("Refreshing!")
                                continue
                            else:
                                p.text_animation("You aren't hungry.")
                                continue
                        else:
                            p.text_animation("You don't have any apples.")
                            continue
                    if beer_button.collidepoint(event.pos):
                        if p.beers > 0:
                            p.time_pass(5)
                            if p.hp < 3:
                                p.hp += 1
                            p.beers -= 1
                            if p.rate > 1:
                                p.rate -= 1
                            p.bac += 0.03
                            p.refresh_game_numbers()
                            p.text_animation(f"You drink a beer.")
                            p.text_animation2("Refreshing!")
                            continue
                        else:
                            p.text_animation("You don't have any beers.")
                            continue
                    if fire_button.collidepoint(event.pos):
                        req = (2 * p.level) + 3
                        if p.trees > req - 1:
                            p.level_up(req)
                            continue
                        else:
                            p.text_animation(f"You need at least {req} logs to make an offering.\n")
                            continue

        pygame.display.update() 
    p.text_animation(f"You cut down {p.cuts} trees.")
    success = int((p.cuts*100) / p.attempts)
    p.text_animation2(f"You had a success rate of {success}%.")
    clear_text()
    pygame.quit()
    sys.exit()    

def shop(p, car):
    running = True
    if p.location == "shop":
        p.time_pass(0)
    else:
        if car.drive_car() == "empty":
            map(p, car)
        else:
            p.time_pass(15)
            p.location = "shop"
    WINDOW.fill(BLACK)
    tree_img = pygame.image.load("tree2.png")
    log_img = pygame.image.load("log.png")
    cig_img = pygame.image.load("cigpack.png")
    monster_img = pygame.image.load("monster.png")
    takis_img = pygame.image.load("takis.png")
    car_img = pygame.image.load("car.png")
    car_img = pygame.transform.scale(car_img, (200,200))
    gas_img = pygame.image.load("gas.jpg")
    gas_img = pygame.transform.scale(gas_img, (65, 65))
    
    while running:
        p.refresh_shop_numbers(car)
        p.time_pass(0)
        tree_button = pygame.Rect(400, 100, 200, 200)
        WINDOW.blit(car_img, (tree_button.x, tree_button.y))
        log_button = pygame.Rect(200, 10, 65, 65)
        WINDOW.blit(log_img, (log_button.x, log_button.y))
        cig_button = pygame.Rect(200, 85, 65, 65)
        WINDOW.blit(cig_img, (cig_button.x, cig_button.y))
        monst_button = pygame.Rect(200, 160, 65, 65)
        WINDOW.blit(monster_img, (monst_button.x, monst_button.y))
        takis_button = pygame.Rect(200, 235, 65, 65)
        WINDOW.blit(takis_img, (takis_button.x, takis_button.y))
        gas_button = pygame.Rect(200, 310, 65, 65)
        WINDOW.blit(gas_img, (gas_button.x, gas_button.y))
        
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if tree_button.collidepoint(event.pos):
                    WINDOW.fill(BLACK)
                    map(p, car)
                if log_button.collidepoint(event.pos):
                    if p.trees > 0:
                        p.money += 1
                        p.trees -= 1
                        p.refresh_shop_numbers(car)
                        continue
                    else:
                        continue
                if cig_button.collidepoint(event.pos):
                    if p.money >= 8:
                        p.money -= 8
                        p.cigs += 20
                        p.refresh_shop_numbers(car)
                        continue
                    else:
                        continue
                if monst_button.collidepoint(event.pos):
                    if p.money >= 2:
                        p.money -= 2
                        p.monsters += 1
                        p.refresh_shop_numbers(car)
                        continue
                    else:
                        continue
                if takis_button.collidepoint(event.pos):
                    if p.money >= 2:
                        p.money -= 2
                        p.takis += 1
                        p.refresh_shop_numbers(car)
                        continue
                    else:
                        continue

        pygame.display.flip()

def map(p, car):
    running = True
    WINDOW.fill(BLACK)
    map_img = pygame.image.load("MAP.png")

    while running:
        p.time_pass(0)
        WINDOW.blit(map_img,(0,0))
        tree_button = pygame.Rect(279, 194, 96, 93)
        shop_button = pygame.Rect(72, 38, 133,129)
        home_button = pygame.Rect(470, 63, 125, 103)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if tree_button.collidepoint(event.pos):
                    WINDOW.fill(BLACK)
                    main_menu(p, car)
                if shop_button.collidepoint(event.pos):
                    if 5 < p.hour < 21:
                        WINDOW.fill(BLACK)
                        shop(p, car)
                    else:
                        p.text_animation2("The shop is closed.")
                if home_button.collidepoint(event.pos):
                    WINDOW.fill(BLACK)
                    home(p, car)
        
        pygame.display.flip()

def home(p, car):
    running = True
    if p.location == "home":
        p.time_pass(0)
    else:
        if car.drive_car() == "empty":
            map(p, car)
        else:
            p.time_pass(15)
            p.location = "home"
    WINDOW.fill(BLACK)
    bed_img = pygame.image.load("bed.png")
    bed_img = pygame.transform.scale(bed_img, (200, 200))
    car_img = pygame.image.load("car.png")
    car_img = pygame.transform.scale(car_img, (200, 200))

    while running:
        p.time_pass(0)
        WINDOW.blit(bed_img,(250,150))
        car_button = pygame.Rect(500, 300, 200, 200)
        bed_button = pygame.Rect(250, 150, 200,100)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if car_button.collidepoint(event.pos):
                    WINDOW.fill(BLACK)
                    map(p, car)
                if bed_button.collidepoint(event.pos):
                    if p.rate < 2:
                        if p.sleepdep > 0:
                            sleep = int(p.sleepdep)
                            mins_slept = sleep % 60
                            hours_slept = int((sleep - mins_slept)/60)
                            p.time_pass(sleep)
                            p.text_animation(f"You sleep for {hours_slept} hours and {mins_slept} minutes")
                            p.sleepdep = 0
                        else:
                            p.text_animation("You just woke up.")
                    else:
                        p.text_animation(f"You are too caffeinated to fall asleep.")
                        p.text_animation2("Wait until it wears off, or drink alcohol!")
        
        pygame.display.flip()

def main():
    pygame.mixer.music.load("higher.mp3")
    pygame.mixer.music.play()
    pygame.mixer.music.set_volume(0.03)
    current_date = datetime.now()

    p = Player(trees = 0,
                takis = 1,
                monsters = 1,
                cigs = 20,
                money = 0,
                level = 1,
                chance_of_fail = 0.10,
                hp = 3,
                cuts = 0,
                attempts = 0,
                heart_attack = 0,
                craving = 0,
                rate = 1,
                debt = 0,
                apples = 0,
                beers = 6,
                hour = 6,
                minute = 0,
                morning = "AM",
                bac = 0.00,
                wagetime = 0,
                sleepdep = 0,
                year = current_date.year,
                month = current_date.month,
                day = current_date.day,
                rent_due = current_date.day,
                talking = False,
                location = "work"

    )
    car = Car(gas = 30)
    game_state = "menu"  # Initial game state is the main menu

    while True:
        if game_state == "menu":
            game_state = main_menu(p, car)

class Player:
    def __init__(self, trees, monsters, cigs, money, level, chance_of_fail, hp, cuts, attempts, heart_attack, craving, rate, debt, takis, apples, beers, bac, hour, minute, morning, wagetime, sleepdep, year, month, day, rent_due, talking, location):
        self.trees = trees
        self.monsters = monsters
        self.cigs = cigs
        self.money = money
        self.level = level
        self.chance_of_fail = chance_of_fail
        self.hp = hp
        self.cuts = cuts
        self.attempts = attempts
        self.heart_attack = heart_attack
        self.craving = craving
        self.rate = rate
        self.debt = debt
        self.takis = takis
        self.apples = apples
        self.beers = beers
        self.bac = bac
        self.year = year
        self.month = month
        self.day = day
        self.hour = hour
        self.minute = minute
        self.morning = morning
        self.wagetime = wagetime
        self.sleepdep = sleepdep
        self.rent_due = rent_due
        self.talking = talking
        self.location = location
        

    def time_pass(self, minutes):
        self.minute += minutes
        self.wagetime += minutes
        self.sleepdep += (minutes / 2)
        if self.sleepdep > 1440:
            self.heart_attack += (minutes / 6000)
        if self.rate > 1:
            self.rate -= (minutes / 320)
        if self.bac > 0:
            self.bac -= (minutes * 0.00025)
        if self.minute >= 60:
            self.minute -= 60
            self.hour += 1
        if self.hour > 23:
            self.hour -= 24
            self.day += 1
        if self.minute < 10:
            zero = "0"
        else:
            zero = ""
        if self.month == 1 or 3 or 5 or 7 or 8 or 10 or 12:
            if self.day > 31:
                self.day -= 31
                self.month += 1
        elif self.month == 4 or 6 or 9 or 11:
            if self.day > 30:
                self.day -= 30
                self.month += 1
        elif self.month == 2:
            if self.day > 28:
                self.day -= 28
                self.month += 1
        elif self.month > 12:
            self.month -= 12
            self.year += 1
        draw_button(350, 5, 150, 40, BLACK)    
        draw_button(350, 30, 150, 40, BLACK)  
        draw_text(f"{self.hour}:{zero}{self.minute} {self.morning}", WHITE, 350, 5)
        draw_text(f"{self.month}/{self.day}/{self.year}", WHITE, 350, 30)

    def text_animation(self, text):
        self.talking = True
        clear_text()
        pygame.display.flip()
        animate_text(text, WHITE, 5, 350)
        draw_text(text, WHITE, 5, 350)
        pygame.time.delay(500)
        self.talking = False

    def text_animation2(self, text):
        self.talking = True
        pygame.display.flip()
        animate_text(text, WHITE, 5, 400)
        draw_text(text, WHITE, 5, 400)
        self.talking = False

    def refresh_game_numbers(self):
        draw_button(15, 45, 65, 65, BLACK)
        draw_button(615, -5, 1000, 65, BLACK)
        draw_button(630, 70, 1000, 40, BLACK)
        draw_button(630, 125, 1000, 40, BLACK)
        draw_button(630, 170, 1000, 40, BLACK)
        draw_button(0, 0, 150, 40, BLACK)
        draw_button(60, 120, 150, 40, BLACK)
        draw_button(615, 225, 1000, 65, BLACK)
        draw_button(630, 270, 1000, 65, BLACK)
        draw_button(60, 160, 150, 40, BLACK)
        draw_button(60, 200, 150, 40, BLACK)
        draw_text(str(self.trees), WHITE, 630, 20)
        draw_text(str(self.cigs), WHITE, 630, 70)
        draw_text(str(self.monsters), WHITE, 630, 125)
        draw_text(str(self.takis), WHITE, 630, 170)
        draw_text(str(self.apples), WHITE, 630, 225)
        draw_text(str(self.beers), WHITE, 630, 270)
        draw_text(f"Level {self.level}", WHITE, 15, 15)
        draw_text(f"${self.money}", WHITE, 15, 45)
        draw_text(f"{((1 - self.heart_attack) * 100):.2f} %", RED, 60, 120)
        draw_text(f"x {int(self.rate)}", RED, 60, 160)
        draw_text(f"{self.bac}", RED, 60, 200)

    def refresh_shop_numbers(self, car):
        draw_button(15, 45, 65, 65, BLACK)
        draw_button(280, 10, 1000, 65, BLACK)
        draw_button(280, 85, 1000, 65, BLACK)
        draw_button(280, 160, 1000, 65, BLACK)
        draw_button(280, 235, 1000, 65, BLACK)
        draw_button(280, 310, 1000, 65, BLACK)
        draw_text(f"x {str(self.trees)}", WHITE, 280, 35)
        draw_text("+ $1", GREEN, 130, 35)
        draw_text(f"x {str(self.cigs)}", WHITE, 280, 105)
        draw_text("- $8", RED, 130, 105)
        draw_text(f"x {str(self.monsters)}", WHITE, 280, 175)
        draw_text("- $2", RED, 130, 175)
        draw_text(f"x {str(self.takis)}", WHITE, 280, 250)
        draw_text("- $2", RED, 130, 250)
        draw_text(f"${self.money}", WHITE, 15, 45)
        cost_of_gas = ((30 - car.gas)*4)/30
        draw_text(f"${cost_of_gas:.2f}", WHITE, 280, 330)



    def level_up(self, req):
        if self.trees > req - 1:
            self.time_pass(10)
            self.level += 1
            if self.heart_attack > 0:
                self.heart_attack = 0
            self.chance_of_fail -= 0.01
            self.trees -= req
            self.hp = 3
            self.bac = 0.00
            self.refresh_game_numbers()

    def cut_tree(self):
        self.debt += 2
        self.attempts += 1
        self.time_pass(15)
        rand = random.random()
        if rand < 0.50:
            self.craving += 1
        if rand < self.heart_attack:
            self.text_animation("You fucking die of a heart attack.")
            death = True
            return death
        elif rand > 0.95:
            self.trees += int(5 * self.rate)
            self.cuts += 1
            self.text_animation("You cut down the tree and collect more logs than usual.")
            self.refresh_game_numbers()
        elif rand < self.chance_of_fail:
            self.text_animation("You fail to cut down the tree.")
            self.text_animation2("Your stomach growls.")
            self.hp -= 1
        elif rand < 0.85:
            self.trees += int(self.rate)
            self.cuts += 1
            self.refresh_game_numbers()
            pygame.mixer.music.load("collect_log.mp3")
            pygame.mixer.music.play()
        else:
            self.trees += int(self.rate)
            self.cuts += self.rate
            self.apples += 1
            self.text_animation("You find an apple!")
            self.refresh_game_numbers()
            pygame.mixer.music.load("collect_log.mp3")
            pygame.mixer.music.play()

class Car:
    def __init__(self, gas):
        self.gas = gas

    def text_animation(self, text):
        self.talking = True
        clear_text()
        pygame.display.flip()
        animate_text(text, WHITE, 5, 350)
        draw_text(text, WHITE, 5, 350)
        pygame.time.delay(500)
        self.talking = False

    def drive_car(self):
        if self.gas > 0:
            self.gas -= 1
        else:
            self.text_animation("Your car is out of gas.")
            return "empty"
            



if __name__ == "__main__":
    main()