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

func SumElfCalories(input []string) []int {
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

func part2(file string) {
	lines := ReadLines(file)
	calories := SumElfCalories(lines)
	top_top3_calories := calories[0:3]
	fmt.Printf("Top 3 calories: %v\n", top_top3_calories)
	total_top3_calories := 0
	for _, num := range top_top3_calories {
		total_top3_calories += num
	}
	fmt.Printf("Total 3 calories: %v\n", total_top3_calories)
}
