package main

import (
	"bufio"
	"log"
	"os"
	"strconv"
	"strings"
)

type queue struct {
	queue []int
}

func newQueue(indices []int) queue {
	q := queue{
		queue: []int{0, 0, 0, 0, 0, 0, 0, 0, 0},
	}
	for _, index := range indices {
		q.queue[index]++
	}
	return q
}

func (q *queue) pop(times int) {
	for i := 0; i < times; i++ {
		newEntries := q.queue[0]
		q.queue = q.queue[1:]
		q.queue = append(q.queue, newEntries)
		q.queue[6] += newEntries
	}
}

func (q *queue) sum() int {
	sum := 0
	for i := 0; i < len(q.queue); i++ {
		sum += q.queue[i]
	}

	return sum
}

func main() {
	//3,4,3,1,2
	// input := []int{3, 4, 3, 1, 2}
	input := readFile("input")
	q := newQueue(input)
	log.Printf("%v", q.queue)
	q.pop(80)
	log.Printf("%v", q.queue)
	log.Printf("%d", q.sum())
	// p2
	q2 := newQueue(input)
	log.Printf("%v", q2.queue)
	q2.pop(256)
	log.Printf("%v", q2.queue)
	log.Printf("%d", q2.sum())
}

func readFile(filename string) []int {
	file, err := os.Open(filename)
	if err != nil {
		log.Fatal(err)
	}
	defer file.Close()

	scanner := bufio.NewScanner(file)

	values := []int{}

	for scanner.Scan() {
		currentLine := scanner.Text()
		res := strings.Split(currentLine, ",")
		for i := 0; i < len(res); i++ {
			val, err := strconv.Atoi(res[i])
			if err != nil {
				log.Fatal(err)
			}
			values = append(values, val)
		}
	}

	if err := scanner.Err(); err != nil {
		log.Fatal(err)
	}

	return values
}
