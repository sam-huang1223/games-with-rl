# Let's play with Reinforcement Learning

[Table of Contents PLACEHOLDER]

## Overview

### Setup
[PLACEHOLDER]

## Goals
1. Practice implementing basic RL algorithms
2. Practice incorporating Python programming best practices
3. Practice object-oriented programming by developing game environments
4. Profit???

## Roadmap
1. Implement Connect4 game environment
2. Set up Table of Contents
3. Implement QLearning algorithm (traditional table-based version)
4. Think through implementation of Ultimate TicTacToe (potentially much more complex than Connect4)

## Changelog
*April 20, 2018*
* Consolidation of progress made

*April 21, 2018*
* Challenge: Recursively populate game board (goal: to allow for efficient implementation of heuristic evaluation compared to old Connect4 implementation) -> every recursion nodes are creating new neighboring nodes to connect to -> MaximumRecursionExceed error as program loops through board creating neighbors to connect to -> need to find a way to allow nodes to check if other neighbors already created the neighboring nodes, then if so, connect to them.
* Combined _get_neighbors and _propagate -> more efficient to recurisvely generate board while checking for neighbors

