package main

import (
	"bufio"
	"log"
	"os"
)

type board struct {
	array   [][]int
	m       int
	n       int
	steps   int
	flashes int
}

func readFile(filename string) [][]int {
	file, err := os.Open(filename)
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)

	var array [][]int

	for scanner.Scan() {
		textRow := scanner.Text()
		row := []int{}

		for _, rune := range textRow {
			row = append(row, int(rune-'0'))
		}

		array = append(array, row)
	}

	if err := scanner.Err(); err != nil {
		log.Fatal(err)
	}

	return array
}

type coord struct {
	x int
	y int
}

func (b *board) step() {

	shouldFlash := []coord{}

	for i := 0; i < b.m; i++ {
		for j := 0; j < b.n; j++ {
			b.array[i][j]++
			if b.array[i][j] > 9 {
				shouldFlash = append(shouldFlash, coord{i, j})
			}
		}
	}

	flashed := make(map[coord]bool)

	for {
		if len(shouldFlash) == 0 {
			break
		}
		c := shouldFlash[0]
		shouldFlash = shouldFlash[1:]
		if flashed[c] == true {
			continue
		}
		flashed[c] = true

		for i := -1; i <= 1; i++ {
			for j := -1; j <= 1; j++ {
				posX := c.x + i
				posY := c.y + j
				if posX >= 0 && posX < b.m && posY >= 0 && posY < b.n {
					b.array[posX][posY]++
					current := coord{posX, posY}
					if b.array[posX][posY] > 9 && flashed[current] != true {
						shouldFlash = append(shouldFlash, current)
					}
				}
			}
		}
	}
	for coord, val := range flashed {
		if val == true {
			b.array[coord.x][coord.y] = 0
			b.flashes += 1
		}
	}

	b.steps += 1
}

func p1() {
	array := readFile("input")
	gameboard := board{array, len(array), len(array[0]), 0, 0}

	for i := 0; i < 100; i++ {
		gameboard.step()
	}
	log.Printf("Val: %d, step: %d \n", gameboard.flashes, gameboard.steps)

}

func p2() {
	array := readFile("input")
	gameboard := board{array, len(array), len(array[0]), 0, 0}

	for {
		gameboard.step()
		sum := 0
		for _, row := range gameboard.array {
			for _, val := range row {
				sum += val
			}
		}

		if sum == 0 {
			log.Printf("First sync: %d", gameboard.steps)
			break
		}
	}
}

func main() {
	p1()
	p2()
}
