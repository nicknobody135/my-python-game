class blit_image():
    def blit_home_screen(game_screen , zero_screen , screen):
        if game_screen == 0:
            screen.blit(zero_screen[0] , (280 , 500))
            screen.blit(zero_screen[1] , (530 , 500))
            screen.blit(zero_screen[2] , (780 , 500))
    def blit_game_screen(game_screen , game_images , screen , helicopter_location , helicopter_facing , net_phase , net_location , thrash_loc , thrash_phase ,c_list):
        if game_screen == 1:
            screen.blit(game_images[2] , (0 , 360))
            if helicopter_facing == "left":
                screen.blit(game_images[0] , helicopter_location)
            elif helicopter_facing == "right":
                screen.blit(game_images[1] , helicopter_location)
            if thrash_phase == 2:
                screen.blit(game_images[3] , (thrash_loc))
            if net_phase == 2:
                screen.blit(game_images[4] , net_location)
            for i in range(0 , len(c_list)):
                if c_list[i][0] == 1:
                    screen.blit(game_images[5] , (c_list[i][1]))