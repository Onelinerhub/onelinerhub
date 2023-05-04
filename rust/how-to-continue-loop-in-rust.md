# How to continue loop in Rust
// plain

Rust provides a number of looping constructs, including `loop`, `while`, and `for`. To continue a loop in Rust, you can use the `continue` keyword. This keyword will cause the loop to skip the rest of the current iteration and start the next one.

```rust
for i in 0..10 {
    if i % 2 == 0 {
        continue;
    }
    println!("{}", i);
}
```

## Output example

```
1
3
5
7
9
```

## Code explanation


- `for i in 0..10`: This is the loop construct, which will iterate from 0 to 10.
- `if i % 2 == 0`: This is a conditional statement which checks if the current value of `i` is even.
- `continue`: This keyword will cause the loop to skip the rest of the current iteration and start the next one.
- `println!("{}", i)`: This statement will print the current value of `i` to the console.

## Helpful links

- [Rust Loops](https://doc.rust-lang.org/book/ch03-03-how-functions-work.html#loops)
- [Rust `continue` keyword](https://doc.rust-lang.org/book/ch03-03-how-functions-work.html#the-continue-keyword)

group: rust-loops