# rps-starter

A Starter Repository for the [Rock Paper Scissors Exercise](https://github.com/prof-rossetti/intro-to-python/blob/main/exercises/rock-paper-scissors/README.md).

# Setup the Repo

Create a virtual environment:

```sh
conda create -n rps-env python=3.8
```

Activate the virtual environment:

```sh
conda activate rps-env
```

Install package dependencies (mainly for testing):

```sh
pip install -r requirements.txt
```
# Pass Environment Variable 

## Option 1: Command Line (Terminal) 
```sh
PLAYER_NAME = "Your Name" python game.py
```
ex) PLAYER_NAME = "Clare" python game.py

## Option 2: Create an ".env." file in your repository
```sh
PLAYER_NAME = "Your Name" 
```
ex) PLAYER_NAME = "Clare" 

Update Requirements.txt 

```sh
python-dotenv
```

In your game.py file, 

```sh
from dotenv import load_dotenv
```

```sh
load_dotenv()
    player_name = os.getenv("PLAYER_NAME", default = "Player One")
```

## Usage

Run the rock paper scissors game:

```sh
PLAYER_NAME = "Clare" python game.py
```

## Testing

Run tests:

```sh
pytest
```

