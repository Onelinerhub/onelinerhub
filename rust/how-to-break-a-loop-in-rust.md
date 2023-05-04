# How to break a loop in Rust
// plain

Breaking a loop in Rust is done using the `break` keyword. This keyword can be used to exit a loop at any point.

```rust
for i in 0..10 {
    if i == 5 {
        break;
    }
    println!("{}", i);
}
```

## Output example

```
0
1
2
3
4
```

- `for i in 0..10`: This is a loop that will iterate from 0 to 10.
- `if i == 5`: This is a condition that will be checked each time the loop iterates.
- `break`: This keyword will exit the loop if the condition is met.

## Helpful links
- [Rust break statement](https://doc.rust-lang.org/book/ch03-05-control-flow.html#the-break-statement)

group: rust-loops