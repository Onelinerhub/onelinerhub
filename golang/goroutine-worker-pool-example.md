# Goroutine worker pool example

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
  
  for a := 1; a <= max_jobs; a++ {
    <-results
  }
}
```

- `func main() {` - declare `main` function that will be launched automatically
- `func worker(` - worker function that will run in parallel
- `const max_jobs` - jobs count
- `jobs` - channel to manage running jobs
- `results` - channel to collect results from worker function
- `go worker` - run `worker` function in parallel
- `jobs <- j` - send each `j` value to `jobs` channel
- `close(jobs)` - close jobs channel after we've sent all jobs
- `<-results` - read `results` channel 10 times to make sure all jobs have been finished

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
  
  for a := 1; a <= max_jobs; a++ {
    <-results
  }
}
```
```
worker 2 1
worker 2 2
worker 2 3
worker 2 4
worker 2 5
worker 2 6
worker 2 7
worker 2 8
worker 2 9
worker 2 10

```

