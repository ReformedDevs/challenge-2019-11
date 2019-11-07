# The Reformed Devs Monthly Challenge

## November 2011

### Background

Birthed out of our Slack org, The Reformed Devs have begun monthly coding challenges for its members, hoping to encourage critical thinking and problem and solving and foster community. You can see our previous challenges here:

* [April 2019](https://github.com/plusuncold/longest-word-test)
* [May 2019](https://github.com/plusuncold/rainfall-calc-challenge)
* [June 2019](https://github.com/ReformedDevs/challenge-2019-06)
* [July 2019](https://github.com/ReformedDevs/challenge-2019-07)
* [September 2019](https://github.com/ReformedDevs/challenge-2019-09)
* [October 2019](https://github.com/ReformedDevs/challenge-2019-10)

### This Month's Challenge

#### Problem

The goal of this month's challenge is to play the _most perfect_ game of Plantaingram.
In Plantaingram, the not-coprighted version of Bananagram, the goal is to place 
tiles to create words, similarly to Scrabble, but without a board or scoring. 
​
The game will play out as follows:
​
- Each program will take a string of ascii, upper case letters as input
- The first 21 letters will be taken from this string
- The program will choose to either "play" these letters from the "hand" onto the "board" or alternatively put one letter from the "hand" into the back of the "tile" queue and select three new "tiles" from the front of the queue
- If "tiles" are "played" to the "board" then one new "tile" is taken from the front of the queue
- The game will continue in this manner, "playing" words onto the "board" or
  alternatively taking "tiles" from the queue until the queue and "hand" are empty (ie all 144 "tiles" are on the board)
- If at anytime during the course of the game the "hand" is entirely empty 21 new "tiles" will be selected from the queue. If the queue has fewer than 21 "tiles" then all remaining "tiles" in the queue will be added to the "hand"
- During each turn "tiles" on the board can be rearranged as needed, but no "tile" which has been "played" to the "board" can be removed back to the "hand" or queue.
​
## Tiles
​
Bananagrams contains the following number of tiles in the "BUNCH":
```
2: J, K, Q, X, Z
3: B, C, F, H, M, P, V, W, Y
4: G
5: L
6: D, S, U
8: N
9: T, R
11: O
12: I
13: A
18: E
```

#### Output

Once your program has finished the game the following will need to be returned to STDOUT:
```
Github Name, Program Language, Total Time (in ms), Rounds Taken, Notes
[ASCII String presenting the final state of your board]
```
​
##### Total time:
​
Timer starts _immediately_. In C, this would mean the first line of `main()` would be the initiation of the timer.
​
##### Rounds taken:
​
A round is measured a one of two actions:
1) A word played, and new tile(s) picked up
2) A "split" -- one tile "put back" and three new tiles "picked up"
​
##### ASCII representation of the board:
​
The board can be visualized as rows and columns. Each column is one character wide and shall be either a uppercase ascii letter or a space. Each row shall be deliminated by an EOL (please use `\n`). Here is an example of what is expected:
```
     T    
HEALTH    
     IS   
     SPACE
      A  A
      RATS
      TREE
      ATE 
      N   
```
​
Please note that the board should be printed on a newline, and not on the same line as the other output data.

#### Scoring

Scores will be determined by log(# of turns) + log(time in ms) with the lowest score being the highest rank.s

### Solution Setup

Put each of your submitted solutions in its own directory at the root of the project. Any directory that is named `alphanumeric-alphanumeric` will be picked up by the test container, but general convention is use `yourlanguage-yourname/handle`.

Your solution directory should include the following:

* `build.sh` file (only if you need to build/compile your solution)
* `run.sh` file (a shell file that has the command to execute your solution)
  * **Important**: Make sure your solution can take an input. The letters to handle will be sent as a string in a BASH variable. See example folder for details on how this will work.
* the file(s) needed to build and run your solution.

See the `example` directory for more guidance.

*Note*: You might need to update the Docker build file if your language is not yet supported (see below.) If you need help, ask in #monthly-challenge in Slack.

### Running the Tests (I.e. Docker and Stuff)

The Docker image is now moved to its own repo and is hosted on Dockerhub.

* [Source](https://github.com/ReformedDevs/challenge-docker)
* [Dockerhub](https://hub.docker.com/r/drewpearce/trd-challenge)

The image tagged latest currently supports these languages:

* C/C++
* .NET
* Node 11
* Python 3.6
* Ruby
* Rust

If you want to add support for another language, you can make a PR to the Source repo referenced above. If you need help, come on over to the #monthly-challenge channel on our Slack.

You can build the container locally by running `./build_docker.sh`.

You can run the container lcoally by running `./run_docker.sh` after building the container.

You can run the tests locally (assuming you have all the language support installed) by running `python(3) run_solutions.py`.

If you only want to run specific directories on a local run (i.e. just test your solution), run `python(3) run_solutions.py comma-separated,list-of,solution-dirs`.

### Leaderboard

This is where the leaderboard will go.

### Oops

If someone offers an incorrect solution, it will get posted here when the test suite is run.
