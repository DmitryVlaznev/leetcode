package checkers

import (
	"fmt"
)

type Scalar interface {
	int | bool | string
}

func CheckScalar[param Scalar](correctValue param, valueToCheck param) string {
	if correctValue == valueToCheck {
		return fmt.Sprintf("[+] CORRECT: %v = %v", correctValue, valueToCheck)
	}

	return fmt.Sprintf("[-] INCORRECT: %v != %v", correctValue, valueToCheck)
}
