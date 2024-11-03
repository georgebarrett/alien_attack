# alien_attack

i hope you survive this text-based, Alien inspired, adventure game

# requirements

python 3.8+
refer to requirements.txt for packages

# playing it!

https://github.com/georgebarrett/alien_attack

then in the terminal - git clone https://github.com/yourusername/alien_attack.git

cd into alien_attack

create a virtual environment: python -m venv venv

activate the environment: source venv/bin/activate

install dependencies with: pip install -r requirements.txt

# PLAY THE GAME!

whilst still in the terminal run: python main.py
follow the prompts
and press control-c to exit if it is too tense!

# testing

in the terminal, cd into alien_attack and run: pytest
for a more verbose visual representation of the test coverage run: pytest -v 

# things that went right

i am plesed with the end result of the game
i challenged myself by writing the game in python, which is my second language after js
i found contructing the classes to be fun
i am pleased that the game is tested, especially as mocking is difficult
i am pleased with the file structure of the game
i am pleased i followed industry standards like creating a virtual environment, having a requirements.txt and using a .gitignore

# things that went wrong

i found following a TDD approach difficult at times. especially as i wanted to follow a top down approach with making the game
i found that i was returning things rather than 'putsing' them to the console, this lead to rewriting tests and methods
i did not check the terminal enough to ensure i was getting the right outputs. upon reflection this was due concentrating too much on writing code
the testing was challenging, especialy engine.py
i think my mindset was one of a software developer and not a game developer
usually i write a test, run it red, make the method/function, run the test green, then commit. i found i lost this pattern at times. maybe due to it being a game and not a web app

# improvements

i love the potential that working with data has
i would have liked to introduce more scenes into the game with Codewars Kata esq problems
the output in the console could look neater
more robust test coverage
