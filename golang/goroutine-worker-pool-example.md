# Goroutine worker pool example

```go
func main() {
  go func() {
    // do something in background
  }()
}
```

- `func main() {` - declare `main` function that will be launched automatically
- `go ` - execute given function in parallel
- `func() {` - anonymous function to execute in background

group: goroutine

## Example: 
```go
package main

import (
  "fmt"
)

func worker(id int, jobs <-chan int, results chan<- int) {
  for j := range jobs {
    fmt.Println("worker", id, j)
    results <- j * 2
  }
}

func main() {

    const max_jobs = 10
    jobs := make(chan int, max_jobs)
    results := make(chan int, max_jobs)

    for w := 1; w <= 2; w++ {
      go worker(w, jobs, results)
    }

    for j := 1; j <= max_jobs; j++ {
      jobs <- j
    }
    
    close(jobs)
}
```

