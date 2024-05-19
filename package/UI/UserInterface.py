import pygame
import pygame_gui
from pygame.locals import *
from pygame_gui.windows import UIColourPickerDialog
from sys import exit

from package.UI.Menu import Menu

pygame.init()

class UserInterface():

    # used colors
    BACKGROUND_WHITE = (248, 248, 248)
    MENU_WHITE = (217,217,217)
    MAIN_BLUE = (0,117,255)

    # icons dimensions (xStart,yStart), (xEnd, yEnd)
    USER_ICON = [[302,15],[343,58]]
    LIST_ICON = [[389,17],[420,52]]
    ADD_ICON = [[464,11],[515,60]]
    REMOVE_ICON = [[558,11],[606,60]]
    HIDE_MENU_ICON = [[409,71],[504,90]]
    SHOW_MENU_ICON = [[414,0],[508,24]]

    def __init__(self, width, height):
        self.width = width
        self.height = height

        self.tela = pygame.display.set_mode((width, height))
        self.draw_shape = True
        self.current_shape = 'triangule'
        self.manager = pygame_gui.UIManager((900, 600))
        self.menu = Menu(self.tela,self.manager)



    def run(self):
        pygame.display.set_caption('Cartesian Plane')
        icon = pygame.image.load("./images/icon.png")
        pygame.display.set_icon(icon)


        while True:
            self.handleEvents()
            self.render()

            pygame.display.update()
    
    def handleEvents(self, e = None):
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                self.handleClickEvents()

    def handleClickEvents(self):
        mouse_pos = pygame.mouse.get_pos()
        print(mouse_pos)

        # to detect clicks on home menu icons
        if (self.menu.getStatus() and self.menu.getCurrentTab() == "home"):
            if (self.USER_ICON[0][0] < mouse_pos[0] < self.USER_ICON[1][0] and self.USER_ICON[0][1] < mouse_pos[1] < self.USER_ICON[1][1]):
                print('clicou')
            if (self.LIST_ICON[0][0] < mouse_pos[0] < self.LIST_ICON[1][0] and self.LIST_ICON[0][1] < mouse_pos[1] < self.LIST_ICON[1][1]):
                print('clicou LSITA')
            if (self.ADD_ICON[0][0] < mouse_pos[0] < self.ADD_ICON[1][0] and self.ADD_ICON[0][1] < mouse_pos[1] < self.ADD_ICON[1][1]):
                self.menu.setCurrentTab('add_shape')
            if (self.REMOVE_ICON[0][0] < mouse_pos[0] < self.REMOVE_ICON[1][0] and self.REMOVE_ICON[0][1] < mouse_pos[1] < self.REMOVE_ICON[1][1]):
                print('clicou REMOVE')
            if (self.HIDE_MENU_ICON[0][0] < mouse_pos[0] < self.HIDE_MENU_ICON[1][0] and self.HIDE_MENU_ICON[0][1] < mouse_pos[1] < self.HIDE_MENU_ICON[1][1]):
                self.menu.setStatus(False)
                    
        # to detect if user wants to close menu
        elif ((not self.menu.getStatus()) and self.SHOW_MENU_ICON[0][0] < mouse_pos[0] < self.SHOW_MENU_ICON[1][0] and self.SHOW_MENU_ICON[0][1] < mouse_pos[1] < self.SHOW_MENU_ICON[1][1]):
            self.menu.setStatus(True)
    
    def render(self):
        self.renderBackground()
        self.menu.renderMenu()

    def renderBackground(self):
        # backgorund 
        self.tela.fill(self.BACKGROUND_WHITE)

        #grid
        blockSize = 20
        for x in range(0, self.width, blockSize):
            for y in range(0, self.height, blockSize):
                rect = pygame.Rect(x, y, blockSize, blockSize)
                pygame.draw.rect(self.tela, (200,200,200), rect, 1)
        
        # x-axis
        pygame.draw.line(self.tela, (35,35,35), (0,self.height-20), (self.width-20,self.height-20), 5)            
        pygame.draw.polygon(self.tela, (35,35,35), 
            [(self.width, self.height-20), (self.width-20, self.height-30),
            (self.width-20, self.height-10)])
            
        # y-axis
        pygame.draw.line(self.tela, (35,35,35), (20,20), (20,self.height), 5) 
        pygame.draw.polygon(self.tela, (35,35,35), 
            [(20, 0), (10, 20),
            (30, 20)])

    def renderFigure(self):
        if self.draw_shape:
            switcher = {
                'triangule': lambda: self.drawRect((136,120,235), 100, 100, 100, 100),
                'square': lambda: self.drawRect((136,120,235), 200, 280, 100, 100),
                'circle': lambda: print('circle')
            }

            switcher.get('square', lambda: print('ola'))()

    def drawTriangule(self, color, point1, point2, point3):
        pygame.draw.polygon(self.tela, color, [point1, point2, point3])
    
    def getMousePosition(self):
        return pygame.mouse.get_pos()
    


