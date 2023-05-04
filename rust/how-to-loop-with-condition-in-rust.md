# How to loop with condition in Rust
// plain

Looping with condition in Rust is done using the `while` and `for` loop.

Example code using `while` loop:
```
let mut x = 0;
while x < 10 {
    println!("{}", x);
    x += 1;
}
```
## Output example

```
0
1
2
3
4
5
6
7
8
9
```

## Code explanation

- `let mut x = 0;`: declares a mutable variable `x` and assigns it the value of 0.
- `while x < 10 {`: checks if the value of `x` is less than 10.
- `println!("{}", x);`: prints the value of `x` to the console.
- `x += 1;`: increments the value of `x` by 1.

## Helpful links
- [Rust Documentation - Loops](https://doc.rust-lang.org/book/ch03-05-control-flow.html#loops)
- [Rust by Example - Loops](https://doc.rust-lang.org/rust-by-example/flow_control/loop.html)

group: rust-loops