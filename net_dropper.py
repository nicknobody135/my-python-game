def move(loc , phase , heli_loc , what_button_is_down):
    if loc[1] >=  610:
        phase = 3
    if phase == 3:
        phase = 0
        loc = [0 , 0]
        return loc , phase
    if phase == 1:
        loc[0] = heli_loc[0]
        loc[1] = 76
        phase = 2
    if phase == 2:
        loc[1] = loc[1] + 10
    if phase == 2 and what_button_is_down[2] == True or what_button_is_down[1] == True:
        loc[1] = loc[1] + 5
    return loc , phase