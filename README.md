# ConwaysWorld: Python Implementation of Conway's Game of Life
Conway's World is a Python implementation of Conway's Game of Life, a classic cellular automaton devised by the British mathematician John Horton Conway in 1970. This implementation utilizes the numpy library for grid manipulation and pygame for creating the graphical user interface (GUI) to play the game.

Conway's Game of Life
Conway's Game of Life is a zero-player game that takes place on an infinite two-dimensional grid of square cells. Each cell can be in one of two states: alive or dead. The game evolves in turns, according to the following rules:

- Underpopulation: Any live cell with fewer than two live neighbors dies, as if by underpopulation.
- Survival: Any live cell with two or three live neighbors lives on to the next generation.
- Overpopulation: Any live cell with more than three live neighbors dies, as if by overpopulation.
- Reproduction: Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.

These simple rules give rise to complex patterns and behaviors, including stable patterns, oscillators, and gliders that move across the grid.
## Double Pendulum Simulation
The Double Pendulum simulation is based on Lagrangian mechanics and utilizes the sympy library for symbolic calculations and matplotlib for plotting the movement of the pendulum.

![Conway's Game of Life](https://upload.wikimedia.org/wikipedia/commons/8/85/Galaxy%28Conway%27s_Game_of_Life%29.gif?20131230023026)

### Usage
#### 1. Ensure you have proper dependencies installed 
```python
pip install pygame numpy
```
#### 2. Running the game
```python
git clone https://github.com/Soham-xT/ConwaysWorld/blob/main/ConwaysWorld.py
cd ConwaysWorld
```
```python
python ConwaysWorld.py
```
#### 3. Playing the Game:
- Press Space to pause/resume the game.
- Use the mouse to select cells: left-click to make a cell alive (white), right-click to make a cell dead (black).
#### 4. Enjoy!

## Contributing: 
Any contributions that can potentailly improve the code are welcomed. Feel free to submit bug reports, feature requests, or pull requests to improve Conway's World.

## License
This project is licensed under the MIT License - see the LICENSE file for details.
Feel free to customize and expand upon this README to better suit your project's needs!
