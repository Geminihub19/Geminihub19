# Function to print the board
def print_board(board):
    print("\n")
    for i in range(3):
        print(" | ".join(board[i]))
        if i < 2:
            print("---------")
    print("\n")

# Function to check for a winner
def check_winner(board, player):
    # Check rows, columns and diagonals
    for i in range(3):
        if all([cell == player for cell in board[i]]):  # Check row
            return True
        if all([board[j][i] == player for j in range(3)]):  # Check column
            return True
    if all([board[i][i] == player for i in range(3)]):  # Check diagonal
        return True
    if all([board[i][2-i] == player for i in range(3)]):  # Check anti-diagonal
        return True
    return False

# Function to check if the board is full
def is_board_full(board):
    return all([cell != " " for row in board for cell in row])

# Main game function
def tic_tac_toe():
    # Initialize the game board
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"
    
    # Game loop
    while True:
        print_board(board)
        print(f"Player {current_player}'s turn:")
        
        # Get the player's move
        try:
            row, col = map(int, input("Enter row and column (0-2) separated by space: ").split())
            if board[row][col] != " ":
                print("Cell is already occupied, try again.")
                continue
        except (ValueError, IndexError):
            print("Invalid input, please enter row and column as two numbers between 0 and 2.")
            continue
        
        # Place the player's mark
        board[row][col] = current_player
        
        # Check if the current player wins
        if check_winner(board, current_player):
            print_board(board)
            print(f"Player {current_player} wins!")
            break
        
        # Check if the board is full (tie game)
        if is_board_full(board):
            print_board(board)
            print("It's a tie!")
            break
        
        # Switch players
        current_player = "O" if current_player == "X" else "X"

# Run the game
tic_tac_toe()
