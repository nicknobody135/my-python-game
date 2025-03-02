import pygame
pygame.init()
def check_if_the_buttons_colide(mouse_location , what_button_is_down):
    if mouse_location[0] >= 200 and mouse_location[0] <= 400 and mouse_location[1] >= 500 and mouse_location[1] <= 575:
        what_button_is_down[0] = True
    if mouse_location[0] >= 530 and mouse_location[0] <= 730 and mouse_location[1] >= 500 and mouse_location[1] <= 575:
        what_button_is_down[1] = True
    if mouse_location[0] >= 780 and mouse_location[0] <= 980 and mouse_location[1] >= 500 and mouse_location[1] <= 575:
        what_button_is_down[2] = True
    return what_button_is_down