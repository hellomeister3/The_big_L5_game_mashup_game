# the big L5 game mashup game

# importing modules
import time
import webbrowser
from random import randint

# function to display game introduction:
def intoduction():
    for i in range(100):
        print('               ---                 '); time.sleep(0.02)
    print('--- a Hi_2014 studios production ---'); time.sleep(1)

    print('''
 .              +   .                .   . .     .  .
                   .                    .       .     *
  .       *                        . . . .  .   .  + .
            "You Are Here"            .   .  +  . . .
.                 |             .  .   .    .    . .
                  |           .     .     . +.    +  .
                 \|/            .       .   . .
        . .       V          .    * . . .  .  +   .
           +      .           .   .      +
                            .       . +  .+. .
  .                      .     . + .  . .     .      .
           .      .    .     . .   . . .        ! /
      *             .    . .  +    .  .       - O -
          .     .    .  +   . .  *  .       . / |
               . + .  .  .  .. +  .
.      .  .  .  *   .  *  . +..  .            *
 .      .   . .   .   .   . .  +   .    .            +

    '''); time.sleep(1)


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

    for i in range(6):
        print('''
    

    ''')
        print('''
(o_
//\\
V_/_'''); time.sleep(1)
        print('''
    
    
    ''')
        print('''
(-_
//\\
V_/_   
    '''); time.sleep(1)

    print('oh sorry, i meant a blinking penguin'); time.sleep(0.7)



# function for tic tac toe game
def tic_tac_toe():
    print(''); time.sleep(0.3)
    board = []
    players_turn = True
    AI_playing = False
    endgame = False
    player1Turn = 1
    AI_turn = 1

    for x in range(0, 3):
        board.append(["■"] * 3)
    print(''); time.sleep(0.3)
    # creates the board as a list

    def print_board(board):
        for row in board:
            print(' '.join(row))
    print(''); time.sleep(0.3)
    # creates a function for printing the board

    print_board(board)
    # prints the board

    print('welcome to the Tic Tac Toe game'); print(''); time.sleep(0.3)
    counter1 = str(input('player 1 would you like to be X or O?')); print(''); time.sleep(0.3)
    if counter1 == 'X':
        AI_counter = 'O'
    elif counter1 == 'O':
        AI_counter = 'X'
    elif counter1 == 'o':
        counter1 = 'O'
        AI_counter = 'X'
    elif counter1 == 'x':
        counter1 = 'X'
        AI_counter = 'O'
    else:
        print('that is not a valid character. player 1 is X, player 2 is O'); print(''); time.sleep(0.3)
        counter1 = 'X'
        AI_counter = 'O'
    # players choose their counters

    print('player 1 is', counter1, ',the AI is', AI_counter); print(''); time.sleep(0.3)
    # players told what their counters are

    def winner_check(what_player):
        if board[0][0] == board[0][1] == board[0][2] == what_player or \
                board[1][0] == board[1][1] == board[1][2] == what_player or \
                board[2][0] == board[2][1] == board[2][2] == what_player or \
                board[0][0] == board[1][1] == board[2][2] == what_player or \
                board[0][2] == board[1][1] == board[2][0] == what_player or \
                board[0][0] == board[1][0] == board[2][0] == what_player or \
                board[0][1] == board[1][1] == board[2][1] == what_player or \
                board[0][2] == board[1][2] == board[2][2] == what_player:
            return True
        return False
    # see if there are three in a row (\ enables multiple lines in code)

    def tie_check():
        if board[0][0] != '■' and \
                board[0][1] != '■' and \
                board[0][2] != '■' and \
                board[1][0] != '■' and \
                board[1][1] != '■' and \
                board[1][2] != '■' and \
                board[2][0] != '■' and \
                board[2][1] != '■' and \
                board[2][2] != '■':
            return True
        return False
    # checks for if it is a tie

    def total_checking():

        winner_check(what_player)
        tie_check()
        # runs functions for winning conditions

    def check_outcomes():
        if tie_check():
            print('its a draw!'); print(''); time.sleep(0.3)
            endgame = True
            players_turn = False
            AI_playing = False

        elif winner_check(what_player) == True:
            print('unlucky, the AI won!'); print(''); time.sleep(0.3)
            endgame = True
            players_turn = False
            AI_playing = False
        # code for if player 1 has won


    # stops the game if it is a tie or a win

    while endgame == False:

        if players_turn == True:
            print(" player 1 turn", player1Turn); print(''); time.sleep(0.3)
            player1Turn += 1
            row = int(input("Row: ")) - 1
            col = int(input("Column: ")) - 1
            print(''); time.sleep(0.3)
            # player chooses the position for their counter

            if board[row][col] == '■':
                board[row][col] = counter1
                print_board(board) #prints the updated board
                print(''); time.sleep(0.3)
                what_player = counter1
            elif IndexError:
                print('this square has already been used, as a penalty your turn is forfeit'); print(''); time.sleep(0.3)#checks for an error
            else:
                print('this square has already been used, as a penalty your turn is forfeit'); print(''); time.sleep(0.3)
            # checks to see if the player has tried to overwrite another counter


            winner_check(what_player)
            tie_check()
            # runs functions for winning conditions


            if tie_check():
                print('its a draw!'); print(''); time.sleep(0.3)
                endgame = True
                players_turn = False
                AI_playing = False

            elif winner_check(what_player) is True:
                print('player 1 wins!'); print(''); time.sleep(0.3)
                endgame = True
                players_turn = False
                AI_playing = False
            # code for if player 1 has won

            else:
                pass
                # stops the game if it is a tie or a win

            if endgame == False:
                players_turn = False
                AI_playing = True

        elif AI_playing == True:
            print('AI turn', AI_turn); print(''); time.sleep(0.3)
            AI_turn += 1

            if (board[0][0] == counter1 or
                    board[0][2] == counter1 or
                    board[2][0] == counter1 or
                    board[2][2] == counter1) and \
                    board[1][1] == '■':
                board[1][1] = AI_counter
                print_board(board); print(''); time.sleep(0.3)
                total_checking()
                check_outcomes()
                if endgame == False:
                    players_turn = True
                    AI_playing = False
            # tells the AI to play in the middle square if its opponent has gone in the corners.

            elif (board[0][1] == counter1 or
                    board[1][2] == counter1 or
                    board[2][1] == counter1 or
                    board[1][0] == counter1) and \
                    board[1][1] == '■':
                board[1][1] = AI_counter
                print_board(board); print(''); time.sleep(0.3)
                total_checking()
                check_outcomes()
                if endgame == False:
                    players_turn = True
                    AI_playing = False
            # tells the AI to play in the middle if its opponent has gone in one of the sides.

            elif board[1][1] == counter1 and \
                    board[0][0] == '■':
                board[0][0] = AI_counter
                print_board(board); print(''); time.sleep(0.3)
                total_checking()
                check_outcomes()
                if endgame == False:
                    players_turn = True
                    AI_playing = False
            # tells the AI to play in the top corner if its opponent has played in the middle.

            elif board[1][1] == counter1 and \
                    board[2][2] == '■' or \
                    board[0][0] == counter1 and \
                    board[2][0] == counter1 and \
                    board[2][1] == counter1 and \
                    board[2][2] == '■':
                board[2][2] = AI_counter
                print_board(board); print(''); time.sleep(0.3)
                total_checking()
                check_outcomes()
                if endgame == False:
                    players_turn = True
                    AI_playing = False
            # counters the opponent if they have 2 in a row

            elif board[2][0] == counter1 and \
                    board[1][1] == counter1 and \
                    board[0][2] == '■' or \
                    board[0][0] == counter1 and \
                    board[0][1] == counter1 and \
                    board[0][2] == '■':
                board[0][2] = AI_counter
                print_board(board); print(''); time.sleep(0.3)
                total_checking()
                check_outcomes()
                if endgame == False:
                    players_turn = True
                    AI_playing = False
            # counters the opponent if they have 2 in a row

            elif board[0][2] == counter1 and \
                    board[0][1] == counter1 and \
                    board[0][0] == '■' or \
                    board[1][0] == counter1 and \
                    board[2][0] == counter1 and \
                    board[0][0] == '■':
                board[0][0] = AI_counter
                print_board(board); print(''); time.sleep(0.3)
                total_checking()
                check_outcomes()
                if endgame == False:
                    players_turn = True
                    AI_playing = False
            # counters the opponent if they have 2 in a row

            elif board[1][0] == counter1 and \
                    board[0][0] == counter1 and \
                    board[2][0] == '■' or \
                    board[2][1] == counter1 and \
                    board[2][2] == counter1 and \
                    board[2][0] == '■':
                board[2][0] = AI_counter
                print_board(board); print(''); time.sleep(0.3)
                total_checking()
                check_outcomes()
                if endgame == False:
                    players_turn = True
                    AI_playing = False
            # counters the opponent if they have 2 in a row

            elif board[2][1] == counter1 and \
                    board[1][1] == counter1 and \
                    board[0][1] == '■' or \
                    board[0][0] == counter1 and \
                    board[0][2] == counter1 and \
                    board[0][1] == '■':
                board[0][1] = AI_counter
                print_board(board); print(''); time.sleep(0.3)
                total_checking()
                check_outcomes()
                if endgame == False:
                    players_turn = True
                    AI_playing = False
            # counters the opponent if they have 2 in a row

            elif board[1][0] == counter1 and \
                    board[1][1] == counter1 and \
                    board[1][2] == '■' or \
                    board[0][2] == counter1 and \
                    board[2][2] == counter1 and \
                    board[1][2] == '■':
                board[1][2] = AI_counter
                print_board(board); print(''); time.sleep(0.3)
                total_checking()
                check_outcomes()
                if endgame == False:
                    players_turn = True
                    AI_playing = False
            # counters the opponent if they have 2 in a row

            elif board[0][1] == counter1 and \
                    board[1][1] == counter1 and \
                    board[2][1] == '■' or \
                    board[2][2] == counter1 and \
                    board[2][0] == counter1 and \
                    board[2][2] == '■':
                board[2][1] = AI_counter
                print_board(board); print(''); time.sleep(0.3)
                total_checking()
                check_outcomes()
                if endgame == False:
                    players_turn = True
                    AI_playing = False
            # counters the opponent if they have 2 in a row

            elif board[1][2] == counter1 and \
                    board[1][1] == counter1 and \
                    board[1][0] == '■' or \
                    board[0][0] == counter1 and \
                    board[2][0] == counter1 and \
                    board[1][0] == '■':
                board[1][0] = AI_counter
                print_board(board); print(''); time.sleep(0.3)
                total_checking()
                check_outcomes()
                if endgame == False:
                    players_turn = True
                    AI_playing = False
            # counters the opponent if they have 2 in a row

            elif board[0][0] == counter1 and \
                    board[2][2] == counter1 and \
                    board[1][1] == '■' or \
                    board[2][0] == counter1 and \
                    board[0][2] == counter1 and \
                    board[1][1] == '■' or \
                    board[0][1] == counter1 and \
                    board[2][1] == counter1 and \
                    board[1][1] == '■' or \
                    board[1][0] == counter1 and \
                    board[1][2] == counter1 and \
                    board[1][1] == '■':
                board[1][1] = AI_counter
                print_board(board); print(''); time.sleep(0.3)
                total_checking()
                check_outcomes()
                if endgame == False:
                    players_turn = True
                    AI_playing = False
            # counters the opponent if they have 2 around the centre.

            elif board[1][1] == AI_counter and \
                     board[0][0] == AI_counter and \
                     board[2][2] == '■' or \
                     board[2][0] == AI_counter and \
                     board[2][1] == AI_counter and \
                     board[2][2] == '■':
                board[2][2] = AI_counter
                print_board(board); print(''); time.sleep(0.3)
                total_checking()
                check_outcomes()
                if endgame == False:
                    players_turn = True
                    AI_playing = False
                # Tells AI to play the third in arrow if the player has not countered it

            elif board[2][0] == AI_counter and \
                     board[1][1] == AI_counter and \
                     board[0][2] == '■' or \
                     board[0][0] == AI_counter and \
                     board[0][1] == AI_counter and \
                     board[0][2] == '■':
                board[0][2] = AI_counter
                print_board(board); print(''); time.sleep(0.3)
                total_checking()
                check_outcomes()
                if endgame == False:
                    players_turn = True
                    AI_playing = False
                # Tells AI to play the third in arrow if the player has not countered it

            elif board[0][2] == AI_counter and \
                     board[0][1] == AI_counter and \
                     board[0][0] == '■' or \
                     board[1][0] == AI_counter and \
                     board[2][0] == AI_counter and \
                     board[0][0] == '■':
                board[0][0] = AI_counter
                print_board(board); print(''); time.sleep(0.3)
                total_checking()
                check_outcomes()
                if endgame == False:
                    players_turn = True
                    AI_playing = False
                # Tells AI to play the third in arrow if the player has not countered it

            elif board[1][0] == AI_counter and \
                     board[0][0] == AI_counter and \
                     board[2][0] == '■' or \
                     board[2][1] == AI_counter and \
                     board[2][2] == AI_counter and \
                     board[2][0] == '■':
                board[2][0] = AI_counter
                print_board(board); print(''); time.sleep(0.3)
                total_checking()
                check_outcomes()
                if endgame == False:
                    players_turn = True
                    AI_playing = False
                # Tells AI to play the third in arrow if the player has not countered it

            elif board[2][1] == AI_counter and \
                     board[1][1] == AI_counter and \
                     board[0][1] == '■' or \
                     board[0][0] == AI_counter and \
                     board[0][2] == AI_counter and \
                     board[0][1] == '■':
                board[0][1] = AI_counter
                print_board(board); print(''); time.sleep(0.3)
                total_checking()
                check_outcomes()
                if endgame == False:
                    players_turn = True
                    AI_playing = False
                # Tells AI to play the third in arrow if the player has not countered it

            elif board[1][0] == AI_counter and \
                     board[1][1] == AI_counter and \
                     board[1][2] == '■' or \
                     board[0][2] == AI_counter and \
                     board[2][2] == AI_counter and \
                     board[1][2] == '■':
                board[1][2] = AI_counter
                print_board(board); print(''); time.sleep(0.3)
                total_checking()
                check_outcomes()
                if endgame == False:
                    players_turn = True
                    AI_playing = False
                # Tells AI to play the third in arrow if the player has not countered it

            elif board[0][1] == AI_counter and \
                     board[1][1] == AI_counter and \
                     board[2][1] == '■' or \
                     board[2][2] == AI_counter and \
                     board[2][0] == AI_counter and \
                     board[2][2] == '■':
                board[2][1] = AI_counter
                print_board(board); print(''); time.sleep(0.3)
                total_checking()
                check_outcomes()
                if endgame == False:
                    players_turn = True
                    AI_playing = False
                # counters the opponent if they have 2 in a row

            elif board[1][2] == AI_counter and \
                     board[1][1] == AI_counter and \
                     board[1][0] == '■' or \
                     board[0][0] == AI_counter and \
                     board[2][0] == AI_counter and \
                     board[1][0] == '■':
                board[1][0] = AI_counter
                print_board(board); print(''); time.sleep(0.3)
                total_checking()
                check_outcomes()
                if endgame == False:
                    players_turn = True
                    AI_playing = False
                # Tells AI to play the third in arrow if the player has not countered it

            elif board[0][0] == AI_counter and \
                     board[2][2] == AI_counter and \
                     board[1][1] == '■' or \
                     board[2][0] == AI_counter and \
                     board[0][2] == AI_counter and \
                     board[1][1] == '■' or \
                     board[0][1] == AI_counter and \
                     board[2][1] == AI_counter and \
                     board[1][1] == '■' or \
                     board[1][0] == AI_counter and \
                     board[1][2] == AI_counter and \
                     board[1][1] == '■':
                board[1][1] = AI_counter
                print_board(board); print(''); time.sleep(0.3)
                total_checking()
                check_outcomes()
                if endgame == False:
                    players_turn = True
                    AI_playing = False
                # Tells AI to play the third in arrow if the player has not countered it

            else:
                if board[0][0] == '■':
                    board[0][0] = AI_counter
                    print_board(board); print(''); time.sleep(0.3)
                    players_turn = True
                    AI_playing = False

                elif board[0][1] == '■':
                    board[0][1] = AI_counter
                    print_board(board); print(''); time.sleep(0.3)
                    players_turn = True
                    AI_playing = False

                elif board[0][2] == '■':
                    board[0][2] = AI_counter
                    print_board(board); print(''); time.sleep(0.3)
                    players_turn = True
                    AI_playing = False

                elif board[1][0] == '■':
                    board[1][0] = AI_counter
                    print_board(board); print(''); time.sleep(0.3)
                    players_turn = True
                    AI_playing = False

                elif board[1][1] == '■':
                    board[1][1] = AI_counter
                    players_turn = True
                    AI_playing = False

                elif board[1][2] == '■':
                    board[1][2] = AI_counter
                    print_board(board); print(''); time.sleep(0.3)
                    players_turn = True
                    AI_playing = False

                elif board[2][0] == '■':
                    board[2][0] = AI_counter
                    print_board(board); print(''); time.sleep(0.3)
                    players_turn = True
                    AI_playing = False

                elif board[2][1] == '■':
                    board[2][1] = AI_counter
                    print_board(board); print(''); time.sleep(0.3)
                    players_turn = True
                    AI_playing = False

                elif board[2][2] == '■':
                    board[2][2] = AI_counter
                    print_board(board); print(''); time.sleep(0.3)
                    players_turn = True
                    AI_playing = False


# function for text based apocalypse game
def apocalypse():
    # introduction
    print(''); time.sleep(1)
    print(''); time.sleep(1)
    print('it was a dark and stormy night...'); print(''); time.sleep(2)
    print('...the waves crashed against the rocks...'); print(''); time.sleep(2)
    print('...we had no notice...'); print(''); time.sleep(2)
    print('...apart from the signs we all chose to ignore...'); print(''); time.sleep(2)
    print('...the storms...'); print(''); time.sleep(2)
    print('...the fires...'); print(''); time.sleep(2)
    print('...'); print(''); time.sleep(2)
    print('...'); print(''); time.sleep(2)
    print('...the virus...'); print(''); time.sleep(2)
    print('...'); print(''); time.sleep(2)
    print('...noone knew what was happening...'); print(''); time.sleep(2)
    print('...untill it was too late...'); print(''); time.sleep(2)

    for i in range(30):
        print('...'); time.sleep(0.5); print('')
    print('WELCOME TO:'); time.sleep(0.5)
    print('''
                               ________________
                          ____/ (  (    )   )  \___
                         /( (  (  )   _    ))  )   )\\
                       ((     (   )(    )  )   (   )  )
                     ((/  ( _(   )   (   _) ) (  () )  )
                    ( (  ( (_)   ((    (   )  .((_ ) .  )_
                   ( (  )    (      (  )    )   ) . ) (   )
                  (  (   (  (   ) (  _  ( _) ).  ) . ) ) ( )
                  ( (  (   ) (  )   (  ))     ) _)(   )  )  )
                 ( (  ( \ ) (    (_  ( ) ( )  )   ) )  )) ( )
                  (  (   (  (   (_ ( ) ( _    )  ) (  )  )   )
                 ( (  ( (  (  )     (_  )  ) )  _)   ) _( ( )
                  ((  (   )(    (     _    )   _) _(_ (  (_ )
                   (_((__(_(__(( ( ( |  ) ) ) )_))__))_)___)
                   ((__)        \\\\||lll|l||///          \_))
                                /(/ (  )  ) )\   
                               ( ( ( | | ) ) )\   
                               /(| / ( )) ) ) )) 
                               ( ((((_(|)_)))))     
                                 ||\(|(|)|/||     
                                 |(||(||)||||        
                                //|/l|||)|\\\\ \     
                         / / //  /|//||||\\\\  \ \  \ _
--------------------------APOCALYPSE: WORLD GO BOOM--------------------------
    '''); print(''); time.sleep(2)
        
    character_health = 0
    chracter_speed = 0
    character_hunger = 0
    character_attack = 0

    print('''
 ------------------------------------------
 --- CHARACTER TYPES:                   ---   
 ---                                    ---
 --- (health, speed, hunger, attack)    ---
 ---                                    ---
 --- Hunter(h): 10, 20, 15, 15          ---
 --- Archer(a): 15, 15, 10, 20          ---
 --- Soldier(s): 20, 10, 10, 20         ---
 ---                                    ---
 ------------------------------------------
    
    '''); print(''); time.sleep(3)
    turn = ''

    while True: 
        character_select = input('please choose a character: '); print(''); time.sleep(1)
        print('you have chosen...'); print(''); time.sleep(1)

        if character_select == 'h':
            print('hunter!'); print(''); time.sleep(1)
            character_health = 10
            character_speed = 20
            character_hunger = 15
            character_attack = 15
            max_health = 10
            max_speed = 20
            max_hunger = 15
            max_attack = 15
            weapon = 'rifle'
            turn = 'h'
            place = 'log cabin'
            break
        elif character_select == 'a':
            print('archer!'); print(''); time.sleep(1)
            character_health = 15
            character_speed = 15
            character_hunger = 10
            character_attack = 20
            max_health = 15
            max_speed = 15
            max_hunger = 10
            max_attack = 20
            weapon = 'bow'
            turn = 'a'
            place = 'tree house'
            break
        elif character_select == 's':
            print('soldier!'); print(''); time.sleep(1)
            character_health = 20
            character_speed = 10
            character_hunger = 10
            character_attack = 20
            max_health = 20
            max_speed = 10
            max_hunger = 10
            max_attack = 20
            weapon = 'pistol'
            turn = 's'
            place = 'barracks'
            break
        else:
            print('... that\'s not a valid character. please @me in the games channel if you have an idea for one.'); print(''); time.sleep(3)

    inventory = []
    inventory.append(weapon)
    print(f'health: {character_health}, speed: {character_speed}, hunger: {character_hunger}, attack: {character_attack}, inventory: {inventory}'); print(''); time.sleep(1)

    print(f'you wake up in your {place}, well rested and fed.'); print(''); time.sleep(1)
    print('you can\'t quite remember what heppend last night, or how you got home'); print(''); time.sleep(1)
    print('anyways, it\'s time for a new adventure!'); print(''); time.sleep(1)

    while character_health > 0:
        print(f'''
-------------------------------------
--- you are at the {place}        ---
---                               ---
--- options:                      ---
--- forage: f                     ---
--- eat: e                        ---
--- rest: r                       ---
--- continue: c                   ---
---                               ---
-------------------------------------       
        '''); print(''); time.sleep(2)
        print(f'health: {character_health}, speed: {character_speed}, hunger: {character_hunger}, attack: {character_attack}, inventory: {inventory}'); print(''); time.sleep(2)
        action = input('what would you like to do? '); print(''); time.sleep(1)

        # lets player find food
        if action == 'f':
            forage = randint(1,4)
            if forage == 1:
                print('you found food!'); print(''); time.sleep(1)
                inventory.append('food')
            else:
                print('you didnt find anything'); print(''); time.sleep(1)

        # lets player gain hunger
        elif action == 'e':
            if 'food' in inventory and character_hunger < max_hunger:
                eat = randint(1, 3)
                character_hunger += eat
                if character_hunger > max_hunger:
                    character_hunger = max_hunger
                inventory.remove('food')
                print(f'you gained {eat} hunger'); print(''); time.sleep(1)
            elif 'food' not in inventory:
                print('you have no food'); print(''); time.sleep(1)
            elif character_hunger == max_hunger:
                print('you are not hungry'); print(''); time.sleep(1)

        # lets player gain speed
        elif action == 'r':
            if character_speed < max_speed:
                rest = randint(1, 4)
                character_speed += rest
                if character_speed > max_speed:
                    character_speed = max_speed
                print(f'you gained {rest} speed'); print(''); time.sleep(1)
            elif character_speed == max_speed:
                print('you are not tired'); print(''); time.sleep(1)

        # lets player continue story
        elif action == 'c':

            if turn == 'h':
                turn = input(' you can to go the woods(w), or the city(ci)'); print(''); time.sleep(1)

            elif turn == 'a':
                turn = input('you can go to the city(ci) or the shooting range(sr)'); print(''); time.sleep(1)

            elif turn == 's':
                turn = input('you can go to the shooting range(sr) or the mess hall(mh)'); print(''); time.sleep(1)

            elif turn == 'w':
                print('you are hunkered down in a shrub, looking out for any animal to cross your path'); print(''); time.sleep(1)
                print(f'you see movement from behind one of the trees and swing your {weapon} round to look'); print(''); time.sleep(1)
                print('but...'); print(''); time.sleep(1)
                print('...thats not a deer...'); print(''); time.sleep(1)
                print('its a car. but, there are no cars anymore...'); print(''); time.sleep(1)
                hunt = randint(1, 5)
                for i in range(hunt):
                    inventory.append('food')
                print('a deer runs across your path'); print(''); time.sleep(1)
                print(f'you shoot it, and manage to salvage {hunt} food before the wolves arrive to finish off the carcas'); print(''); time.sleep(1)
                turn = input('now with some food, you can either go to the city(ci) or the abandoned village(av) '); print(''); time.sleep(1)

            elif turn == 'ci':
                print('you arrive in the city, weaving your way past the rubble and shacks'); print(''); time.sleep(1)
                print('you notice more poeple around than usual, but you dismiss it'); print(''); time.sleep(1)
                turn = input(' you can either go to the shooting range(sr), the abandoned village(av), the woods(w) or the radioactive plains(rp)'); print(''); time.sleep(1)

            elif turn == 'sr':
                print(f'you arrive at the shooting range {weapon} in hand'); print(''); time.sleep(1)
                target = randint(2,7)
                print('you sidle up to the first platform, taking each shot in quick sucession'); print(''); time.sleep(1)
                print(f'you get {target} bullseyes!'); print(''); time.sleep(1)
                print('you notice that the targets have far more holes in than last week'); print(''); time.sleep(1)
                turn = input('you can either go to the mess hall(mh), the city(ci), the radioactive plains(rp) or the halls of death(hd)'); print(''); time.sleep(1)

            elif turn == 'mh':
                print('you arrive at the mess hall, and jump for joy! the line is very small!'); print(''); time.sleep(1)
                meal = randint(1,3)
                print(f'you get to the counter quickly and receive {meal} food'); print(''); time.sleep(1)
                for i in range(meal):
                    inventory.append('food')
                turn = input('you can either go to the shooting range(sr) or the halls of death(hd)'); print(''); time.sleep(1)

            elif turn == 'av':
                attack = randint(1,3)
                if attack == 1:
                    nomads = randint(3,6)
                    print(f'you arrive in the abandoned village, and are ambushed by {nomads} nomads!'); print(''); time.sleep(1)
                    shots = randint(1, character_speed)
                    for i in range(nomads, shots):
                        shoot = input('type . to shoot! '); print(''); time.sleep(0.3)
                    if shots > nomads and character_attack > 6:
                        print('you managed to shoot them all!'); print(''); time.sleep(1)
                    else:
                        lose = randint(1, nomads)
                        character_health -= lose
                        print(f'oh no! you lost {lose} health before defeating them!'); print(''); time.sleep(1)
                        if character_health == 0:
                            print('---  GAME OVER  ---'); print(''); time.sleep(1)
                            break
                else:
                    print(' you arrive in the abandoned village, and spot a group of nomads on the other side'); print(''); time.sleep(1)
                    house = randint(1,2)
                    for i in range(house):
                        inventory.append('food')
                    print(f' you go into some of the houses and find {house} food!'); print(''); time.sleep(1)
                turn = input(' you can either go to the radioactive plains(rp), the witches hut(wh) or the desert(d)'); print(''); time.sleep(1)

            elif turn == 'rp':
                if character_health < 8:
                    print(' you arrive on the radioacctive plains, but you re too weak to withstand the radiation!'); print(''); time.sleep(1)
                    character_health = 0
                    print('---  GAME OVER  ---'); print(''); time.sleep(1)
                mutants = randint(5,9)
                print(f'you arrive on the radioactive plains, and are attacked by {mutants} mutants!'); print(''); time.sleep(1)
                shots = randint(2, character_speed)
                for i in range(mutants, shots):
                    shoot = input('type . to shoot! '); print(''); time.sleep(0.3)
                if shots > mutants and character_attack > 5:
                    print('you managed to shoot them all!'); print(''); time.sleep(1)
                else:
                    lose = randint(1, mutants)
                    character_health -= lose
                    print(f'oh no! you lost {lose} health before defeating them!'); print(''); time.sleep(1)
                    if character_health == 0:
                        print('---  GAME OVER  ---'); print(''); time.sleep(1)
                        break
                turn = input('you can either go to the witches hut(wh) or the castle(ca)'); print(''); time.sleep(1)

            elif turn == 'hd':
                print(' you arrive in the halls of death and.. oh no...'); print(''); time.sleep(1)
                print('there are zombies everywhere!'); print(''); time.sleep(1)
                for i in range(1, 3):
                    print(f'---  ROUND {i} ---'); print(''); time.sleep(1)
                    zombies = randint(4, 12)
                    print(f'there are {zombies} zombies apporaching!'); print(''); time.sleep(1)
                    shots = randint(4, character_speed)
                    if (shots > zombies and character_attack > 8) or (shots > zombies*2 and character_attack > 4):
                        print('you killed them all!'); print(''); time.sleep(1)
                    else:
                        lose = randint(1, zombies)
                        print(f'oh no! you lost {lose} health before defeating them'); print(''); time.sleep(1)
                        if character_health == 0:
                            print('---  GAME OVER  ---'); print(''); time.sleep(1)
                print('well done! you sucessfully defeated all the zombies!'); print(''); time.sleep(1)
                print('a flash on the wall draws your attention...'); print(''); time.sleep(1)
                print('you see some writing in what looks to be made of gold'); print(''); time.sleep(1)
                print(' you can only make out a few of the characters:'); print(''); time.sleep(1)
                print(''' 
                
:1111::10100:1111::10100:1000:101::100:101:10011:101:

                '''); print(''); time.sleep(1)
                turn = input(' you can either go to the radioactive plains(rp) or the castle(ca)'); print(''); time.sleep(1)


            elif turn == 'wh':
                witch = randint(1,4)
                print(' you arrive at the witches hut, and see that the witch is not there'); print(''); time.sleep(1)
                ingo = input('do you go in? y/n '); print(''); time.sleep(1)
                if ingo == 'y':
                    print('you go into the witches hut, and notice a dark red liquid in the cauldron'); print(''); time.sleep(1)
                    safe = randint(1,2)
                    drink = input('do you drink it? y/n '); print(''); time.sleep(1)
                    if drink == 'y':
                        if safe == 1:
                            character_health = temp
                            max_health += 5
                            character_health = max_health
                            print(f'it was a health potion! you gained {character_health - temp} health!'); print(''); time.sleep(1)
                        elif safe == 2:
                            max_health -= 5
                            character_health -= 5
                            print(f'oh no! it was a poison potion! you lost 5 health'); print(''); time.sleep(1)
                    if witch == 1:
                        print('oh no! the witch is outside!'); print(''); time.sleep(1)
                        if character_speed < 10:
                            print('you couldn\'t get out the window fast enough! the witch caught you!'); print(''); time.sleep(1)
                            print('she puts a bag over your head and starts to drag you away...'); print(''); time.sleep(1)
                            print(' the last thing you notice before you pass out is the sound of construction, and a sweltering heat'); print(''); time.sleep(1)
                            turn = 'dtw'
                        else:
                            print('you make it out a window before the witch comes in. phew'); print(''); time.sleep(1)
                            turn = input('you can either go to the desert temple(dt) or the castle(ca)')
                    else:
                        print('yyou leave the witch hut and head towards the castle'); print(''); time.sleep(1)
                        turn = 'ca'
                else:
                    print('you decide to stear this one clear, and head on towards the castle'); print(''); time.sleep(1)
                    turn = 'ca'

            elif turn == 'ca':
                print('you arrive at the castle, and are greeted by the guards'); print(''); time.sleep(1)
                guards = randint(1,7)
                print('they ask to see identification, you give it to them'); print(''); time.sleep(1)
                if guards == 1:
                    print('oh no! your identity card was damaged on your way here!, the guards don\'t allow you to enter'); print(''); time.sleep(1)
                    print('you turn and leave')
                    if speed < 4:
                        print('you are so slow that the guards impale you for not leaving!'); print(''); time.sleep(1)
                        print('as you lay there, injured, by the side of the moat, you notice a flash in the distance'); print(''); time.sleep(1)
                        print('wait, thats coming from the d...'); print(''); time.sleep(2)
                        turn = 'F'

            elif turn == 'd':

            elif turn == 'dt':

            elif turn == 'dtw':

            elif turn == 'F':

            elif turn == 'ae':

    print('''
                               ________________
                          ____/ (  (    )   )  \___
                         /( (  (  )   _    ))  )   )\\
                       ((     (   )(    )  )   (   )  )
                     ((/  ( _(   )   (   _) ) (  () )  )
                    ( (  ( (_)   ((    (   )  .((_ ) .  )_
                   ( (  )    (      (  )    )   ) . ) (   )
                  (  (   (  (   ) (  _  ( _) ).  ) . ) ) ( )
                  ( (  (   ) (  )   (  ))     ) _)(   )  )  )
                 ( (  ( \ ) (    (_  ( ) ( )  )   ) )  )) ( )
                  (  (   (  (   (_ ( ) ( _    )  ) (  )  )   )
                 ( (  ( (  (  )     (_  )  ) )  _)   ) _( ( )
                  ((  (   )(    (     _    )   _) _(_ (  (_ )
                   (_((__(_(__(( ( ( |  ) ) ) )_))__))_)___)
                   ((__)        \\\\||lll|l||///          \_))
                                /(/ (  )  ) )\   
                               ( ( ( | | ) ) )\   
                               /(| / ( )) ) ) )) 
                               ( ((((_(|)_)))))     
                                 ||\(|(|)|/||     
                                 |(||(||)||||        
                                //|/l|||)|\\\\ \     
                         / / //  /|//||||\\\\  \ \  \ _
-------------------------------------------------------------------------------
    '''); print(''); time.sleep(2)
    print('---    THANK YOU FOR PLAYING:    ---'); print(''); time.sleep(2)
    print('---  APOCALYPSE: WORLD GO BOOM!  ---'); print(''); time.sleep(2)


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
--- welcome to the big game mashup game!      ---
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
--- tic tac toe: xox                          ---
--- apocalypse game: world go boom            ---
--- random game: idk                          ---
--- exit program: bye                         ---
---                                           ---
--- new games/ improvements welcome, just     ---
--- @ me in the games channel                 ---
-------------------------------------------------          
 ''')
        # asking user to select game
        game_select = input('enter game choice: '); print(''); time.sleep(0.5)
        time.sleep(0.5); print('you have chosen...'); print(''); time.sleep(0.5)
        game = 0
        maybe = randint(1, 10)

        # 1 in 5 chance of being rickrolled
        if maybe == 1:
            print(' surprise!'); time.sleep(0.7)
            webbrowser.open("https://www.youtube.com/watch?v=dQw4w9WgXcQ")

        else:
            
            # random game selection
            if game_select == 'idk':
                print('random game!'); time.sleep(0.5); print('')
                print('processing...'); time.sleep(0.5)
                for i in range(500):
                    game = randint(1,999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999999)
                    print(game); time.sleep(0.01)
                game = randint(1,9); time.sleep(0.5)
                print('your game is...'); time.sleep(1)
                print(''); time.sleep(0.4)
            
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

            # tic tac toe
            elif game_select == 'xox' or game == 8:
                print('tic tac toe!');
                tic_tac_toe()

            # apocalypse
            elif game_select == 'world go boom' or game == 9:
                print('Apocalypse: world go boom!')        
                apocalypse()    

            # exit program
            elif game_select == 'bye':
                exit_program()
                break
            
            # error message
            else:
                print('...I don\'t know that game, please choose a game from the games list')



user_interface()