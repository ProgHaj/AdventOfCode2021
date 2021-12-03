package main

import (
	"bufio"
	"log"
	"math"
	"os"
)

type boolFunc func(int, float64) bool

func bool_to_int(a bool) int {
	if a {
		return 1
	} else {
		return 0
	}
}

func recursion(entries [][]int, width int, height int, pos int, calc boolFunc) ([]int, int) {
	if pos >= width || len(entries) == 1 {
		return entries[0], pos
	}

	total := 0
	for _, entry := range entries {
		total += entry[pos]
	}

	treshold := float64(height) / 2
	key := bool_to_int(calc(total, treshold))

	log.Printf("len %d, total %d, treshold %f, key %d, pos %d", len(entries), total, treshold, key, pos)

	var res [][]int
	for _, entry := range entries {
		if entry[pos] == key {
			res = append(res, entry)
		}
	}

	return recursion(res, width, len(res), pos+1, calc)
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
	var total [][]int

	for scanner.Scan() {
		tempText := scanner.Text()
		if bitlength == 0 {
			bitlength = len(tempText)
		}

		row := make([]int, bitlength)

		for i, rune := range tempText {
			row[i] += int(rune - '0')
		}

		total = append(total, row)
		entries++
	}

	if err := scanner.Err(); err != nil {
		log.Fatal(err)
	}

	var ogr_func = func(total int, treshold float64) bool {
		return float64(total) >= treshold
	}
	var csr_func = func(total int, treshold float64) bool {
		return float64(total) < treshold
	}

	log.Printf("%v", total)
	// Calc ogr
	val_ogr, pos_ogr := recursion(total, bitlength, entries, 0, ogr_func)
	ogr := 0
	for i, bit := range val_ogr {
		ogr += bit * int(math.Pow(2, float64((bitlength-i-1))))
	}
	log.Printf("val_ogr: %v, ogr: %d, pos: %d", val_ogr, ogr, pos_ogr)

	// Calc csr
	val_csr, pos_csr := recursion(total, bitlength, entries, 0, csr_func)
	csr := 0
	for i, bit := range val_csr {
		csr += bit * int(math.Pow(2, float64((bitlength-i-1))))
	}
	log.Printf("val_csr: %v, csr: %d, pos: %d", val_csr, csr, pos_csr)

	//RES
	log.Printf("res: %d", csr*ogr)
}
