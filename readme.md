### Tic Tac Toe Game with Python and Tkinter GUI

#### Project Overview

This project is a graphical implementation of the classic Tic Tac Toe game, created using Python and the Tkinter library for the graphical user interface (GUI). The game provides a simple and intuitive interface for two players to enjoy the classic 3x3 grid game on a single computer.

#### Features

- **Interactive GUI**: The game board is displayed using Tkinter buttons, providing a clean and interactive user experience.
- **Player Turn Display**: A label shows the current player's turn, helping players keep track of whose move it is.
- **Win and Draw Detection**: The game automatically detects when a player wins or when the game ends in a draw, displaying appropriate messages.
- **Reset Functionality**: Players can reset the game board at any time to start a new game, without restarting the application.
- **Visual Feedback**: The buttons change color based on the player (X or O), enhancing the visual feedback and user experience.

#### Technical Details

- **Language**: Python
- **Libraries**: Tkinter (for GUI)
- **Game Logic**: Implemented using simple list operations and conditional checks to determine wins and draws.
- **GUI Layout**: The layout is structured using Tkinter frames, with the game board, turn indicator, and reset button organized for easy interaction.

#### How to Play

1. **Start the Game**: Launch the application to see the game board and the initial turn indicator.
2. **Make a Move**: Click on any empty button on the 3x3 grid to place your marker (X or O).
3. **Check for Win/Draw**: The game will automatically check for a win or draw after each move and display a message if the game ends.
4. **Reset the Game**: Click the "Reset" button to clear the board and start a new game.

#### Installation and Setup

1. **Install Python**: Ensure Python is installed on your machine.
2. **Install Tkinter**: Tkinter is included with Python standard library, but if needed, install it using `pip install tk`.
3. **Run the Game**: Execute the Python script to start the game.

#### Code Structure

- **Logic Part**: Contains the game logic, including functions to check for a win, check for a draw, handle button clicks, and toggle turns.
- **GUI Part**: Contains the code to set up the Tkinter GUI, including the creation of buttons, frames, and labels.

#### Conclusion

This Tic Tac Toe project demonstrates the integration of game logic with a graphical user interface, providing a fun and interactive way to play a classic game. It serves as a great example of using Python and Tkinter to create simple yet engaging applications.