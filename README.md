# ROCK-PAPER-SCISSORS-GAME

# Local Environment Setup

## Prerequisites

  + Anaconda 3.7+
  + Python 3.7+
  + Pip

## Installation

Fork this [remote repository](https://github.com/prof-rossetti/my-first-python-app) under your own control, then "clone" or download your remote copy onto your local computer.

Then navigate there from the command line (subsequent commands assume you are running them from the local repository's root directory):

```sh
cd my-first-python-app
```

Use Anaconda to create and activate a new virtual environment, perhaps called "my-first-env":

```sh
conda create -n my-first-env python=3.8
conda activate my-first-env
```

After activating the virtual environment, install package dependencies (see the ["requirements.txt"](/requirements.txt) file):

```sh
pip install -r requirements.txt
```

> NOTE: if this command throws an error like "Could not open requirements file: [Errno 2] No such file or directory", make sure you are running it from the repository's root directory, where the requirements.txt file exists (see the initial `cd` step above).

## Setup

In the root directory of your local repository, create a new file called ".env", and update the contents of the ".env" file to specify your desired username (then make sure to SAVE the ".env" file aftwards):

Update your program to allow the user to configure their own player name by passing an environment variable called "PLAYER_NAME" stored in a local ".env" file.

    PLAYER_NAME= "MAAHIRA"

> NOTE: the ".env" file is usually the place for passing configuration options and secret credentials, so as a best practice we don't upload this file to version control (which is accomplished via a corresponding entry in the [".gitignore"](/.gitignore) file). This means we need to instruct each person who uses our code needs to create their own local ".env" file.

## Usage

*Run the Python script: python game.py

*Choose either 'rock', 'paper' or 'scissors' when prompted

> NOTE: 
> If you want to play again, run the python script: python game.py
> If your choice is invalid, the computer will not be able to determine a result of the game and will instead tell you that your choice is invalid (ensure you are typing in lowercase). 
> If you want to exit the game, run the command: exit ()

