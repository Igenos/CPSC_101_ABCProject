from lib.Grid_GameABC import Grid_Game, Board_State
from abc import ABC, abstractmethod
import sqlite3
import datetime

from pathlib import Path

class tic_tac_toe(Grid_Game):

    def __init__(self):
        self.first_turn: bool = True
        self.current_directory: Path = Path(__file__).parent.absolute()
        self.save_directory: Path = self.current_directory / 'current_game.db'
        self.conecction = sqlite3.connect(self.save_directory)
        self.cursor = self.conecction.cursor()
        self.table_name: str = f"Game({time})"

    def start_game(self) -> bool:
        """This function holds the logic of game progression and recursively calls itself until game end"""

        if self.first_turn == True:
            if setup_board():
                if 

    def setup_board(self) -> list[tuple]:
        # initial_values: list[tuple] = [("Turn", 1),
        #                                ("Number_Players",2),
        #                                ("Current_Player",None),
        #                                ("Player_Move",None),
        #                                ("isWinner",False),
        #                                ]
        
        #"CREATE TABLE <table name> (<column> <type>, <column2> <type>, )"
        self.cursor.execute(f"CREATE TABLE {self.table_name} (Turn INTEGER, Players INTEGER, Current_Player INTEGER, Player_Move TEXT, isWinner BOOLEAN)")
        
        
        return True



    def game_record(self, board_update: list[tuple]) -> bool:
        for column, value in enumerate(board_update):
        


choose_next_player(last_player: int) -> int
A function that takes the last player as an arg and returns the next player, or returns the first player if the first_move flag is True.
player_move(board_state) -> board_state
A function that takes the current board state as an arg and returns a move. This contains all the logic or options that agent has available to them.
update_board_state(board_state) -> board_state
A function that takes a player move and the current board state as args, verifies their validity, then returns a new immutable board state object that stores all the vectors for the spaces and the move argument it was originally passed. It will have the turn number in it's name and that will be stored in the Game Record.
check_win_condition(board_state) -> bool
A function that checks the board state against the defined end conditions and returns either a player or False.
progress_game(bool) -> None
Chooses either to progress to the next turn or do something else at game end.

if __name__ == "__main__":
    time = datetime.datetime.now()
    # print(time)
    print("It worked.")