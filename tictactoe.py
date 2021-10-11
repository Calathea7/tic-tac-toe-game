import random

# Prints out the tic tac toe board in the console
def show_board(board):
  print('')
  print('                         Reference board:')
  print('    |    |', '                   |    |')
  print(' ' + board[1] + '  |  ' + board[2] + ' |  ' + board[3], '             1  |  2 |  3 ')
  print('    |    |', '                   |    |')
  print('  __________  ', '             __________  ')
  print('    |    |', '                   |    |')
  print(' ' + board[4] + '  |  ' + board[5] + ' |  ' + board[6], '             4  |  5 |  6 ')
  print('    |    |', '                   |    |')
  print('  __________  ', '             __________  ')
  print('    |    |', '                   |    |')
  print(' ' + board[7] + '  |  ' + board[8] + ' |  ' + board[9], '             7  |  8 |  9 ')
  print('    |    |', '                   |    |')
  print('')


def mark_choice():
  mark = ''
  while not (mark == 'X' or mark == 'O'):
    print("Do you want to play as 'X' or 'O'? (type x/o)")
    mark = input().upper()

  if mark == 'X':
    return ['X', 'O']
  return ['O', 'X']


# A coin toss to decide who goes first
def play_order():
  if random.randint(0, 1) == 0:
    return 'human'
  return 'computer'


# winning combos [1,2,3],[4,5,6],[7,8,9],[1,4,7],[2,5,8],[3,6,9],[1,5,9],[3,5,7]
def check_win(board, mark):
  return (
    (board[1] == mark and board[2] == mark and board[3] == mark) or
    (board[4] == mark and board[5] == mark and board[6] == mark) or
    (board[7] == mark and board[8] == mark and board[9] == mark) or
    (board[1] == mark and board[4] == mark and board[7] == mark) or
    (board[2] == mark and board[5] == mark and board[8] == mark) or
    (board[3] == mark and board[6] == mark and board[9] == mark) or
    (board[1] == mark and board[5] == mark and board[9] == mark) or
    (board[3] == mark and board[5] == mark and board[7] == mark)
  )


def human_move(board):
  move = ' '
  while move not in ['1', '2', '3', '4', '5', '6', '7', '8', '9'] or not board[int(move)] == ' ':
    print("Choose your next move: (1-9)")
    move = input()
  return int(move)


# Pick a move for the computer if there are no immediate win/block moves
def pick_random_move(board, move_list):
  available_moves = []
  for i in move_list:
    if board[i] == ' ':
      available_moves.append(i)

  if len(available_moves) != 0:
    return random.choice(available_moves)
  return None


def copy_board(board):
  board_copy = []
  for i in board:
    board_copy.append(i)

  return board_copy


def computer_move(board, comp_mark, human_mark):
  # Check if there is a winning move
  for i in range(1, 10):
    copy = copy_board(board)
    if copy[i] == ' ':
      copy[i] = comp_mark
      if check_win(copy, comp_mark):
        return i

  # Check which move to block from human player
  for i in range(1, 10):
    copy = copy_board(board)
    if copy[i] == ' ':
      copy[i] = human_mark
      if check_win(copy, human_mark):
        return i

  if board[5] == ' ':
    return 5

  # Check if corners are availble
  move = pick_random_move(board, [1, 3, 7, 9])
  if move != None:
    return move

  return pick_random_move(board, [2, 4, 6, 8])


# Check for empty spaces on the board
def check_full_board(board):
  for i in range(1, 10):
    if board[i] == ' ':
      return False
  return True


def main_game():
  print("Let's play a game of Tic Tac Toe")
  while True:
    board = [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ', ' ']
    human_mark, comp_mark = mark_choice()
    turn = play_order()
    print(turn.capitalize(), 'will make a first move')
    play = True

    while play:
      if turn == 'human':
        show_board(board)
        move = human_move(board)
        board[move] = human_mark

        if check_win(board, human_mark):
          show_board(board)
          print("Congratulations! You are the winner!")
          play = False
        else:
          if check_full_board(board):
            show_board(board)
            print("It's a tie!")
            break
          turn = 'computer'
      else:
        move = computer_move(board, comp_mark, human_mark)
        board[move] = comp_mark

        if check_win(board, comp_mark):
          show_board(board)
          print("Computer is the winner")
          play = False
        else:
          if check_full_board(board):
            show_board(board)
            print("It's a tie!")
            break
          turn = 'human'

    print("Do you want to play another game? (y/n)")
    reply = input().lower()
    if reply.startswith('y'):
      continue
    print("Thank you for playing")
    break


if __name__ == '__main__':
  main_game()
