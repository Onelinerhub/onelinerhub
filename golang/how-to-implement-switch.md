# How to implement switch

### You can use `if...else` to easily implement absent `switch` functionality:

```go
package main

func main() { 
  test := "hi"
  
	if test == "hello" {
		print("oh, good day")
	} else if test == "hi" {
		print("aloha")
	} else if test == "..." {
		print("hm...")
	}
}
```

- `package main` - default package declaration
- `func main() {` - declare `main` function that will be launched automatically
- `if` - start if block with condition to check
- `else` - execute this block if previous condition(s) were not met

## Example: 
```go
package main

func main() {
  test := "hi"
  
	if test == "hello" {
		print("oh, good day")
	} else if test == "hi" {
		print("aloha")
	} else if test == "..." {
		print("hm...")
	}
}
```
```
aloha
```

