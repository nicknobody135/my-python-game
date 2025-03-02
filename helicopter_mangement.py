def start_up_the_heli(helicopter_location , helicopter_facing , key_down):
    if key_down[0] == True and helicopter_location[0] >= 0:
        helicopter_facing = "left"
        helicopter_location[0] = helicopter_location[0] - 5
    if key_down[1] == True and helicopter_location[0] <= 1080:
        helicopter_location[0] = helicopter_location[0] + 5
        helicopter_facing = "right"
    return helicopter_location , helicopter_facing