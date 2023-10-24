package main

import ("fmt"
		""
)

func main() {
	var num1 int = 4
	//para declarar altomaticamente o tipo ":="
	num2 := 2

	result := calc.Dividir(num1,num2)

	fmt.Println(result)
}

