# How to borrow in loop in Rust
// plain

Looping in Rust is done using the `loop` keyword. This keyword allows you to create an infinite loop, which can be used to iterate over a collection of items.

```rust
let mut count = 0;

loop {
    count += 1;
    println!("{}", count);
    if count == 10 {
        break;
    }
}
```

## Output example

```
1
2
3
4
5
6
7
8
9
10
```

The code above creates an infinite loop that prints out the numbers from 1 to 10. The `loop` keyword is followed by a set of curly braces `{}` which contain the code that will be executed in the loop. The `break` keyword is used to exit the loop when the condition is met.

## Code explanation

- `let mut count = 0;`: This line declares a mutable variable `count` and initializes it to 0.
- `loop {`: This line starts the loop.
- `count += 1;`: This line increments the value of `count` by 1.
- `println!("{}", count);`: This line prints the value of `count` to the console.
- `if count == 10 {`: This line checks if the value of `count` is equal to 10.
- `break;`: This line exits the loop.

## Helpful links
- [Rust Loops](https://doc.rust-lang.org/book/ch03-05-control-flow.html#loops)

group: rust-borrow