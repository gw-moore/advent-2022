package main

import (
	"bufio"
	"fmt"
	"os"
	"strings"
)

func readLines(filepath string) ([]string, error) {
	file, err := os.Open(filepath)
	if err != nil {
		return nil, err
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)
	lines := []string{}
	for scanner.Scan() {
		lines = append(lines, scanner.Text())
	}
	return lines, scanner.Err()
}

func evalGame(oppMove, myMove string) int {
	moveValueMap := make(map[string]int)
	moveValueMap["rock"] = 1
	moveValueMap["paper"] = 2
	moveValueMap["scissors"] = 3

	oppMoveMap := make(map[string]string)
	oppMoveMap["A"] = "rock"
	oppMoveMap["B"] = "paper"
	oppMoveMap["C"] = "scissors"
	oppPlays := oppMoveMap[oppMove]

	myMoveMap := make(map[string]string)
	myMoveMap["X"] = "rock"
	myMoveMap["Y"] = "paper"
	myMoveMap["Z"] = "scissors"
	myPlays := myMoveMap[myMove]
	playValue := moveValueMap[myPlays]

	if oppPlays == myPlays {
		playValue += 3
	} else if (oppPlays == "rock") && (myPlays == "paper") {
		playValue += 6
	} else if (oppPlays == "rock") && (myPlays == "scissors") {
		playValue += 0
	} else if (oppPlays == "paper") && (myPlays == "scissors") {
		playValue += 6
	} else if (oppPlays == "paper") && (myPlays == "rock") {
		playValue += 0
	} else if (oppPlays == "scissors") && (myPlays == "rock") {
		playValue += 6
	} else if (oppPlays == "scissors") && (myPlays == "paper") {
		playValue += 0
	}

	return playValue
}

func main() {
	file := os.Args[1]
	lines, err := readLines(file)

	if err != nil {
		panic(err)
	}

	runningTotal := 0
	for _, game := range lines {
		gameSlice := strings.Fields(game)
		gameValue := evalGame(gameSlice[0], gameSlice[1])
		runningTotal += gameValue
	}

	fmt.Printf("Total score: %v\n", runningTotal)
}
