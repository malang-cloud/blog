package main

import (
	"fmt"
)

func main() {
	var a, b int

	// input
	fmt.Print("Nilai A: ")
	fmt.Scanln(&a)

	fmt.Print("Nilai B: ")
	fmt.Scanln(&b)

	// proses
	c := a + b

	// output
	fmt.Printf("Nilai A + B = %d\n", c)
}
