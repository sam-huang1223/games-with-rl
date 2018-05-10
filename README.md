# Let's play with Reinforcement Learning

Welcome to my primary project for the summer of 2018. I'm super excited to learn more about RL while developing some interesting game environments.

### Table of Contents
[Setup Instructions](#setup-instructions)

[Goals](#goals)

[Roadmap](#roadmap)

[Changelog](#changelog)

&nbsp;&nbsp;&nbsp;&nbsp;[April 20, 2018 - The Beginning](#april-20-2018)

&nbsp;&nbsp;&nbsp;&nbsp;[April 21, 2018 - Graph not Array](#april-21-2018)

&nbsp;&nbsp;&nbsp;&nbsp;[May 10, 2018 - Visualizing as a Graph](#may-10-2018)


## Setup Instructions
**Follow instructions below to allow for visualization of game environment**
1. Install required package
> pip install bokeh

**Follow instructions below to allow for visualization of game trees**
1. Install required package
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
*The Beginning*
* Consolidation of progress made

<br>

##### *April 21, 2018*
*Graph not Array*
* **Challenge #1**: Recursively build graph-based game board
    
    **Goal**: To allow for efficient implementation of heuristic evaluation compared to old array-based Connect4 implementation)

    **Problem**: Every recursion, nodes are creating new neighboring nodes to connect to

    &rarr; MaximumRecursionExceed error as program infinitely loops through board creating neighbors to connect to

    &rarr; Need to find a way to allow nodes to check if other neighbors already created neighboring nodes, then if so, connect to them

* Combined _get_neighbors and _propagate &rarr; more efficient to recursively generate the board *while* checking for existence of neighbors instead of *after*

<br>

##### *May 10, 2018*
*Visualizing as a Graph*
* **Challenge #2**: Design a generalizable method for visualizing game environments 

    **Goal**: Minimize code repetition and practice writing modular code
    
    **Problem**: After writing the algorithm for parsing data and implementing the graph visualization, I realized that the PyDotPlus graph visualization library  cannot display the graph in any understandable way. Lack of control over node positioning means that I cannot faithfully replicate the Connect4 board - or any other structured game environment. Time to find another approach
    
* Moved testing code to separate folder (+1 for modularity!!) - run "pytest" on command line to execute tests

<br>

##### *May _, 2018*
*Visualize on a Graph*