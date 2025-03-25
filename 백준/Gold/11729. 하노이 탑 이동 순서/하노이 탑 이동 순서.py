import sys

def not_selected_col(col1,col2):
    if col1 ==1 :
        return 2 if col2==3 else 3
    elif col1 ==2 :
        return 1 if col2==3 else 3
    else :
        return 1 if col2==2 else 2


def hanoi(move_size,move_from_col,move_to_col,moves):
    if move_size <=1 :
        moves.append(" ".join([str(move_from_col),str(move_to_col)]))
    
    else :
        temp_col = not_selected_col(move_from_col,move_to_col)
        hanoi(move_size-1,move_from_col,temp_col,moves)
        moves.append(" ".join([str(move_from_col),str(move_to_col)]))
        hanoi(move_size-1,temp_col,move_to_col,moves)


n = int(sys.stdin.readline())
moves = []
hanoi(n,1,3,moves)

print(len(moves))

for move in moves :
    print(move)