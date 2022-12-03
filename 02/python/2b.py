from enum import Enum
from dataclasses import dataclass
from pathlib import Path
import sys

file = sys.argv[1]
lines = Path(file).read_text().split("\n")

ROCK = "ROCK"
PAPER = "PAPER"
SCISSORS = "SCISSORS"

opp_play_map = {"A": ROCK, "B": PAPER, "C": SCISSORS}
result_map = {"X": "LOSE", "Y": "DRAW", "Z": "WIN"}


class PlayValue(Enum):
    ROCK = 1
    PAPER = 2
    SCISSORS = 3


class ResultValue(Enum):
    WIN = 6
    LOSE = 0
    DRAW = 3


@dataclass
class Game:
    opponents_play_code: str
    expected_result_code: str

    def decode_inputs(self):
        self.opponents_play = opp_play_map[self.opponents_play_code]
        self.expected_result = result_map[self.expected_result_code]

    def determine_response(self):
        self.response = "UNDEFINED"
        if self.expected_result == "DRAW":
            self.response = self.opponents_play
        elif self.expected_result == "LOSE":
            if self.opponents_play == ROCK:
                self.response = SCISSORS
            elif self.opponents_play == PAPER:
                self.response = ROCK
            elif self.opponents_play == SCISSORS:
                self.response = PAPER
        elif self.expected_result == "WIN":
            if self.opponents_play == ROCK:
                self.response = PAPER
            elif self.opponents_play == PAPER:
                self.response = SCISSORS
            elif self.opponents_play == SCISSORS:
                self.response = ROCK

    def eval_game(self) -> int:
        return ResultValue[self.expected_result].value + PlayValue[self.response].value


file = sys.argv[1]
lines = Path(file).read_text().split("\n")

rounds = []
while len(lines) > 0:
    line = lines.pop(0)
    l = line.split()

    game = Game(opponents_play_code=l[0], expected_result_code=l[1])
    # print(game)
    game.decode_inputs()
    print(game.expected_result)
    print(game.opponents_play)
    game.determine_response()
    print(game.response)
    print()
    score = game.eval_game()

    rounds.append(score)

print(sum(rounds))
