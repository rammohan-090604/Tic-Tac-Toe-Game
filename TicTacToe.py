class TicTacToe:
    #Constructor to initialize the board while calling the TicTacToe
    def __init__(self, board_size=3):
        self.board_size = board_size
        self.board = [['_' for _ in range(self.board_size)] for _ in range(self.board_size)]
        self.players = ['X', 'O']
        self.current_player = self.players[0]
        self.game_running = True
    
    # Function to print the board
    def print_board(self):
        for row in self.board:
            for cell in row:
                print(cell, end = "|")
            print("")
    
    # Function to take input from the player and place their mark on the board
    def take_input(self):
        while True:
            print(f"Player {self.current_player}'s turn")
            x_coordinate = int(input(f"Enter row number (1-{self.board_size}): "))
            y_coordinate = int(input(f"Enter column number (1-{self.board_size}): "))
            
            if 1 <= x_coordinate <= self.board_size and 1 <= y_coordinate <= self.board_size:
                if self.board[x_coordinate - 1][y_coordinate - 1] == "_":
                    self.board[x_coordinate - 1][y_coordinate - 1] = self.current_player
                    break
                else:
                    print("That position is already taken. Please choose another.")
            else:
                print("Invalid coordinates. Please try again.")
    
    # Function to check if there's a winner
    def check_winner(self):
        # Check rows and columns
        for i in range(self.board_size):
            if all(self.board[i][j] == self.current_player for j in range(self.board_size)) or \
               all(self.board[j][i] == self.current_player for j in range(self.board_size)):
                return True
        
        # Check diagonals
        if all(self.board[i][i] == self.current_player for i in range(self.board_size)) or \
           all(self.board[i][self.board_size - 1 - i] == self.current_player for i in range(self.board_size)):
            return True
        
        return False
    
    def is_board_full(self):
        # Function to check if the board is full
        for row in self.board:
            if "_" in row:
                return False
        return True
    
    def play_game(self):
        # Main game loop
        while self.game_running:
            self.print_board()
            self.take_input()
            
            if self.check_winner():
                self.print_board()
                print(f"Player {self.current_player} wins!")
                self.game_running = False
            elif self.is_board_full():
                self.print_board()
                print("It's a draw!")
                self.game_running = False
            else:
                # Switch player
                self.current_player = self.players[1] if self.current_player == self.players[0] else self.players[0]

if __name__ == "__main__":
    print("Let's play Tic Tac Toe!")
    board_size = int(input("Enter the board size : "))
    game = TicTacToe(board_size)
    game.play_game()
