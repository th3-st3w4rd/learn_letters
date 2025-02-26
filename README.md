# learn_letters
This is a little CLI game to help kids practice reading capital/lowercase letter, symbols,
numbers, and get them used to a keyboard. This game is NOT meant for kids to play by themselves, because of it's technical implimentation...but it's really helpful for techy parents, family, or caregivers to sit down and help thier kids figure out how to recognize and match letters.

The game also keeps track of how many correct and incorrect answers were given. Maybe parents
could relate prizes to how many attempts the child tried.
## Gameplay, Commands, & Usage
usage:  
python (or python3) learn_letters.py -l -L -n -s

Practice typing, reading, and matching letters & symbols.

options:  
  -h, --help           show this help message and exit  
  -l, --lower-letters  Includes 'lowercase letters' when loading the game.  
  -L, --upper-letters  Includes 'uppercase letters' when loading the game.  
  -n, --numbers        Includes 'numbers' when loading the game.  
  -s, --symbols        Includes 'symbols' when loading the game.  

During the game, enter -- to quit and end the game.

### Examples:
#### To practice learning uppercase letters and numbers on a Windows PC:

python learn_letters.py -Ln  
python learn_letters.py --upper-letters --numbers  
python learn_letters.py -n --upper-letters  

\* Any combination of the above options/switches will work the same.
#### To practice lowercase, symbols, and uppercase letters on a Linux PC:

python3 learn_letters.py -lsL  
python3 learn_letters.py --lower-letters --symbols --upper-letters  
python3 learn_letters.py -Ls --lower-letters  

\* Any combination of the above options/switches will work the same.
## Future Improvements
- [ ] Create more congratualtions statements.
- [ ] Create more better luck next time statements.
- [ ] Create a better points system, rewarding trying over performance.
- [ ] Create better CLI layout (Mock GUI)
- [ ] Put more life into G34r-B0lt.
- [ ] Create levels of difficulty, to include whole words and sentences.
- [x] Use argparse to setup game settings.
- [x] Create narrator \(G43r-B0lt\).
