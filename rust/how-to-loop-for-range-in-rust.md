# How to loop for range in Rust
// plain

Looping through a range in Rust is done using the `for` loop. The `for` loop takes a range as an argument and iterates over each element in the range.

Example:
```
for i in 0..5 {
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

## Code explanation

- `for`: keyword used to start a loop
- `i`: variable used to store the current value of the loop
- `0..5`: range of values to loop over
- `println!`: macro used to print the value of `i`

## Helpful links
- [Rust Loops](https://doc.rust-lang.org/book/ch03-05-control-flow.html#loops)
- [Rust Range](https://doc.rust-lang.org/std/ops/struct.Range.html)

group: rust-loops