import os
from pathlib import Path
import sqlite3
import datetime
time = datetime.datetime.now()

# print(__file__)
# print(os.path.join(os.path.dirname(__file__), '..'))
# print(os.path.dirname(os.path.realpath(__file__)))
# print(type(os.path.abspath(os.path.dirname(__file__))))

first_turn: bool = True
current_directory: Path = Path(__file__).parent.absolute()
save_directory: Path = current_directory / 'current_game.db'
conecction = sqlite3.connect(save_directory)
cursor = conecction.cursor()
table_name: str = f"Game({time})"

print(type(table_name))

command = f"CREATE TABLE {table_name} (Turn INTEGER, Players INTEGER, Current_Player INTEGER, Player_Move TEXT, isWinner TEXT)"

cursor.execute(command)
        