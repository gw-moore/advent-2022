from pathlib import Path
import sys

opponent_rps_map = {"A": "rock", "B": "paper", "C": "scissors"}
resp_rps_map = {"X": "rock", "Y": "paper", "Z": "scissors"}
resp_value_map = {"rock": 1, "paper": 2, "scissors": 3}

result_map = {
    "rock_paper": 6,
    "paper_scissors": 6,
    "scissors_rock": 6,
    "rock_scissors": 0,
    "paper_rock": 0,
    "scissors_paper": 0,
}


def eval_game(opponent: str, resp: str) -> int:
    resp_value = resp_value_map[resp]
    if opponent == resp:
        return 3 + resp_value

    return result_map[f"{opponent}_{resp}"] + resp_value


file = sys.argv[1]
lines = Path(file).read_text().split("\n")

rounds = []
while len(lines) > 0:
    line = lines.pop(0)
    l = line.split()

    # convert the code into rsp
    opponent = opponent_rps_map[l[0]]
    resp = resp_rps_map[l[1]]
    rounds.append(eval_game(opponent=opponent, resp=resp))

print(sum(rounds))
