# How to implement while loop

```go
package main

func main() {
	t := 0
	for t > -10 {
	  t -= 1
	}
	print(t)
}

```

- `package main` - default package declaration
- `func main() {` - declare `main` function that will be launched automatically
- `for t > -10 {` - we can use only a single condition to check if `for` loop which is identical to `while` loops in other languages

group: while

## Example: 
```go
package main

func main() {
	t := 0
	for t > -10 {
	  t -= 1
	}
	print(t)
}

```
```
-10
```

