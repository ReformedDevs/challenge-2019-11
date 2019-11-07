# The Reformed Devs Monthly Challenge

## Month Year

### Background

Birthed out of our Slack org, The Reformed Devs have begun monthly coding challenges for its members, hoping to encourage critical thinking and problem and solving and foster community. You can see our previous challenges here:

* [April 2019](https://github.com/plusuncold/longest-word-test)
* [May 2019](https://github.com/plusuncold/rainfall-calc-challenge)
* [June 2019](https://github.com/ReformedDevs/challenge-2019-06)
* [July 2019](https://github.com/ReformedDevs/challenge-2019-07)
* [September 2019](https://github.com/ReformedDevs/challenge-2019-09)
* [October 2019](https://github.com/ReformedDevs/challenge-2019-10)

#### Future Challenge Ideas

* Boggle Solver
* Sudoku Generator/Solver
* Algorithm trainer
* Next best scrabble move
* Provide a game API and have solutions play against each other
* Prisoner puzzle best time

### This Month's Challenge

#### Problem

A description of the problem(s) to be solved. Include an example to be helpful. Explicit is better than implicit.

#### Output

Running your solution should output your info in the following format: `desired, output, items, here`.

#### Scoring

Description of how rank will be determined.

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
