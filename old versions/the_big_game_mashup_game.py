# the big L5 mashup game

import time
import webbrowser
from random import randint


def intoduction():
    print('silence...'); time.sleep(1)
    for i in range(10): print(''); time.sleep(0.5)
    print('but then...'); time.sleep(1)
    for i in range(10): print(''); time.sleep(0.5)
    print('penguins!'); time.sleep(1)
    print('''
  #######
###########
############
####  & ####_
########### __\\
 ##########_ /
  ########
 ##########
 ######### (
;#####)###  |
#####/###    \\
####/###      |
###/####       \\
##/#####         |
#/######          |
/ #######         |   
  ########        |
  #########      |
  ##########    /
 /###########  /
/##/ ######  '
##    | ||= C
#     | ___ C
    ''')
    print('')

def void_sitting():
    void_timer = 0
    while True:
        print(''); time.sleep(1)
        void_timer += 1
        if void_timer == 60:
            print('you have been here for a minute'); time.sleep(0.7)
            print(':('); time.sleep(0.7)
            print('have some company :)'); time.sleep(0.7)
            print(''' 
 ('>
 /V\\
<(_)
  ~~'''); break

def blinking_penguin():
    for i in range(20):
        print('''
    

    '''); time.sleep(0.7)
        print('''
(o_
//\\
V_/_'''); time.sleep(0.7)
        print('''
    
    
    '''); time.sleep(0.7)
        print('''
(-_
//\\
V_/_'   
    '''); time.sleep(0.7)
    print('oh sorry, i meant a blinking penguin')


def exit_program():
    print('to leave me?'); time.sleep(1); print('')
    print('why?'); time.sleep(1); print('')
    print('what did i do'); time.sleep(1); print('')
    print('no, please don\'t go...'); time.sleep(1); print('')
    print('don\'t leave me ;-;' ); time.sleep(1); print('')
    print('wait!'); time.sleep(1); print('')
    print('I have something extremely important to tell you'); time.sleep(1); print('')
    print('Don\'t go into th£ ~@:>{(£^*'); time.sleep(1); print('')
    print('~@:>}{&*$" @:<?@&-')
    
def user_interface():
     while True:
        print(''); time.sleep(0.5)
        print('''
-------------------------------------------------
--- welcome to the big L5 game mashup game!   ---
---                                           ---
--- games list:                               ---
---                                           ---
--- diep.io: pew                              ---
--- skribbl.io: sksksk                        ---
--- storiumedu: steu                          ---
--- agar.io: blob                             ---
--- google halloween: boo!                    ---
--- pengiun dance: pengu                      ---
--- just sitting in the void: .               ---
--- exit program: bye                         ---
---                                           ---
--- new games/ improvements welcome, just     ---
--- @ harry in games for L5                   ---
-------------------------------------------------          
 ''')
        game_select = input('enter game choice: '); print(''); time.sleep(0.5)
        time.sleep(0.5); print('you have chosen...'); print(''); time.sleep(0.5)

        maybe = randint(1, 3)
        if maybe == 1:
            print(' surprise!'); time.sleep(0.7)
            webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")            
        else:
            if game_select == 'pew':
                print('diep.io!'); webbrowser.open("https://diep.io/")                
            elif game_select == 'sksksk':
                print('skribbl.io!'); webbrowser.open("https://skribbl.io/")                
            elif game_select == 'steu':
                print('storiumedu!'); webbrowser.open("https://storiumedu.com/")               
            elif game_select == 'blob':
                print('agar.io!'); webbrowser.open("https://agar.io/")                
            elif game_select == 'boo!':
                print('google halloween!'); webbrowser.open("https://www.google.com/doodles/halloween-2018")        
            elif game_select == 'pengu':
                print('dancing penguins!')
                blinking_penguin()
            elif game_select == '.':
                print('just sitting. '); time.sleep(1)
                print('in the void'); time.sleep(1)
                print('forever'); time.sleep(1)
                void_sitting()
            elif game_select == 'bye':
                exit_program()
                break
            else:
                print('...I don\'t know that game, please choose a game from the games list')


intoduction()
user_interface()