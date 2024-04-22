board = {'1h': 'bking', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking'}

def isValidChessBoard(chessBoard):
    
    
    b_pieces = 0
    w_pieces = 0

    bking_pieces = 0
    wking_pieces = 0
    
    bqueen_pieces = 0
    wqueen_pieces = 0

    bpawn_pieces = 0
    wpawn_pieces = 0
    
    valid_pos = set([f"{num}{char}" for num in '12345678' for char in 'abcdefgh'])

    
    for pos, piece in board.items():
        if piece.startswith('b'):
            b_pieces +=1
            match piece:
                case 'bking':  bking_pieces +=1
                case 'bpawn':  bpawn_pieces +=1
                case 'bqueen': bqueen_pieces +=1
        if piece.startswith('w'):
            w_pieces +=1
            match piece:
                case 'wking':  wking_pieces +=1
                case 'wpawn':  wpawn_pieces +=1
                case 'wqueen': wqueen_pieces +=1
        
        

    if b_pieces <= 16 and w_pieces <= 16:
        if bking_pieces == 1 and wking_pieces == 1:
            if bqueen_pieces == 1 and wqueen_pieces == 1:
                if pos in valid_pos:
                    return True
    

    return False
print(isValidChessBoard(board))