package main

import (
	"os"
)

func main() {
	if len(os.Args) < 3 {
		panic("need a part (a or b) argument and a filename")
	}
	filename := os.Args[1]
	switch os.Args[2] {
	case "a":
		part1(filename)
	case "b":
		part2(filename)
	default:
		panic("Unknown part argument")
	}
}
