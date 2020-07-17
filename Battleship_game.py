#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random as rand

ships = {'S':1,'D':2,'C':3,'B':4,'A':5}

names_ships = {'S':'Submarine','D':'Destroyer','C':'Cruiser','B':'Battleship','A':'Carrier'}


# In[2]:


def determine_size():
    while True:
        try:
            value = int(input("""How big should I make the playboard? \n provide me with a number between 10-12 to define the witdh and length of the board.
            \n\n\n Type 99 to exit the game \n\n"""))
        except ValueError:
            print("Sorry, I didn't understand that.")
            continue

        if value == 99:
            print('You are a coward captain you are leaving our men behind')
            break 
        elif value < 9:
            print("Sorry, your response must fall between 10 and 12")
            continue
        elif value > 12:
            print("Sorry, your response must fall between 10 and 12")
        else:
            break
    return value


# In[3]:


def make_field(x):
    x = int(x)
    board = []
    playerboard = []
    for i in range(x):
        board.append(["0"] * (x))
        playerboard.append(["0"] * (x))
    return board,playerboard


# In[4]:


def place_computer_ships(field,ship):
    for key,size in ship.items():
        length = len(field) - size - 1 
        location_y = rand.randint(0,length)
#         print(location_y)
        
#         location_y = location_check(location_y,field,size)
        location_x = rand.randint(0,len(field)-1)

        for i in range(0,size):
            field[location_x-i][location_y] = key
    return field    
            


# In[5]:

# In[6]:


def place_ships(field,ships):
    print("Captain the enemy is upon us :(. To the battlestations!")
    for key,size in ships.items(): 
        y = int(input('Provide the x coordinate for your {0}  :'.format(names_ships.get(key))))
        x = int(input('Provide the y coordinate for your {0}  :'.format(names_ships.get(key))))
#         field[int(x)][int(y)] = key

        


        for i in range(0,size):
            field[x-i][y] = key
    
    return field


# In[7]:


def location_check(location,field,size):
    fieldsize = (len(field) -1) 
    if location + size > (fieldsize):
        x = (fieldsize - (size + location))
#         y = y - x
        return location + x 
    else:
        return location


# ###### field = enemy
# y_loc = 10
# size = 5

# In[8]:


def shooting(player,field):
    if player != 'Human':
        x_shot = rand.randint(0,len(field)-1)
        y_shot = rand.randint(0,len(field)-1)
        return int(y_shot),int(x_shot) 
    
    else:
        while True:
            try:
                x_shot = int(input('Sir provide the fire X coordinates between 0 and 9 : '))
                y_shot = int(input('Sir provide the fire Y coordinates between 0 and 9 : '))
                cond = (y_shot == 99) or (x_shot == 99)
            except ValueError:
                print("Sorry captain I don't understand your orders")
                continue
            
            if(y_shot == 99 or x_shot == 99):
                print('You are a coward captain you are leaving our men behind')
                break 
            if y_shot < 0 or x_shot <0 :
                print("Your coordinate is not on the map")
                continue
            elif  (x_shot > 9) or  (y_shot > 9):
                print("Your coordinate is not on the map")
            else:
                return int(y_shot),int(x_shot) 
    


# In[9]:


def player_move(hitpoints,player):
    coordinates = shooting('Human',player)
    space = player[coordinates[0]][coordinates[1]] 
    if space == '0':
        print('We missed Captain, the enemy has {} hitpoints left'.format(hitpoints))
        space = 'X'
        return hitpoints
    elif space == 'X':
        print('We already hit this space sir')
        return hitpoints
    else: 
        hitpoints -= 1
        print('')
        print('We have hit their {0}, they have: {1} hitpoint left'.format(names_ships.get(space),hitpoints))
        return hitpoints


# In[10]:


def enemy_move(hitpoints,enemy):
    coordinates = shooting('CPU',enemy)
    space = enemy[coordinates[0]][coordinates[1]] 
    if space == '0':
        print('The missed us captain , our fleet has {} hitpoints left'.format(hitpoints))
        space = 'X'
        return hitpoints
    elif space == 'X':
        print('They have hit the same spot again ')
        return hitpoints
    else: 
        hitpoints -= 1
        print('')
        print('\nThey have hit our {0}, our fleet has: {1} hitpoint left\n'.format(names_ships.get(space),hitpoints))
        return hitpoints


# In[15]:


def play_game():
    
    enemy,player = make_field(determine_size())
    
    enemy = place_computer_ships(enemy,ships)
    
    player = place_ships(player,ships)
    
    hitpoints_enemy = len([j for i in enemy for j in i if j != '0' and j != 'X'])
    hitpoints_player = len([j for i in player for j in i if j != '0' and j != 'X'])

    while hitpoints_enemy or hitpoints_player:
        hitpoints_player =  enemy_move(hitpoints_player,player)
        hitpoints_enemy =  player_move(hitpoints_enemy,enemy)
        if hitpoints_enemy < 1:
            print('We won the battle captain the sea is ours')
            break
        elif hitpoints_player < 1:
            print('They finished our last ship Captain we are doomed')
            break
        if (hitpoints_enemy != 0 or hitpoints_player != 0):
            continue

#     print('We have won the battle captain')


# # play_game()

# play_game()

# In[16]:


play_game()


# In[ ]:




