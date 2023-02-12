import pygame
import random
import time
import tkinter as tk
from tkinter import *

def startagain():
    class Worm:
        def __init__(self, x, y, width, height, color):
            self.x = x
            self.y = y
            self.s=15
            self.width = width
            self.height = height
            self.color = color
            self.speed = 1
            self.time=0.04
            self.growth = 3
            self.score = 0
            self.tail = []
            self.tail_length = 10
            self.game_over = False
            #root1 = tk.Tk()
            #root1.geometry("250x80")
            #root1.title('Select Level')
            #label1 = tk.Label(root1, text="Choose Level:", font=("Arial", 14),fg="red")
            #label1.pack()
            #root1.eval('tk::PlaceWindow . center')
            #button3 = Button(root1, text="Easy" , command=root1.destroy)
            #button4 = Button(root1, text="Meduim" , command=root1.destroy)
            #button5 = Button(root1, text="Hard" , command=root1.destroy)
            #button3.pack(side=BOTTOM , anchor="center")
            #button4.pack(side=LEFT ,anchor="center")
            #button5.pack (side=RIGHT,anchor="center")
            #root1.mainloop()


        
        def move(self,x_dir, y_dir):
            
            # font
            font = pygame.font.Font(None, 30)
            
            # add current position to tail list
            self.tail.append((self.x, self.y))
            
            # remove oldest position from tail list if it exceeds the tail_length
            if len(self.tail) > self.tail_length:
                self.tail.pop(0)
                
            self.x += x_dir * self.speed
            self.y += y_dir * self.speed
        
            # check if worm is going out of screen
            if self.x < 0:
                self.x = 0
            if self.x > 700 - self.width:
                self.x = 700 - self.width
            if self.y < 0:
                self.y = 0
            if self.y > 500 - self.height:
                self.y = 500 - self.height
            for pos in self.tail:
                if pos[0] == self.x and pos[1] == self.y:
                   game_over = True
                   root = tk.Tk()
                   root.geometry("200x80")
                   root.title('Start Again')
                   label = tk.Label(root, text="GameOver!!!", font=("Arial", 14),fg="red")
                   label.pack()
                   root.eval('tk::PlaceWindow . center')
                   frame1 = Frame(root)
                   frame1.pack(expand=True, fill=BOTH)
                   button1 = Button(frame1, text='Start',command=lambda: [root.destroy(),startagain()])
                   button1.pack(side=BOTTOM)
                   frame2 = Frame(root)
                   frame2.pack(expand=True, fill=BOTH)
                   def closeall():
                       root.destroy()
                       pygame.quit()
                   button2 = Button(frame2, text='Close',command=closeall)
                   button2.pack(side=BOTTOM)
                   root.mainloop()
                   

        def grow(self):
            self.tail_length += self.growth

        def draw(self, screen):
            # draw rectangles for tail
            for i, pos in enumerate(self.tail):
                pygame.draw.rect(screen, self.color, (pos[0], pos[1], self.width, self.height))
            # draw rectangle for worm head
            pygame.draw.rect(screen,self.color, (self.x, self.y, self.width, self.height))

    class Fruit:
        def __init__(self, x, y, radius, color):
            self.x = x
            self.y = y
            self.radius = radius
            self.color = color


        def draw(self, screen):
            pygame.draw.circle(screen, self.color, (int(self.x), int(self.y)), self.radius)

        def respawn(self, worm):
            white = (255, 255, 255)
            while True:
                self.x = random.randint(10, 670)
                self.y = random.randint(10, 470)
                if self.color == white:
                   self.color=random_hex_color()
                self.color=random_hex_color()
                if worm.score == worm.s:
                    worm.time -=0.007
                    worm.s +=15
                if (self.x <= worm.x + worm.width and 
                    self.x + self.radius > worm.x and 
                    self.y < worm.y + worm.height and 
                    self.y + self.radius > worm.y):
                    continue
                else:
                    break

    def random_hex_color():
            hex_chars = '0123456789ABCDEF'
            return '#' + ''.join(hex_chars[random.randint(0, 15)] for _ in range(6))

    def check_collision(worm, fruit):
        if (worm.x < fruit.x + fruit.radius and 
            worm.x + worm.width > fruit.x and 
            worm.y < fruit.y + fruit.radius and 
            worm.y + worm.height > fruit.y):
            return True
        else:
            return False


    def draw_text(text, font, color, surface, x, y):
        textobj = font.render(text, 1, color)
        textrect = textobj.get_rect()
        textrect.topleft = (x, y)
        surface.blit(textobj, textrect)


    # initialize pygame and create a window
    pygame.init()

    size = (700, 500)
    screen = pygame.display.set_mode(size)

    pygame.display.set_caption("Worm Game")

    # colors
    black = (0, 0, 0)
    white = (255, 255, 255)

    # worm
    worm = Worm(350, 250, 20, 20, ("#32CD32"))

    # apple
    apple = Fruit(random.randint(0, 680), random.randint(0, 480), 10, (random_hex_color()))
    # game loop
    game_over = False

    # font
    font = pygame.font.Font(None, 30)

    x_dir, y_dir = 0, 0
    g=5;
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_dir = -5
                    worm.move(-5, 0)
                    worm.move(x_dir, y_dir)
                    g=0
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RIGHT:
                    x_dir = 5
                    worm.move(5, 0)
                    worm.move(x_dir, y_dir)
                    g=1
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    y_dir = -5
                    worm.move(0, -5)
                    worm.move(x_dir, y_dir)
                    g=2
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_DOWN:
                    y_dir = 5
                    worm.move(0, 5)
                    worm.move(x_dir, y_dir)
                    g=3
        x_dir, y_dir = 0, 0
        if g == 0:
           worm.move(-5, 0)
           time.sleep(worm.time)
        if g == 1:
           worm.move(5, 0)
           time.sleep(worm.time)
        if g == 2:
           worm.move(0, -5)
           time.sleep(worm.time)
        if g == 3:
           worm.move(0, 5)
           time.sleep(worm.time)
        


        # check for collision with apple
        if check_collision(worm, apple):
            worm.grow()
            worm.score += 1
            apple.respawn(worm)

        # check if the apple is spawning on top of the worm
        while check_collision(worm, apple) or (apple.x, apple.y) in worm.tail:
            apple.respawn(worm)
       
        # clear the screen
        screen.fill(white)

        # draw the worm and apple
        worm.draw(screen)
        apple.draw(screen)

        # draw score
        draw_text("Score: " + str(worm.score), font, black, screen, 10, 10)

        # update the display
        pygame.display.flip()


    pygame.quit()
startagain()

