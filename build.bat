REM Run PyInstaller with assets
pyinstaller --windowed --onedir ^
  --name "TicTacToe" ^
  --add-data "game/saves/saved_games.db;game/saves" ^
  --add-data "game/images/ttt_logo.png;game/images" ^
  --add-data "lib/tttgame.log;lib" ^
  main.py