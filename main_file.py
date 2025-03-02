import pygame
import sys
import bliter
import load_images
import button_detection
import helicopter_mangement
import thrash_mover
import net_dropper
import co2_management
pygame.init()
dem = (1280, 720)
screen = pygame.display.set_mode((dem))
bg_color = (3, 154, 255)
running = True
fps = pygame.time.Clock()
what_screen = 0
screen_zero_images = []
game_images = []
screen_zero_images , game_images = load_images.load_images(screen_zero_images , game_images)
mouse_down = False
what_button_is_down = [False , False , False]
key_down = [False , False]
space_down = False
helicopter_location = [500 , 0]
helicopter_facing = "right"
net_phase = 0
net_location = [0 , 0]
thrash_loc = [0 , 0]
thrash_phase = 0
score = 0
tick = 0
clock = 0
wait_time = 0
temp = 0
temp_2 = False
co2_list = []
go = False
do_again = True
left_or_right = "left"
while running:
    if what_screen == 1:
        tick = tick + 1
        if tick == 60:
            tick = 0
            clock = clock + 1
            temp_2 = True
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                key_down[0] = True
            if event.key == pygame.K_d:
                key_down[1] = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                key_down[0] = False
            if event.key == pygame.K_d:
                key_down[1] = False
        if what_screen == 1:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if net_phase == 0:
                        net_phase = 1
                        net_location , net_phase = net_dropper.move(net_location , net_phase , helicopter_location , what_button_is_down)
    if event.type == pygame.MOUSEBUTTONDOWN:
        if pygame.mouse.get_pressed()[0]:
            mouse_down = True
    if mouse_down == True and what_screen == 0:
        what_button_is_down = [False , False , False]
        what_button_is_down = button_detection.check_if_the_buttons_colide(pygame.mouse.get_pos() , what_button_is_down)
        if what_button_is_down[0] == True or what_button_is_down[1] == True or what_button_is_down[2] == True:
            what_screen = 1
    if what_screen == 1:
        helicopter_location , helicopter_facing = helicopter_mangement.start_up_the_heli(helicopter_location , helicopter_facing , key_down)
        if net_phase == 2:
            net_location , net_phase = net_dropper.move(net_location , net_phase , helicopter_location , what_button_is_down)
        if what_button_is_down[1] == True or what_button_is_down[2] == True:
            go = False
        thrash_loc , thrash_phase , score , temp_2 , wait_time , temp , go  , left_or_right = thrash_mover.move_thrash(thrash_loc , thrash_phase , score , net_location , wait_time , temp , temp_2 , go , what_button_is_down , left_or_right)
        font = pygame.font.SysFont("Stencil", 50)
        score = str(score)
        txtsurf = font.render(score, True, "white")
        if do_again == True:    
            co2list , do_again = co2_management.make(co2_list , what_button_is_down , do_again)
        if what_button_is_down[1] == True or what_button_is_down[2] == True:
            go = False
        co2_list , do_again  , go , score = co2_management.move(co2_list , do_again , go , score , mouse_down , pygame.mouse.get_pos() , what_button_is_down)
    mouse_down = False
    screen.fill(bg_color)
    fps.tick(60)
    print(fps)
    if what_screen == 0:
        bliter.blit_image.blit_home_screen(what_screen, screen_zero_images , screen)
    if what_screen == 1:
        bliter.blit_image.blit_game_screen(what_screen, game_images , screen , helicopter_location , helicopter_facing , net_phase , net_location , thrash_loc , thrash_phase , co2_list)
        screen.blit(txtsurf , (0 , 0))
        score = int(score)
    pygame.display.update()
    space_down = False