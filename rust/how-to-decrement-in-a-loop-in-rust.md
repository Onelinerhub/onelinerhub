# How to decrement in a loop in Rust
// plain

Decrementing in a loop in Rust is done using the `loop` and `for` keywords. The `loop` keyword is used to create an infinite loop, while the `for` keyword is used to create a loop with a specific number of iterations.

## Example code

```
for i in (1..10).rev() {
    println!("{}", i);
}
```

## Output example

```
9
8
7
6
5
4
3
2
1
```

## Code explanation


1. `for` keyword: used to create a loop
2. `i`: variable used to store the current iteration number
3. `1..10`: range of numbers from 1 to 10
4. `rev()`: reverses the range of numbers
5. `println!`: prints the current iteration number

## Helpful links

- [Rust loops](https://doc.rust-lang.org/book/ch03-03-how-functions-work.html#loops)
- [Rust range](https://doc.rust-lang.org/std/ops/struct.Range.html)

group: rust-loops