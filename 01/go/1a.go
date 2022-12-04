package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"sort"
	"strconv"
)

func ReadLines(filepath string) []string {
	file, err := os.Open(filepath)
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)
	lines := []string{}
	for scanner.Scan() {
		lines = append(lines, scanner.Text())
	}
	return lines
}

func q1(input []string) []int {
	elves := []int{}
	var sum int = 0
	for _, line := range input {
		if line == "" {
			elves = append(elves, sum)
			sum = 0
		} else {
			num, err := strconv.Atoi(line)
			if err != nil {
				log.Fatal(err)
			}
			sum += num
		}
	}
	elves = append(elves, sum)
	sort.Slice(elves, func(i, j int) bool {
		return elves[i] > elves[j]
	})
	return elves
}

func main() {
	file := os.Args[1]
	lines := ReadLines(file)
	elves := q1(lines)
	fmt.Printf("Max calories: %v\n", elves[0])
}
