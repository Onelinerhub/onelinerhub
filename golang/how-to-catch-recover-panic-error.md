# How to catch (recover) panic() error

```go
package main

func main() {
  test()
  print("world after panic")
}

func test() {
  defer func() {
		if err := recover(); err != nil {
			print("catched panic, ha ha ha...")
		}
	}()
	
	panic("noooo")
}
```

- `package main` - default package declaration
- `func main() {` - declare `main` function that will be launched automatically
- `func test()` - test function has `panic()` call and its handler via `recover()`
- `if err := recover()` - catch panic via `recover()`
- `print("world after panic")` - this should would if panic was catches successfully

group: panic

## Example: 
```go
package main

func main() {
  test()
  print("world after panic")
}

func test() {
  defer func() {
		if err := recover(); err != nil {
			print("catched panic, ha ha ha...")
		}
	}()
	
	panic("noooo")
}
```
```
catched panic, ha ha ha...world after panic
```

