# the big L5 mashup game

# importing modules
import time
import webbrowser
from random import randint

# function to display game introduction:
def intoduction():
    print('silence...'); time.sleep(1)

    for i in range(10): 
        print(''); time.sleep(0.5)

    print('but then...'); time.sleep(1)

    for i in range(10): 
        print(''); time.sleep(0.5)

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


# function for game: sitting in the void
def void_sitting():
    void_timer = 0

# keeps track of the time game has been running for (seconds)
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


# function for game: blinking penguin
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


# function to display exit message
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



# function to display the user interface
def user_interface():
    intoduction()

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
--- random game: idk                          ---
--- exit program: bye                         ---
---                                           ---
--- new games/ improvements welcome, just     ---
--- @ harry in games for L5                   ---
-------------------------------------------------          
 ''')
        # asking user to select game
        game_select = input('enter game choice: '); print(''); time.sleep(0.5)
        time.sleep(0.5); print('you have chosen...'); print(''); time.sleep(0.5)
        game = 0
        maybe = randint(1, 5)

        # 1 in 5 chance of being rickrolled
        if maybe == 1:
            print(' surprise!'); time.sleep(0.7)
            webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")

        else:
            
            # random game selection
            if game_select == 'idk':
                for i in range(500):
                    game = randint(1,7); print(game); time.sleep(0.01)

            # diep.io
            if game_select == 'pew' or game == 1:
                print('diep.io!'); webbrowser.open("https://diep.io/")

            # skribbl.io
            elif game_select == 'sksksk' or game == 2 :
                print('skribbl.io!'); webbrowser.open("https://skribbl.io/")

            # storiumedu
            elif game_select == 'steu' or game == 3:
                print('storiumedu!'); webbrowser.open("https://storiumedu.com/")

            # agar.io
            elif game_select == 'blob' or game == 4:
                print('agar.io!'); webbrowser.open("https://agar.io/")

            # google doodles halloween 2018
            elif game_select == 'boo!' or game == 5:
                print('google halloween!'); webbrowser.open("https://www.google.com/doodles/halloween-2018")

            # blinking penguin
            elif game_select == 'pengu' or game == 6:
                print('dancing penguins!')
                blinking_penguin()
            
            # sitting in the void
            elif game_select == '.' or game == 7:
                print('just sitting. '); time.sleep(1)
                print('in the void'); time.sleep(1)
                print('forever'); time.sleep(1)
                void_sitting()

            # exit program
            elif game_select == 'bye':
                exit_program()
                break
            
            # error message
            else:
                print('...I don\'t know that game, please choose a game from the games list')



user_interface()