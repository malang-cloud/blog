package main

import (
	"fmt"
	"os"
)

func main() {
	var a, b int

	fmt.Print("Nilai A: ")
	fmt.Scanln(&a)

	fmt.Print("Nilai B: ")
	fmt.Scanln(&b)

	c := a + b

	fmt.Printf("Nilai A + B = %d\n", c)

	os.Exit(0)
}
