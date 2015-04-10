import battle_board as bb
import game_pieces as gp

# Set up initial board and pieces
gameboard = bb.create_gameboard()
piece_dictionary = gp.instatiate_pieces()


'''
Players place all pieces on board, behind 20 yard
line. No piece can be in the same position as another
'''
print 'Place your team behind your 20 yard line'
for team in ['home','away']:
    for piece_index in range(0,11):
        piece = piece_dictionary[team][piece_index]
        print 'Please place your ' + piece.name

        while True:    
            try:             
                x = int(raw_input("row: "))
                y = int(raw_input("column: "))
            except ValueError:
                print("Sorry, bad input")
                continue
            if(bb.place_piece(piece_index,(x,y), gameboard)):                
                piece.place_on_board(x,y)
                bb.print_board(gameboard)
                break
            else:
                continue    

