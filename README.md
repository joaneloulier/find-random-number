For this README, I used alec-chernicki template : https://github.com/alec-chernicki/portfolio-template

# Find a random number between 1 and 100
The goal of this game is to guess a number between 1 and 100, a random number generated upon launching the app, or when you hit replay.


## Installation:

```bash
# Clone the repo
git clone https://github.com/joaneloulier/find-random-number.git
cd trouve-le-nombre

# Create a virtual environment
python -m venv .venv
source .venv/bin/activate  # Linux/macOS
# .venv\Scripts\activate   # Windows

# Install the package in dev mode
pip install -e .
```

## Usage:

After installing, you can launch the game in two ways:

```bash
# Via the installed command
trouve-le-nombre

# Or via the Python module
python -m trouve_le_nombre
```


## How It's Made:

**Tech used:** Python, PySide6

I decided to build an app using Python and PySide6 / Qt Framework. My goal was to showcase the skills acquired during my internship within a much simpler app.

The logic is organized in four parts : 
- the tabs (the login tab, the game tab and the result tab).
- signals.py : all of the signals used to communicate between the different instances, I used a Singleton (maybe not necessary).
- workers.py : the functions that connect the gui to the backend, orchestrates the reception of the number then runs the backend to know if the number is the same one.


## Lessons Learned:

I perfected my learning of PySide6, PyQt, of packaging for pip but also deepened my understanding of Application design.
I had to think about how to make my app the most efficiently possible and it was really fun to design.

A note : I chose this little game because when I learnt Python back in highschool I made little programs to entertain my little brothers (without an interface) and "Guess the number" was their favorite.
