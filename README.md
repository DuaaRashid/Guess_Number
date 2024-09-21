# Guess The Number Game

This project is a simple **Guess The Number** game written in Python. The user must guess a randomly generated number between 1 and 50. The game includes two difficulty levels: *Easy* (10 attempts) and *Hard* (5 attempts).

## How It Works

1. **Difficulty Selection**: The player chooses their difficulty level:
   - Easy: 10 attempts to guess the correct number.
   - Hard: 5 attempts to guess the correct number.
   
2. **Guessing Process**: 
   - The program randomly selects a number between 1 and 50.
   - The player inputs a guess, and the program provides feedback on whether the guess is too high or too low.
   - The player continues guessing until they either guess the correct number or run out of attempts.
   
3. **Win/Loss Conditions**:
   - The player wins if they guess the number correctly within the allowed number of attempts.
   - The player loses if they run out of attempts before guessing the correct number. In this case, the program reveals the correct number.

## Usage

### Clone the repository

```bash
git clone https://github.com/yourusername/guess-the-number-game.git
cd guess-the-number-game
```

### Run the game

```bash
python guess_the_number.py
```

## Example Gameplay

```bash
     *Guess The Number Game* 
What's your level? 
1. Easy 
2. Hard 
1
You have 10 attempts to guess the number.
Guess the number between 1 to 50: 25
Your guess 25 is too low. Guess again, you have 9 attempts left.
Guess the number between 1 to 50: 40
Your guess 40 is too high. Guess again, you have 8 attempts left.
Guess the number between 1 to 50: 35
Congratulations! Your guess 35 is correct.
```

If the player runs out of attempts, the game will display the correct number and end.

## Requirements

- Python 3.x

## License

This project is licensed under the MIT License.
