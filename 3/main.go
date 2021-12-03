package main

import (
	"bufio"
	"log"
	"math"
	"os"
)

func bool_to_int(a bool) int {
	if a {
		return 1
	} else {
		return 0
	}
}

func main() {
	file, err := os.Open("input")
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)

	entries := 0
	bitlength := 0
	var total []int

	for scanner.Scan() {
		tempText := scanner.Text()
		if total == nil {
			bitlength = len(tempText)
			total = make([]int, bitlength)
		}

		for i, rune := range tempText {
			total[i] += int(rune - '0')
		}

		entries++
	}

	if err := scanner.Err(); err != nil {
		log.Fatal(err)
	}

	gam := make([]int, bitlength)
	eps := make([]int, bitlength)
	gam_val := 0
	eps_val := 0
	treshold := entries / 2

	for i, val := range total {
		gam[i] = bool_to_int(val > treshold)
		eps[i] = bool_to_int(val < treshold)
		gam_val += gam[i] * int(math.Pow(2, float64((bitlength-i-1))))
		eps_val += eps[i] * int(math.Pow(2, float64((bitlength-i-1))))
	}

	log.Printf("Entries: %d, Bitlength: %d", entries, bitlength)
	log.Printf("total: %v", total)
	log.Printf("Gam>: %v, Eps<: %v", gam, eps)
	log.Printf("GamVal: %d, EpsVal: %d", gam_val, eps_val)
	log.Printf("Val: %d", (gam_val * eps_val))

}
