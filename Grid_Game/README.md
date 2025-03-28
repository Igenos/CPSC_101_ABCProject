# Description

- **Grid_Game (Root Directory):**  
  This folder is the parent directory for the project. When using the template, rename it appropriately.

- **game/**  
  Houses all assets required by the game:
  - **cache/**: For temporary files generated during game operations.
  - **gui/**: Contains GUI dependencies and components.
  - **images/**: All graphics and visual elements.
  - **audio/**: Sound files utilized within the game.
  - **saves/**: Stores game save files, following a naming convention like `saved_game_001.txt`, which record the game state.

- **lib/**  
  Contains the implementation of the `Grid_Game` Abstract Base Class along with any supporting modules necessary for game functionality.

- **game.py:**  
  The main entry point for launching the game. This script initializes and runs the game using the ABC defined in the `lib` directory.

- **game.exe:**  
  A compiled version of the game, created after project completion. This version is useful for distribution and deployment.

- **log.txt:**  
  Logs runtime messages and errors to assist with debugging and monitoring the game’s execution.

## Build and Deployment

- **Compiling the Game:**  
  Instructions for generating `game.exe` from `game.py` will be provided here or in an accompanying build documentation file.

- **Running the Game:**  
  During development, you can run the game with:
  
  ```bash
  python game.py
