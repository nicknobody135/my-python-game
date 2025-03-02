import random
def move_thrash(thrash_loc , thrash_phase , score , net_loc , wt , t , t2 , go , b , left_or_right):
    if thrash_phase == 0:
        wt = random.randint(3 , 7)
        if b[0] == False:
            thrash_phase = 1
        if b[0] == True and go == False:
            thrash_phase = 1
        t = 0
        cd = random.randint(1 ,2)
        if cd == 1:
            left_or_right = "left"
            thrash_loc = [0 , 550]
        if cd == 2:
            left_or_right = "right"
            thrash_loc = [1280 , 550]
        return thrash_loc , thrash_phase , score , t2 , wt , t ,go , left_or_right
    if thrash_phase == 1:
        if t2 == True:
            t = t + 1
            t2 = False
            return thrash_loc , thrash_phase , score , t2 , wt , t , go , left_or_right
        if t == wt and go == False:
            thrash_phase = 2
        return thrash_loc , thrash_phase , score , t2 , wt , t , go , left_or_right
    if thrash_phase == 2:
        if left_or_right == "left":
            if b[1] == True:
                thrash_loc[0] = thrash_loc[0] + 2
            if b[2] == True:
                thrash_loc[0] = thrash_loc[0] + 3
            thrash_loc[0] = thrash_loc[0] + 5
            if thrash_loc[0] > 1297 and b[2] == True:
                thrash_phase = 0
                score = score - 5
        if left_or_right == "right":
            if b[1] == True:
                thrash_loc[0] = thrash_loc[0] - 2
            if b[2] == True:
                thrash_loc[0] = thrash_loc[0] - 3
            thrash_loc[0] = thrash_loc[0] - 5
            if thrash_loc[0] < 0:
                thrash_phase = 0
                score = score - 5
        if b[2] == True:
            go = True
        if b[1] == True or b[2] == True:
            go = False
        if net_loc[0] + 10 < thrash_loc[0] and thrash_loc[0] < net_loc[0] + 210 and net_loc[1] + 10 < thrash_loc[1] and thrash_loc[1] + 110 < net_loc[1] + 200:
            thrash_phase = 0
            score = score + 1
            go = True
            if b[1] == True or b[2] == True:
                go = False
        return thrash_loc , thrash_phase , score , t2 , wt , t , go , left_or_right