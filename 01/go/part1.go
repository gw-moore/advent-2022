package main

import (
	"bufio"
	"fmt"
	"log"
	"os"
	"sort"
	"strconv"
)

func readLines(filepath string) []string {
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

func sumElfCalories(input []string) []int {
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
	lines := readLines(file)
	elves := sumElfCalories(lines)
	fmt.Printf("Max calories: %v\n", elves[0])
}
