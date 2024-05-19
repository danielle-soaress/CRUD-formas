import pygame
import pygame_gui
import pygame_menu

from pygame.locals import *


class Menu():

    SHAPES_OPTIONS = ['Circle', 'Rectangle', 'Triangule', 'Line', 'Point']

    def __init__(self, tela, manager):
        self.__manager = manager
        self.__tela = tela
        self.__status = True
        self.__current_tab = 'home'
        self.__images_path = {
            'home': "images/menu.png",
            'add_shape': "images/menu_new_shape.png"
        }


    def setStatus(self, status: bool):
        self.__status = status

    def getStatus(self):
        return self.__status
    
    def setCurrentTab(self, tab):
        self.__current_tab = tab
    
    def getCurrentTab(self):
        return self.__current_tab

    def setMenu(self):
        image = pygame.image.load(self.__images_path[self.__current_tab])
        self.__tela.blit(image, (255,0))
        
        if (self.__current_tab == "add_shape"):
            self.addShapeMenu()

    def renderMenu(self):
        # menu
        if self.__status:
            self.setMenu()
        else:
            menu_tab = pygame.image.load("images/menu_tab.png")
            self.__tela.blit(menu_tab, (410,0))
    
    # menu tabs UI


    def addShapeMenu(self):
        font = pygame.font.Font("./font/itim.ttf", 20)

        content_coords = [(340,70), (240, 120)] # (Xs, Ys), (w,h)

        # input name


        # input shape

        # input color


