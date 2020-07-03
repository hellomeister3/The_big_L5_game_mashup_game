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
                            (   /(/ (  )  ) )\   )
                          (    ( ( ( | | ) ) )\   )
                           (   /(| / ( )) ) ) )) )
                         (     ( ((((_(|)_)))))     )
                          (      ||\(|(|)|/||     )
                        (        |(||(||)||||        )
                          (     //|/l|||)|\\\\ \     )
                        (/ / //  /|//||||\\\\  \ \  \ _)
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
        character_select = input('please choose a character: '); print(''); time.sleep(0.5)
        print('you have chosen...'); print(''); time.sleep(0.5)

        if character_select == 'h':
            print('hunter!'); print(''); time.sleep(0.5)
            character_health = 10
            character_speed = 20
            character_hunger = 15
            character_attack = 15
            max_health = 10
            max_speed = 20
            max_hunger = 15
            max_attack = 15
            turn = 'h'
            place = 'log cabin'
            break
        elif character_select == 'a':
            print('archer!'); print(''); time.sleep(0.5)
            character_health = 15
            chracter_speed = 15
            character_hunger = 10
            character_attack = 20
            max_health = 15
            max_speed = 15
            max_hunger = 10
            max_attack = 20
            turn = 'a'
            place = 'tree house'
            break
        elif character_select == 's':
            print('soldier!'); print(''); time.sleep(0.5)
            character_health = 20
            chracter_speed = 10
            character_hunger = 10
            character_attack = 20
            max_health = 20
            max_speed = 10
            max_hunger = 10
            max_attack = 20
            turn = 's'
            place = 'barracks'
            break
        else:
            print('... that\'s not a valid character. please @me in the games channel if you have an idea for one.'); print(''); time.sleep(3)

    inventory = []
    print(f'health: {character_health}, speed: {character_speed}, hunger: {character_hunger}, attack: {character_attack}, inventory: {inventory}'); time.sleep(2)
   

            print(f'you wake up in your {place}, well rested and fed.'); print(''); time.sleep(0.5)
            print('you can\'t quite remember what heppend last night, or how you got home'); print(''); time.sleep(0.5)
            print('anyways, it\'s time for a new adventure!'); print(''); time.sleep(0.5)

    while health > 0:
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
        action = input('what would you like to do? '); print(''); time.sleep(0.5)

        # lets player find food
        if action == 'f':
            forage = randint(1,5)
            if forage == 2:
                print('you found food!'); print(''); time.sleep(0.5)
                inventory.append('food')
            else:
                print('you didnt find anything'); print(''); time.sleep(0.5)

        # lets player gain hunger
        elif action == 'e':
            if 'food' in inventory and character_hunger < max_hunger:
                eat = randint(1, 3)
                character_hunger += eat
                if character_hunger > max_hunger:
                    character_hunger = max_hunger
                print(f'you gained {eat} hunger'); print(''); time.sleep(0.5)
            elif 'food' not in inventory:
                print('you have no food'); print(''); time.sleep(0.5)
            elif character_hunger == max_hunger:
                print('you are not hungry'); print(''); time.sleep(0.5)

        # lets player gain speed
        elif action == 'r':
            if character_speed < max_speed:
                rest = randint(1, 4)
                character_speed += rest
                if character_speed > max_speed:
                    character_speed = max_speed
                print(f'you gained {rest} speed'); print(''); time.sleep(0.5)
            elif character_speed = max_speed:
                print('you are not tired'); print(''); time.sleep(0.5)

        # lets play continue story
        elif action == 'c':

            if turn == 'h':
                print(' you can to go the woods')

            elif turn == 'a':

            elif turn == 's':

            elif turn == '1':

            elif turn == '2':

            elif turn == '4':

            elif turn == '5':

            elif turn == '6':

            elif turn == '7':

            elif turn == '8':

            elif turn == '9':
            
            elif turn == '10':

            elif turn == '11':

            elif turn == 'F':

            elif turn == 'AE'



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
        maybe = randint(1, 5)

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