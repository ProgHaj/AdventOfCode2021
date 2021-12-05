package main

import (
	"bufio"
	"log"
	"os"
	"strconv"
	"strings"
)

type coord struct {
	x int
	y int
}

type path struct {
	source      coord
	destination coord
}

func readFile(filename string) ([]path, coord) {

	file, err := os.Open(filename)
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)

	paths := []path{}
	max_coord := coord{}

	for scanner.Scan() {
		currentLine := scanner.Text()
		res := strings.Split(currentLine, " -> ")
		source := strings.Split(res[0], ",")
		destination := strings.Split(res[1], ",")
		s_x, err := strconv.Atoi(source[0])
		if err != nil {
			log.Fatal(err)
		}
		s_y, err := strconv.Atoi(source[1])
		if err != nil {
			log.Fatal(err)
		}
		source_coord := coord{s_x, s_y}

		d_x, err := strconv.Atoi(destination[0])
		if err != nil {
			log.Fatal(err)
		}
		d_y, err := strconv.Atoi(destination[1])
		if err != nil {
			log.Fatal(err)
		}
		destin_coord := coord{d_x, d_y}

		paths = append(paths, path{source_coord, destin_coord})

		if destin_coord.x >= max_coord.x {
			max_coord.x = destin_coord.x
		}

		if destin_coord.y >= max_coord.y {
			max_coord.y = destin_coord.y
		}

		if source_coord.x >= max_coord.x {
			max_coord.x = source_coord.x
		}

		if source_coord.y >= max_coord.y {
			max_coord.y = source_coord.y
		}
	}

	if err := scanner.Err(); err != nil {
		log.Fatal(err)
	}

	return paths, max_coord
}

func fillPipe(pipe_map *[][]int, s coord, d coord) {
	if s.x == d.x {
		start := 0
		end := 0
		if s.y <= d.y {
			start = s.y
			end = d.y
		} else {
			start = d.y
			end = s.y
		}
		for i := start; i <= end; i++ {
			(*pipe_map)[s.x][i] += 1
		}
	} else if s.y == d.y {
		start := 0
		end := 0
		if s.x <= d.x {
			start = s.x
			end = d.x
		} else {
			start = d.x
			end = s.x
		}
		for i := start; i <= end; i++ {
			(*pipe_map)[i][s.y] += 1
		}
	}
}

func fillPipe2(pipe_map *[][]int, s coord, d coord) {
	if s.x == d.x {
		start := 0
		end := 0
		if s.y <= d.y {
			start = s.y
			end = d.y
		} else {
			start = d.y
			end = s.y
		}
		for i := start; i <= end; i++ {
			(*pipe_map)[s.x][i] += 1
		}
	} else if s.y == d.y {
		start := 0
		end := 0
		if s.x <= d.x {
			start = s.x
			end = d.x
		} else {
			start = d.x
			end = s.x
		}
		for i := start; i <= end; i++ {
			(*pipe_map)[i][s.y] += 1
		}
	} else {
		startCoord := coord{}
		endCoord := coord{}
		if s.x <= d.x {
			startCoord = s
			endCoord = d
		} else {
			startCoord = d
			endCoord = s
		}

		length := endCoord.x - startCoord.x

		if startCoord.y <= endCoord.y {
			for i := 0; i <= length; i++ {
				(*pipe_map)[startCoord.x+i][startCoord.y+i] += 1
			}
		} else {
			for i := 0; i <= length; i++ {
				(*pipe_map)[startCoord.x+i][startCoord.y-i] += 1
			}
		}

	}
}

func main() {

	paths, max_coord := readFile("input")
	pipe_map := make([][]int, max_coord.x+1)
	for i := 0; i < max_coord.y+1; i++ {
		pipe_map[i] = make([]int, max_coord.y+1)
	}

	for _, path := range paths {
		s := path.source
		d := path.destination

		// fillPipe(&pipe_map, s, d)
		fillPipe2(&pipe_map, s, d)
	}

	total := 0
	for _, row := range pipe_map {
		for _, numb := range row {
			if numb >= 2 {
				total++
			}
		}
	}

	log.Printf("score: %d", total)
}
