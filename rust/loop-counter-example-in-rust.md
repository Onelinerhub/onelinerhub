# Loop counter example in Rust
// plain

Loop counter example in Rust is a way to iterate over a collection of items and perform an action on each item. The most common way to do this is with a `for` loop. The `for` loop takes a variable, called a counter, and assigns it a value from the collection. The loop then executes a block of code for each value of the counter.

```
for counter in 0..10 {
    println!("Counter is {}", counter);
}
```

## Output example

```
Counter is 0
Counter is 1
Counter is 2
Counter is 3
Counter is 4
Counter is 5
Counter is 6
Counter is 7
Counter is 8
Counter is 9
```

## Code explanation

- `for` loop: the loop that iterates over the collection of items
- `counter`: the variable that is assigned a value from the collection
- `0..10`: the range of values that the counter will take
- `println!`: the function that prints out the value of the counter

## Helpful links
- [Rust Loops](https://doc.rust-lang.org/book/ch03-05-control-flow.html#loops)
- [Rust For Loop](https://doc.rust-lang.org/book/ch03-05-control-flow.html#for-loops)

group: rust-loops