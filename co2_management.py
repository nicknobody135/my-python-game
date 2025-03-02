import random
def make(clist , button , a):
    if button[0] == True:
        clist.append([0 , [0 , 100]])
        a = False
    if button[1] == True or button[2] == True:
        cd = random.randint(1 , 2)
        if cd == 1:
            clist.append([0 , [0 , 100]])
        if cd == 2:
            clist.append([0 , [0 , 200]])
        a = False
    return clist , a
def move(clist , a , go , score , mouse_down , m_loc , what_button_is_down): 
    for i in range(0 , len(clist)):
        if clist[i][0] == 0 and go == True or clist[i][0] == 0 and what_button_is_down[1] == True or what_button_is_down[2] == True:
            clist[i][0] = 1
        if go == True and clist[i][0] == 1 or what_button_is_down[1] == True and clist[i][0] == 1 or what_button_is_down[2] == True and clist[i][0] == 1:
            clist[i][1][0] = clist[i][1][0] + 5
            if what_button_is_down[1] == True:
                clist[i][1][0] = clist[i][1][0] + 2
            if what_button_is_down[2] == True:
                clist[i][1][0] = clist[i][1][0] + 3
        if clist[i][1][0] > 1279:
            clist.pop(i)
            a = True
            go = False
            if what_button_is_down[2] == True:
                score = int(score)
                score = score - 5
            return clist , a , go , score
        if mouse_down == True and m_loc[0] >= clist[i][1][0] and m_loc[0] < clist[i][1][0] + 62 and m_loc[1] > clist[i][1][1] and m_loc[1] < clist[i][1][1] + 37:
            clist.pop(i)
            a = True
            go = False
            score = int(score)
            score = score + 1
            return clist , a , go , score
    return clist , a , go , score