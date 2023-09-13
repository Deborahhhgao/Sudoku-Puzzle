from threading import stack_size
from support import *

def num_hours() -> float:
    return 240.0


def print_board(board: Board) -> None:
    for i in range(0,9):
        for j in range(0,9):
            if board[i][j] == None:
                board[i][j] = " "
            if j==2 or j==5:
                print(str(board[i][j])+'|',end = '')
            elif j==8:
                print(str(board[i][j])+' '+str(i))
            else:
                print(board[i][j],end = '')
        if i == 2 or i == 5:
            print('-----------')
    print()
    print('012 345 678')


def read_board(raw_board: str) -> Board:
    board_list=[]
    for i in raw_board:
        if i == " ":
            i = None
        else:
            i = int(i)
        board_list.append(i)
    Board_list=[]
    for n in range(0,73,9):
        toolboard=[]
        for m in board_list[n:n+9]:
            toolboard.append(m)
        Board_list.append(toolboard)
    return Board_list


def is_empty(position: tuple[int, int], board: Board) -> bool:
    if board[position[0]][position[1]] == None:
        return True
    else:
        return False


def update_board(position: tuple[int, int], value: Optional[int], board: Board) -> None:
   # board[[position[0]][position[1]]] = value
   board[position[0]][position[1]] = value


def clear_position(position: tuple[int, int], board: Board) -> None:
    board[position[0]][position[1]] = None


def matrix_slices(board: Board) -> Board:
    board_slices=[]
    for i in range(0,9,3):
        toollist1=[]
        toollist2=[]
        toollist3=[]
        for j in range(0,9):
            for m in range(0,3):
                if j<3:
                    toollist1.append(board[j][i+m])
                if j>=3 and j<6:
                    toollist2.append(board[j][i+m])
                if j>=6 and j<9:
                    toollist3.append(board[j][i+m])
        board_slices.append(toollist1)
        board_slices.append(toollist2)
        board_slices.append(toollist3)
    return board_slices
   

def rank_list(insertlist: list) -> bool:
    tool_list = insertlist.copy()
    for i in range(9):
        if tool_list[i] == None or tool_list[i] == ' ':
            tool_list[i]=0
        else:
            tool_list[i] = int(tool_list[i])
    compare_list = sorted(tool_list)
    true_list=[1,2,3,4,5,6,7,8,9]
    if compare_list==true_list:
        return True
    else:
        return False


def column_board(board: Board) -> Board:
    column_board=[]
    for i in range(0,9):
        toollist=[]
        for j in range(0,9):
            toollist.append(board[j][i])
        column_board.append(toollist)
    return column_board


def has_won(board: Board) -> bool:
    board_slices=matrix_slices(board)
    column_boards=column_board(board)
    for i in range(9):
        if rank_list(board[i])==False:
            return False
    for i in range(9):
        if rank_list(board_slices[i])==False:
            return False
    for i in range(9):
        if rank_list(column_boards[i])==False:
            return False
    return True


def main() -> None:
    finalkey=False
    while finalkey==False:
        board=load_board(input(START_GAME_PROMPT))
        change_board=read_board(board)
        boardcopy=read_board(board)
        print_board(change_board)
        key=False
        while key==False:
            start_game=input(INPUT_PROMPT)
            if start_game == 'H' or start_game=='h':
                print(HELP_MESSAGE)
                print()
                print_board(change_board)
            elif start_game == 'Q' or start_game =='q':
                break
            else:
                inputone=int(start_game[0])
                inputtwo=int(start_game[2])
                inputthree=start_game[4]
                if is_empty((int(inputone),int(inputtwo)),boardcopy):
                    if inputthree=='C':
                        clear_position((inputone,inputtwo),change_board)
                        print_board(change_board)                
                    else:
                        update_board((inputone,inputtwo),inputthree,change_board)
                        print_board(change_board)  
                else:
                    print(INVALID_MOVE_MESSAGE)
                    print_board(change_board)
            key=has_won(change_board)
        if start_game=='Q' or start_game=='q':
            break
        if key:
            print(WIN_MESSAGE)
        restartkey=input(NEW_GAME_PROMPT)
        if restartkey=='y'or restartkey=='Y'or restartkey==" ":
            finalkey=False
        else:
            finalkey=True
    return


if __name__ == '__main__':
    main()






















