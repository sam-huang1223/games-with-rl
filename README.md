# Let's play with Reinforcement Learning

Welcome to my primary project for the summer of 2018. I'm super excited to learn more about RL while developing some interesting game environments

### Table of Contents
[Setup Instructions](#setup-instructions)

[Goals](#goals)

[Roadmap](#roadmap)

[Changelog](#changelog)

&nbsp;&nbsp;&nbsp;&nbsp;[April 20, 2018](#april-20-2018)

&nbsp;&nbsp;&nbsp;&nbsp;[April 21, 2018](#april-21-2018)


## Setup Instructions
**Follow instructions below to allow for visualization of game environments**
1. Install required visualization package
> pip install pydotplus
2. Install the GraphViz backend using the installer found in the install_files folder. If the installation directory is not 'C:/Program Files (x86)/Graphviz2.38/bin/', then modify the GRAPHVIZ_BIN_PATH variable in config.py

## Goals
1. Practice implementing basic RL algorithms
2. Practice incorporating Python programming best practices
3. Practice object-oriented programming by developing game environments
4. Profit???

## Roadmap
1. Implement Connect4 game environment
2. Implement QLearning algorithm (traditional table-based version)
3. Think through implementation of Ultimate TicTacToe (potentially much more computationally complex than Connect4)

## Changelog
##### *April 20, 2018*
* Consolidation of progress made

##### *April 21, 2018*
* Challenge #1: Recursively populate game board (goal: to allow for efficient implementation of heuristic evaluation compared to old Connect4 implementation) -> every recursion nodes are creating new neighboring nodes to connect to -> MaximumRecursionExceed error as program loops through board creating neighbors to connect to -> need to find a way to allow nodes to check if other neighbors already created the neighboring nodes, then if so, connect to them.
* Combined _get_neighbors and _propagate -> more efficient to recurisvely generate board while checking for neighbors

##### *April _, 2018*
