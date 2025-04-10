# Import assests from the ABC. Includes Board_State, Move, and Grid_Game
from Grid_GameABC import *

class TTT_Board(Board_State):
    def __init__(self, turn = 1, current_player = 1, moves_played = None, player_count = 2, is_winner = False):
        super().__init__(turn, current_player, moves_played, player_count, is_winner)

class tic_tac_toe(Grid_Game):
    """Implements the Tic-Tac-Toe game logic and interface using tkinter."""

    def __init__(self):
        super().__init__()

        # Find out where we are.
        self.save_directory: Path = Path(self.resource_path('game/saves/saved_games.db'))
        self.log_directory: Path = Path(self.resource_path('lib/tttgame.log'))
        self.image_assets_directory: Path = Path(self.resource_path('game/images/')).absolute()

        # Start logger
        self.current_time = datetime.datetime.now()
        self.logger = logging.getLogger(__name__)
        logging.basicConfig(filename= str(self.log_directory), encoding='utf-8', level=logging.INFO)
        self.logger.info(f"{self.current_time} - New game started")        

        # Post paths to logfile for debug.
        self.logger.info(f"{self.current_time} - Path to working directory : {str(self.resource_path)}")
        self.logger.info(f"{self.current_time} - Path to save files : {str(self.save_directory)}")
        self.logger.info(f"{self.current_time} - Path to log files : {str(self.log_directory)}")
        self.logger.info(f"{self.current_time} - Path to image files : {str(self.image_assets_directory)}")

        # SQLite setup
        # save_file = open(self.save_directory, "r")
        # self.connection = sqlite3.connect(str(self.save_directory))
        # self.cursor = self.connection.cursor()
        # self.table_name: str = f"Game({})"

        # Define board boundaries and create current_board object. 
        # These vairables drive all the logic, so if you want to play a 10 x 10 game of TTT, you can.
        self.x_max = 3
        self.y_max = 3
        self.win_length = 3
        self.current_board: TTT_Board = TTT_Board()

        # Create interface objects using tkinter.
        self.root = Tk()
        self.root.title("Tic-Tac-Toe")

        # Layout will use three frames, main frame will have the game grid as it's child so that we can pull x, y co-ords off it for logic.
        
        # Top frame for logo.
        self.top_frame = Frame(self.root)
        self.top_frame.grid(row=0, column=0, columnspan=self.x_max, sticky='N')
        logo_image = PhotoImage(file=self.image_assets_directory / 'ttt_logo.png')
        self.logo = ttk.Label(self.top_frame, image= logo_image)
        self.logo.grid(row= 0, column=0, columnspan=self.x_max, sticky='N' )        
        
        # Main frame for game elements with m x n grid to contain ttt buttons.
        self.main_frame = Frame(self.root)
        self.main_frame.grid(row=1, column=0, columnspan=self.x_max, sticky=(N,W,E,S), padx=20)
        # self.main_frame.columnconfigure(0, weight=1)
        # self.main_frame.rowconfigure(0, weight=1)

        self.buttons = []
        for y_grid in range(self.y_max):
            row_of_buttons = []
            for x_grid in range(self.x_max):
                button = Button(
                    self.main_frame, text="",font=("Helvetica", 20), width=5, height=2,
                    command=lambda x=x_grid, y=y_grid: self.game_loop_onclick(x, y)
                )
                button.grid(row=y_grid, column=x_grid)
                row_of_buttons.append(button)
            self.buttons.append(row_of_buttons)

        # Bottom frame for messages and game control buttons.
        self.bottom_frame = Frame(self.root)
        self.bottom_frame.grid(row=3, column=0, columnspan=self.x_max, sticky='N' )
        
        # Create message label and reset button
        self.message_label = Label(self.bottom_frame, text="Player 1's turn", font=("Helvetica", 12))
        self.message_label.grid(row=0, column=0, columnspan=self.x_max, sticky='N', pady=10)
        
        # Create Reset button.
        self.reset_button = Button(self.bottom_frame, text="Reset", command=self.reset_game)
        self.reset_button.grid(row=1, column=0, columnspan=self.x_max, sticky='N', pady=10)

        # Start GUI mainloop.
        self.root.mainloop()


    def game_loop_onclick(self, x_dim, y_dim) -> None:

        move = self.player_move(x_dim, y_dim)
        updated_board = self.update_board_state(self.current_board, move)
        updated_board = self.check_win_condition(updated_board)
        self.game_record(updated_board)
        self.choose_next_player(updated_board)

        if updated_board.is_winner:
            self.message_label.config(text=f"Player {self.current_board.current_player} wins!")
        elif updated_board.is_tie:
            self.message_label.config(text="It's a tie!")
        else:
            self.message_label.config(text=f"Player {updated_board.current_player}'s turn")

        self.current_board = updated_board
        

    def reset_game(self):
        """Resets the game state and UI to start a new game."""
        
        # TODO Save game using game_record and start new record.
        
        self.current_board = TTT_Board()
        for y in range(self.y_max):
            for x in range(self.x_max):
                self.buttons[y][x]["text"] = ""
                self.buttons[y][x]["state"] = "normal"
        self.message_label.config(text="Player 1's turn")

    def game_record(self, board_update: TTT_Board) -> bool:
        # TODO make this.
        return True


    def player_move(self, x_dim, y_dim, piece: tuple = None) -> Move:

        self.buttons[y_dim][x_dim]["state"] = "disabled"
        self.buttons[y_dim][x_dim]["text"] = "X" if self.current_board.current_player == 1 else "O"
        
        return Move(self.current_board.current_player, [x_dim, y_dim])


    def update_board_state(self, old_board: TTT_Board, played_move: Move) -> TTT_Board:
        
        new_board_vectors: dict = old_board.board_vectors.copy()
        new_board_vectors[f"Turn {old_board.turn}"] = played_move
        return TTT_Board(
            turn=old_board.turn,
            current_player=old_board.current_player,
            moves_played=new_board_vectors
        )


    def check_win_condition(self, current_board: TTT_Board) -> TTT_Board:

        directions = [
            (-1, -1), (-1, 0), (-1, 1),
            (0, -1),           (0, 1),
            (1, -1),  (1, 0),  (1, 1)
        ]

        for move in current_board.position_map.keys():
            player = current_board.position_map[move]
            for dx, dy in directions:
                length = 1

                pos_direction = (move[0] + dx, move[1] + dy)
                while pos_direction in current_board.position_map and current_board.position_map[pos_direction] == player:
                    length += 1
                    self.logger.debug(f"Checking length in direction ({dx}, {dy}) -> {length}")
                    pos_direction = (pos_direction[0] + dx, pos_direction[1] + dy)

                neg_direction = (move[0] - dx, move[1] - dy)
                while neg_direction in current_board.position_map and current_board.position_map[neg_direction] == player:
                    length += 1
                    self.logger.debug(f"Checking length in direction ({dx}, {dy}) -> {length}")
                    neg_direction = (neg_direction[0] - dx, neg_direction[1] - dy)

                if length >= self.win_length:
                    current_board.is_winner = True

        # Check for tie after all win conditions are verified, if all spaces are filled and there's no winner, that's a tie.
        if not current_board.is_winner and len(current_board.position_map) == self.x_max * self.y_max:
            for y_dim in range(self.y_max):
                for x_dim in range(self.x_max):
                    self.buttons[y_dim][x_dim]["state"] = "disabled"
            current_board.is_tie = True
            self.logger.debug(f"Tie check True")
            return current_board

        # Check for winner after all win conditions and  are verified
        if current_board.is_winner:
            for y_dim in range(3):
                for x_dim in range(3):
                    self.buttons[y_dim][x_dim]["state"] = "disabled"
            self.logger.debug(f"Win check true")
            return current_board

        return current_board


if __name__ == "__main__":
    time = datetime.datetime.now()
    test_game = tic_tac_toe()
    logging.info(f"{datetime.datetime.now()} - Game executed successfully.")
