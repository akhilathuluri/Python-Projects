The program is an implementation of a slot machine game that allows the user to deposit money and play multiple rounds. The game involves spinning a slot machine and checking if the symbols in the machine match up in a specific pattern.

## The following concepts are used in this program:

- Input/output: The program prompts the user for input to deposit money and place bets, and displays the results of each spin.
- Variables: The program uses variables to keep track of the game state, such as the player's balance and the symbols and their values.
- Data structures: The program uses a list to represent the columns in the slot machine and a dictionary to store the count and value of each symbol.
- Functions: The program defines several functions, including check_winnings, get_slot_machine_spin, print_slot_machine, deposit, get_number_of_lines, get_bet, and spin. These functions help to organize the program and perform specific tasks.
- Control flow: The program uses loops and conditional statements to control the flow of the game and ensure that the user inputs valid values.
- Randomness: The program uses the random module to randomly select symbols for each column in the slot machine.


# Slot Machine Game Documentation
## Game Overview
This is a simple slot machine game where players can place bets on multiple lines and spin the slot machine. The game is played on a 3x3 grid with symbols randomly generated each time the player spins. If the symbols match on a winning line, the player will win money based on the value of the symbols and their bet.

## Game Rules

1. The player must deposit money to play the game.
2. The player can bet on up to 3 lines, and can adjust their bet per line.
3. The player must have enough balance to place the bet.
4. The player spins the slot machine to generate random symbols.
5. If the symbols match on a winning line, the player will win money based on the value of the symbols and their bet.
6. The game ends when the player chooses to quit or when their balance is 0.

## Code Overview

1. **check_winnings(columns, lines, bet, values)** - This function checks if there are any winning lines in the provided columns. If there is a winning line, it calculates the winnings based on the value of the symbols and the player's bet.

2. **get_slot_machine_spin(rows, cols, symbols)** - This function generates a 3x3 grid of symbols based on the provided symbols and their respective counts.

3. **print_slot_machine(columns)** - This function prints the provided columns in a slot machine-like format.

4. **deposit()** - This function prompts the player to deposit money and returns the amount as an integer.

5. **get_number_of_lines()** - This function prompts the player to select the number of lines they want to bet on and returns the selected number as an integer.

6. **get_bet()** - This function prompts the player to select their bet amount and returns the selected amount as an integer.

7. **spin(balance)** - This function executes a single spin of the slot machine based on the player's input. It generates the slot machine symbols, prints the slot machine, checks for winning lines, calculates the winnings, and returns the difference between the winnings and the total bet.

8. **main()** - This function runs the main game loop. It prompts the player to deposit money, allows the player to spin the slot machine, updates the player's balance, and ends the game when the player chooses to quit or their balance is 0.

## Game Configuration

- MAX_LINES - The maximum number of lines the player can bet on.
- MAX_BET - The maximum amount the player can bet per line.
- MIN_BET - The minimum amount the player can bet per line.
- ROWS - The number of rows in the slot machine.
- COLS - The number of columns in the slot machine.
- symbol_count - A dictionary of symbol names and their respective counts in the game.
- symbol_values - A dictionary of symbol names and their respective values in the game.
