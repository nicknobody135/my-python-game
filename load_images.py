import pygame
pygame.init()
def load_images(zero_images , game_images):
    easy_button = pygame.image.load("images\easy.png").convert_alpha()
    easy_button = pygame.transform.scale(easy_button , (200 , 75))
    medium_button = pygame.image.load("images\medium.png").convert_alpha()
    medium_button = pygame.transform.scale(medium_button , (200 , 75))
    hard_button = pygame.image.load("images\hard.png").convert_alpha()
    hard_button = pygame.transform.scale(hard_button , (200 , 75))
    helicopter_left = pygame.image.load("images\helicopter_left.png").convert_alpha()
    helicopter_left = pygame.transform.scale(helicopter_left , (200 , 75))
    helicopter_right = pygame.image.load("images\helicopter_right.png").convert_alpha()
    helicopter_right = pygame.transform.scale(helicopter_right , (200 , 75))
    ocean = pygame.image.load("images\ocean.png").convert_alpha()
    ocean = pygame.transform.scale(ocean , (1280 , 360))
    thrash = pygame.image.load("images\\real_garbage.png").convert_alpha()
    thrash = pygame.transform.scale(thrash , (100 , 100))
    net = pygame.image.load("images\\net.png").convert_alpha()
    net = pygame.transform.scale(net , (200 , 150))
    co2 = pygame.image.load("images\\c02.png").convert_alpha()
    co2 = pygame.transform.scale(co2 , (62 , 37))
    zero_images = [easy_button , medium_button , hard_button]
    game_images = [helicopter_left , helicopter_right , ocean , thrash , net , co2]
    return zero_images , game_images